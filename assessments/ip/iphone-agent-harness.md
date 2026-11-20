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

- System in focus: the delivered Safari browser-local model/phone automation Harness plus its ESP32 WebRTC/Bluetooth bridge operating one or two independent phones under validated physical-input authority.
- Purpose and identity: accept a user's natural-language phone goal, observe actual iOS frames, choose bounded actions and verify physical outcomes without blindly trusting successful command delivery.
- Relevant environment: changing iPhone/iPad screen/app state, user-authorized screen capture, ESP32 BLE/RTC target, competing browser sessions and writer leases, provider/relay availability and installed local Skills.
- Standard-distribution boundary: `apps/web/` Safari UI, `apps/web/core/` model/tool/plan/device/session code, shipped `firmware/IPhoneAutomationHarness/`, bundled skills/prompts and first-party device protocol. External model providers, Apple iOS/Shortcuts, user's phone/apps, and optional MCP services are dependencies, not credited implementations.
- Credited operating / distribution surfaces: `apps/web/core/{harness,plan,device,device-rtc,store,skills,skill-context}.js`, bundled action plan schema, first-party ESP32 target lease/identity/receipt handling and built-in phone interaction skills.
- Adjacent first-party surfaces excluded from ownership: public skill author community and third-party skill logic, hosting/relay as a separate control-plane, provider-agent internals, generic external browser and iOS accessibility policies, marketing demos, repository CI and maintainer governance.
- First-party operating / deployment modes considered: single-phone task/auto with model-selected gestures; read-only plan and chat modes; two independent Safari sessions paired to two phone targets through one bridge; optional installed community skill refresh; explicit user device pairing and Stop.
- Recursion level: one owner-controlled phone automation harness with its S1 model tool loop, optionally two separate S1 phone runs sharing a bridge; does not thereby become a global multi-phone S3 organization.
- Reviewed revision: `b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f`.
- Observation date: 2026-11-20.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

Safari owns the agent run, local IndexedDB sessions/frames/credentials, prompt and installed Skill context. The model proposes phone steps or tool calls; the browser checks schema, frame freshness, target identity, lease, execution TTL and physical-input safety before compiling limited HID commands. WebRTC sends segments to the ESP32 bridge, which issues Bluetooth input and returns a receipt. The same model receives new screenshots and corrects action according to actual app response. Two separate browser connections can select independent phone targets but must not concurrently mutate one target: target binding and active writer leases arbitrate this shared physical resource. An action receipt confirms delivery, not independent semantic success. Local session continuity, retries, failure pause and hardware budgets are operational constraints rather than a whole-organization manager.

Bundled Skill instructions guide S1 gestures. A community install/refresh path can replace unchanged installed Skills from an outside catalog and make the new version available to the agent. That is automatic package maintenance and local capability refresh, **not** source proof of a prospective model-owned S4 intelligence process choosing responses to future external disturbances.

Primary evidence: [docs/architecture/overview.md](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/docs/architecture/overview.md), [docs/architecture/actions.md](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/docs/architecture/actions.md), [docs/architecture/runtime.md](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/docs/architecture/runtime.md), [apps/web/core/harness.js](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/apps/web/core/harness.js), [apps/web/core/plan.js](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/apps/web/core/plan.js), [apps/web/core/device.js](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/apps/web/core/device.js), [apps/web/core/skills.js](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/apps/web/core/skills.js).

## Operational model

One model-backed phone agent owns observation, choice of next input and verification. Hardware adapters and deterministic validation enforce identity/lease and action bounds. The optional two-phone configuration creates **two operational S1 units** sharing one bridge, with source-native exclusive target binding as limited S2. No first-party cross-run commitment supervisor, independent semantic auditor, proactive future strategy controller or ultimate-policy issue authority is demonstrated.

## S1 — Operations

