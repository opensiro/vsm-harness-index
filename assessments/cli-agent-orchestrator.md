---
harness_id: cli-agent-orchestrator
project_name: CLI Agent Orchestrator
repository: https://github.com/awslabs/cli-agent-orchestrator
review_ref: ffa9fc742c7d47ce038d3d951ccc5527ba0c0218
reviewed_at: 2026-10-12
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: ?
autonomy_s5: ?
---

# CLI Agent Orchestrator

## Review boundary
- System in focus: CAO's shipped local supervisor/worker organization formed through a first-party agent profile, provider adapters, CAO server, MCP orchestration protocol and optional isolated worktree mode.
- Purpose and identity: provide agent-originated delegation and feedback control over independently executing coding CLI worker units in a shared user project, using first-party supervisor/worker profiles and tools.
- Relevant environment: coding repository, per-agent CLI tool processes, developer/reviewer roles, session/terminal statuses, git worktrees, operator preferences, MCP/API/CLI transport and external model providers.
- Standard-distribution boundary: supported PyPI/Python CAO app, built-in `code_supervisor`, `developer`, `reviewer` profiles and wired in-session MCP `assign`/`handoff`/`send_message`; no Claude Code, Kiro, Codex or other provider internal agent loop/autonomous policies credited. [README.md](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/README.md#L29-L56); [CODEBASE.md](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/CODEBASE.md#L9-L107).
- Credited operating / distribution surfaces: [src/cli_agent_orchestrator/agent_store/code_supervisor.md](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/src/cli_agent_orchestrator/agent_store/code_supervisor.md); [src/cli_agent_orchestrator/agent_store/developer.md](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/src/cli_agent_orchestrator/agent_store/developer.md); [src/cli_agent_orchestrator/agent_store/reviewer.md](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/src/cli_agent_orchestrator/agent_store/reviewer.md); [src/cli_agent_orchestrator/mcp_server/server.py](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/src/cli_agent_orchestrator/mcp_server/server.py#L279-L389); [src/cli_agent_orchestrator/mcp_server/server.py](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/src/cli_agent_orchestrator/mcp_server/server.py#L568-L645); [src/cli_agent_orchestrator/utils/orchestration.py](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/src/cli_agent_orchestrator/utils/orchestration.py#L1614-L1740); [src/cli_agent_orchestrator/services/worktree_service.py](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/src/cli_agent_orchestrator/services/worktree_service.py).
- Adjacent first-party surfaces excluded from ownership: optional user-authored workflow scripts not part of the published built-in supervisor, demo/CI/test agents, uninstalled plugins, unrelated hosted infrastructure, third-party provider CLI internal models/tools/agent loops or their private state. Retrospector/learning are considered separately but do not silently become S4.
- First-party operating / deployment modes considered: local supervisor with built-in developer/reviewer roles, nonblocking assign, blocking handoff, optional per-terminal isolated worktrees, sibling/session monitoring, operator control-plane workflows and opt-in self-learning.
- Recursion level: one user project's CAO supervisor-and-workers session (supervisor as higher-recursion control actor over distinct worker S1 units); not entire AWS Lab, model provider, or cross-user fleet.
- Reviewed revision: `ffa9fc742c7d47ce038d3d951ccc5527ba0c0218`.
- Observation date: 2026-10-12.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture
The installed `cao` CLI launches a local server and agent profiles; the provider adapter starts an external CLI session, while first-party MCP tools enable one CAO-provisioned supervisor actor to instantiate an independent developer or reviewer worker and return its results. `assign` creates a worker and asks for an asynchronous response through `send_message`; `handoff` waits for output and cleans up a worker. The inbox service retries/delivers messages only when the destination is ready ([README.md](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/README.md#L85-L111); [src/cli_agent_orchestrator/mcp_server/server.py](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/src/cli_agent_orchestrator/mcp_server/server.py#L279-L389); [src/cli_agent_orchestrator/mcp_server/server.py](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/src/cli_agent_orchestrator/mcp_server/server.py#L568-L645); [src/cli_agent_orchestrator/mcp_server/server.py](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/src/cli_agent_orchestrator/mcp_server/server.py#L827-L854); [src/cli_agent_orchestrator/services/inbox_service.py](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/src/cli_agent_orchestrator/services/inbox_service.py)).
An opt-in `use_worktree=True` on first-party assign/handoff creates a per-worker Git checkout/branch, explicitly targeted at overlapping agent writes/races. The built-in supervisor profile instructs a model actor to assign tasks, monitor results, reassign failed tasks and send code to a distinct reviewer; the read-oriented reviewer is separately role-limited and reports defects to the supervisor ([src/cli_agent_orchestrator/services/worktree_service.py](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/src/cli_agent_orchestrator/services/worktree_service.py#L1-L19); [src/cli_agent_orchestrator/services/worktree_service.py](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/src/cli_agent_orchestrator/services/worktree_service.py#L92-L123); [src/cli_agent_orchestrator/agent_store/code_supervisor.md](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/src/cli_agent_orchestrator/agent_store/code_supervisor.md#L12-L48); [src/cli_agent_orchestrator/agent_store/reviewer.md](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/src/cli_agent_orchestrator/agent_store/reviewer.md#L23-L49); [docs/tool-restrictions.md](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/docs/tool-restrictions.md#L27-L49)).

## Operational model
CAO owns the deployed organizational orchestration surface (roles/profile instructions, launching, isolation, messaging, results, state and operator controls) while delegated CLI providers execute lower-level coding agent loops. It is in-scope because a first-party, runnable supervisor profile uses CAO's own MCP decision/feedback interfaces; only this integration and role-specific decisions are credited. External CLI internals remain outside.

## S1 — Operations
- State: A
- Function: Multiple model-directed worker sessions implement assigned coding/review tasks and return artifacts/findings to the supervisor through the supported CAO runtime.
- Disturbance / variety regulated: User requests, changing code, individual task failures and defects, separate worker provider responses.
- Decisive decision or feedback right: CAO-started worker agents decide how to perform the delegated task within their advertised developer/reviewer role; the supervisor allocates tasks separately.
- Decision owner: Shipped first-party configured agent profiles running model-driven sessions through supported external CLI providers; external provider reasoning details are not credited as first-party code.
- Supporting / enforcement mechanisms: Profile roles, terminal/provid­er adapter, model process, CAO MCP messages and terminal session manager.
- Closure path: Supervisor task/message → first-party-created worker CLI context → worker produces code/review findings → CAO handoff output or inbox callback → supervisor sees completion and selects follow-up.
- Boundary reachability: The documented install/launch path exposes built-in code_supervisor; its MCP server can launch developer/reviewer sessions from installed first-party profiles ([README.md](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/README.md#L85-L111); [src/cli_agent_orchestrator/agent_store/code_supervisor.md](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/src/cli_agent_orchestrator/agent_store/code_supervisor.md#L12-L48); [src/cli_agent_orchestrator/utils/orchestration.py](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/src/cli_agent_orchestrator/utils/orchestration.py#L1614-L1740)).
- Why this is / is not agent-owned: Work and review choices are generated by actual delegated agent roles, not a deterministic tmux replay; no claim is made about external provider-native internal planning.
- Evidence: [README.md](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/README.md#L29-L39); [src/cli_agent_orchestrator/agent_store/developer.md](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/src/cli_agent_orchestrator/agent_store/developer.md); [src/cli_agent_orchestrator/agent_store/reviewer.md](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/src/cli_agent_orchestrator/agent_store/reviewer.md); [src/cli_agent_orchestrator/mcp_server/server.py](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/src/cli_agent_orchestrator/mcp_server/server.py#L279-L389); [src/cli_agent_orchestrator/mcp_server/server.py](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/src/cli_agent_orchestrator/mcp_server/server.py#L568-L645).
- Basis: structural
- Confidence: medium
- Caveats: Agentic model quality/actual tool executions were not tested; positive first-party scope is CAO's bundled model-driven composition mode, not inference from capabilities hidden inside the provider CLI.

## S2 — Coordination
- State: C
- Function: Prevent damaging shared-source interference among separately acting coding workers when the supported opt-in worktree isolation mode is used.
- Distinct S1 units: Independently launched developer/worker terminal sessions via the first-party `assign`/`handoff` MCP tools ([src/cli_agent_orchestrator/mcp_server/server.py](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/src/cli_agent_orchestrator/mcp_server/server.py#L279-L389); [src/cli_agent_orchestrator/mcp_server/server.py](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/src/cli_agent_orchestrator/mcp_server/server.py#L568-L645)).
- Inter-S1 disturbance: Concurrent spawned workers share a Git checkout by default and can race/overwrite one another's edits or create merge conflicts; first-party worktree service explicitly identifies these exact hazards ([src/cli_agent_orchestrator/services/worktree_service.py](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/src/cli_agent_orchestrator/services/worktree_service.py#L1-L10)).
- Attenuating coordination relation: Supervisor's opt-in worktree parameter causes CAO to create distinct branch/checkouts for individual child sessions, separating conflicting write contexts; worker results return to the supervisor for explicit integration.
- Feedback into subsequent S1 behaviour: Worktree-provisioned workers execute in separated checkouts, return task outcome through handoff or inbox callback; supervisor then selects further assignments/repair or integration rather than allowing concurrent edits to the original shared checkout ([src/cli_agent_orchestrator/utils/orchestration.py](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/src/cli_agent_orchestrator/utils/orchestration.py#L1614-L1740); [src/cli_agent_orchestrator/mcp_server/server.py](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/src/cli_agent_orchestrator/mcp_server/server.py#L827-L854)).
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: Evidence ties per-worker isolation directly to an explicitly documented concrete inter-worker file race/overwrite hazard, not to ordinary message delivery or terminal creation alone.
- Disturbance / variety regulated: Overlapping mutations and checkout interference between active coding units.
- Decisive decision or feedback right: The choice to request isolated worktree mode belongs to supervisor/constructor configuration; CAO creates a fresh branch/worktree and enforces the isolated execution context.
- Decision owner: First-party optional isolation constructor with developer/supervisor-provided enablement; no autonomous S2-level admission or merge-convergence policy is shown.
- Supporting / enforcement mechanisms: Per-worker server-generated terminal ID, Git worktree creation, per-terminal checkout path, cleanup, MCP assign/handoff callback.
- Closure path: Explicit collision risk → assign/handoff with `use_worktree=True` → distinct Git branches and isolated next S1 edits → result delivered to supervisor → subsequent unit work/integration decisions.
- Boundary reachability: `use_worktree` is a shipped argument on both first-party MCP tools and forwarded to the local terminal service; `create_worktree` makes an actual branch/checkout ([src/cli_agent_orchestrator/mcp_server/server.py](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/src/cli_agent_orchestrator/mcp_server/server.py#L568-L645); [src/cli_agent_orchestrator/utils/orchestration.py](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/src/cli_agent_orchestrator/utils/orchestration.py#L452-L580); [src/cli_agent_orchestrator/services/worktree_service.py](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/src/cli_agent_orchestrator/services/worktree_service.py#L100-L123)).
- Why this is / is not agent-owned: Contention-specific relation is built by CAO; the optional activation owner is the supervisor but no independent agent S2 conflict-resolution policy is presumed.
- Evidence: [src/cli_agent_orchestrator/services/worktree_service.py](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/src/cli_agent_orchestrator/services/worktree_service.py#L1-L19); [src/cli_agent_orchestrator/services/worktree_service.py](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/src/cli_agent_orchestrator/services/worktree_service.py#L100-L123); [src/cli_agent_orchestrator/utils/orchestration.py](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/src/cli_agent_orchestrator/utils/orchestration.py#L1614-L1740); [src/cli_agent_orchestrator/mcp_server/server.py](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/src/cli_agent_orchestrator/mcp_server/server.py#L568-L645).
- Basis: explicit
- Confidence: medium
- Caveats: Positive restricted to explicitly enabled per-worker worktree mode; default shared directory does **not** receive this S2 closure. No automatic conflict-free merge or code acceptance is claimed.

## S3 — Inside-and-now control
- State: A
- Function: First-party model-driven code_supervisor governs commitments and rework across its active developer and reviewer worker units.
- Disturbance / variety regulated: Unfinished assignments, failed/defective code, availability and outputs of launched agents, shared artifact paths.
- Decisive decision or feedback right: Supervisor chooses which worker gets each task, when findings trigger rework and when review is satisfactory.
- Decision owner: Bundled code_supervisor model role, not the tmux scheduler, status endpoint or underlying provider's hidden native agent hierarchy.
- Supporting / enforcement mechanisms: CAO `assign`/`handoff`, result callbacks, inbox delivery/status, supervisor file/task directory rules.
- Whole-system current view: Within the expressly bounded supervisor team, supervisor tracks assigned tasks, known code artifacts, callbacks and reviewer findings, not all sessions/fleets of external agents.
- Current-control decision scope: Developer/reviewer assignment, repair/retry commitments and task convergence at the supervisor-team recursion.
- Closure path: Subordinate outcomes and reviewer feedback → supervisor checks team current work and chooses assignment/retry/approval → new worker work and returned completion.
- Boundary reachability: `cao install code_supervisor` and `cao launch --agents code_supervisor` are documented; its first-party role/instructions require task assignment, progress tracking, rework on failed review, and delegate through wired MCP tools ([README.md](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/README.md#L85-L111); [src/cli_agent_orchestrator/agent_store/code_supervisor.md](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/src/cli_agent_orchestrator/agent_store/code_supervisor.md#L12-L48); [src/cli_agent_orchestrator/mcp_server/server.py](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/src/cli_agent_orchestrator/mcp_server/server.py#L568-L645)).
- Why this is / is not agent-owned: Supervisor decides commitments based on returned worker/reviewer observations; tool transport/terminal service only enforces dispatch and delivery.
- Evidence: [src/cli_agent_orchestrator/agent_store/code_supervisor.md](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/src/cli_agent_orchestrator/agent_store/code_supervisor.md#L14-L48); [src/cli_agent_orchestrator/mcp_server/server.py](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/src/cli_agent_orchestrator/mcp_server/server.py#L568-L645); [src/cli_agent_orchestrator/utils/orchestration.py](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/src/cli_agent_orchestrator/utils/orchestration.py#L1614-L1740).
- Basis: explicit
- Confidence: medium
- Caveats: The claimed whole-system view is limited to the supervisor's own team, not an arbitrary larger fleet; no S3=P inferred solely from separate human CLI controls.

## S3* — Complementary audit
- State: A
- Function: A distinct code-review worker audits produced source/code artifacts and sends independent problem findings back into the supervisor's repair/acceptance loop.
- Disturbance / variety regulated: Code quality, correctness, missing test coverage, security vulnerabilities in developer-produced work.
- Decisive decision or feedback right: Dedicated reviewer model makes its own source-inspection judgment; supervisor decides whether findings require developer repair.
- Decision owner: Separate built-in `reviewer` model session for audit judgment; supervisor owns follow-up commitments.
- Supporting / enforcement mechanisms: First-party reviewer role/tool-access limits, shared artifact paths, CAO handoff/assign and return message mechanism.
- Claim being audited: Developer completion/quality claims about newly produced project files.
- Ordinary reporting path: Developer sends work artifacts/status to the CAO supervisor.
- Complementary access path: A separately instantiated read-oriented reviewer receives source paths and inspects code independently of the developer's self-report.
- Independence boundary: Separate worker terminal/profile, read-oriented reviewer tools and independently model-produced findings; it is neither the developer's own loop nor a deterministic assertion of completion.
- Who acts on findings: Supervisor relays defects to developer, repeats review and decides when satisfied.
- Closure path: Developer artifact → separate reviewer source examination → findings to supervisor → subsequent developer correction/re-review before finishing.
- Boundary reachability: Built-in supervisor explicitly requires a code-review worker after development and repair loops; the shipped reviewer profile has a review-only role and sends findings back over the first-party MCP channel ([src/cli_agent_orchestrator/agent_store/code_supervisor.md](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/src/cli_agent_orchestrator/agent_store/code_supervisor.md#L35-L48); [src/cli_agent_orchestrator/agent_store/reviewer.md](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/src/cli_agent_orchestrator/agent_store/reviewer.md#L23-L49); [docs/tool-restrictions.md](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/docs/tool-restrictions.md#L35-L49)).
- Why this is / is not agent-owned: Distinct model reviewer produces content-specific defect judgments; model independence is role/process-level, not proof of different provider weights or guaranteed statistical independence.
- Evidence: [src/cli_agent_orchestrator/agent_store/code_supervisor.md](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/src/cli_agent_orchestrator/agent_store/code_supervisor.md#L35-L48); [src/cli_agent_orchestrator/agent_store/reviewer.md](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/src/cli_agent_orchestrator/agent_store/reviewer.md#L23-L49); [src/cli_agent_orchestrator/mcp_server/server.py](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/src/cli_agent_orchestrator/mcp_server/server.py#L279-L389); [src/cli_agent_orchestrator/mcp_server/server.py](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/src/cli_agent_orchestrator/mcp_server/server.py#L827-L854).
- Basis: explicit
- Confidence: medium
- Caveats: Positive only in the bundled developer+reviewer supervisor mode, not every launch. Reviewer is independently running but no claim is made of organizational independence outside this task-level CAO team.

## S4 — Outside-and-then intelligence
- State: ?
- Function: Optional learning/outcome/retrospector/instruction-promotion path might adapt future agents, but its external-prospective S4 function and decisive owner remain unresolved.
- Disturbance / variety regulated: Recurring historical workflow failures and future task differences.
- Decisive decision or feedback right: Retrospector stores lessons; separate operator must explicitly apply promoted lessons into agent profiles, but it is unproven whether this constitutes full outside-and-then intelligence rather than retrospective process optimization.
- Decision owner: Mixed autonomous retrospector and operator for promotion; no complete S4 autonomous or first-party parent mode established.
- Supporting / enforcement mechanisms: Outcome records, memory_recall, retrospector profile, opt-in learning flags, `cao memory promote --apply`.
- External distinction: Work outcomes can carry evidence of changing task environments, but the explicit external opportunity/threat prospective appraisal is not established.
- Future / prospective distinction: Promoted lessons affect future new sessions, unlike an ordinary retry.
- Adaptation option generated: Retrospector may distill up to three reusable lessons; human-triggered promotion writes them to future profiles.
- Path back into current capability / S3: Profile learned patterns apply on later sessions; first-party prospective external intelligence judgment/authority boundary still under review.
- Closure path: Reported outcome → retrospector lesson → user promotion → future profile instructions, without an established independent outside-and-then appraisal.
- Why this is / is not agent-owned: Automatic memory capture and config editing do not by themselves establish the organizational S4 function.
- Evidence: [docs/self-learning.md](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/docs/self-learning.md#L1-L65); [docs/self-learning.md](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/docs/self-learning.md#L110-L155); [docs/self-learning.md](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/docs/self-learning.md#L180-L209); [src/cli_agent_orchestrator/services/promotion_service.py](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/src/cli_agent_orchestrator/services/promotion_service.py#L104-L208).
- Basis: unknown
- Confidence: low
- Caveats: The explicit opt-in/fail-closed gate and human-triggered promotion must not silently become S4=A(P) or P without function-specific foresight evidence.

## S5 — Policy and identity
- State: ?
- Function: First-party tool roles and operator approval policy restrict action, but ultimate project identity/organizational policy authority return path remains unresolved.
- Disturbance / variety regulated: Tool permissions, agent identities and allowed delegation, workflow safety/custody and operator oversight.
- Decisive decision or feedback right: User/deployer selects launch permissions and approvals; roles bound available MCP/CLI actions.
- Decision owner: Operator for safety and profile policy; model supervisor chooses within constraints. No S5-specific parent closure established.
- Supporting / enforcement mechanisms: Role-based allowedTools, profile schema and permission checks, workflow plan approval gate with opt-in setting and persistent approved plan ID.
- Identity / ultimate-policy issue: Accepted tool/role policy of the CAO session and approved workflow intent.
- Ultimate authority in each claimed mode: Not credited; operator can approve specific actions, but project-wide identity/policy decision loop has not been established.
- Return-to-operation path: Profile/tool restrictions affect what worker may call; workflow approval gates permit/deny runs. These are enforcement/approval paths, not proven ultimate-policy closure.
- Closure path: Agent attempts tools → permission/approval checks → allowed/blocked execution; unresolved higher-level policy decision ownership.
- Why this is / is not agent-owned: Read-only reviewer role and guarded workflow approval do not turn static constraints or generic human approval into S5.
- Evidence: [docs/tool-restrictions.md](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/docs/tool-restrictions.md#L5-L78); [src/cli_agent_orchestrator/services/approval_gate.py](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/src/cli_agent_orchestrator/services/approval_gate.py#L116-L161); [src/cli_agent_orchestrator/agent_store/code_supervisor.md](https://github.com/awslabs/cli-agent-orchestrator/blob/ffa9fc742c7d47ce038d3d951ccc5527ba0c0218/src/cli_agent_orchestrator/agent_store/code_supervisor.md#L59-L64).
- Basis: unknown
- Confidence: low
- Caveats: Verify legitimate parent policy identity authority and complete return into operating system if eventually claiming S5=P.

## Recursion
Separate CAO-launched developer and reviewer agents perform task-level S1 work while first-party `code_supervisor` manages current task commitments and code-review feedback at the project team recursion. External provider CLI cognition and project owner remain separate authorities. Parallel isolated-worktree mode is optional; it does not imply S2 autonomy in default shared-directory mode.

## Variety and escalation
Supervisor absorbs task-allocation and audit-feedback disturbances; optional worktrees attenuate concrete concurrent-write interference; first-party inbox/status reports return worker results. User approval, plan gates and opt-in retrospection exist without automatic S5/S4 state upgrades. Repo tooling and CI are not retroactively credited as part of the live agent governance loop.

## Evidence gaps
Source-first assessment at immutable commit; no external CLI execution benchmark was conducted. S1/S3/S3* are restricted to explicit installed supervisor/reviewer mode, S2 to optional worktree mode. Possible future-facing opt-in learning (S4) and ultimate parent policy (S5) remain `?` pending source-grounded adjudication; lack of evidence is not absence. Downstream reviewer should verify whether worktree constructor feedback fully meets the S2 function threshold without conflating isolation with ordinary sandboxing.
