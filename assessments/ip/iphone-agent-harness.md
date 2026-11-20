---
harness_id: iphone-agent-harness
project_name: iPhone Agent Harness
repository: https://github.com/cccat6/iphone-agent-harness
review_ref: b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f
reviewed_at: 2026-11-20
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# iPhone Agent Harness

## Review boundary

- System in focus: the shipped browser-local Safari/iPhone automation harness and accompanying ESP32 firmware, configured with an external model and one or two phone targets over local WebRTC/Bluetooth; no physical run performed.
- Purpose and identity: execute a human-requested iPhone workflow by reading screen frames, obtaining a model-authored phone action plan, safely applying bounded HID inputs, and checking observed consequences.
- Relevant environment: iOS app screens and dynamic layouts, phone orientation, Bluetooth input, local Wi-Fi and ESP32 state, selected provider API, optional authorised MCP tools and browser-local user settings.
- Standard-distribution boundary: `apps/web/core/`, bundled prompts, skills and static browser UI plus `firmware/IPhoneAutomationHarness/` ESP32 bridge; external model internals, iOS apps, MCP servers, Apple Shortcuts and public hosted community are dependencies/adjacent systems.
- Credited operating / distribution surfaces: `apps/web/core/{harness,plan,capture,device-rtc,store,skills,prompt}.js`, bundled prompts/skill defaults, ESP32 firmware's `RtcPeerOwnership.h` and input transport, configured model reply-to-tool execution path.
- Adjacent first-party surfaces excluded from ownership: public skill publisher/community and operator/maintainer governance, static-site deployment, first-party CI/test simulations and prerecorded demonstration, documentation about future releases and external provider models' own autonomous reasoning or policy.
- First-party operating / deployment modes considered: normal Safari conversation auto/task execution with optional model, one phone and one run, shared ESP32 with up to two concurrent independent Harness clients/target phones, human Stop/pause/resume and per-task review/settings modes.
- Recursion level: each independent phone-workflow actor as an S1 unit; shared target lease between concurrent browser agents is a narrow S2 function in the bridge composite. No implied organizational S3/S5 from the device's internal FSM.
- Reviewed revision: `b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f`.
- Observation date: 2026-11-20.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The Safari runtime holds local conversation, captures and API credentials. It obtains model responses with fixed tools such as `phone_observe`, `phone_execute_plan` and `task_report`. A model-proposed bounded plan is validated in `apps/web/core/plan.js` against trusted session/target/frame/orientation and input-release state before any mutation. The browser compiles gestures and dispatches them to the ESP32 over WebRTC; the MCU sends Bluetooth keyboard/pointer reports and returns receipts. The browser waits on released input before capture, stores fresh evidence, reconciles uncertain input and requires real observed frame IDs before accepting a completion report. The default completion mode additionally returns visibly to Harness. `apps/web/core/store.js` prevents two competing tabs running the same session.

The bridge explicitly supports two independent WebRTC clients/phone targets. Firmware `RtcPeerOwnership` records client and target lease ownership per peer and `claim` forgets prior leases for the same target; subsequent mutations require the current matching lease/identity, attenuating simultaneous competing writers. This bridge-level S2-specific construction is narrower than general multi-agent project coordination. It is not an S3 scheduler of budgets, commitments or priorities and does not generate a distinct independent S3* audit judgment. Browser screenshots are ordinary same-agent operational feedback, not a separate auditor. External Web/MCP/skill features are task-level capabilities, not a standing S4 intelligence office.

Principal evidence: [docs/architecture/overview.md](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/docs/architecture/overview.md); [docs/architecture/runtime.md](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/docs/architecture/runtime.md); [docs/architecture/actions.md](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/docs/architecture/actions.md); [apps/web/core/harness.js](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/apps/web/core/harness.js); [apps/web/core/plan.js](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/apps/web/core/plan.js); [firmware/IPhoneAutomationHarness/src/RtcPeerOwnership.h](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/firmware/IPhoneAutomationHarness/src/RtcPeerOwnership.h).

## Operational model

The model-backed browser phone operator is S1. Shared bridge target leases plus client identity provide a limited first-party S2 anti-interference control when multiple independent phone actors connect. No separate whole-organization current-control decision owner, independent audit actor, external prospective intelligence loop, or ultimate identity-policy resolution was found in the standard runtime; authorization, physical safety bounds and user Stop are not upgraded into those higher functions.

