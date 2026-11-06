---
harness_id: harniqo
project_name: Harniqo
repository: https://github.com/StateKnot/Harniqo
review_ref: 456f0f92786bd5753b08ec8a3c2db08c69e284dd
reviewed_at: 2026-11-06
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Harniqo

**Proposed canonical disposition:** `excluded-no-agentic-vsm` at this frozen revision. This is a scope finding, not a judgment that its real VM isolation, resource-broker, transport, event-spool, native qualification or desktop engineering work is ineffective. The stated product is a future control center for external agent harnesses; the shipped desktop does not yet connect to one, and the standalone host Modules and qualification harnesses do not constitute a first-party agent-owned operational loop.

## Review boundary

- System in focus: Harniqo's own delivered control-center/desktop distribution plus reusable Linux Runner Modules, restricted model transport, contracts and first-party native qualification tooling.
- Purpose and identity: eventually provision, connect to, operate and compare third-party AI harness sessions across macOS/Windows/Linux clients and cloud/isolated Linux runners.
- Relevant environment: desktop Electron renderer and preload, separate server/VM host, libvirt/QEMU, offline installed modules, contract schemas, qualification operators, provider credentials and *externally authored* Hermes/OpenCode/OpenClaw/Octop/DSH agents.
- Standard-distribution boundary: the runnable desktop is an explicitly disconnected, read-only M1-01 engineering shell; host resource Broker, console capture, event spool and HTTPS upstream transport expose separately invoked interfaces. M2's authenticated product connection, real harness sessions, production Runner allocator and control-plane-to-model integration are unfinished. Do not equate M0 native qualification fixtures with a supported customer execution mode.
- Credited operating / distribution surfaces: [project README](https://github.com/StateKnot/Harniqo/blob/456f0f92786bd5753b08ec8a3c2db08c69e284dd/README.md), [M0/M1/M2 mainline](https://github.com/StateKnot/Harniqo/blob/456f0f92786bd5753b08ec8a3c2db08c69e284dd/docs/planning/MAINLINE.md), [actual renderer](https://github.com/StateKnot/Harniqo/blob/456f0f92786bd5753b08ec8a3c2db08c69e284dd/apps/desktop/src/renderer/main.tsx), [desktop Interface](https://github.com/StateKnot/Harniqo/blob/456f0f92786bd5753b08ec8a3c2db08c69e284dd/apps/desktop/README.md), [Broker service](https://github.com/StateKnot/Harniqo/blob/456f0f92786bd5753b08ec8a3c2db08c69e284dd/apps/runner/resource_broker/SERVICE.md), [event spool](https://github.com/StateKnot/Harniqo/blob/456f0f92786bd5753b08ec8a3c2db08c69e284dd/apps/runner/event-spool/README.md), [egress transport](https://github.com/StateKnot/Harniqo/blob/456f0f92786bd5753b08ec8a3c2db08c69e284dd/apps/model-egress/README.md).
- Adjacent operating surfaces excluded from ownership: the independent Hermes/OpenCode/OpenClaw/Octop/DSH model-and-tool choices exercised by qualification scripts, future M2 product integrations, planned S3/S4/S5-like architecture boxes, externally operated cloud/SaaS control planes and simulation/test stubs. No borrowed model agency.
- First-party operating / deployment modes considered: local/native packaged Electron shell; host-local Broker `check/initialize/serve/watch`, IPC `ensure/renew/observe/revoke`, console capture, isolated event-spool, trusted-caller HTTPS `exchange`; actual M0 technical-qualification probes against external harnesses. Planned team-private and multi-tenant product modes were checked for implementation reachability but are not treated as delivered.
- Recursion level: current project software as a proposed *harness management product*, with isolated deterministic host service Modules; external harnesses are qualification subjects, not Harniqo-owned autonomous S1 units. A future platform could establish a different recursion and require reassessment.
- Reviewed revision: `456f0f92786bd5753b08ec8a3c2db08c69e284dd`.
- Observation date: 2026-11-06.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The Electron main process serves signed-source local assets to a sandboxed renderer. Its only preload exposure is a zero-argument `getRuntimeInfo()` call; the rendered app displays an explicit disconnected state, with no login, model exchange, session opening, tool selection, or authenticated server channel. The separate Broker service handles fixed 1–64 resource templates, immutable host identity/ACL policies and leases through supervised IPC and a watch loop; a raw console store bounds output, an event spool durably buffers scoped event records pending a separately authenticated uploader, and a restricted HTTPS transport sends a *trusted host caller's already-admitted* bytes to fixed routes. None is a model decision-maker or owns a running first-party agent cycle. The M0 reports distinguish real native third-party harness probes from the unfinished product. Evidence: [renderer](https://github.com/StateKnot/Harniqo/blob/456f0f92786bd5753b08ec8a3c2db08c69e284dd/apps/desktop/src/renderer/main.tsx), [desktop limits](https://github.com/StateKnot/Harniqo/blob/456f0f92786bd5753b08ec8a3c2db08c69e284dd/apps/desktop/README.md), [Broker](https://github.com/StateKnot/Harniqo/blob/456f0f92786bd5753b08ec8a3c2db08c69e284dd/apps/runner/resource_broker/README.md), [spool](https://github.com/StateKnot/Harniqo/blob/456f0f92786bd5753b08ec8a3c2db08c69e284dd/apps/runner/event-spool/README.md), [transport](https://github.com/StateKnot/Harniqo/blob/456f0f92786bd5753b08ec8a3c2db08c69e284dd/apps/model-egress/README.md), [M0 outcomes](https://github.com/StateKnot/Harniqo/blob/456f0f92786bd5753b08ec8a3c2db08c69e284dd/docs/planning/M0-RESULTS.md).

**Counterfactual ownership test:** remove the separately installed third-party harnesses and the qualification operators' external model sessions. Harniqo retains a disconnected metadata UI, a working resource lease/watch Module, byte transports, event archives and contract validators, but no first-party owner that chooses an open-ended operational task and revises its tool actions from model/environment feedback. Keeping a simulator or calling a fixed external test script does not recover such an operational S1.

## Operational model

Currently supported pathways: human/trusted operator preconfigures finite VM templates, identity, routes and lease limits → deterministic Broker/watch enforces lifecycle and returns observations; trusted caller may explicitly exchange bytes through fixed HTTPS routes or archive event chunks; desktop reads only its build identity. Qualification scripts invoke external harnesses under a finite test plan and report factual outcomes, not an ongoing first-party customer agent session. M0 marks 4/8 completed, M1 0/8 and real product harness connectivity as later M2 work. These are real technical operations with valuable feedback, but agent-owned adaptive tasks do not close at Harniqo's shipped boundary. [MAINLINE](https://github.com/StateKnot/Harniqo/blob/456f0f92786bd5753b08ec8a3c2db08c69e284dd/docs/planning/MAINLINE.md), [M0 evidence](https://github.com/StateKnot/Harniqo/blob/456f0f92786bd5753b08ec8a3c2db08c69e284dd/docs/planning/M0-RESULTS.md).

## S1 — Operations

- State: —
- Function: first-party autonomous model-bearing harness sessions would perform and adapt meaningful tasks through returned tool/environment observations.
- Disturbance / variety regulated: actual host VM failures, expired leases, unsafe paths, console overflow, unavailable egress, missing cloud connection and external harness qualification outcomes.
- Decisive decision or feedback right: choose and revise substantive model/task actions after returned results; no shipped Harniqo model/task actor has that right.
- Decision owner: trusted host administrator and qualification operator for requested resources/test cases, deterministic service/watch and transport for invariant enforcement, separate third-party harness model for any agent decisions exercised during M0.
- Supporting / enforcement mechanisms: fixed-template Broker, IPC/watch, bounded console/event spool, pre-admitted HTTPS routes and read-only Electron runtime metadata.
- Closure path: requested lease/observation → deterministic host-resource state and return; or operator-selected external harness probe → test receipt. Neither path loops observations into a first-party model that chooses new operational tools.
- Why this is / is not agent-owned: a fixed resource-state reconciler is not an agent deciding goals; the live model/tool loops present only inside separately installed external harness qualification cases.
- Evidence: [read-only desktop](https://github.com/StateKnot/Harniqo/blob/456f0f92786bd5753b08ec8a3c2db08c69e284dd/apps/desktop/README.md), [resource service](https://github.com/StateKnot/Harniqo/blob/456f0f92786bd5753b08ec8a3c2db08c69e284dd/apps/runner/resource_broker/service.py), [native OpenCode qualification](https://github.com/StateKnot/Harniqo/blob/456f0f92786bd5753b08ec8a3c2db08c69e284dd/scripts/qualification/run_opencode_qualification.py), [mainline](https://github.com/StateKnot/Harniqo/blob/456f0f92786bd5753b08ec8a3c2db08c69e284dd/docs/planning/MAINLINE.md).
- Basis: explicit product-status statements plus source-structural negative.
- Confidence: high at the frozen shipped boundary.
- Caveats: some third-party native probes reached genuine model/provider sessions; exclusion does not negate those results. Neither a production native customer session nor independently repeatable model E2E was executed by this Index review.

### Absence scope

- Surfaces inspected: desktop main/preload/renderer Interface, Broker service and IPC, model-egress transport, event spool, M0 qualification scripts and mainline acceptance status.
- Plausible first-party paths checked: external Hermes/OpenCode/Octop live probes, headless Broker/watch, future M2 cloud harness session wiring and planned SDK adapters.
- Why no material first-party path remains: the desktop has no session API; transport explicitly lacks model-admission/session semantics; qualification tests own their schedule and external harness cognition, not an installed Harniqo task agent.

## S2 — Coordination

- State: —
- Function: no first-party coordination of conflicting intents between two autonomous Harniqo-owned S1 task agents is delivered.
- Disturbance / variety regulated: potential simultaneous VM ensure/renew/revoke calls, allocation collisions, lease expiry and concurrent event writes.
- Decisive decision or feedback right: reconcile conflicting *agent commitments* and return modified execution plans to those agents; absent.
- Decision owner: fixed Broker exclusive state/journal and credential-scoped IPC for host resources; external test operator handles multiple distinct provider harness cases.
- Supporting / enforcement mechanisms: pre-registered resource IDs, finite leases, watcher, immutable journal and spool sequence/ACK constraints.
- Closure path: resource reconciliation can preserve or terminate a VM; no returned inter-agent task coordination path exists in the disconnected product.
- Why this is / is not agent-owned: resource lock/lease integrity is an important substrate for a future S2, but no first-party S1 workers presently coordinate through it.
- Evidence: [Broker README](https://github.com/StateKnot/Harniqo/blob/456f0f92786bd5753b08ec8a3c2db08c69e284dd/apps/runner/resource_broker/README.md), [IPC contract](https://github.com/StateKnot/Harniqo/blob/456f0f92786bd5753b08ec8a3c2db08c69e284dd/apps/runner/resource_broker/IPC.md), [event spool](https://github.com/StateKnot/Harniqo/blob/456f0f92786bd5753b08ec8a3c2db08c69e284dd/apps/runner/event-spool/README.md).
- Basis: structural negative.
- Confidence: high.
- Caveats: the broker actually regulates shared host resources; `—` means no demonstrated inter-S1 VSM function, not no useful mutual exclusion.

### Absence scope

- Surfaces inspected: Broker instance group and lease API, IPC identity binding, spool uniqueness and roadmap for multi-harness integration.
- Plausible first-party paths checked: concurrent callers to a single Broker, independent VM watchdog, multiple external agent probes and possible distributed parent mode.
- Why no material first-party path remains: identities refer to caller/resource authorization and test fixtures rather than two supported Harniqo-owned S1 decision loops that receive coordination feedback.

## S3 — Inside-and-now control

- State: —
- Function: no delivered whole-agent-portfolio current control over active task priorities, resource tradeoffs and operational commitments.
- Disturbance / variety regulated: VM lifecycle, CPU/memory limits, credential admission, current status data and qualification capacity.
- Decisive decision or feedback right: observe current agent portfolio and reallocate/reprioritize work through a binding managerial intervention; not shipped.
- Decision owner: host admin fixes immutable template/lease policy, supervisor/operator invokes resource operations, deterministic watcher enforces lease and state.
- Supporting / enforcement mechanisms: Broker observation, host cgroup thresholds and local event receipts; unimplemented M1 control-plane UI and M2 orchestration.
- Closure path: watcher produces VM correction/stop on lease/resource conditions, but there is no current agent-task control panel returning decisions to owned first-party S1 workers.
- Why this is / is not agent-owned: automatic safety stop and status counters are fixed host protections, not a deliberative whole-system task-controller.
- Evidence: [Broker service](https://github.com/StateKnot/Harniqo/blob/456f0f92786bd5753b08ec8a3c2db08c69e284dd/apps/runner/resource_broker/SERVICE.md), [model-egress omissions](https://github.com/StateKnot/Harniqo/blob/456f0f92786bd5753b08ec8a3c2db08c69e284dd/apps/model-egress/README.md), [M0/M1/M2 mainline](https://github.com/StateKnot/Harniqo/blob/456f0f92786bd5753b08ec8a3c2db08c69e284dd/docs/planning/MAINLINE.md).
- Basis: explicit incomplete integration plus structural negative.
- Confidence: high.
- Caveats: robust host-state feedback exists but currently ends at resource safety rather than portfolio-level agent action control.

### Absence scope

- Surfaces inspected: resource limits and watcher, IPC status, client renderer/IPC, model egress and control-plane milestones.
- Plausible first-party paths checked: up to 64 fixed instances as an operational portfolio, native M0 evidence collection and future parent private-host/SaaS modes.
- Why no material first-party path remains: running VM instances alone do not constitute active agent S1 goals and commitments, and no shipped managerial action returns to them.

## S3* — Complementary audit

- State: —
- Function: no independent complementary audit of first-party S1 outcome claims with a corrective return to current control.
- Disturbance / variety regulated: false VM/service readiness, unsafe source assertions, test/guest event mismatch and missed loss/replay gaps.
- Decisive decision or feedback right: independently challenge completed operational agent claims and require changes to whole-current execution; not present.
- Decision owner: qualification operator, deterministic checks, independent host test/audit scripts and manual acceptance own *technical evidence*, not an agent-organization S3* function over an S1 task portfolio.
- Supporting / enforcement mechanisms: source hashes, native smoke identity checks, event receipts, dedicated-VM audit and preservation of failed probes.
- Closure path: evidence checks accept/reject native qualification and preserve failures; no independent result judgment is returned to a delivered Harniqo agent-control loop.
- Why this is / is not agent-owned: tested separate native audit is credited as real technical assurance, but neither S1 task outcome ownership nor S3* corrective intervention exists in the product.
- Evidence: [M0 evidence boundaries](https://github.com/StateKnot/Harniqo/blob/456f0f92786bd5753b08ec8a3c2db08c69e284dd/docs/planning/M0-RESULTS.md), [desktop native smoke](https://github.com/StateKnot/Harniqo/blob/456f0f92786bd5753b08ec8a3c2db08c69e284dd/apps/desktop/src/main/smoke.ts), [spool ack](https://github.com/StateKnot/Harniqo/blob/456f0f92786bd5753b08ec8a3c2db08c69e284dd/apps/runner/event-spool/README.md).
- Basis: explicit source boundaries and structural negative.
- Confidence: medium-high.
- Caveats: this is not a claim that native qualification has no independent verification, only that its subject is infrastructure rather than a shipped first-party agent S1 result.

### Absence scope

- Surfaces inspected: M0 real-host reports and second-party checks, native desktop smoke, event authenticity/ACK constraints and acceptance gates.
- Plausible first-party paths checked: dedicated VM independent inspector, test replay, parallel contract CI and later comparative eval UI.
- Why no material first-party path remains: technical qualification checks validate bounded premises and have no corrective binding return into a current agent task organization.

## S4 — Outside-and-then intelligence

- State: —
- Function: no delivered prospective scan of a changing operating environment feeding durable first-party agent capability adaptation.
- Disturbance / variety regulated: future provider/harness diversity, model API compatibility, OS packages, VM limits and product requirements.
- Decisive decision or feedback right: choose future capability changes from prospective alternatives and return authorized redesign into autonomous operations; absent.
- Decision owner: human product authors, roadmap and research documents; qualification operators perform fixed candidate evaluations.
- Supporting / enforcement mechanisms: M0 compatibility matrix, research, backlog, schema contracts and planned M4 comparison.
- Closure path: research and test findings can guide a human's later engineering milestone; no shipped agent-governed future adaptation returns to a first-party operational S1.
- Why this is / is not agent-owned: a serious roadmap and technical selection are not by themselves an active S4 feedback loop in the assessed running product.
- Evidence: [mainline](https://github.com/StateKnot/Harniqo/blob/456f0f92786bd5753b08ec8a3c2db08c69e284dd/docs/planning/MAINLINE.md), [multi-harness research](https://github.com/StateKnot/Harniqo/blob/456f0f92786bd5753b08ec8a3c2db08c69e284dd/research/multi-harness-client-research.md), [roadmap](https://github.com/StateKnot/Harniqo/blob/456f0f92786bd5753b08ec8a3c2db08c69e284dd/docs/planning/ROADMAP.md).
- Basis: explicit planning vs operation distinction.
- Confidence: high.
- Caveats: human-led compatibility intelligence genuinely informs development but is not credited as an operating autonomous harness S4.

### Absence scope

- Surfaces inspected: product roadmap, M0 acceptance/results, research and release criteria, shipped desktop and transport interfaces.
- Plausible first-party paths checked: cross-harness evaluation comparisons, roadmap migration and future adaptive provider selection.
- Why no material first-party path remains: future roadmap/comparison is not an exercised returning adaptation cycle; model choice in external tests is fixed by operator.

## S5 — Policy and identity

- State: —
- Function: no first-party agent-organization constitutional identity/purpose adjudicator with binding return to operational units.
- Disturbance / variety regulated: unauthorized guest execution, secret propagation, tenant/resource identity confusion and future product vs OSS mission conflicts.
- Decisive decision or feedback right: decide ultimate purpose and resolve policy identity disputes for a running first-party agent organization; not wired.
- Decision owner: human developer/administrator controls OSS mission, fixed trust contracts, peer authorization, allowed routes and project backlog.
- Supporting / enforcement mechanisms: immutable Broker/IPC configuration, ACL and source checks, restricted HTTPS destinations, security-conscious Electron sandbox.
- Closure path: human-authored restrictions enforce transport/resource operations and reject unsafe requests, but no S5 legitimacy decision closes to an autonomous Harniqo S1.
- Why this is / is not agent-owned: authentication and security policy are important preconditions, not evidence of a legitimate ultimate-policy agent function at an unimplemented harness-platform recursion.
- Evidence: [Broker strict service contract](https://github.com/StateKnot/Harniqo/blob/456f0f92786bd5753b08ec8a3c2db08c69e284dd/apps/runner/resource_broker/SERVICE.md), [HTTPS route authorization limitations](https://github.com/StateKnot/Harniqo/blob/456f0f92786bd5753b08ec8a3c2db08c69e284dd/apps/model-egress/README.md), [desktop sandbox](https://github.com/StateKnot/Harniqo/blob/456f0f92786bd5753b08ec8a3c2db08c69e284dd/apps/desktop/README.md).
- Basis: explicit fixed-policy boundary plus structural negative.
- Confidence: high.
- Caveats: future private-deployment or SaaS governance may develop legitimate S5, but it is not a shipped source-only property here.

### Absence scope

- Surfaces inspected: product identity/roadmap, fixed host/VM identity and ACL, transport routes, security interface and multi-tenant plan.
- Plausible first-party paths checked: host administrator as parent authority, dedicated supervisor identity, tenant authorization and OSS project maintainer policy.
- Why no material first-party path remains: current authorization checks protect components, without any running agent organization receiving an ultimate-policy decision.

## Distributed OSS parent arrangement

The repository has a human-led development roadmap and M0 qualification effort. Separate external harness projects and their operators retain model/task decision rights. No released Harniqo parent agent organization is established by multiple supported deployments, qualification agents or proposed private/SaaS modes.

## Self-hosted and non-human modes

The Broker, watcher, event-spool and restricted HTTPS transport can be independently invoked by trusted host software and include automatic deterministic resource-failure responses. The actual desktop reads metadata only. No supported unattended non-human **task-agent** mode owns a provider loop and tool feedback; external model sessions in M0 are bounded qualification cases.

## Recursion

Host resources and VM processes are subcomponents of future execution infrastructure, not independently owned Harniqo agentic S1 units. Raising the recursion to a hypothetical SaaS organization or external harness coalition would import owners not implemented at the frozen product boundary.

## Variety and escalation

Lease expiry, guest failure, unsafe identity and spool pressure can trigger safe rejection, reconciliation or stop. External technical results inform human milestone acceptance. These are concrete host/quality controls, but the feedback has no first-party model-task action selection at S1 or higher VSM re-entry.

## Evidence gaps

- The assessment is frozen-source/structural; it did not rerun native KVM qualification, external paid models, a packaged Electron app or multi-OS build. Reported M0 success is credited only to its described bounded verification scope.
- Future M1/M2 implementation may enable genuine native harness sessions; re-evaluate that later commit rather than projecting planned functions backward.
- Absence is bounded to the inspected first-party standard distribution, host Modules, qualification paths and documented legitimate modes. No claim is made about private, unpublished Harniqo installations.
