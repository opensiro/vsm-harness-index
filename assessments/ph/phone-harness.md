---
harness_id: phone-harness
project_name: Phone Harness
repository: https://github.com/ShawnPana/phone-harness
review_ref: a80f8845e125269545bbf462967fe7b620691422
reviewed_at: 2026-10-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Phone Harness

## Review boundary

- System in focus: Phone Harness's first-party installed phone-control CLI plus its **documented Hermes Agent plugin integration**, forming an agent-facing operational phone-control cell. The bare CLI alone is a callable tool, not an independently autonomous actor.
- Purpose and identity: Let a supported installed agent observe and operate a user's real or rented iPhone/Android, producing user-requested mobile outcomes with a reusable phone I/O interface.
- Relevant environment: Changing phone screens and app workflows, device connectivity, OCR/accessibility errors, physical device permissions, different host operating systems, user consent, and an optional separately hosted Phone Harness Cloud device.
- Standard-distribution boundary: The Python package, bundled agent skill and helpers, iPhone/Android/remote backends, and explicitly shipped `integrations/hermes` plugin. In the Hermes mode, an **installed external Hermes model/agent runtime** supplies the cognitive loop and Phone Harness's plugin deliberately wires it to phone observations/actions. Credit the composed supported installed mode, not authorship of Hermes's model loop or a nonexistent standalone Phone Harness planner.
- Credited operating / distribution surfaces: [public installation and Hermes route](https://github.com/ShawnPana/phone-harness/blob/a80f8845e125269545bbf462967fe7b620691422/README.md#L26-L87), [Hermes plugin manifest](https://github.com/ShawnPana/phone-harness/blob/a80f8845e125269545bbf462967fe7b620691422/integrations/hermes/plugin.yaml#L1-L24), [tool/approval/skill registration](https://github.com/ShawnPana/phone-harness/blob/a80f8845e125269545bbf462967fe7b620691422/integrations/hermes/__init__.py#L684-L704), [model-code → CLI subprocess → model-output path](https://github.com/ShawnPana/phone-harness/blob/a80f8845e125269545bbf462967fe7b620691422/integrations/hermes/__init__.py#L596-L641), [CLI execution](https://github.com/ShawnPana/phone-harness/blob/a80f8845e125269545bbf462967fe7b620691422/src/phone_harness/run.py#L402-L427), [phone transport/helpers](https://github.com/ShawnPana/phone-harness/blob/a80f8845e125269545bbf462967fe7b620691422/src/phone_harness/helpers.py#L1-L54).
- Adjacent first-party surfaces excluded from ownership: Phone Harness Cloud's separately hosted device/account service (only its publicly shipped client is in source); package-update notices and usage telemetry; tests and fixtures; README demo videos; user-written Python scripts; agent-workspace defaults; upstream Hermes's decision loop, any other external Claude Code/Codex/MCP-client actor, and their independent governance or background agent operations. The first-party Hermes adapter is credited **as wiring**, not as a second first-party LLM.
- First-party operating / deployment modes considered: Plain Python-stdin CLI under a separately selected external actor; the explicitly installable Hermes plugin with `phone_exec`, skill registration and per-tool approval (default); optional classifier auto-run (off unless opted in); personal iPhone through Mirroring, local Android through adb, cloud Android/iPhone via separately supplied account/device session. A phone user must handle connections/sign-in.
- Recursion level: One supported installed phone-control agent cell and, for S2 only, multiple Hermes subagent cells contending for the same phone in one host process; not the upstream Hermes organization, cloud business or host user's entire software-agent fleet.
- Reviewed revision: `a80f8845e125269545bbf462967fe7b620691422`, frozen in [intake #2012](https://github.com/opensiro/vsm-harness-index/issues/2012) and [serial batch #2013](https://github.com/opensiro/vsm-harness-index/issues/2013).
- Observation date: 2026-10-24.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

`src/phone_harness/` implements the phone interface, local iOS Mirroring and Android adb backends, cloud-session selection, HTTPS device operations, OCR and accessibility helpers, installation/upgrades and telemetry. The CLI accepts a **caller-written Python program** on stdin and executes it with the helpers pre-imported. The helpers expose `screen`, `tap`, `scroll`, `wait_for_text`, `open_app`, etc. and return screen/device observations without deciding the user's objective. Cloud session/account management is transport infrastructure, not first-party agent planning. [CLI runner](https://github.com/ShawnPana/phone-harness/blob/a80f8845e125269545bbf462967fe7b620691422/src/phone_harness/run.py#L402-L427), [helpers](https://github.com/ShawnPana/phone-harness/blob/a80f8845e125269545bbf462967fe7b620691422/src/phone_harness/helpers.py#L1-L54), [cloud boundary](https://github.com/ShawnPana/phone-harness/blob/a80f8845e125269545bbf462967fe7b620691422/src/phone_harness/cloud.py#L1-L20), [remote transport](https://github.com/ShawnPana/phone-harness/blob/a80f8845e125269545bbf462967fe7b620691422/src/phone_harness/remote.py#L88-L129).

The included Hermes plugin is an explicit first-party composition: it registers `phone_exec`, a pre-tool-call approval hook and the packaged skill; Hermes's model chooses the next code snippet; the plugin passes it through a Python child process; stdout/stderr/exit status and an optional screenshot return to Hermes for its **subsequent** choice. Scripts in one host process share an exclusive phone lock with a bounded wait. The model runtime, agent/subagent scheduling and tool-call selection still belong to external installed Hermes. The included 50 plugin unit tests replace Hermes and the phone with mocks, checking adapter behavior but not demonstrating model effectiveness. [plugin readme](https://github.com/ShawnPana/phone-harness/blob/a80f8845e125269545bbf462967fe7b620691422/integrations/hermes/README.md#L1-L21), [execution and concurrency](https://github.com/ShawnPana/phone-harness/blob/a80f8845e125269545bbf462967fe7b620691422/integrations/hermes/__init__.py#L475-L491), [tool](https://github.com/ShawnPana/phone-harness/blob/a80f8845e125269545bbf462967fe7b620691422/integrations/hermes/__init__.py#L596-L641), [test fakes](https://github.com/ShawnPana/phone-harness/blob/a80f8845e125269545bbf462967fe7b620691422/tests/test_hermes_plugin.py#L1-L70).

## Operational model

A human selects/connects a device, configures access and installs the phone skill/plugin into an external model-backed host. In the **documented Hermes mode** the Hermes agent chooses Python code using the registered `phone_exec` tool; first-party Phone Harness executes phone input and returns current screen state/result, enabling the agent to choose subsequent action. Without Hermes (or another externally composed agent), the CLI is a deterministic script runner and does not independently execute open-ended user tasks. Concurrent Hermes subagents can independently request access, but first-party `_THREAD_LOCK` serializes their physical phone operations and returns a busy result after a fixed timeout. S2 coordination is attributed narrowly to the first-party phone-contention path, not to Hermes-wide task orchestration. [Hermes pathway](https://github.com/ShawnPana/phone-harness/blob/a80f8845e125269545bbf462967fe7b620691422/integrations/hermes/README.md#L61-L80).

## S1 — Operations

- State: A
- Function: Perform a mobile-user task through a composed agent that observes the phone, chooses successive gestures/scripts and returns an outcome to the requester.
- Disturbance / variety regulated: App navigation uncertainty, OCR and accessibility variations, asynchronous screen changes, disconnections, app-specific layouts and errors that change the next appropriate tool action.
- Decisive decision or feedback right: In the documented installed Hermes mode, **the Hermes model/agent** chooses the Python script for each `phone_exec` call and chooses further steps after seeing the output. The Phone Harness-owned tool registration, phone transport and result return make that feedback reachable at the declared deployment boundary.
- Decision owner: The **composed installed Hermes model-backed actor** for task-specific action decisions; external Hermes supplies its reasoning/turn loop and inference provider, while Phone Harness supplies the first-party adapter and operational phone interface. Bare CLI scripts are developer/host-selected, not autonomous Phone Harness decisions.
- Supporting / enforcement mechanisms: Tool schema, pre-tool approval, input script runner, iOS/Android/remote transport, accessibility/OCR and screenshot returns, user/device permissions, session/timeout handling and persistent helper workspace.
- Closure path: User mobile objective → configured Hermes agent selects `phone_exec(code=...)` → first-party plugin executes a caller-authored script on the actual selected device → observation, error or screenshot returns in the tool result → Hermes receives the result and chooses the next action or final response.
- Boundary reachability: `integrations/hermes/plugin.yaml` declares the installable dependency/tool/hook; `register` wires the handler into Hermes; `phone_exec` returns the actual child execution result and image to the model. Thus the composite agent loop is operationally *wired* rather than borrowed from unrelated dogfood. This is not evidence that Phone Harness implements a general model loop on its own.
- Why this is / is not agent-owned: The user intent and resulting screen state leave open-ended choice of next action to Hermes's model-backed actor in the first-party supported integration; the deterministic Phone Harness backend only executes chosen actions. Removing Hermes while keeping the CLI leaves script execution but removes the task-level autonomous owner (counterfactual test).
- Evidence: [README agent setup](https://github.com/ShawnPana/phone-harness/blob/a80f8845e125269545bbf462967fe7b620691422/README.md#L26-L87); [Hermes documented model/tool cycle](https://github.com/ShawnPana/phone-harness/blob/a80f8845e125269545bbf462967fe7b620691422/integrations/hermes/README.md#L1-L21); [phone tool source](https://github.com/ShawnPana/phone-harness/blob/a80f8845e125269545bbf462967fe7b620691422/integrations/hermes/__init__.py#L596-L641); [registration](https://github.com/ShawnPana/phone-harness/blob/a80f8845e125269545bbf462967fe7b620691422/integrations/hermes/__init__.py#L695-L704).
- Basis: Structural installed-mode wiring plus explicit agent-tool cycle documented by maintainer; no model or phone session was run.
- Confidence: High for implementable composed-agent wiring; lower for actual task effectiveness, which this Index does not measure.
- Caveats: `S1=A` is **limited to the supported composed Hermes deployment**; it does not imply that the bare CLI, generic MCP client, or Phone Harness package independently contains a model, agent planner or trained policy. The optional cloud-device service is not inspected as a separate first-party agent.

## S2 — Coordination

- State: C
- Function: Attenuate simultaneous access collisions between independently operating Hermes subagents controlling one physical phone through the same first-party plugin process.
- Disturbance / variety regulated: Two distinct subagent scripts could interleave taps/typing and leave both agents observing a phone state that neither intended; a single phone input surface cannot safely execute both at once.
- Distinct S1 units: Separate Hermes subagent work cells with distinct selected `phone_exec` scripts, sharing one plugin process and device; not the individual Python helper calls within a single script.
- Inter-S1 disturbance: Concurrent subagents contending for a single phone screen/input target could corrupt each other's navigation and observation state.
- Attenuating coordination relation: A first-party process-wide `threading.Lock()` wraps each tool's entire child script run; a wait deadline rejects concurrent access as `PhoneBusy` rather than sending overlapping gestures.
- Feedback into subsequent S1 behaviour: A contender waits until the current script releases the phone or gets an explicit busy/error tool result. The external model/subagent can use that result to revise/retry its next phone action instead of unknowingly acting on colliding state.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The mutex is deliberately attached to **shared physical phone contention among distinct subagents**; it prevents destructive inter-S1 interference, not generic sequential workflow edges or parent task delegation.
- Decisive decision or feedback right: Admit only one subagent's requested device transaction at a time and deliver a conflict/timeout result to rejected contenders.
- Decision owner: First-party **deterministic Hermes-plugin constructor** owns the collision attenuation. No autonomous agent chooses a negotiated scheduling priority or a global coordination plan, so this is the narrower constructor path `C`, not agent-owned `A`.
- Supporting / enforcement mechanisms: `_THREAD_LOCK`, bounded 120-second wait, child-process lifecycle and termination, separate stdout/stderr responses; Hermes itself provides subagents and their later cognitive choices.
- Closure path: Subagents request `phone_exec` concurrently → lock serializes device transactions or emits `PhoneBusy` → the prior script completes before the next acts, or an unsuccessful contender receives a busy tool result and can reconsider a future call.
- Boundary reachability: `_phone_lock` is used directly inside the shipped registered `phone_exec` handler, and the plugin documentation explicitly describes subagents taking turns on the phone in one process; not a test-only mock feature.
- Why this is / is not agent-owned: First-party serialization and error feedback are real S2-specific coordination support, but policy is fixed and the agent's eventual retry/decision comes from the external Hermes actor. No independent first-party S2 deliberative owner is shipped.
- Evidence: [plugin lock and intent](https://github.com/ShawnPana/phone-harness/blob/a80f8845e125269545bbf462967fe7b620691422/integrations/hermes/__init__.py#L1-L17); [lock constructor](https://github.com/ShawnPana/phone-harness/blob/a80f8845e125269545bbf462967fe7b620691422/integrations/hermes/__init__.py#L37-L43); [scope/acquire/release](https://github.com/ShawnPana/phone-harness/blob/a80f8845e125269545bbf462967fe7b620691422/integrations/hermes/__init__.py#L475-L491); [busy tool feedback](https://github.com/ShawnPana/phone-harness/blob/a80f8845e125269545bbf462967fe7b620691422/integrations/hermes/__init__.py#L596-L641); [doc concurrency](https://github.com/ShawnPana/phone-harness/blob/a80f8845e125269545bbf462967fe7b620691422/integrations/hermes/README.md#L61-L80).
- Basis: Direct installed-path source plus documented cross-subagent phone conflict and operational feedback.
- Confidence: High for in-process mutual exclusion; medium for behaviour of uninspected Hermes subagents after a busy error.
- Caveats: Only one Hermes process shares this mutex. No distributed locks or coordination across unrelated agents, hosts or cloud phone consumers are claimed. `C` does not imply the operator's entire fleet is centrally coordinated.

## S3 — Inside-and-now control

- State: —
- Function: No first-party whole-current manager is evidenced for a population of mobile-task S1 units.
- Disturbance / variety regulated: Conflicting tasks, resource commitments and priorities across a subagent portfolio are outside this plugin's present decision scope.
- Decisive decision or feedback right: Not established. A single-device lock and fixed script timeout are execution constraints, not decisions about whole-portfolio priorities, accountability or reassignment.
- Decision owner: No first-party S3 agent, S3 constructor or complete parent managerial loop at the declared recursion; Hermes or a user may make broader management decisions externally.
- Supporting / enforcement mechanisms: Mutex, timeouts, per-tool user approval, phone-session configuration and telemetry.
- Closure path: Local phone transactions succeed/fail and return to their callers; no whole-current view selects and feeds back changed portfolio-level commitments.
- Why this is / is not agent-owned: Serializing physical access does not confer discretion to allocate a portfolio's resources or revise current organizational priorities.
- Evidence: [tool and lock](https://github.com/ShawnPana/phone-harness/blob/a80f8845e125269545bbf462967fe7b620691422/integrations/hermes/__init__.py#L475-L641); [CLI command scope](https://github.com/ShawnPana/phone-harness/blob/a80f8845e125269545bbf462967fe7b620691422/src/phone_harness/run.py#L14-L32).
- Basis: Bounded negative source review.
- Confidence: Medium-high.
- Caveats: Hermes may manage its own agents, but that management is not asserted as first-party Phone Harness's S3.

### Absence scope

- Surfaces inspected: Phone command entry points and helpers, Hermes tool/hook registration, mutex/timeout handler, cloud session selector and published skill policy.
- Plausible first-party paths checked: Mutex contention, busy feedback, approval hook, device-session selection, timeout enforcement and telemetry.
- Why no material first-party path remains: These paths act on one device/tool call and expose no whole-current view with discretionary S1 portfolio-level allocation, intervention or returned regulation.

## S3* — Complementary audit

- State: —
- Function: No sufficiently independent complementary audit of ordinary phone task claims and S1/S3 reporting is packaged.
- Disturbance / variety regulated: A phone agent can misreport completion or miss visual details; returned screenshots/OCR help its own execution but do not create an independent auditing authority.
- Decisive decision or feedback right: Not established. The same acting agent receives raw phone observations, and a pre-tool approval hook checks permission, not independent operational claims.
- Decision owner: No first-party complementary auditor; the external user or optional Hermes host would need to supply any independent audit judgment.
- Supporting / enforcement mechanisms: OCR, screenshots, tool stdout/stderr, optional image attachment, tests and telemetry.
- Closure path: Observations feed ordinary next S1 choices; no independent alternative audit route corrects system-level current control.
- Why this is / is not agent-owned: Phone screen observations are evidence of the operating task, but the same agent consumes them and makes its own completion claim.
- Evidence: [tool result and image](https://github.com/ShawnPana/phone-harness/blob/a80f8845e125269545bbf462967fe7b620691422/integrations/hermes/__init__.py#L596-L641); [approval handler](https://github.com/ShawnPana/phone-harness/blob/a80f8845e125269545bbf462967fe7b620691422/integrations/hermes/__init__.py#L302-L318); [Hermes observations](https://github.com/ShawnPana/phone-harness/blob/a80f8845e125269545bbf462967fe7b620691422/integrations/hermes/README.md#L61-L80).
- Basis: Bounded absence of complementary, sufficiently independent audit closure.
- Confidence: Medium-high.
- Caveats: Uninspected agent-host auditing capabilities are not credited or denied.

### Absence scope

- Surfaces inspected: Hermes model-to-tool transport, screenshot/OCR attachments, approval hooks, skill consent guidance, telemetry and deterministic tests.
- Plausible first-party paths checked: Image review in ordinary loop, user approval, plugin AST heuristic, telemetry and test mocks.
- Why no material first-party path remains: Each is ordinary work observation, permission enforcement or development verification; none is a distinct sufficiently independent check whose findings return to metasystem control.

## S4 — Outside-and-then intelligence

- State: —
- Function: No first-party external-and-prospective sensing/option loop is evidenced for phone-control capability.
- Disturbance / variety regulated: Platform/API/tool capability changes and future app behavior might demand adaptation, but released runtime only responds to current phone conditions or user-invoked configuration/upgrade.
- Decisive decision or feedback right: None evidenced at S4. The model's navigation planning concerns its current user task, not modeling future external conditions and choosing sustained adaptation.
- Decision owner: Changes to the skill, CLI version, device default and phone choice come from developer or operator; no S4-specific accountable adaptation agent or closed parent mode is shipped.
- Supporting / enforcement mechanisms: Skill instructions to verify screen effects, persistent workspace notes, update check, platform selection, diagnostics and cloud/device alternatives.
- Closure path: Local screen feedback changes the next immediate phone action; upgrade/configuration can alter tools but is not coupled to a prospective environmental-model/option/adoption process.
- Why this is / is not agent-owned: Current UI adaptation and a writable helper file do not establish an outside-and-then organizational intelligence function.
- Evidence: [skill working method](https://github.com/ShawnPana/phone-harness/blob/a80f8845e125269545bbf462967fe7b620691422/SKILL.md#L130-L190); [CLI updater/configuration](https://github.com/ShawnPana/phone-harness/blob/a80f8845e125269545bbf462967fe7b620691422/src/phone_harness/run.py#L14-L29); [workspace defaults](https://github.com/ShawnPana/phone-harness/blob/a80f8845e125269545bbf462967fe7b620691422/src/phone_harness/workspace.py#L1-L23).
- Basis: Negative within the supported package and Hermes plugin mode.
- Confidence: Medium-high.
- Caveats: A host agent could conduct external research outside Phone Harness; it is not a first-party wired prospective adaptation mode here.

### Absence scope

- Surfaces inspected: Skill work instructions, workspace persistence, platform/tool configuration, package updates and Hermes tool/approval hooks.
- Plausible first-party paths checked: Screen-verify-adapt guidance, persistent `agent_helpers.py`, model tool-selection, update alerts and user-chosen new devices.
- Why no material first-party path remains: These operate within a current phone task or under manual tool maintenance; no external/future modeling produces an accountable option and returns an adopted capability decision to ongoing operations.

## S5 — Policy and identity

- State: —
- Function: No first-party runtime channel closes identity or ultimate-policy disputes at the assessed agent-cell recursion.
- Disturbance / variety regulated: User consent, credential handling and risky phone actions require boundaries, but this product documents rules and an invocation approval gate rather than ultimate policy adjudication.
- Decisive decision or feedback right: No identity-level decision path is established; the user approves ordinary `phone_exec` invocations, while the skill asks for consent before outward-facing or irreversible actions.
- Decision owner: User and external Hermes host govern consent and model identity; the plugin registers a fixed approval hook, not an S5 authority.
- Supporting / enforcement mechanisms: Pre-tool-call `approve` responses, optional classifier auto-run, Hermes session rule keys, skill consent guidance and secret scrubbing.
- Closure path: Approval/denial affects one script execution, but no identity-level issue reaches a legitimate policy authority and returns an authoritative organization-policy resolution that governs subsequent operation.
- Why this is / is not agent-owned: The difference between permissions for a task and ultimate identity policy is material; policy text and user confirmation are not by themselves S5.
- Evidence: [approval hook](https://github.com/ShawnPana/phone-harness/blob/a80f8845e125269545bbf462967fe7b620691422/integrations/hermes/__init__.py#L283-L318); [consent instructions](https://github.com/ShawnPana/phone-harness/blob/a80f8845e125269545bbf462967fe7b620691422/SKILL.md#L180-L195); [Hermes per-call approval rules](https://github.com/ShawnPana/phone-harness/blob/a80f8845e125269545bbf462967fe7b620691422/integrations/hermes/README.md#L82-L99).
- Basis: Bounded negative first-party governance/authority review.
- Confidence: Medium-high.
- Caveats: No claim is made about ultimate policy in Hermes itself or the cloud provider's institutional governance.

### Absence scope

- Surfaces inspected: Plugin tool/hook wiring, opt-in classifier, skill consent policy, Hermes approval documentation and CLI configuration.
- Plausible first-party paths checked: Ordinary user approval, tool-script classifier, credential rules, per-session plugin settings and configuration changes.
- Why no material first-party path remains: The reviewed paths enforce invocation permissions and static operator settings, not a closed identity/ultimate-policy disagreement route with legitimate authority and return into later organization-wide operation.

## Distributed OSS parent arrangement

The repository's open-source maintenance and Hermes's upstream organization are distinct systems. Plugin users may each run independent agents, but local user permissions and external contributor governance are not promoted to parent S3/S4/S5 modes at this phone-cell recursion.

## Self-hosted and non-human modes

Local devices and self-installed Hermes compositions are supported. The Phone Harness Cloud backend is an external device-session infrastructure dependency and does not supply a credited metasystem agent. The tool's deterministic mutex/approval enforcement does not establish autonomous whole-system governance.

## Recursion

An Hermes subagent using this phone tool has a bounded mobile operation, but no first-party evidence establishes its own recursively viable S2–S5 metasystem. The tool handler and individual Python scripts are not separately viable recursive systems.

## Variety and escalation

Device/OCR/platform variety reaches the agent via helper results. Deterministic backend checks attenuate transport errors; a shared mutex attenuates in-process concurrent device interference. Device connection and sensitive outward-facing actions are escalated to the user as execution permissions. No algedonic/S3/S4/S5 claim is made from errors, busy states or telemetry alone.

## Evidence gaps

- The separately installed Hermes package, its model loop implementation and provider behavior are not included in this frozen source. The first-party **plugin registration and tool-result return** are inspected; live autonomous effectiveness, provider reachability and end-to-end device outcomes are not tested.
- The cloud server and physical-device OS are outside this source distribution; the repository only shows client operations. No claim is made for cross-process/device S2 isolation or cloud-side governance.
- Source-based deterministic validation: `python -m unittest discover -s tests -p 'test_hermes_plugin.py' -q` passed **50/50** using a fake host and child runner. This checks adapter/lock/approval construction, not actual model reasoning or device safety.