## S1 — Operations

- State: A
- Function: perform the concrete requested phone workflow by interpreting changing screen context and selecting the next tap, swipe, key, wait, capture or task completion.
- Disturbance / variety regulated: changing mobile UI state, timing, orientation, tool failures, unknown HID delivery and delayed app response.
- Decisive decision or feedback right: adapt the next proposed action or changed plan from observed fresh screen frames and input receipts; decide task progress or request user assistance.
- Decision owner: model-backed browser Harness run using the installed tool/action contract; selected external provider performs inference but does not own host action validation, target identity, tool routing or observation persistence.
- Supporting / enforcement mechanisms: `phone_observe` / `phone_execute_plan`, strict `validatePlan`, deadline limits, verified target/client/lease, timed device segments, local capture and evidence storage.
- Closure path: action plan executes through WebRTC/ESP32 Bluetooth → input receipt and fresh captured iPhone frame → model reevaluates observed outcome, plans next change or reports completion with actual frame IDs.
- Boundary reachability: shipping Safari web app and precompiled ESP32 firmware plus a user-configured supported model; plan validation and execution are first-party, no user-authored plugin required.
- Why this is / is not agent-owned: the model selects the context-sensitive gesture/target outcome while browser/ESP32 make deterministic safety and actuation checks; neither a raw Bluetooth firmware loop nor hosted provider alone supplies this installed composed S1 closure.
- Evidence: [docs/architecture/overview.md](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/docs/architecture/overview.md); [apps/web/core/harness.js](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/apps/web/core/harness.js); [apps/web/core/plan.js](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/apps/web/core/plan.js); [docs/architecture/actions.md](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/docs/architecture/actions.md).
- Basis: structural
- Confidence: high for designed source path, unmeasured live execution
- Caveats: no live phone, WebRTC, ESP32 or real model invocation; user may need to enable screen sharing and configure provider.

## S2 — Coordination

- State: C
- Function: prevent two independently running browser/phone automation actors from simultaneously taking authoritative control of one physical target and corrupting input.
- Disturbance / variety regulated: target/lease contention, input sent by a stale client, a disconnected peer continuing actions, and target identity confusion.
- Decisive decision or feedback right: accept a current peer/target lease and reject or fence competing stale writers at the bridge/host execution boundary.
- Decision owner: source-encoded ESP32 client-target ownership and browser's trusted identity/lease checks; there is no autonomous multi-phone coordinator choosing the relation.
- Supporting / enforcement mechanisms: `RtcPeerOwnership::claim`, `owns`, per-target previous-lease invalidation, WebRTC target and lease envelope, current state checks and browser-local per-session run lock.
- Closure path: current peer claims a physical target, stale peer loses ownership; its subsequent mutation cannot satisfy lease/target validation, causing a safe error or pause/reconciliation instead of conflicting input.
- Boundary reachability: shipped MCU code plus regular one- or two-phone WebRTC mode; documentation states two independent bridge connections with one active writer per target.
- Why this is / is not agent-owned: anti-conflict mechanism exists first-party, but target admission is deterministic, not an agent-owned adaptive S2 function.
- Evidence: [firmware/IPhoneAutomationHarness/src/RtcPeerOwnership.h](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/firmware/IPhoneAutomationHarness/src/RtcPeerOwnership.h); [docs/architecture/overview.md](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/docs/architecture/overview.md); [docs/architecture/lan-connection.md](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/docs/architecture/lan-connection.md); [apps/web/core/plan.js](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/apps/web/core/plan.js).
- Basis: structural
- Confidence: medium; limited to explicit lease/identity regulation
- Caveats: two independent phone clients are a supported but optional mode; device leasing alone does not show team-wide allocation or general cross-agent resource negotiation.
- Distinct S1 units: two independent Safari Harness model-backed runs connected to a shared ESP32, each operating its own phone or attempting the same physical target.
- Inter-S1 disturbance: competing writes to the same phone's sole Bluetooth pointer/keyboard input can misdirect gestures and invalidate observed action results.
- Attenuating coordination relation: MCU per-target peer lease identity invalidates an earlier owner on a new `claim`, and browser plan execution requires present lease/target validity before mutation.
- Feedback into subsequent S1 behaviour: rejected execution or unknown input forces the affected run into pause/fresh observation/reconciliation rather than unsafe continued mutation.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: per-target exclusion attenuates an actual interference channel between independently active phone S1 actors, not merely carrying commands between browser and ESP32.

