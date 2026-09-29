---
harness_id: raven
project_name: Raven
repository: https://github.com/EverMind-AI/Raven
review_ref: e6c0344cb7ce00db25d554e4bb671ec1909a8f9f
reviewed_at: 2026-09-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-29
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A(P)
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: P
---

# Raven

## Review boundary

- System in focus: one first-party Raven Host Agent organization at pinned revision `e6c0344cb7ce00db25d554e4bb671ec1909a8f9f`, including the shared Agent Loop/Spine runtime, built-in Raven agents, host delegation and DAG machinery, Raven-Code's standard code-flow harness, permissions, session state, context/memory/skill integration, and supported user/control surfaces.
- Purpose and identity: provide a persistent host agent that can execute tasks directly or orchestrate specialized first-party and third-party agents, preserve state across turns, and expose reusable orchestration and control surfaces.
- Relevant environment: user objectives/interventions; workspace and Git state; configured model providers; tool/MCP/plugin results; built-in and external sub-agent outputs; remote A2A peers; memory/Skill Hub services; process and network failures.
- Standard-distribution boundary: the `raven/` runtime plus shipped agent definitions and first-party plugins under `agents/` when reached through supported launch/delegation paths. External model endpoints, MCP servers, third-party ACP/CLI/HTTP agents, remote A2A peers, EverOS service internals, and user repositories remain dependencies/environment.
- Credited operating / distribution surfaces: `raven/core/runtime.py`; Spine and Agent Loop; `spawn`; `run_subagent_dag`; shipped Raven-Code/Design/Oncall/PPT/Research definitions; Raven-Code code-flow tools/read ledger/Harness Manifest; task/session history; permissions; Agent-home bootstrap identity files and context assembly.
- Adjacent first-party surfaces excluded from ownership: standalone `evolver/`; benchmark suites; repository-development CI/plans; experimental simulations; documentation-only examples. They may corroborate architecture but do not become production-runtime owners.
- First-party operating / deployment modes considered: ordinary Host Agent turns; direct tool use; focused `spawn`; foreground/background DAGs; stateful sub-agent instances and steering; Raven-Code coding sessions; stored Playbooks executed through DAG machinery; ACP-hosted shipped agents; WebUI/TUI/RPC control.
- Recursion level: one Raven Host Agent organization around a session/workspace objective. Delegated built-in agent sessions and active DAG workers are lower-recursion S1 units. Independently operated A2A peers and third-party agents remain environmental organizations.
- Reviewed revision: `e6c0344cb7ce00db25d554e4bb671ec1909a8f9f`.
- Observation date: 2026-09-29.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Raven's supported entrances converge on one runtime assembly and Agent Loop. The Spine schedules turns; the Agent Loop owns turn state, tool execution, persistence and event ordering; the Host Agent can act directly or delegate to a roster of built-in and configured external agents. `run_subagent_dag` validates dependencies/capabilities, schedules ready nodes, records node states/results and exposes current-control operations including continuation, replanning, abandonment and cancellation.

Raven-Code adds two relevant first-party mechanisms. Its code-flow tool face keeps a per-session read ledger: with read-before-edit enabled, edits against unread or externally changed content are refused. This supplies a bounded stale-write S2 path for plural Raven-Code sessions sharing a checkout. Separately, after a Raven-Code turn, the code-flow hook machine-reads Git state and emits a Harness Manifest through ACP metadata. The manifest explicitly does not take its facts from model prose and fails closed to blockers when facts or attribution are uncertain.

The repository's `evolver/` is intentionally outside this production boundary. Raven's own docs describe it as a standalone benchmark-driven harness-development tool; the runtime does not import it, selected candidates remain commits rather than automatically replacing the running subject, and deployment remains separate. It therefore does not donate S4 ownership to the Host Agent organization.

Primary evidence:

- [`docs-site/docs/architecture.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/docs-site/docs/architecture.md)
- [`docs-site/docs/orchestration.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/docs-site/docs/orchestration.md)
- [`docs-site/docs/agent-collaboration.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/docs-site/docs/agent-collaboration.md)
- [`docs-site/docs/agent-integrations.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/docs-site/docs/agent-integrations.md)
- [`agents/raven-code/plugins/code-flow/code_flow/config.py`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/agents/raven-code/plugins/code-flow/code_flow/config.py)
- [`agents/raven-code/plugins/code-flow/code_flow/flow.py`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/agents/raven-code/plugins/code-flow/code_flow/flow.py)
- [`agents/raven-code/plugins/code-flow/code_flow/manifest.py`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/agents/raven-code/plugins/code-flow/code_flow/manifest.py)
- [`docs-site/docs/permissions.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/docs-site/docs/permissions.md)
- [`raven/context_engine/segments/render.py`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/raven/context_engine/segments/render.py)
- [`agents/README.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/agents/README.md)
- [`docs-site/docs/evolver.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/docs-site/docs/evolver.md)
- [`docs-site/docs/skills-and-extensions.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/docs-site/docs/skills-and-extensions.md)

## Operational model

The Host Agent is the organization-level operational actor. A model-driven turn can select ordinary tools, choose specialists, submit a DAG, inspect delegated results and continue the task. Delegated built-in workers execute their own model/tool feedback loops. Constructor/runtime mechanisms such as permission gates, concurrency limits, path confinement, DAG validation, read-before-edit checks and Git-state collection constrain or verify those loops without automatically becoming agent-owned decisions.

## S1 — Operations

