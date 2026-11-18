---
harness_id: octopus-si-os
project_name: Octopus SI OS
repository: https://github.com/miuuyy/Octopus-SI-OS
review_ref: 68fd20dc7432909f964f9378b52b71b508e0185f
reviewed_at: 2026-11-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: ?
autonomy_s5: P
---

# Octopus SI OS

## Review boundary

- System in focus: One operator-owned Octopus installation, with a named project EE and its persistent model-driven worker runs as the operational cells. Project-local parent decisions are distinguished from the application's developers.
- Purpose and identity: Pursue an operator-defined project goal through persistent agent tasks using a registry of declared interfaces, workers, tool rooms, and controlled artifact exchanges.
- Relevant environment: Operator requests, files, applications, sensors and other World-facing interfaces, configured model services, changing project needs, and work/evidence arriving at persistent checkpoints.
- Standard-distribution boundary: Shipped Rust kernel, policy/grant and verifier crates, registry descriptors and life processes, first-party macOS client/CLI, and a configured provider running Codex-backed worker turns. Provider inference and user-added code are external.
- Credited operating / distribution surfaces: Runtime-formed grants and persisted run/checkpoint paths, installed project/agent/task and operator views, worker and interface registries, owner-installed extensions and drivers when bound and permitted.
- Adjacent first-party surfaces excluded from ownership: Repository development, CI, uninstalled registry examples, standalone companion benchmarks under `examples/`, future exploratory scenarios, and provider-internal decisions/code not in the checked distribution.
- First-party operating / deployment modes considered: Supported macOS operator installation with the bundled Codex provider bridge, project worker tasks, optional concurrent run/checkpoint dependencies, user-approved project permission setup and registry edits.
- Recursion level: The project delivery organization inside the owner's Octopus installation. A worker/EE nesting does not automatically establish an autonomous higher VSM recursion.
- Reviewed revision: `68fd20dc7432909f964f9378b52b71b508e0185f`.
- Observation date: 2026-11-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The Rust runtime stores runs, EEs, artifact movements and checkpoints durably. The active worker is a descriptor pin, not a process; model-driven sessions are invoked through provider interfaces. Each arriving artifact is admitted through first-party policy formation, checked against the worker ceiling, EE chain and authored bindings, and recorded in the append-only movement ledger. Verifier packages may gate individual checkpoint requirements before a mark is admitted. The UI projects Projects, Agents, Tasks and the movement ledger for the owner. Capabilities may be extended with first-party registry semantics, but installing a descriptor does not demonstrate a currently exercised model-owned strategic control loop. The project's scenarios expressly describe intended possibilities rather than tested ready-to-use workflows.

## Operational model

A project has a persisted goal and permissions; its model-backed worker runs use granted external interfaces, tools and artifacts to produce task outputs. Distinct worker runs can exchange artifacts and wait on predecessor checkpoints. The operator establishes the project's mission and execution boundary, reviews current tasks and their direct evidence, and may choose drivers, capability ceilings and per-task intervention. Deterministic grants, verification and ledger logging constrain actions without automatically owning the organizational decisions they enforce.

## S1 — Operations