## S3 — Inside-and-now control

- State: —
- Function: no distinct team/whole-system controller allocating current commitments or mediating interactions of the independent phone workers is established beyond per-run task operation.
- Disturbance / variety regulated: cross-run task priorities, shared work capacity or whole-fleet reprioritisation could require S3 but are not regulated as a collective.
- Decisive decision or feedback right: no shipped right to allocate or rebalance whole-system commitments across phone actors; each run executes a user-defined goal.
- Decision owner: no whole-system model-backed, constructor or parent S3 owner demonstrated; user mode chooses its own phone's task and Stop, not a shared organization-wide policy.
- Supporting / enforcement mechanisms: local one-run lock, `plan` mode, deadlines, capture pause and device leases enforce individual operation/anti-interference only.
- Closure path: per-run failure and success return to the same S1 actor; no cross-run current state → substantive fleet resource/priority intervention → changed collective commitments loop found.
- Why this is / is not agent-owned: a model supervising its own step plan is S1 feedback, not a metasystem S3 deciding among several autonomous units.
- Evidence: [docs/architecture/runtime.md](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/docs/architecture/runtime.md); [apps/web/core/harness.js](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/apps/web/core/harness.js); [apps/web/core/store.js](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/apps/web/core/store.js); [docs/architecture/overview.md](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/docs/architecture/overview.md).
- Basis: bounded source absence
- Confidence: medium
- Caveats: deployment-specific external fleet controller not included; no claim that any single-agent system requires S3.
 
### Absence scope

- Surfaces inspected: browser run lifecycle, plan/task modes, session ownership, target leasing, bridge connections and user Start/Stop.
- Plausible first-party paths checked: model plan review, `task_report`, persistent sessions, human intervention, concurrent bridge target leasing.
- Why no material first-party path remains: these govern one task/target or resource exclusion; none exposes current multiple-unit commitments and a distinct controller with authority to revise them.

## S3* — Complementary audit

- State: —
- Function: no independent checker/auditor evaluates the phone agent's accomplishment against a separate evidence path with substantive verdict and intervention.
- Disturbance / variety regulated: a falsely successful task report would require independent checking, but shipped screenshot evidence is ordinary run feedback.
- Decisive decision or feedback right: no distinct independently sourced audit verdict authority; `task_report` verifies existence of frames without independent semantic judgment on task correctness.
- Decision owner: same task model and deterministic browser checks own completion evidence; no separately dispatched auditor or source-independent checker found.
- Supporting / enforcement mechanisms: fresh capture, `hasRunFrame`, input receipts, return-to-Harness visibility and schema checks.
- Closure path: observed frames return to the running model and can reject a missing evidence frame; no independent auditor reads different evidence and returns a separate challenge into system control.
- Why this is / is not agent-owned: screenshots and receipts make S1 stronger and safer, but cannot be relabelled independent S3* without a distinct audit actor/route.
- Evidence: [apps/web/core/harness.js](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/apps/web/core/harness.js); [apps/web/core/plan.js](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/apps/web/core/plan.js); [docs/architecture/harness-runtime-implementation.md](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/docs/architecture/harness-runtime-implementation.md).
- Basis: bounded source absence
- Confidence: medium-high
- Caveats: provider-side tool traces or external user observation could constitute another system's audit, not the shipped Harness's S3*.

### Absence scope

- Surfaces inspected: runtime task report, screenshot/receipt/reconciliation, plan validation, skills, provider/relay adapter and user completion settings.
- Plausible first-party paths checked: execution receipts, per-plan validators, same-model visual verification, return-to-app screen evidence and user final acknowledgement.
- Why no material first-party path remains: no separate independent actor/evidence route, substantive adverse verdict, and return-to-controller audit cycle is shipped.

## S4 — Outside-and-then intelligence

