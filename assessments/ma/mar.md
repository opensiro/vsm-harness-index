---
harness_id: mar
project_name: MAR
repository: https://github.com/myagentroam/mar
review_ref: a4bd266e50a662f12e939fea43121912e39e0780
reviewed_at: 2026-11-20
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: C
autonomy_s4: P
autonomy_s5: —
---

# MAR

## Review boundary

- System in focus: One authorized Node and Workspace using native MAR Agent and the unactivated Community workbench.
- Purpose and identity: Operate coding sessions on a user-controlled workspace, coordinating bounded child or peer contributions and returning evidence.
- Relevant environment: Workspace files, Node resources, owner, configured model services and the Community Server/Console bridge.
- Standard-distribution boundary: Native MAR Agent, Node, and the applicable Apache-2.0 Server Core and Web Core paths used in the documented Community installation.
- Credited operating / distribution surfaces: [Scope and operating modes](https://github.com/myagentroam/mar/blob/a4bd266e50a662f12e939fea43121912e39e0780/README.md) · [Exact licensing scope](https://github.com/myagentroam/mar/blob/a4bd266e50a662f12e939fea43121912e39e0780/LICENSING.md) · [Native session runtime](https://github.com/myagentroam/mar/blob/a4bd266e50a662f12e939fea43121912e39e0780/mar-node/src/runner/mar-agent/session-runtime.ts) · [Agent operations](https://github.com/myagentroam/mar/blob/a4bd266e50a662f12e939fea43121912e39e0780/mar-agent/src/runtime/execution.ts)
- Adjacent first-party surfaces excluded from ownership: Activated Enterprise governance, enterprise-only cross-user authorization or audits, other Runner internals, model services, contributor tooling and demo records. Product composition is source-available under MAR-ESAL-1.0. The independently licensed Agent, Node, Protocol, Server Core, Web Core and marctl paths are Apache-2.0.
- First-party operating / deployment modes considered: Community self-hosted workbench and connected native Node with the Agent Network enabled for authorized workspace sessions.
- Recursion level: The authorized Workspace session portfolio on one Node.
- Reviewed revision: a4bd266e50a662f12e939fea43121912e39e0780
- Observation date: 2026-11-20
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

The Node hosts native MAR Agent execution with durable sessions and an optional Agent Network extension. Workbench sessions reach the Node through the Server. Native child and peer runs have separate histories and relationships. The Node projects current goals, work status and child outcomes while checking owner, workspace and model authorization. The Web Core exposes session views and separate artifact inspection. The licensed product composition and the independently licensed components are distinguished in LICENSING.md.

## Operational model

A native MAR Agent session can carry out workspace work and make tool-path decisions. A child or peer can own a distinct deliverable in a separate execution. The parent session can coordinate or intervene within authorized Workspace boundaries and receive results. The operator can inspect and intervene through the workbench.

## S1 — Operations

- State: A
- Function: Perform model-directed workspace coding and investigation in persistent sessions.
- Disturbance / variety regulated: Workspace state, tool outcomes and evidence change the feasible next actions.
- Decisive decision or feedback right: Choose the next tool or response and revise the operation after observed results.
- Decision owner: The native session model, or the child model for its independent run.
- Supporting / enforcement mechanisms: Node capabilities, SDK tool loop, execution policy, state persistence and workspace authorization.
- Closure path: Tool observations feed later model calls and the durable session result can enter its parent's context.
- Why this is / is not agent-owned: The model chooses and revises operational actions. Approval rules and the owner supply constraints.
- Boundary reachability: Node session runtime creates the native MAR Agent and wires Workspace operations and the optional Agent Network extension in a regular Workspace session.
- Evidence: [Operational execution](https://github.com/myagentroam/mar/blob/a4bd266e50a662f12e939fea43121912e39e0780/mar-agent/src/runtime/execution.ts) · [Product session binding](https://github.com/myagentroam/mar/blob/a4bd266e50a662f12e939fea43121912e39e0780/mar-node/src/runner/mar-agent/session-runtime.ts) · [Operator session usage](https://github.com/myagentroam/mar/blob/a4bd266e50a662f12e939fea43121912e39e0780/docs/help/en-US/runners/mar-agent.md)
- Basis: structural
- Confidence: high
- Caveats: Other Runner decision internals are outside the assessment.

## S2 — Coordination

- State: A
- Function: Partition overlapping work between separately acting native sessions in a shared Workspace.
- Disturbance / variety regulated: Parallel write tasks can target the same paths, and parent and children can duplicate research or implementation.
- Decisive decision or feedback right: Choose a separable objective and read-only or non-overlapping write scope; use received child evidence to adjust subsequent work.
- Decision owner: The coordinating native model in the Agent Network mode.
- Supporting / enforcement mechanisms: Tool-specific coordination instructions, scoped handoffs, parent-linked sessions and automatic status/result return.
- Closure path: The child acts from the scoped handoff. Its terminal evidence returns to the parent model, which can change its own next work or send revised guidance.
- Why this is / is not agent-owned: The coordinator model selects when and how to partition work within the existing Workspace rights. The runtime delivers and observes the decision.
- Boundary reachability: The Node attaches the native extension with an explicit non-overlap coordination instruction and the supported child and feedback tools.
- Distinct S1 units: Independent persistent native sessions can each handle a real deliverable with their own execution and history.
- Inter-S1 disturbance: Concurrent agents sharing workspace files can overwrite work or duplicate an independently assigned task.
- Attenuating coordination relation: The coordinating model hands off separable tasks with a read-only or disjoint write scope, and the parent is instructed to avoid duplicate work while children run.
- Feedback into subsequent S1 behaviour: Child output and terminal observations are returned into the parent context before the next model request, allowing a changed task or follow-up.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The installed extension specifically directs regulated allocation of shared Workspace write scope to reduce overlapping changes, and wires observation of the independent work back to the coordinator.
- Evidence: [Scoped coordination and tool binding](https://github.com/myagentroam/mar/blob/a4bd266e50a662f12e939fea43121912e39e0780/mar-node/src/runner/mar-agent/agent-network-extension.ts) · [Child-result observation](https://github.com/myagentroam/mar/blob/a4bd266e50a662f12e939fea43121912e39e0780/mar-node/src/service/agent-network-observations.ts) · [Collaboration and shared-workspace warning](https://github.com/myagentroam/mar/blob/a4bd266e50a662f12e939fea43121912e39e0780/README.md)
- Basis: structural
- Confidence: medium
- Caveats: Scopes in task text rely on model behavior. No dedicated per-child filesystem reservation or isolation is claimed.

## S3 — Inside-and-now control

- State: A(P)
- Function: Inspect and revise authorized current commitments across a Workspace session portfolio.
- Disturbance / variety regulated: A current Goal can become unnecessary, compete with other work, or need an intervention as session evidence changes.
- Decisive decision or feedback right: Select the target commitment to stop, steer, or revise using visible current state.
- Decision owner: The coordinating model in Agent Network mode, or the actual run owner in the distinct direct workbench mode.
- Supporting / enforcement mechanisms: Bounded session list/view, status and Goal projection, ownership checks, target authorization and run-control machinery.
- Closure path: The selected stop clears its Goal and interrupts the execution. A revised Goal or replacement input changes subsequent work, and returns an operation result.
- Why this is / is not agent-owned: Model or human chooses the affected commitment. Authorization and run control enforce the decision but lack the discretion to choose it.
- Boundary reachability: The native Agent Network exposes actual list/view and stop/Goal operations across authorized sessions. The workbench exposes the same bounded workspace to its owner through session list/tree and run controls.
- Whole-system current view: The portfolio of visible authorized sessions in the chosen Node and Workspace can be listed and refined with state, goals and activity for each session.
- Current-control decision scope: Agent intervention can stop an authorized target or replace its durable Goal. The workbench run owner can independently select and stop or steer current work from the workspace session surfaces.
- Evidence: [Authorized current view](https://github.com/myagentroam/mar/blob/a4bd266e50a662f12e939fea43121912e39e0780/mar-node/src/service/agent-network-list.ts) · [Stop and Goal intervention](https://github.com/myagentroam/mar/blob/a4bd266e50a662f12e939fea43121912e39e0780/mar-node/src/service/agent-network-service.ts) · [Owner intervention from session list/tree](https://github.com/myagentroam/mar/blob/a4bd266e50a662f12e939fea43121912e39e0780/docs/help/en-US/workbench/sessions.md) · [Workbench run control](https://github.com/myagentroam/mar/blob/a4bd266e50a662f12e939fea43121912e39e0780/packages/server-core/src/run-control-routes.ts)
- Basis: structural
- Confidence: medium
- Caveats: Whole-current scope is the authorized Workspace portfolio at one Node. This claim does not extend to other workspaces, users' nondelegated runs or the installation's enterprise estate.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Coordinator native model | Authorized session status or changed whole-work commitments | Select a target from list/view, stop or revise its Goal, and observe the result. | [Authorized current-control service](https://github.com/myagentroam/mar/blob/a4bd266e50a662f12e939fea43121912e39e0780/mar-node/src/service/agent-network-service.ts) |
| Parent (`P`) | Workspace operator with run ownership | User decides to intervene after inspecting the Workspace sessions and goals | Select the relevant session in the workbench and stop or steer its current run. | [Operator controls](https://github.com/myagentroam/mar/blob/a4bd266e50a662f12e939fea43121912e39e0780/docs/help/en-US/workbench/sessions.md) · [Run owner authorization](https://github.com/myagentroam/mar/blob/a4bd266e50a662f12e939fea43121912e39e0780/mar-node/src/service/run-ownership-policy.ts) |

## S3* — Complementary audit

- State: C
- Function: Enable a complementary examination of implementation claims and return findings to ongoing work.
- Disturbance / variety regulated: A session narrative can omit actual workspace changes or defects visible to a reviewer.
- Decisive decision or feedback right: Choose the claim to challenge, inspect raw workspace evidence and issue corrective findings.
- Decision owner: Separately composed review session or human reviewer, with the coordinator or operator acting on its findings.
- Supporting / enforcement mechanisms: Independent session histories and tool access, shared Workspace artifacts, Git/file inspection, review guidance and returned child outcomes.
- Closure path: The reviewer can send its findings or end a child run with them; the coordinator can steer implementation after receiving the result.
- Why this is / is not agent-owned: A first-party constructor combines separate evidence access and a feedback path. The operator or coordinator must compose an adequately independent reviewer and meaningful trigger.
- Boundary reachability: The documented native reviewer pattern can start a separate session with read-only task scope, use Workspace file or Git evidence, and use the same shipped Agent Network to return results.
- Claim being audited: Whether the implementation agent's reported changes and output match the material Workspace artifacts and satisfy the review objective.
- Ordinary reporting path: The implementation session reports in its own transcript and standard child outcome.
- Complementary access path: A separate reviewer session can directly inspect files or Git changes. The operator can inspect patch resources or the net Git state independently of the agent's summary.
- Independence boundary: Reviewer execution and history are separate from implementer reporting. The review must be composed and given direct artifact access rather than only a summary.
- Who acts on findings: The coordinator can return findings to the implementation session through guidance or replacement work. The operator can also send a corrective message.
- Evidence: [Documented independent review pattern](https://github.com/myagentroam/mar/blob/a4bd266e50a662f12e939fea43121912e39e0780/README.md) · [Direct patch resource inspection](https://github.com/myagentroam/mar/blob/a4bd266e50a662f12e939fea43121912e39e0780/packages/web-core/src/service/tool-change-review-service.ts) · [Independent Workspace evidence](https://github.com/myagentroam/mar/blob/a4bd266e50a662f12e939fea43121912e39e0780/docs/help/en-US/workbench/git-changes.md) · [Return and corrective intervention](https://github.com/myagentroam/mar/blob/a4bd266e50a662f12e939fea43121912e39e0780/mar-node/src/service/agent-network-service.ts)
- Basis: structural
- Confidence: medium
- Caveats: Patch resources cover individual apply_patch operations. Git and files are needed for net changes and shell writes. The review role and adequate independence require explicit composition.

## S4 — Outside-and-then intelligence

- State: P
- Function: Introduce an externally observed model option into subsequent Workspace operation.
- Disturbance / variety regulated: The configured provider can list new, removed or changed model options and associated limits.
- Decisive decision or feedback right: Select which observed live provider model to import, configure and use in later work.
- Decision owner: Authorized model owner or administrator.
- Supporting / enforcement mechanisms: Credential-backed live catalog, import form, settings persistence, authorization and runtime model resolution.
- Closure path: Imported model records become candidates for authorized later sessions. The selected use reaches the Node's operating model configuration.
- Why this is / is not agent-owned: The authorized human selects adoption using the externally observed option. Fetching and persisting it are deterministic.
- Boundary reachability: Personal models and credential-backed catalog import are documented in the Community-capable model management surface and wired through Server Core and the Node runner.
- External distinction: The credential-backed provider catalog is fetched live outside the Workspace.
- Future / prospective distinction: Selected imports add a model capability to future native sessions independently of existing model entries.
- Adaptation option generated: A returned provider model and its supported limits form an importable candidate.
- Path back into current capability / S3: The persisted enabled model becomes available in authorized session model selection and affects future execution.
- Evidence: [Provider catalog sensing](https://github.com/myagentroam/mar/blob/a4bd266e50a662f12e939fea43121912e39e0780/packages/server-core/src/credential-catalog-service.ts) · [Config management and import routes](https://github.com/myagentroam/mar/blob/a4bd266e50a662f12e939fea43121912e39e0780/packages/server-core/src/mar-agent-model-routes.ts) · [User-operated adoption and model eligibility](https://github.com/myagentroam/mar/blob/a4bd266e50a662f12e939fea43121912e39e0780/docs/help/en-US/runners/mar-agent.md)
- Basis: structural
- Confidence: medium
- Caveats: The mapped loop does not claim automatic adoption or Enterprise model sharing.

## S5 — Policy and identity

- State: —
- Function: Resolve ultimate policy and identity tensions in the assessed Workspace.
- Disturbance / variety regulated: Persistent instructions, workspace ownership and model eligibility can shape operation.
- Decisive decision or feedback right: No Community Workspace identity-level decision path with an authoritative return is evidenced.
- Decision owner: Operator controls Workspace instructions and approved execution mode.
- Supporting / enforcement mechanisms: Persistent session prompt, Goal settings, run-control ownership and resource authorization.
- Closure path: Next executions take revised prompts or access controls. These are session or resource-level changes.
- Why this is / is not agent-owned: The model exercises task-level and current-control discretion inside existing authority. The operator surfaces do not present an installed ultimate-policy resolution loop at this boundary.
- Evidence: [Persistent session settings](https://github.com/myagentroam/mar/blob/a4bd266e50a662f12e939fea43121912e39e0780/docs/help/en-US/workbench/sessions.md) · [Run and queue controller ownership](https://github.com/myagentroam/mar/blob/a4bd266e50a662f12e939fea43121912e39e0780/mar-node/src/service/run-ownership-policy.ts) · [Operating and model policy modes](https://github.com/myagentroam/mar/blob/a4bd266e50a662f12e939fea43121912e39e0780/docs/help/en-US/runners/mar-agent.md) · [Enterprise boundary](https://github.com/myagentroam/mar/blob/a4bd266e50a662f12e939fea43121912e39e0780/LICENSING.md)
- Basis: structural
- Confidence: medium
- Caveats: Enterprise governance belongs to an excluded mode and was not used to supply a positive claim.

### Absence scope

- Surfaces inspected: Community sessions, persistent prompts and model configuration, Agent Network authority and the edition boundary.
- Plausible first-party paths checked: Owner policy-level changes, standing constraints, and a return path for Community identity or S3–S4 policy decisions.
- Why no material first-party path remains: The shipped owner and model paths govern commitments, per-session instructions or tool and model access. An ultimate identity/policy matter and authoritative Community return were not found.

## Recursion

One authorized Node/Workspace contains root, child and grandchild session relationships. Each credited operational session can own a deliverable. Those relationships alone do not demonstrate another viable-system recursion.

## Variety and escalation

Tool approval requests, child evidence and terminal status feed the relevant humans or models. Direct worktree and per-operation artifacts supply a separate source of evidence. Live model catalogs give the authorized owner prospective options.

## Evidence gaps

The source review did not execute the workbench or a provider. S2 is limited to the documented model-enacted work scope protocol. The assessment excludes Enterprise-only authorities and product licensing beyond the source boundary recorded above.