- State: A
- Function: Model-backed worker execution of an operator's project tasks and admitted external events.
- Disturbance / variety regulated: Variable user tasks, external tool results, unknown code/files and provider replies.
- Decisive decision or feedback right: Choose substantive next tool, artifact output and work within the run's current grant.
- Decision owner: Active model-backed worker session; kernel owns admissible transitions, not the worker's task judgment.
- Supporting / enforcement mechanisms: Runtime checkpoint ledger, policy grant, bound provider, room executor and typed interface movements.
- Closure path: Model emits tool requests and receives admitted result artifacts, then continues or returns an output to its operator-facing interface.
- Boundary reachability: Supported macOS installation bundles a Codex provider path and shipped worker/room/interface templates capable of executing a model-driven task.
- Why this is / is not agent-owned: Tool selection and task content are chosen by the model, while interface movement and grants are first-party deterministic support.
- Evidence: [runtime model/provider loop](https://github.com/miuuyy/Octopus-SI-OS/blob/68fd20dc7432909f964f9378b52b71b508e0185f/docs/architecture.md#L286-L326), [worker/run bindings](https://github.com/miuuyy/Octopus-SI-OS/blob/68fd20dc7432909f964f9378b52b71b508e0185f/docs/contracts/WORKER_TYPES.md#L49-L96), [supported provider boundary](https://github.com/miuuyy/Octopus-SI-OS/blob/68fd20dc7432909f964f9378b52b71b508e0185f/README.md#L24-L43), [policy formation](https://github.com/miuuyy/Octopus-SI-OS/blob/68fd20dc7432909f964f9378b52b71b508e0185f/docs/contracts/POLICY.md#L42-L70).
- Basis: structural
- Confidence: medium
- Caveats: Only one provider path is reported end-to-end in this preview; external model behavior was not executed in this review.

## S2 — Coordination

- State: —
- Function: No shipped, S2-specific inter-S1 interference regulation with a closed corrective return was established at the reviewed project boundary.
- Disturbance / variety regulated: Concurrent worker runs can compete for project artifacts, source paths or execution capacity, but merely sharing a project/ledger does not demonstrate a specific mutual-adjustment disturbance.
- Decisive decision or feedback right: Runtime checks legal grants, moves artifacts and waits on checkpoint dependencies; no evidenced S2-specific actor choosing or revising conflict-attenuating relations for distinct S1 workers.
- Decision owner: Authoring model/developer owns ordinary run task planning; deterministic kernel owns route and grant enforcement.
- Supporting / enforcement mechanisms: Per-EE authority narrowing, awaited artifact/mark dependencies, optional worktree driver and gate refusals.
- Closure path: Dependency markers can allow a later run to proceed, and policy gates can refuse unauthorized use; those alone do not establish feedback that regulates a concrete inter-unit conflict.
- Why this is / is not agent-owned: A worker handoff and a general permissions intersection do not decide how to resolve competing operational commitments or an identified harmful oscillation.
- Evidence: [authored delegation graph](https://github.com/miuuyy/Octopus-SI-OS/blob/68fd20dc7432909f964f9378b52b71b508e0185f/docs/contracts/WORKER_TYPES.md#L91-L112), [marks as dependencies](https://github.com/miuuyy/Octopus-SI-OS/blob/68fd20dc7432909f964f9378b52b71b508e0185f/docs/contracts/VERIFIERS.md#L186-L199), [hierarchical policy narrowing](https://github.com/miuuyy/Octopus-SI-OS/blob/68fd20dc7432909f964f9378b52b71b508e0185f/docs/contracts/POLICY.md#L110-L157), [optional worktree driver](https://github.com/miuuyy/Octopus-SI-OS/blob/68fd20dc7432909f964f9378b52b71b508e0185f/docs/client.md#L162-L171).
- Basis: structural
- Confidence: medium
- Caveats: A custom configuration can express explicit cross-worker reservations or conflict remediation. It is not credited without a checked shipped path satisfying the function-specific test.

### Absence scope

- Surfaces inspected: Worker/EE architecture and contracts, verifier/mark dependencies, grant policy, bundled client task/worktree surface and runtime source ownership.
- Plausible first-party paths checked: Worker handoff, checkpoint wait graph, per-EE narrowing, branch isolation and event/ledger routing as potential S2 coordination.
- Why no material first-party path remains: The inspected standard paths provide valid sequencing, isolation and authority enforcement but do not evidence a specific actual or structurally observed inter-worker interference, an actor selecting its attenuation, and corrective return into later distinct S1 behavior together.

## S3 — Inside-and-now control

- State: P
- Function: Operator's supervision of current project operations and their permitted working resources.
- Disturbance / variety regulated: Multiple project tasks and drivers run within a shared owner account, potentially exceeding the owner's current priorities, access allowance or permitted work.
- Decisive decision or feedback right: Choose current project access/driver boundary and agents, inspect running work/evidence, and stop a requested operation or withhold an unapproved installation.
- Decision owner: The installation/project owner through shipped authenticated client/terminal control, not the model or kernel.
- Supporting / enforcement mechanisms: Project and task lists, source-folder/driver configuration, operator Inbox and movement dashboard, kernel formed grants and task-stop behavior.
- Closure path: Changes to project EE and permitted drivers bind later tasks; stopping an active Home operation prevents its pending changes; approved/denied package actions alter what subsequent runs may use.
- Boundary reachability: Bundled client exposes Projects, Agents, Tasks, Drivers, Inbox and Dashboard; operator actions project into underlying EE/configuration and task execution.
- Why this is / is not agent-owned: Operator chooses current shared commitments and access boundaries; deterministic grant and client UI do not thereby own the decision.
- Whole-system current view: The operator's Tasks/Projects and Dashboard project named EEs, active task histories, worker rooms, arrivals and marks rather than one model's private narrative.
- Current-control decision scope: Set execution-environment scope of active project work, approve current capabilities, stop pending Home changes and choose the operational room for new tasks.
- Evidence: [project agent/task and permission controls](https://github.com/miuuyy/Octopus-SI-OS/blob/68fd20dc7432909f964f9378b52b71b508e0185f/docs/client.md#L127-L171), [live current evidence UI](https://github.com/miuuyy/Octopus-SI-OS/blob/68fd20dc7432909f964f9378b52b71b508e0185f/docs/client.md#L180-L206), [stop prevents subsequent requested effects](https://github.com/miuuyy/Octopus-SI-OS/blob/68fd20dc7432909f964f9378b52b71b508e0185f/docs/client.md#L325-L338), [project policy and run relocation](https://github.com/miuuyy/Octopus-SI-OS/blob/68fd20dc7432909f964f9378b52b71b508e0185f/docs/contracts/ENVIRONMENTS.md#L16-L60).
- Basis: structural
- Confidence: medium
- Caveats: A UI's visual task order is not an execution-priority control; ordinary per-tool approval does not become autonomous S3. Parent credit is restricted to supported project-level operator interventions.

## S3* — Complementary audit

- State: —
- Function: No separately owned complementary audit of operational reality feeding current control was demonstrated beyond routine checkpoint evidence validation.
- Disturbance / variety regulated: A model might claim a result without it being correct or safe.
- Decisive decision or feedback right: Checkpoint's explicitly bound verifier decides whether its evidence artifact satisfies its regular condition; there is no shipped independent sporadic audit controller.
- Decision owner: Deterministic verifier package owns the check at ordinary artifact admission; operator may inspect ledger but no independent audit-to-intervention loop is established.
- Supporting / enforcement mechanisms: Verifier package script, movement ledger, mark names and dashboard movements.
- Closure path: A failed ordinary verification prevents the checkpoint mark and is recorded. It is not separate complementary access returned to a higher-level S3 reviewer.
- Why this is / is not agent-owned: The model does not emit marks; script gating is distinct from the model, but independence of implementation alone does not make routine acceptance S3*.
- Evidence: [verifier is mandatory edge check](https://github.com/miuuyy/Octopus-SI-OS/blob/68fd20dc7432909f964f9378b52b71b508e0185f/docs/contracts/VERIFIERS.md#L1-L49), [verifier cannot wake/edit control](https://github.com/miuuyy/Octopus-SI-OS/blob/68fd20dc7432909f964f9378b52b71b508e0185f/docs/contracts/VERIFIERS.md#L79-L102), [mark limitations](https://github.com/miuuyy/Octopus-SI-OS/blob/68fd20dc7432909f964f9378b52b71b508e0185f/docs/contracts/VERIFIERS.md#L207-L214), [operator ledger is observational](https://github.com/miuuyy/Octopus-SI-OS/blob/68fd20dc7432909f964f9378b52b71b508e0185f/docs/client.md#L191-L202).
- Basis: structural
- Confidence: medium
- Caveats: A separate audit verifier and escalation could be composed, but no source-backed independent sampling/probing/claim-correction closure was identified in the shipped project mode.

### Absence scope

- Surfaces inspected: Verifier/mark implementation contracts, ledger and movement viewer, worker run checking and operator review entry points.
- Plausible first-party paths checked: External verifier scripts as independent audit, marks/proofs as audit decisions, ledger as alternative reality channel and human Inbox inspection.
- Why no material first-party path remains: Verifiers are ordinary required artifact-edge gates that cannot initiate an independent audit or revise control, and ledger displays do not supply a separate audit judgment/returned corrective control path.

## S4 — Outside-and-then intelligence

- State: ?
- Function: An external-and-prospective adaptation loop is plausible through live interface/goal/tool changes but its first-party closure is unresolved.
- Disturbance / variety regulated: Changing environmental needs, novel sensors, triggers and model/tool capabilities may require different future operating affordances.
- Decisive decision or feedback right: Under granted rights, a worker can author new interface/worker/goal descriptors and bind capabilities to later runs; it is not established whether the shipped model currently selects future-oriented options from environmental distinctions rather than merely responding to a requested implementation task.
- Decision owner: Model can select task-local authored changes; future adaptation judgment at project/installation scope not independently established.
- Supporting / enforcement mechanisms: Registry live discovery, authorized file changes, EE descriptors, verifiers and persisted run/checkpoint bindings.
- Closure path: Successfully installed interfaces and modified triggers may change what subsequent runs can see/do; specific prospective diagnosis → adapted option → present project control reconciliation is not source-proven.
- Why this is / is not agent-owned: The live construction and persistence mechanism is first-party and reachable in granted modes, but a constructor substrate is not the S4 function itself.
- Evidence: [native environment modifications](https://github.com/miuuyy/Octopus-SI-OS/blob/68fd20dc7432909f964f9378b52b71b508e0185f/docs/architecture.md#L606-L637), [extension packaging and execution boundary](https://github.com/miuuyy/Octopus-SI-OS/blob/68fd20dc7432909f964f9378b52b71b508e0185f/docs/contracts/EXTENSION_SURFACES.md#L5-L79), [illustrative scenarios not verified products](https://github.com/miuuyy/Octopus-SI-OS/blob/68fd20dc7432909f964f9378b52b71b508e0185f/docs/scenarios.md#L1-L11), [models do not yet take initiative](https://github.com/miuuyy/Octopus-SI-OS/blob/68fd20dc7432909f964f9378b52b71b508e0185f/docs/architecture.md#L641-L657).
- Basis: structural
- Confidence: low
- Caveats: Unresolved supported-path distinction: whether any first-party configured model mode actually detects future environmental change, adjudicates adaptation options and returns them into a changed current capability. The docs expressly report unobserved model initiative.

## S5 — Policy and identity

- State: P
- Function: Define the project's ultimate goal and allowable operating authority under a legitimate human parent.
- Disturbance / variety regulated: The project must retain its selected mission and capability boundary despite changes in worker requests or proposed self-modifications.
- Decisive decision or feedback right: Operator establishes project EE goal and permission boundary, selects the allowed worker/tool scope, and can refuse untrusted/undesired client capabilities.
- Decision owner: Authenticated installation owner acting as parent at this project recursion; kernel and models only obey/enforce granted policy.
- Supporting / enforcement mechanisms: Persisted EE goal and narrowing, owner project settings, worker ceiling, grant formation and client installation-review gate.
- Closure path: Owner chooses project mission/permissions → EE and worker configuration written into persistent registry/state → runtime re-forms grants from those policy inputs on later arrivals → subsequent operations are constrained accordingly.
- Boundary reachability: The bundled client creates project EEs and applies an owner-chosen project goal/permission scope; subsequent tasks pin the agent and project.
- Why this is / is not agent-owned: The owner retains authority to define the project identity/mandate, while a model's file writes cannot widen an existing grant by declaring its own rights.
- Identity / ultimate-policy issue: Which project purpose and authority envelope constitute legitimate activity for the project, not an ordinary approval over one tool call.
- Ultimate authority in each claimed mode: One operator for the project; no autonomous S5 A/C mode is credited.
- Return-to-operation path: Owner project EE decision and capability setup → persisted records → runtime recomputes legal grants → later worker turns execute only within the resulting mandate.
- Evidence: [project goal and policies](https://github.com/miuuyy/Octopus-SI-OS/blob/68fd20dc7432909f964f9378b52b71b508e0185f/docs/contracts/ENVIRONMENTS.md#L16-L48), [client creates goals, access and agents](https://github.com/miuuyy/Octopus-SI-OS/blob/68fd20dc7432909f964f9378b52b71b508e0185f/docs/client.md#L127-L171), [grant re-formation rather than model authority](https://github.com/miuuyy/Octopus-SI-OS/blob/68fd20dc7432909f964f9378b52b71b508e0185f/docs/contracts/POLICY.md#L12-L64), [trusted owner vs untrusted model](https://github.com/miuuyy/Octopus-SI-OS/blob/68fd20dc7432909f964f9378b52b71b508e0185f/docs/security-model.md#L5-L43).
- Basis: structural
- Confidence: medium
- Caveats: This is project-local legitimate parent mission/authority, not a claim that the open-source repository maintainer or a model autonomously decides Octopus-wide ultimate identity. An ordinary policy check/approval would not suffice without this project goal-to-future-task link.

## Distributed OSS parent arrangement

Only the owner of the installed project has the claimed S3/S5 parent authority. Maintainers and issue/PR reviewers of the public Octopus implementation govern an adjacent development organization and are not imported into the deployed project boundary.

## Self-hosted and non-human modes

The kernel can operate without its desktop client, but these specific P states are bound to a supported operator-owned deployment with project setup and control surfaces. No independent nonhuman S3/S5 mode was established. Descriptor existence and the research scenario catalog do not prove an installed autonomous organization has the claimed additional systems.

## Recursion

Nested EEs and worker pin references are structural organization scopes, not a demonstration of nested viable systems. The project is the assessed recursion; its workers contribute operational actions, but their complete internal metasystems are unproven.

## Variety and escalation

The intersection of worker ceiling, EE chain and run bindings limits authority variety; typed checkpoint evidence and ledger movements preserve failed operations and future resumption. A task can return to owner control through UI interaction. A model changing a registry descriptor under granted rights remains distinct from the operator's ultimate-policy decision.

## Evidence gaps

Source-based review of the pinned public tree, docs and associated Rust policy/verifier runtime surfaces. No macOS runtime, model provider or user-deployed sensor was exercised; no independent S3* audit or autonomous S4 future adaptation was observed. The S4 `?` intentionally preserves uncertainty about the unproven initiative-to-capability closure, not a claim of demonstrated self-improvement.