- State: A
- Function: transform user/task objectives into answers, files, repository changes, research/design/oncall outputs or other tool-mediated outcomes through repeated model decisions and returned observations.
- Disturbance / variety regulated: open-ended task ambiguity; changing workspace/files; model/tool/MCP/plugin results; failed operations; child-agent outputs; conversation state and environmental feedback.
- Decisive decision or feedback right: choose the next substantive tool, response, delegation or task action after observing current context and prior results.
- Decision owner: the model-driven Raven Host Agent for host work, or the model-driven built-in Raven child agent for its delegated operational task.
- Supporting / enforcement mechanisms: Spine scheduling; Agent Loop; context engine; session persistence; tool registry; permissions; model-provider binding; child backends; DAG runner; cancellation and runtime limits.
- Closure path: objective enters a supported entrance → Agent Loop assembles context/tools → model chooses response/tool/delegation → runtime executes/dispatches → observations return → model chooses the next action or completion → outcome persists or is delivered.
- Boundary reachability: the Agent Loop is the documented standard execution path for the shipped host surfaces, and built-in agents are launched as supported Raven runtimes rather than examples.
- Why this is / is not agent-owned: without the model decision maker, scheduling and enforcement remain but open-ended substantive action selection is absent.
- Evidence: [`docs-site/docs/architecture.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/docs-site/docs/architecture.md); [`docs-site/docs/agent-integrations.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/docs-site/docs/agent-integrations.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: inference and some environmental actions can be supplied by external providers/tools; those dependencies do not own Raven's first-party operational loop.

## S2 — Coordination

- State: C
- Function: attenuate stale-write interference among concurrently operating Raven-Code S1 sessions sharing one repository checkout.
- Disturbance / variety regulated: two Raven-Code sessions can read the same file, one can modify it, and the other can later attempt an edit based on stale content, risking overwrite/invalid work.
- Decisive decision or feedback right: decide whether an edit may proceed against the version the session observed or must be refused because the content is unread/stale/externally changed.
- Decision owner: constructor-defined Raven-Code code-flow/read-ledger policy; the model does not decide whether the stale-version guard fires.
- Supporting / enforcement mechanisms: per-session read records; `require_read_before_edit`; live session ledger; workspace-concurrency notice; tool-error feedback to the agent.
- Closure path: S1-A reads file → S1-B changes same shared file → S1-A requests edit against stale observation → first-party guard refuses write → refusal returns to S1-A → S1-A must re-read/replan/stop rather than silently overwrite B.
- Boundary reachability: Raven-Code is shipped; its launcher enables the code-flow/tool configuration and the integration guide documents refusal for externally changed versions.
- Distinct S1 units: separate Raven-Code sessions/instances execute independent coding tasks through their own model/tool loops while pointing at one checkout.
- Inter-S1 disturbance: a write by one session invalidates another session's previously read content and can otherwise produce a stale/lost edit.
- Attenuating coordination relation: the read-version precondition blocks the stale edit at the first-party file-tool boundary; live concurrency notices additionally expose the shared-directory condition.
- Feedback into subsequent S1 behaviour: the refused edit is returned to the affected Raven-Code loop, which can re-read current state, narrow work or stop/report the conflict.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the witness detects a concrete cross-S1 write disturbance and prevents one stale action from entering the shared environment; it is not merely messaging, DAG order or delegation.
- Why this is / is not agent-owned: the coordination choice is fixed by configured tool policy rather than selected by a model after reasoning over inter-worker state, so the state is `C`.
- Evidence: [`docs-site/docs/agent-integrations.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/docs-site/docs/agent-integrations.md); [`agents/raven-code/plugins/code-flow/code_flow/config.py`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/agents/raven-code/plugins/code-flow/code_flow/config.py); [`agents/raven-code/plugins/code-flow/code_flow/flow.py`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/agents/raven-code/plugins/code-flow/code_flow/flow.py).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: this is a bounded S2 witness, not general workspace isolation. Raven documents that shared checkouts have no universal file locks/worktrees and full writes are not universally guarded.

## S3 — Inside-and-now control

- State: A(P)
- Function: maintain current control over an active delegated organization by inspecting live DAG/worker/task state and changing ongoing commitments through continuation, replanning, abandonment, cancellation or targeted steering.
- Disturbance / variety regulated: delegated nodes can be pending/running/completed/exceptional/failed/skipped/cancelled/interrupted; outputs can be incomplete; dependencies can block; current work may need correction or retirement.
- Decisive decision or feedback right: decide which current delegated work continues, receives corrective instructions, is replanned/replaced, is abandoned/cancelled, or is steered while running.
- Decision owner: base `A` mode — Host Agent using first-party DAG/status/control tools; parent `P` mode — authorized user/control client using first-party task/instance inspection plus direct instance turns or supported steering.
- Supporting / enforcement mechanisms: DAG run/node records; `dag_status`; `resolve_dag_node`; `cancel_dag`; instance history; direct instance chat; steering RPC; foreground/background lifecycle.
- Closure path: workers execute → Raven records statuses/results/exceptions → current-control owner inspects run/instances → owner selects intervention → runtime applies it → later execution proceeds under the updated commitment.
- Boundary reachability: DAG controls are part of shipped orchestration; task/instance inspection and steering are exposed by first-party collaboration/RPC surfaces.
- Whole-system current view: DAG status and persisted graph state expose the current node set/run status to the host; first-party task/instance views expose active delegated work to the parent controller.
- Current-control decision scope: intervention changes current worker instructions or commitments rather than only enforcing a fixed semaphore, timeout or permission rule.
- Why this is / is not agent-owned: base mode is model-selected current-control after reading current evidence; the parent path is a separate supported ownership mode over the same ongoing organization.
- Evidence: [`docs-site/docs/orchestration.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/docs-site/docs/orchestration.md); [`docs-site/docs/agent-collaboration.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/docs-site/docs/agent-collaboration.md).
- Basis: explicit + structural.
- Confidence: high for base mode; medium-high for parent mode.
- Caveats: steering support is backend-dependent; the parent witness is the supported Raven instance/control path, not every external backend.

### Mode matrix

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Host Agent | Current DAG/node status, exception, output or task evidence requires intervention | Host chooses continue/replan/abandon/cancel and runtime applies the changed commitment to subsequent delegated execution | [`orchestration.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/docs-site/docs/orchestration.md) |
| Parent (`P`) | Authorized user/control client | Parent observes an active delegated task/instance that requires correction | Direct instance turn or supported `subagents.instance.steer` returns correction into the active child path | [`agent-collaboration.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/docs-site/docs/agent-collaboration.md) |

## S3* — Audit

- State: C
- Function: independently audit a Raven-Code session's repository-side completion/integration claims against machine-read Git reality and expose blockers/attribution to the host.
- Disturbance / variety regulated: a coding agent can claim completion while the workspace has uncommitted changes, no commits past the pinned base, unreadable Git state, or changes that cannot be attributed to that session because another session shared the directory.
- Decisive decision or feedback right: determine manifest status from independently read repository facts rather than the worker's prose.
- Decision owner: constructor-defined Raven-Code manifest logic; status calculation is deterministic, not chosen by the coding model.
- Supporting / enforcement mechanisms: per-session base commit; Git reads for HEAD/branch/status/log/diff; shared-session ledger; fail-closed blockers; ACP `_meta` publication.
- Closure path: Raven-Code works and returns ordinary model response → archive hook separately reads Git/workspace state → manifest logic computes attribution/status/blockers → report is attached to ACP metadata → Host Agent/user can use independent facts for integration/continuation/escalation.
- Boundary reachability: Raven-Code's shipped code-flow hook calls `build_manifest()` on normal turn archive and publishes `raven.harnessManifest` through ACP metadata.
- Claim being audited: whether the coding session produced attributable repository changes that are in a complete, integration-ready Git state.
- Ordinary reporting path: Raven-Code model's natural-language completion response and checklist/task claims.
- Complementary access path: direct Git/worktree measurement from the first-party code-flow hook; manifest fields are machine-read and explicitly not sourced from model prose.
- Independence boundary: the coding model does not choose manifest values; unknown/shared evidence becomes a blocker rather than accepting the worker claim. This is complementary runtime evidence, not an external trust domain.
- Who acts on findings: Host Agent or authorized user/controller receiving ACP metadata decides whether to integrate, continue, reassign or investigate.
- Why this is / is not agent-owned: the audit verdict is deterministic runtime policy, so `C`; downstream management ownership does not transfer ownership of the audit decision itself.
- Evidence: [`manifest.py`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/agents/raven-code/plugins/code-flow/code_flow/manifest.py); [`flow.py`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/agents/raven-code/plugins/code-flow/code_flow/flow.py); [`agent-integrations.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/docs-site/docs/agent-integrations.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the manifest audits repository state/attribution, not arbitrary semantic code correctness; model-based DAG verdicts and optional Eval Engine are not separately credited as S3*.

## S4 — Intelligence / adaptation

- State: —
- Function: no first-party production-runtime owner is established for a prospective environment-model/adaptation loop that changes the Host Agent organization's future operating capabilities and returns those changes into production operation.
- Disturbance / variety regulated: Raven can retrieve memories/skills, build task-specific worker tables, load Playbooks and react to current task evidence, but these do not by themselves establish prospective organizational adaptation.
- Decisive decision or feedback right: choose and adopt an organizational capability change from future/external evidence, with that change becoming part of later production operation.
- Decision owner: not established inside the declared Host Agent runtime boundary.
- Supporting / enforcement mechanisms: Memory/EverOS recall; SkillForge retrieval; local skills/Playbooks; dynamic worker generation; separate `evolver/` benchmark tooling.
- Closure path: no qualifying runtime closure is established. Retrieval changes current context and operators can install/edit artifacts, while the stronger harness-change loop lives in separate Evolver and stops at candidate commits/evidence pending later deployment.
- Why this is / is not agent-owned: current-task planning/memory/skill selection are operational assistance; the benchmark-driven harness adaptation tool is explicitly outside the production runtime and does not automatically deploy its selected candidate.
- Evidence: [`skills-and-extensions.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/docs-site/docs/skills-and-extensions.md); [`evolver.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/docs-site/docs/evolver.md); [`architecture.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/docs-site/docs/architecture.md).
- Basis: explicit boundary analysis.
- Confidence: high.
- Caveats: Raven has substantial R&D/self-improvement tooling; this state only says adjacent Evolver is not imported as S4 ownership of the assessed production Host Agent runtime.

### Absence scope

- Surfaces inspected: Host Agent planning/delegation; context engine; memory/SkillForge; Playbooks; dynamic Worker Table generation; proactivity references; Eval Engine; Evolver architecture/usage and runtime-import boundary.
- Plausible first-party paths checked: memory recall as adaptation; SkillForge retrieval/install as learning; generated worker charters as redesign; Playbook reuse as adaptation; Eval Engine verdict history as learning; Evolver candidate promotion as production self-modification.
- Why no material first-party path remains: runtime paths select current context/procedures or require operator installation, while explicit harness evolution is a separate developer tool whose candidate commits are not automatically adopted by the running Raven distribution.

## S5 — Identity / ultimate policy

- State: P
- Function: establish durable identity/behavior and non-overridable operating policy within which the Raven organization may act.
- Disturbance / variety regulated: model/tool behavior can drift across tasks; tools can request unsafe/disallowed actions; specialized agents require stable identity/conduct across sessions and launches.
- Decisive decision or feedback right: define/edit Agent-home identity/conduct files and configure persistent allow/ask/deny rules/permission mode that constrain subsequent tool dispatch.
- Decision owner: legitimate operator/user maintaining Raven Agent home and configuration; no first-party autonomous agent is established as ultimate authority over these controls.
- Supporting / enforcement mechanisms: `agent_memory/profile/soul.md`; `agent_memory/profile/agent.md`; context bootstrap assembly; launcher seeding/preservation of operator edits; Permission Gate; persistent tool rules; built-in denials.
- Closure path: operator edits identity/conduct/policy → runtime/launcher preserves files/config → context assembler injects identity/behavior into later model calls and Permission Gate evaluates later tool calls → subsequent operation occurs inside returned policy boundary.
- Boundary reachability: bootstrap identity files are live standard context inputs; shipped agent launchers preserve operator edits; permission rules are evaluated before first-party tool dispatch.
- Identity / ultimate-policy issue: what the agent is instructed to be/how it must behave, and which classes of tool actions are permitted, require approval or are forbidden even when a model wants to execute them.
- Ultimate authority in each claimed mode: in the claimed parent-governed mode, the operator/user controlling Agent home and Raven configuration is the legitimate ultimate authority; constructor built-in denials remain above ordinary model discretion and no autonomous agent override path is established.
- Return-to-operation path: changed identity files are read into future system context; changed permission rules/mode are applied to future tool decisions, governing later operational turns.
- Why this is / is not agent-owned: Raven agents operate under these identity/policy inputs but no supported autonomous path grants them legitimate final authority to rewrite or bypass operator identity and deny rules.
- Evidence: [`render.py`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/raven/context_engine/segments/render.py); [`agents/README.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/agents/README.md); [`permissions.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/docs-site/docs/permissions.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: session mode changes and smart permission review can alter ordinary operation but do not supersede user deny rules or constructor denials; generic per-action approval is not itself the S5 witness.

## Distributed / OSS / self-hosted notes

- Raven is Apache-2.0 and can run through local process/ACP/self-hosted surfaces; model providers and optional services remain separately configured dependencies.
- External agents connected through ACP/CLI/HTTP do not automatically inherit every Raven permission/isolation guarantee; their native policy boundary remains environmental unless Raven enforcement explicitly reaches it.
- A2A peers are independent remote hosts, not local DAG workers; their autonomy is not imported into Raven's ownership vector.
- EverOS memory is separately distributed; this assessment credits Raven's integration paths, not the service internals as owners.
- Raven is described as pre-alpha at the reviewed revision. Classification records evidenced ownership/closure, not product maturity.

## Recursion

At the assessed recursion level, the Host Agent is the organization-level operational/current-control actor around one objective/session/workspace. Shipped child agents and DAG nodes can form lower-recursion S1 units. Parent/user control remains outside base recursion but is admitted where a supported first-party parent mode closes the same function, as in S3 and S5. Remote A2A peers and standalone Evolver remain separate organizations across explicit boundaries.

## Variety and escalation

Raven absorbs open-ended task variety through the Host Agent model/tool loop and delegates specialized variety through the roster/DAG. Node dependencies, concurrency limits, task charters, permissions and backend capability checks reduce execution variety. Exceptions and failed results return as current-control evidence; the host can continue, replan, abandon or cancel affected work. Parent inspection/steering and ask-tier permissions supply supported escalation. Raven-Code additionally returns machine-read Git blockers through the Harness Manifest so integration decisions need not rely only on worker prose.

## Evidence gaps

- Source/documentation review only at the pinned public revision; no claim of live end-to-end execution of every backend or optional service.
- Third-party agents vary by backend/release; positive claims rely on first-party Raven/Host paths rather than assuming external agents honor Raven steering/permissions.
- S2 is intentionally bounded to Raven-Code stale-edit protection; Raven does not claim general shared-checkout isolation.
- S3* is intentionally bounded to Git/workspace completion evidence for Raven-Code; DAG model verdicts and optional Eval Engine are not promoted to independent audit.
- Optional memory/Skill Hub/proactivity behavior depends on external configuration and is not required for recorded positive states.
- Evolver is present but separate and marked for planned retirement pending sign-off; that lifecycle does not alter the production-runtime S4 boundary.
