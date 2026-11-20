---
harness_id: phimint
project_name: phimint
repository: https://github.com/hibuka-labs/phimint
review_ref: 5db119c9338f7f5844e927a36455fbdddf5f03a4
reviewed_at: 2026-11-20
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: ?
autonomy_s4: P
autonomy_s5: —
---

# phimint

## Review boundary

- System in focus: One phimint terminal installation and its workspace sessions.
- Purpose and identity: Carry out model-backed coding work in a local workspace.
- Relevant environment: Operator, workspace, configured inference endpoints, publisher release mirrors and expressly enabled external integrations.
- Standard-distribution boundary: First-party terminal entry point, bundled library wiring, model/tool assembly, child runtime, external-tool connection and supported standalone updater.
- Credited operating / distribution surfaces: [Binary and features](https://github.com/hibuka-labs/phimint/blob/5db119c9338f7f5844e927a36455fbdddf5f03a4/Cargo.toml) · [Startup and assembly](https://github.com/hibuka-labs/phimint/blob/5db119c9338f7f5844e927a36455fbdddf5f03a4/src/main.rs) · [Agent assembly](https://github.com/hibuka-labs/phimint/blob/5db119c9338f7f5844e927a36455fbdddf5f03a4/src/agent/build.rs) · [Operator modes](https://github.com/hibuka-labs/phimint/blob/5db119c9338f7f5844e927a36455fbdddf5f03a4/README.md)
- Adjacent first-party surfaces excluded from ownership: Contributor instructions, CI, experiments, external tool implementations, and model-provider internals.
- First-party operating / deployment modes considered: Interactive terminal with auto, ask or deny approval modes; read-only and explicitly writable child runs; standalone release update.
- Recursion level: Installation, with root workspace sessions and their delegated child tasks.
- Reviewed revision: 5db119c9338f7f5844e927a36455fbdddf5f03a4
- Observation date: 2026-11-20
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

The shipped binary configures the phi-agent runtime, versioned library dependencies, workspace tools, model routing, approval handling, and the TUI. The root can delegate to children using a product-specific tool inventory. Session history, memory and context rotation support repeated turns. Diagnostics and a compile tool provide task evidence. Tool connections and capability changes happen through the host assembly and operator surfaces.

## Operational model

The root model chooses coding, inspection and verification actions within the session. Child models conduct bounded individual investigations or approved write work. The operator controls the selected run mode, approvals and installed capabilities. The runtime supplies tools and enforces controls.

## S1 — Operations

- State: A
- Function: Perform workspace coding and investigation from a user request.
- Disturbance / variety regulated: Workspace structure and failed edits or checks can require a different next action.
- Decisive decision or feedback right: Select tools or completion and revise actions in response to workspace results.
- Decision owner: Root model, with child models owning delegated task-level decisions in enabled modes.
- Supporting / enforcement mechanisms: Phi runtime, workspace tool assembly, approval enforcement and session records.
- Closure path: Tool output and verification results enter the model's next turn or report.
- Why this is / is not agent-owned: Without the model the assembled tools and approval policy do not select or revise the coding trajectory.
- Boundary reachability: The binary assembles the provider and tool registry in the built-in PhiAgent and enters the shipped interactive shell.
- Evidence: [Entry](https://github.com/hibuka-labs/phimint/blob/5db119c9338f7f5844e927a36455fbdddf5f03a4/src/main.rs) · [Agent builder](https://github.com/hibuka-labs/phimint/blob/5db119c9338f7f5844e927a36455fbdddf5f03a4/src/agent/build.rs) · [Operator usage](https://github.com/hibuka-labs/phimint/blob/5db119c9338f7f5844e927a36455fbdddf5f03a4/README.md)
- Basis: structural
- Confidence: high
- Caveats: Provider operation was assessed through the source wiring.

## S2 — Coordination

- State: —
- Function: Attenuate interference between independently acting workspace units.
- Disturbance / variety regulated: The same workspace or browser view can be affected by concurrent parent and child activity.
- Decisive decision or feedback right: No peer-specific intervention with feedback into subsequent peer operation was established.
- Decision owner: The root delegates work and children choose their scoped operations.
- Supporting / enforcement mechanisms: Read-only default kits, exclusion of browser tools from child rosters, approval inheritance, limits and timeouts.
- Closure path: Child results return through delegation; static separation of browser capability protects the root view.
- Why this is / is not agent-owned: The product preassigns capability boundaries, while the exposed child control path returns task results and timeout errors.
- Evidence: [Child policy and browser contention](https://github.com/hibuka-labs/phimint/blob/5db119c9338f7f5844e927a36455fbdddf5f03a4/src/agent/subagents.rs) · [Child registration and dispatch](https://github.com/hibuka-labs/phimint/blob/5db119c9338f7f5844e927a36455fbdddf5f03a4/src/agent/build.rs) · [Child tool policy tests](https://github.com/hibuka-labs/phimint/blob/5db119c9338f7f5844e927a36455fbdddf5f03a4/src/agent/tests/wiring.rs)
- Basis: structural
- Confidence: medium
- Caveats: Static browser segregation addresses concrete interference but the child path supplies no returned browser-conflict adjustment.

### Absence scope

- Surfaces inspected: Shipped agent assembly, child tool rules, spawn resolver and wiring tests.
- Plausible first-party paths checked: Concurrent workspace work, browser contention, inherited approvals and timeout/error return.
- Why no material first-party path remains: The browser remains outside every child role. Explicit write access and generic task messages expose delegation controls without a peer conflict decision and return loop.

## S3 — Inside-and-now control

- State: —
- Function: Regulate the installation's current shared operational commitments.
- Disturbance / variety regulated: Independent runs could compete for installed tools, workspace access or provider resources.
- Decisive decision or feedback right: No installation-wide current-work judgment and intervention path was established.
- Decision owner: The root controls its delegated task and the operator controls the active session.
- Supporting / enforcement mechanisms: Turn, repeat-tool and child time limits, operator approvals, model switching and run cancellation.
- Closure path: Interventions alter the current task or selected configuration. There is no established portfolio-wide return.
- Why this is / is not agent-owned: Root discretion is expressed within a requested task. Enforcement limits apply to the run or child.
- Evidence: [Run and cancellation wiring](https://github.com/hibuka-labs/phimint/blob/5db119c9338f7f5844e927a36455fbdddf5f03a4/src/main.rs) · [Limits and agent wiring](https://github.com/hibuka-labs/phimint/blob/5db119c9338f7f5844e927a36455fbdddf5f03a4/src/agent/build.rs) · [Session controls](https://github.com/hibuka-labs/phimint/blob/5db119c9338f7f5844e927a36455fbdddf5f03a4/README.md)
- Basis: structural
- Confidence: medium
- Caveats: The assessment boundary is the installation. The root task may contain several child operations.

### Absence scope

- Surfaces inspected: Startup, terminal command surface, child management and run guard assembly.
- Plausible first-party paths checked: Whole-installation view across live work, resource or priority reallocation, and an operator path owning such a loop.
- Why no material first-party path remains: Supported session and child controls act within a selected turn or task. Neither supplies a whole-installation discretionary work and resource view.

## S3* — Complementary audit

- State: ?
- Function: Independently challenge a substantive completion claim and return a corrective finding.
- Disturbance / variety regulated: A coding agent can report completion before workspace evidence supports that report.
- Decisive decision or feedback right: A pinned judge can adjudicate a candidate end condition; its independent evidence access is unresolved.
- Decision owner: Model-backed guard judge for the verdict; root agent for corrective work.
- Supporting / enforcement mechanisms: Pinned model routing, guard middleware and the separate task-level verify tool.
- Closure path: Guard calls are dispatched in the running loop; compiler results can be reflected in later model output.
- Why this is / is not agent-owned: A separate model endpoint can distinguish judge ownership, but that alone leaves the complementary observation boundary unresolved.
- Evidence: [Judge attachment and configuration](https://github.com/hibuka-labs/phimint/blob/5db119c9338f7f5844e927a36455fbdddf5f03a4/src/agent/build.rs) · [Pinned guard forwarding](https://github.com/hibuka-labs/phimint/blob/5db119c9338f7f5844e927a36455fbdddf5f03a4/src/model/lite_pin.rs) · [Ordinary compile feedback](https://github.com/hibuka-labs/phimint/blob/5db119c9338f7f5844e927a36455fbdddf5f03a4/src/tools/verify.rs) · [Verify middleware](https://github.com/hibuka-labs/phimint/blob/5db119c9338f7f5844e927a36455fbdddf5f03a4/src/agent/gate.rs)
- Basis: structural
- Confidence: medium
- Caveats: The product wrapper does not establish whether the locked guard implementation receives evidence independently of normal agent reporting.

## S4 — Outside-and-then intelligence

- State: P
- Function: Adopt a future version of the installed operating capability after observing a publisher release.
- Disturbance / variety regulated: External release channels can supply a newer runtime than the installed binary.
- Decisive decision or feedback right: Decide whether to invoke the standalone replacement for the announced newer release.
- Decision owner: Legitimate installation operator.
- Supporting / enforcement mechanisms: Release manifest comparison, platform matching, archive validation and standalone replacement.
- Closure path: The approved update command replaces the installed executable; restart uses the new runtime.
- Why this is / is not agent-owned: The operator chooses adoption. The startup notice and explicit CLI update are the reachable path; the model is not consulted.
- Boundary reachability: The interactive wiring exposes the release check and directs the operator to the packaged standalone update command.
- External distinction: Configured release manifests provide versions published outside the installation.
- Future / prospective distinction: The available candidate can change subsequent sessions after replacement and restart.
- Adaptation option generated: Compare the published release to the installed version and surface a supported upgrade option.
- Path back into current capability / S3: The explicit update command applies the chosen upgrade to the binary used for subsequent operation.
- Evidence: [Startup notice](https://github.com/hibuka-labs/phimint/blob/5db119c9338f7f5844e927a36455fbdddf5f03a4/src/shell/wire.rs) · [Remote release comparison](https://github.com/hibuka-labs/phimint/blob/5db119c9338f7f5844e927a36455fbdddf5f03a4/src/update/checker.rs) · [Operator update and replacement](https://github.com/hibuka-labs/phimint/blob/5db119c9338f7f5844e927a36455fbdddf5f03a4/src/update/command.rs)
- Basis: structural
- Confidence: medium
- Caveats: Positive parent mode is scoped to standalone builds. Managed installs send the operator to the external package manager.

## S5 — Policy and identity

- State: —
- Function: Resolve an ultimate-policy or installation-identity matter with authoritative return.
- Disturbance / variety regulated: Operators can change approval and tool access as operational risk changes.
- Decisive decision or feedback right: No shipped authority path for deciding the installation's ultimate mission or policy conflicts was established.
- Decision owner: The owner chooses ordinary run permissions and external-tool authorization.
- Supporting / enforcement mechanisms: Tool-scope approval and persistent capability permission state.
- Closure path: The selected tool-access policy and connection settings affect later calls.
- Why this is / is not agent-owned: Tool-level consent and provider identity stamping govern access and display, without resolving the harness's ultimate purpose or policy.
- Evidence: [Runtime permission modes](https://github.com/hibuka-labs/phimint/blob/5db119c9338f7f5844e927a36455fbdddf5f03a4/README.md) · [Capability admission](https://github.com/hibuka-labs/phimint/blob/5db119c9338f7f5844e927a36455fbdddf5f03a4/src/tools/add_tool.rs) · [Runtime model identity stamp](https://github.com/hibuka-labs/phimint/blob/5db119c9338f7f5844e927a36455fbdddf5f03a4/src/model/identity.rs) · [Startup and operator wiring](https://github.com/hibuka-labs/phimint/blob/5db119c9338f7f5844e927a36455fbdddf5f03a4/src/main.rs)
- Basis: structural
- Confidence: medium
- Caveats: The assessment credits the local operating installation. Repository governance and ownership use a different recursion.

### Absence scope

- Surfaces inspected: Startup, approval and tool registration, model identity, external state, and contributor surfaces.
- Plausible first-party paths checked: Live policy authority, dynamic tool approval, and an authoritative mission or S3–S4 policy conflict path.
- Why no material first-party path remains: The operator surfaces resolve routine tool and model choices. The shipped policy mechanisms enforce scoped permission without an ultimate-policy matter and authoritative return.

## Recursion

The installation supplies sessions. Delegated children are scoped operations under one root task; a child runtime does not by itself establish a separate full VSM recursion.

## Variety and escalation

Workspace errors and tool limits return through tool evidence and guard paths. The operator sees approval requests and release notices. These paths have different receiving decisions and scopes.

## Evidence gaps

The locked completion judge's input and independent observation path require direct confirmation to resolve S3*. No live provider, local project execution, or upgrade was performed.