- State: A
- Function: Choose and execute context-sensitive phone actions to satisfy the requested screen/app task.
- Disturbance / variety regulated: Unexpected layout, delayed controls, unreadable picker state, failed gestures, apps changing over time and tool/capture errors.
- Decisive decision or feedback right: Based on current user goal and fresh screen frames, select taps, drags, keyboard/clipboard commands, waits, new observations and completion/recovery.
- Decision owner: Configured provider-backed model agent called by first-party Safari Harness; provider supplies inference, but this standard installed model/observe/phone tool loop and its authority boundary are source-native.
- Supporting / enforcement mechanisms: Plan shape and stale-frame validation, verified target identity and lease, fresh capture, action TTL/segment limits, ESP32 receipts and local persisted task checkpoint.
- Closure path: The model proposes plan → browser validates → ESP32 sends BLE input → new screen confirms effect → model changes action or verifies result and returns response.
- Boundary reachability: Published browser page plus first-party bridge firmware, user-paired phone and configured provider; no custom downstream agent implementation is required.
- Why this is / is not agent-owned: The model chooses task actions based on open-ended screen context, while runtime validators/HID adapter merely constrain and effect those choices.
- Evidence: [docs/architecture/overview.md](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/docs/architecture/overview.md); [apps/web/core/harness.js](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/apps/web/core/harness.js); [apps/web/core/plan.js](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/apps/web/core/plan.js); [docs/architecture/actions.md](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/docs/architecture/actions.md).
- Basis: source structural
- Confidence: high for shipped mode
- Caveats: No real iOS device, bridge, AI provider or physical gesture executed in this review.


## S2 — Coordination

- State: C
- Function: Prevent mutually interfering commands to the same phone when separate Harness browser agents share a physical bridge and target.
- Disturbance / variety regulated: Two independently running page/model sessions may concurrently claim or mutate the same Bluetooth iPhone; stale target binding or writer leases can direct input to the wrong device.
- Decisive decision or feedback right: Select which verified client/target has the right to write and block concurrent lease claims or mismatched target commands.
- Decision owner: First-party deterministic browser/ESP32 target binding and writer-lease enforcement, not an autonomously adapting S2-specific model.
- Supporting / enforcement mechanisms: Two independent WebRTC channels, clientId, boardId, targetId, binding verification, leases, one active writer per target and rejected stale commands.
- Closure path: Conflicting writer is denied or paused, while the valid target-bound writer may send bounded HID; after release/lease expiry subsequent claim is checked afresh.
- Boundary reachability: Shipped two-phone bridge mode and browser DeviceClient API; no user-written synchronization plugin.
- Why this is / is not agent-owned: Actual inter-agent interference is source-natively attenuated but all access/lease decisions are mechanical; per-phone model does not choose a cross-client policy.
- Evidence: [docs/architecture/overview.md](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/docs/architecture/overview.md); [docs/architecture/lan-connection.md](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/docs/architecture/lan-connection.md); [apps/web/core/device.js](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/apps/web/core/device.js); [apps/web/core/device-rtc.js](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/apps/web/core/device-rtc.js).
- Basis: structural
- Confidence: medium-high (bounded to shared bridge target)
- Caveats: No coordination of two task goals, team priorities or global multi-phone resource strategy is claimed.
- Distinct S1 units: Two separate Safari pages with independently running model/phone task sessions through separate WebRTC links.
- Inter-S1 disturbance: Both may send physical inputs to the same Bluetooth target, overriding gestures or acting on invalidated screen assumptions.
- Attenuating coordination relation: Exclusive per-target writer lease, verified target binding and two-connection target routing reject conflict and stale clients.
- Feedback into subsequent S1 behaviour: Rejected client receives busy/lease/target error and cannot submit its next mutation until valid ownership is restored.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The access fence specifically prevents simultaneous hostile physical-input effects between otherwise independent S1 task actors.


## S3 — Inside-and-now control