- State: —
- Function: no separate agent-owned or constructor path for adapting the Harness organization to future outside changes was found.
- Disturbance / variety regulated: future iOS, Bluetooth, provider and app changes are plausible external adaptation stimuli but not proactively managed.
- Decisive decision or feedback right: a future-option decision changing installed capabilities or organization would be required and is not supplied.
- Decision owner: none in shipped runtime; external model responds to an ongoing user phone task, while operator/published community changes occur adjacent to that run.
- Supporting / enforcement mechanisms: online skill community, provider catalog and MCP tools extend what the current agent can execute, without a standing organizational adaptation judgment.
- Closure path: no outside-future change → prospective option → selected organizational adaptation → updated current S3/S1 capacity loop is supplied.
- Why this is / is not agent-owned: retrieval of user-requested skills or Web/MCP responses cannot by itself establish a first-party future intelligence function.
- Evidence: [apps/web/core/skills.js](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/apps/web/core/skills.js); [apps/web/core/mcp.js](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/apps/web/core/mcp.js); [docs/architecture/overview.md](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/docs/architecture/overview.md); [apps/web/core/harness.js](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/apps/web/core/harness.js).
- Basis: bounded source absence
- Confidence: medium
- Caveats: public community developers can publish new skills; that external development process is excluded from this installed runtime.

### Absence scope

- Surfaces inspected: shipped skills/community, provider models, MCP client, browser tool selection, firmware update/deployment and runtime.
- Plausible first-party paths checked: skill catalog sync, user-added skills, new-provider connections and task-level browser/Web tools.
- Why no material first-party path remains: all require the user/third party to decide or serve current tasks; none forms an installed prospective future signal/option/adoption loop.

## S5 — Policy and identity

- State: —
- Function: no identity-level ultimate-purpose issue resolution loop is supplied in this personal phone automation harness.
- Disturbance / variety regulated: ultimate goal/policy conflicts between agent current work and future viability are not framed as a separate organizational question.
- Decisive decision or feedback right: no distinct authority for a binding identity-policy verdict beyond per-task user preferences and permissions.
- Decision owner: user controls task goals and source permission settings, but no S5-specific issue→ultimate ruling→returned governance transaction is shown.
- Supporting / enforcement mechanisms: static tool grants, target leases, local settings, human Stop, screen sharing, auth/privacy checks.
- Closure path: changing a task's permission or stopping an action does not yield a binding policy/identity decision returned to an S3/S4 office; that loop is absent.
- Why this is / is not agent-owned: task-level user authority and deterministic safety restraints are not organizational identity governance.
- Evidence: [apps/web/core/control.js](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/apps/web/core/control.js); [apps/web/core/harness.js](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/apps/web/core/harness.js); [docs/architecture/runtime.md](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/docs/architecture/runtime.md); [docs/architecture/overview.md](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/docs/architecture/overview.md).
- Basis: bounded source absence
- Confidence: medium
- Caveats: operator's broader personal or institutional policy is external and not credited as a first-party S5.

### Absence scope

- Surfaces inspected: settings, task completion and Stop, tool permissions, plan validation, phone target identity, user session interface and external hosting.
- Plausible first-party paths checked: user instruction precedence, policy preferences, device safety gates and community governance.
- Why no material first-party path remains: none raises a genuine ultimate-identity issue for adjudication and returns its ruling to re-govern current/future organizational functions.

## Distributed OSS parent arrangement

Open-source maintainers and community skill publishers own the public project and hosted distribution, not the organizational policy of an arbitrary user's installed local Safari agent. Two user phones do not become a corporate organization with shared S5 solely by connecting to the same bridge.

## Self-hosted and non-human modes

The web app and ESP32 firmware are self-hostable and usable with the user's own API provider. A model can continue acting subject to plan limits and screen-sharing preconditions. The human can Stop/Resume, enable permissions or disable return-to-app completion. None of these operator actions by itself supplies an S3/S4/S5 parent decision loop.

## Recursion

Each model-backed phone task is an operational S1, with a limited shared bridge S2 coordination path across independent browser actors. No separate S3 whole-system current allocation, S3* independent audit, S4 future adaptation, or S5 ultimate-policy loop established within the shipped combined runtime.

## Variety and escalation

New screens feed the model's S1 plan. Host validates current target/frame/lease, bridge delivers bounded input, captures and receipts return to S1. An invalid/stale lease or uncertain input pauses/reconciles rather than repeating unsafe actions. Owner physical intervention is a safety escape, not automatic higher-function closure.

## Evidence gaps

Source-only structural review at the frozen ref. No paid model calls, real iPhone, Bluetooth, Wi-Fi or physical device actuation. The S2 candidate relies on documented concurrent browser clients and explicit target lease exclusion; not a claim of distributed organizational optimization. Negative S3–S5 findings cover inspected first-party bundled surfaces, not hypothetical downstream operators or future releases. The assessment is a VSM function/owner map, not a judgment of product value.