- State: —
- Function: No first-party current whole-organization controller beyond each individual phone task loop is established.
- Disturbance / variety regulated: Competing phone-agent commitments, shared work priorities and multi-run progress would demand a whole-system supervisory decision.
- Decisive decision or feedback right: Would determine reallocation of concurrent agents and intervene on whole-team commitments; no such decision right was found.
- Decision owner: Browser model manages its own active task; human can Stop or select settings, but no autonomous/parent system-wide S3 controller is supplied.
- Supporting / enforcement mechanisms: Single active run per page, per-session store and device capacity checks prevent race but do not assess whole-team commitments.
- Closure path: No all-runs view → whole-work intervention decision → reallocated team/task feedback is evidenced.
- Why this is / is not agent-owned: A model deciding its own next phone gesture is S1, and two independent channels with leases are S2, not whole-system S3.
- Evidence: [docs/architecture/runtime.md](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/docs/architecture/runtime.md); [apps/web/core/harness.js](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/apps/web/core/harness.js); [apps/web/core/store.js](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/apps/web/core/store.js); [docs/architecture/overview.md](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/docs/architecture/overview.md).
- Basis: bounded source absence
- Confidence: medium
- Caveats: No inference about an external user organization that might coordinate many phones.
### Absence scope

- Surfaces inspected: per-page run ownership, execution context, multi-connection bridge, task resume/Stop and local sessions.
- Plausible first-party paths checked: two-phone bridge, store activeRun and in-loop task planning; none owns current commitments across both independent phone agents.
- Why no material first-party path remains: only run-local model choices and deterministic resource ownership are present; no shared organizational supervisor with a returned intervention.

## S3* — Complementary audit

- State: —
- Function: No complementary independent evidence audit actor apart from the operational model's own observation-and-result checks.
- Disturbance / variety regulated: A phone model might falsely believe a task succeeded based on visual observations or input receipt.
- Decisive decision or feedback right: Independent challenge of the operational agent's claimed task outcome would be necessary but is not assigned to another authority.
- Decision owner: Same phone-running model examines its fresh screen evidence; browser source/receipt validators are deterministic, not independent substantive auditors.
- Supporting / enforcement mechanisms: Screenshots, segment receipts, identity and input-release checks support S1 verification and safety.
- Closure path: Operational agent observes its effects and revises actions; no independent audit findings return to supervising authority or force separate review.
- Why this is / is not agent-owned: Direct evidence used by the task actor is ordinary S1 feedback; verified device delivery is not independent semantic scrutiny.
- Evidence: [docs/architecture/harness-runtime-implementation.md](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/docs/architecture/harness-runtime-implementation.md); [apps/web/core/harness.js](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/apps/web/core/harness.js); [apps/web/core/plan.js](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/apps/web/core/plan.js).
- Basis: bounded source absence
- Confidence: medium-high
- Caveats: External user could manually review actions, but that does not establish a shipped separate S3* mode.
### Absence scope

- Surfaces inspected: run model/tool loop, screenshots and task completion evidence, plan validations, receipt reconciliations and operator controls.
- Plausible first-party paths checked: fresh visual task verification, input receipt checks, optional user plan review; none supplies a complementary independent actor with separate source and return.
- Why no material first-party path remains: correctness is evaluated within the same operational run or deterministic validators, not a distinct autonomous or constructor-audit channel.

## S4 — Outside-and-then intelligence

- State: —
- Function: No installed prospective external-intelligence owner choosing future organizational adaptations beyond immediate phone tasks.
- Disturbance / variety regulated: Changes in outside app ecosystems, device capabilities and community patterns could require new operating skills/strategy.
- Decisive decision or feedback right: Would choose future-aligned adaptation options from external uncertain signals and feed adopted choices back to present capability; such owner is not evidenced.
- Decision owner: User explicitly chooses skills/install and model acts on current tasks; package updater deterministically refreshes already installed unmodified community skills.
- Supporting / enforcement mechanisms: `syncInstalledCommunitySkills` checks outside package revisions and updates local instructions, and `synchronizeSkills` injects changed guidance into current context.
- Closure path: External package-version update may refresh operational instructions but is not a prospective future-environment analysis/decision/return loop.
- Why this is / is not agent-owned: Version synchronization and user skill publishing are software maintenance/capability inputs; an independent model-led future intelligence controller is not supplied.
- Evidence: [apps/web/core/skills.js](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/apps/web/core/skills.js); [apps/web/core/skill-context.js](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/apps/web/core/skill-context.js); [docs/architecture/skills.md](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/docs/architecture/skills.md); [apps/web/skills/skill-authoring/SKILL.md](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/apps/web/skills/skill-authoring/SKILL.md).
- Basis: bounded source absence after inspecting strongest candidate
- Confidence: medium
- Caveats: Skill-authoring and community extension could enable new capabilities, but unshipped future S4 logic is not credited.
### Absence scope

- Surfaces inspected: first-party skill community installer, periodic unchanged-install refresh, skill context version pinning, user-authored skill publication and runtime research/tools.
- Plausible first-party paths checked: remote skill updates and newly published community skills; these are version-based reactive updates or explicit user installations rather than future disturbance interpretation.
- Why no material first-party path remains: no dedicated prospective evaluator selects among external changes and returns a strategic adaptation decision to a separate present-control function.

## S5 — Policy and identity

- State: —
- Function: No ultimate identity/policy conflict resolution and returned binding organizational direction is implemented at the local phone-agent recursion.
- Disturbance / variety regulated: Identity/purpose conflicts over which tasks or future direction the harness should govern.
- Decisive decision or feedback right: Would decide final purpose/policy issues and return changed governing commitments across S3/S4; none is supplied.
- Decision owner: Human user authorizes device pairing, task goal, provider, screenshot sharing and local skills; those are task authorization, not an evidenced S5 adjudicator.
- Supporting / enforcement mechanisms: Authentication, credentials, physical-target binding, permission-mode and model/safety prompts govern local execution.
- Closure path: No distinct identity-policy issue → final ruling → binding whole-system direction change is evidenced.
- Why this is / is not agent-owned: User preferences and device safety controls do not themselves close ultimate identity-policy issues.
- Evidence: [docs/architecture/overview.md](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/docs/architecture/overview.md); [apps/web/core/control.js](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/apps/web/core/control.js); [docs/architecture/runtime.md](https://github.com/cccat6/iphone-agent-harness/blob/b6e8ec900ce3eb902ad3dff3553a5adf3efc2e2f/docs/architecture/runtime.md).
- Basis: bounded source absence
- Confidence: medium-high
- Caveats: The external owner can impose an organizational policy not implemented by this harness.
### Absence scope

- Surfaces inspected: personal task goals, provider and device settings, auth, user Stop and community skill controls.
- Plausible first-party paths checked: permission restrictions, model modes, device trust and user task completion preferences.
- Why no material first-party path remains: no source-level identity-policy conflict trigger, legitimate ultimate authority decision and governing return to present/future controllers was found.

## Distributed OSS parent arrangement

The public project ships a standalone browser/ESP32 harness; it does not control the ultimate policies of locally installed phone agents. The user/operator is a task owner, not automatically an in-boundary identity governor.

## Self-hosted and non-human modes

Browser-based model execution may run tasks automatically while user-authorized screen sharing and a verified bridge remain active, but all physical input is subject to device/session/lease and TTL safeguards. Two independent clients may use one bridge, while each phone has one active writer; this is limited S2 access control, not a multi-agent S3 manager.

## Recursion

The primary unit is one phone task agent (S1), with a limited two-phone shared bridge exposing S2 for interfering writers. Browser local session store and cloud model/relay are not separate VSM metasystem actors by default.

## Variety and escalation

UI disturbances are absorbed by model-generated correction and fresh screen evidence. Physical safety uncertainty pauses dependent inputs, requires lease/identity verification and exposes user Stop/Resume. No separate audit or future organizational/policy authority is inferred from those operational fences.

## Evidence gaps

Read-only source/architecture inspection at the exact commit, no ESP32 actuation, Bluetooth pairing, iOS capture, model-provider invocation, screenshot data or empirical two-client race. S2 claims are confined to verified target writer contention. Negative states retain the bounded-surface falsifiers above rather than claiming future extensions impossible.
