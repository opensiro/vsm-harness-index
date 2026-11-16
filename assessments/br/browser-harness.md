---
harness_id: browser-harness
project_name: Browser Harness
repository: https://github.com/browser-use/browser-harness
review_ref: 8ec26f6974015a78eaf5494fe35bb9ba1f6b3598
reviewed_at: 2026-11-16
generated_profile_version: 0.2.2
generated_assessment_procedure_version: 0.3.1
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
last_checked_ref: 8ec26f6974015a78eaf5494fe35bb9ba1f6b3598
last_checked_at: 2026-11-16
assessment_changed_at: 2026-09-18
last_reassessment_round: R3
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Browser Harness

## Review boundary

- System in focus: the first-party Browser Harness browser-control organization, comprising its shipped CLI/CDP/daemon/helper/skill/MCP surface and supported agent-workspace conventions; not the developer organization as a separate recursion.
- Purpose and identity: enable coding/LLM agents to execute browser tasks in real or hosted browsers while retaining tab state and allowing task-specific helper extension.
- Relevant environment: web pages and logged-in Chrome/Chromium, Browser Use Cloud, external coding/LLM agents and tool hosts, user permission prompts, site access constraints.
- Standard-distribution boundary: the shipped first-party `browser-harness` entry point, Python package, skill instructions, default/named local daemon, supported remote/cloud browser modes, optional domain skills and recording/video features.
- Credited operating / distribution surfaces: [src/browser_harness/run.py](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/src/browser_harness/run.py), [src/browser_harness/daemon.py](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/src/browser_harness/daemon.py), [src/browser_harness/helpers.py](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/src/browser_harness/helpers.py), [src/browser_harness/admin.py](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/src/browser_harness/admin.py), [src/browser_harness/mcp_cli.py](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/src/browser_harness/mcp_cli.py), [src/browser_harness/recorder.py](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/src/browser_harness/recorder.py), [SKILL.md](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/SKILL.md), [agent-workspace/agent_helpers.py](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/agent-workspace/agent_helpers.py), [CONTRIBUTING.md](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/CONTRIBUTING.md).
- Adjacent first-party surfaces excluded from ownership: Browser Use company/maintainer governance and its GitHub PR/release activity, Browser Use's separately packaged host CLI/product, repository CI, tests, benchmark/dogfood demonstrations and contributor-authored domain-skill curation decisions. These may provide context but are not wired into this assessed harness as its own S3/S4/S5 owner.
- First-party operating / deployment modes considered: default local Chrome daemon, named local daemon, remote/cloud browser helpers, CLI and MCP, opted-in domain skills (`BH_DOMAIN_SKILLS=1`), opted-in recording/video production, and documented trusted-orchestrator environment flags.
- Recursion level: a browser-work organization with one or more external agent actors as candidate S1 units; the maintainer organization and separately hosted agent platform are higher/adjacent systems.
- Reviewed revision: `8ec26f6974015a78eaf5494fe35bb9ba1f6b3598`.
- Observation date: 2026-11-16.
- Generated Profile version: `0.2.2`.
- Generated Methodology version: `0.3.1`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.8`.

## Repository architecture

The standalone `browser-harness` CLI accepts an agent-authored Python task and dispatches browser operations through a persistent CDP daemon; [src/browser_harness/run.py](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/src/browser_harness/run.py) supplies entry points and [src/browser_harness/daemon.py](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/src/browser_harness/daemon.py) mediates tab state and browser connections. [src/browser_harness/helpers.py](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/src/browser_harness/helpers.py) exposes navigation, observations, input, screenshots, cloud/network helpers and a task-editable `agent_helpers.py` import. [src/browser_harness/mcp_cli.py](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/src/browser_harness/mcp_cli.py) is an alternate tool-facing surface.

The first-party [SKILL.md](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/SKILL.md) provides task/tab discipline, explicit guidance about the shared mutable local daemon, isolation alternatives, user consent, domain-skill lookup and optional recordings. `BH_DOMAIN_SKILLS=1` only enables lookup in the local workspace; helper files do not create a distinct strategic decision-maker. Recording/video pathways in [src/browser_harness/recorder.py](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/src/browser_harness/recorder.py), [src/browser_harness/video.py](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/src/browser_harness/video.py) and [src/browser_harness/video_render.py](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/src/browser_harness/video_render.py) preserve or inspect local task artifacts and video compositions. The repository [README.md](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/README.md) says Browser Harness is now also used as an engine by the separate Browser Use product; this does not import that adjacent product's ownership into the assessed first-party package.

Maintainer decisions on which examples to include or remove occur in the **development organization**, not as a shipped runtime identity-policy decision protocol. For example [PR #972](https://github.com/browser-use/browser-harness/pull/972) and [PR #976](https://github.com/browser-use/browser-harness/pull/976) establish and apply domain-skill access policy in upstream contribution/release governance. Their effect on shipped files is real, but they do not establish an in-boundary S5 decision right.

## Primary evidence

- [README.md](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/README.md) — delivery boundary, separate Browser Use wrapper, external agent workflow.
- [SKILL.md](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/SKILL.md) — S1 browser interaction, S2 shared-daemon conflict and coordination, parent/user task permission and recording instructions.
- [src/browser_harness/run.py](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/src/browser_harness/run.py) · [src/browser_harness/helpers.py](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/src/browser_harness/helpers.py) · [src/browser_harness/daemon.py](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/src/browser_harness/daemon.py) — first-party task execution and browser-state machinery.
- [src/browser_harness/admin.py](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/src/browser_harness/admin.py) · [src/browser_harness/mcp_cli.py](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/src/browser_harness/mcp_cli.py) — local/cloud daemon controls and alternate invocation.
- [src/browser_harness/recorder.py](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/src/browser_harness/recorder.py) · [src/browser_harness/video_render.py](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/src/browser_harness/video_render.py) — recording and video-composition checks, not independently governed S3* operational audit.
- [CONTRIBUTING.md](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/CONTRIBUTING.md) · [PR #976](https://github.com/browser-use/browser-harness/pull/976) — development-only governance context; excluded from runtime S5 ownership.

## Operational model

An external model-driven coding agent chooses its browser tasks and the order of browser actions, calls the first-party CLI/MCP and receives observations. The harness supplies CDP transport, browser attachment and persistent tab mechanics. The same agent can edit its task-specific helper workspace, but the developer/host remains the owner of overall multi-agent orchestration. Browser permissions, human login/consent and Cloud/browser costs constrain operation without themselves creating the higher-level VSM decision rights of S3, S4 or S5. Supported optional recording and domain skills remain task/operational features.

## S1 — Operations

- State: A
- Function: produce browser task outcomes in live external websites, including navigation, inspection, form interaction and extraction.
- Disturbance / variety regulated: changing web UI, navigation state, logged-in sessions, dynamic pages, browser CDP state and site-specific task mechanics.
- Decisive decision or feedback right: the model-driven agent selects and revises actual browser actions, observations and task-local helpers.
- Decision owner: agent actor using the shipped browser-control skill and CLI/MCP.
- Supporting / enforcement mechanisms: daemon, CDP helpers, IPC, persistent tabs, optional domain skills, screen/video and diagnostics.
- Closure path: helper/CDP calls alter browser state; subsequent observations return to the agent and inform its next step or completed user task.
- Boundary reachability: [SKILL.md](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/SKILL.md) documents direct invocation and a realistic browser-action loop; [src/browser_harness/run.py](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/src/browser_harness/run.py) and [src/browser_harness/helpers.py](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/src/browser_harness/helpers.py) supply the shipped executable/task primitives. No development-only agent is needed to operate this mode.
- Why this is / is not agent-owned: the external model-driven agent exercises browser-task discretion; deterministic helpers transport the selected actions but do not replace that discretion.
- Evidence: [SKILL.md](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/SKILL.md); [src/browser_harness/run.py](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/src/browser_harness/run.py); [src/browser_harness/helpers.py](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/src/browser_harness/helpers.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the agent is supplied by a supported external host; the package does not itself bundle a first-party model planner. This is consistent with the published assessment's agent-actor boundary.

## S2 — Coordination

- State: C
- Function: dampen interference when multiple agent tasks share one mutable local browser-attachment lane.
- Disturbance / variety regulated: two agent actors switching tabs and acting simultaneously can target or screenshot one another's attached tab.
- Decisive decision or feedback right: choose serialization of local browser operations or independent browser lanes for genuinely simultaneous work.
- Decision owner: externally composed agent host/operator/participating actors, not an autonomous first-party regulator inside the daemon.
- Supporting / enforcement mechanisms: shared local daemon/tab discipline, named-daemon alternative, cloud/remote browser isolation, [src/browser_harness/admin.py](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/src/browser_harness/admin.py).
- Closure path: the chosen serialized schedule or separated remote browsers changes which S1 actor may act on which browser lane subsequently.
- Boundary reachability: [SKILL.md](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/SKILL.md) explicitly identifies the concrete shared-daemon race and prescribes serialization/isolation within its supported local/cloud modes. This is an S2-specific constructor protocol available to the invoking host, not merely a generic message queue.
- Why this is / is not agent-owned: the function-specific disturbance and mitigation are first-party, but the autonomous coordinating owner across external hosts is not supplied; constructor assembly is needed.
- Distinct S1 units: multiple agents using the same local Chrome instance for separate tasks.
- Inter-S1 disturbance: tab switching and input/screenshot calls can race on the one mutable attached/current tab.
- Attenuating coordination relation: serialize local browser calls or use independent remote browsers per concurrent task.
- Feedback into subsequent S1 behaviour: the schedule/isolation choice governs subsequent browser attachment and actions, avoiding cross-task interference.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the first-party documentation identifies a concrete, structurally supported inter-agent tab collision and offers a corresponding isolation/serialization response.
- Evidence: [SKILL.md](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/SKILL.md); [src/browser_harness/daemon.py](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/src/browser_harness/daemon.py); [src/browser_harness/admin.py](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/src/browser_harness/admin.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: no evidence of an autonomous first-party multi-agent S2 owner; separate Browser Use/agent orchestrators are outside the credited boundary.

## S3 — Inside-and-now control

- State: —
- Function: no established first-party whole-system current control over agent units' resources, priorities or commitments.
- Disturbance / variety regulated: local browser connectivity and lifecycle failures are handled, but organizational tradeoffs among current S1 commitments are not decided.
- Decisive decision or feedback right: no evidenced S3-specific whole-current allocator or negotiator; local daemon restart/Cloud stop choices remain user/host/task-scoped.
- Decision owner: external agent host/operator for task choices; daemon merely executes predefined lifecycle rules.
- Supporting / enforcement mechanisms: [src/browser_harness/admin.py](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/src/browser_harness/admin.py) daemon/cloud lifecycle, [src/browser_harness/daemon.py](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/src/browser_harness/daemon.py) connection/tab state and trusted-orchestrator flags in [SKILL.md](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/SKILL.md).
- Closure path: connection recovery affects future browser calls, not whole-system current commitments.
- Why this is / is not agent-owned: no first-party autonomous or parent-governed whole-current decision right is established at this recursion.
- Evidence: [src/browser_harness/admin.py](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/src/browser_harness/admin.py); [src/browser_harness/daemon.py](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/src/browser_harness/daemon.py); [SKILL.md](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/SKILL.md).
- Basis: explicit + structural negative.
- Confidence: high.
- Caveats: an external orchestration system can supply S3, but its authority is not shipped as part of this assessed harness.

### Absence scope

- Surfaces inspected: first-party daemon/admin/CLI, SKILL operating modes, local/cloud lifecycle helpers, original evaluation and examples.
- Plausible first-party paths checked: daemon management, named/local/remote isolation, auto-recovery, cloud browser start/stop, trusted-orchestrator env controls, human Chrome permission.
- Why no material first-party path remains: none supplies a whole-system operational view with a legitimate owner choosing/revising shared resources or priorities across multiple S1 agents and returning the choice into their current commitments. Human permission and cleanup are operational controls, not S3 parent governance.

## S3* — Complementary audit

- State: —
- Function: no established complementary, independent audit judgment that corrects current organization-wide regulation.
- Disturbance / variety regulated: runtime/task observation and video-provenance integrity are supported; challenging S1 claims independently with returned corrective control is not established.
- Decisive decision or feedback right: task/recording operator reviews or checks artifacts; no shipped independent audit owner and corrective decision path.
- Decision owner: ordinary acting agent/operator and developer/test runner rather than a separate complementary audit channel.
- Supporting / enforcement mechanisms: [src/browser_harness/recorder.py](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/src/browser_harness/recorder.py), [src/browser_harness/video.py](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/src/browser_harness/video.py), [src/browser_harness/video_render.py](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/src/browser_harness/video_render.py), screenshots and tests.
- Closure path: video composition checking and review may correct a media export; no first-party path shown that routes a separate operational-audit judgment back to current S3 control.
- Why this is / is not agent-owned: the video `review` command and source-manifest verification are source-artifact/renderer checks, not independently sourced organizational-operational audits.
- Evidence: [src/browser_harness/video_render.py](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/src/browser_harness/video_render.py); [src/browser_harness/recorder.py](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/src/browser_harness/recorder.py); [tests/unit/test_video_render.py](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/tests/unit/test_video_render.py).
- Basis: structural negative.
- Confidence: medium-high.
- Caveats: users can separately audit recorded runs, but such a composed independent reviewer/controller is outside the shipped mode.

### Absence scope

- Surfaces inspected: screenshots, recording/video manifest/compiler and review paths, daemon diagnostic reporting, unit/integration tests, skill/operator instructions.
- Plausible first-party paths checked: capture traces and screenshots, video rendering `review` of frames/clicks, source-manifest integrity verification, doctor diagnostics and external evaluation/benchmark references.
- Why no material first-party path remains: checks inspect or edit the task/media output and do not provide an independent complementary judgment about operational reality with a returned corrective path to system-wide S3; development tests/benchmarks are adjacent rather than an included runtime audit owner.

## S4 — Outside-and-then intelligence

- State: —
- Function: no supplied external-and-prospective adaptation loop returning future options to present whole-system capability.
- Disturbance / variety regulated: new site layouts or task mechanics can prompt a task agent to add helper/skill content, but this is task-local learning rather than a dedicated prospective environmental regulation loop.
- Decisive decision or feedback right: the task agent/developer decides which helper to write; no future-oriented organization-wide adaptation decision/right is shipped.
- Decision owner: operating agent and optionally maintainer/host outside the assessed boundary.
- Supporting / enforcement mechanisms: task-editable [agent-workspace/agent_helpers.py](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/agent-workspace/agent_helpers.py), domain-skill lookup from [src/browser_harness/helpers.py](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/src/browser_harness/helpers.py), [CONTRIBUTING.md](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/CONTRIBUTING.md).
- Closure path: a helper may become reusable on later tasks, but no first-party process constructs externally informed future options and integrates them through S3 current-capability feedback.
- Why this is / is not agent-owned: agent-owned helper authoring does not independently establish S4 when the decisions remain current-task operational problem solving.
- Evidence: [src/browser_harness/helpers.py](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/src/browser_harness/helpers.py); [agent-workspace/agent_helpers.py](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/agent-workspace/agent_helpers.py); [CONTRIBUTING.md](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/CONTRIBUTING.md); [SKILL.md](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/SKILL.md).
- Basis: explicit + structural negative.
- Confidence: high.
- Caveats: upstream domain-skill publication reflects developer adaptation outside this system-in-focus.

### Absence scope

- Surfaces inspected: helper extension, packaged domain-skills selection, source contribution policy, daemon/tool modes and agent skill instructions.
- Plausible first-party paths checked: editable helpers, `BH_DOMAIN_SKILLS` lookup, site-specific techniques, user-facing agent recovery instructions, maintainer updates and Browser Use parent product integration.
- Why no material first-party path remains: no shipped prospective external/environment model and independent adaptation-option judgment is wired into current whole-system S3 capability. Repo governance is adjacent; generic helper accumulation lacks the required two-way S4↔S3 closure.

## S5 — Policy and identity

- State: —
- Function: no first-party identity/ultimate-policy decision loop with legitimate ownership and return-to-operation at the assessed browser-work recursion.
- Disturbance / variety regulated: user permissions, opt-in recordings, domain-skill access guidance, external site constraints and local/cloud access decisions limit ordinary browser actions.
- Decisive decision or feedback right: genuine top-level project identity and domain-skill admission/rejection decisions remain with product maintainers; task permissions remain with the user/host. Neither is a shipped runtime identity-level decision closure.
- Decision owner: maintainers govern the adjacent development/project recursion; the user/host controls task-scoped permissions; no qualifying first-party S5 owner/path supplied inside Browser Harness.
- Supporting / enforcement mechanisms: [SKILL.md](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/SKILL.md) rules for login/MFA/consent and recording, `BH_DOMAIN_SKILLS` opt-in, [src/browser_harness/recorder.py](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/src/browser_harness/recorder.py) persistent recording preference, user Chrome approval and other local safeguards.
- Closure path: user consent can alter a task/recording or Chrome connection, and maintainer PR merges alter future packaged files; neither demonstrates an in-boundary identity/ultimate-policy dispute reaching legitimate S5 authority with authoritative response governing subsequent browser-work organization.
- Why this is / is not agent-owned: there is no such agent decision right or first-party S5 constructor; human/maintainer presence is not automatically `P`.
- Evidence: [SKILL.md](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/SKILL.md); [src/browser_harness/recorder.py](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/src/browser_harness/recorder.py); [src/browser_harness/helpers.py](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/src/browser_harness/helpers.py); [CONTRIBUTING.md](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/CONTRIBUTING.md); [PR #972](https://github.com/browser-use/browser-harness/pull/972); [PR #976](https://github.com/browser-use/browser-harness/pull/976).
- Basis: explicit + structural negative with adjacent-governance contrast.
- Confidence: high for the declared shipped boundary.
- Caveats: Browser Use as a developer organization can exercise S5 at its own recursion. This assessment does not deny that; it does not credit its GitHub decision workflow as Browser Harness runtime S5.

### Absence scope

- Surfaces inspected: published skill/CLI rules, browser approval and user permission paths, domain-skill enablement/loading, recording preferences and video review, daemon/admin lifecycle, operator flags, [CONTRIBUTING.md](https://github.com/browser-use/browser-harness/blob/8ec26f6974015a78eaf5494fe35bb9ba1f6b3598/CONTRIBUTING.md) and maintainer policy PRs as adjacent counterevidence.
- Plausible first-party paths checked: task-level human MFA/login/consent, Chrome remote-debugging Allow, recording opt-in, Cloud usage prompts, opt-in domain-skill discovery and blocking-site example removal, user-authored helper configuration, CLI telemetry opt-out, developer-release decisions.
- Why no material first-party path remains: permissions and deterministic constraints are ordinary operational choices; no shipped policy-conflict escalation to a legitimate identity/ultimate-policy authority and returned decision governing later browser operation exists in the assessed mode. A public maintainer PR is a decision at the project governance recursion, not a first-party parent-governed S5 mode in the installed harness. This is a bounded absence conclusion, not proof a future `P` implementation is impossible.

## Recursion

The system-in-focus is one browser-work organization. External coding-agent hosts supply S1 actors; shared daemon/browser lanes are operational substrates. Browser Use as company/product, upstream contributors and maintainers are adjacent or parent organizational structures and cannot be silently imported into the shipped harness's S3/S4/S5 state. Independently operated cloud browsers are not automatically independent viable recursive systems.

## Variety and escalation

The CDP helper interface absorbs diverse browser/UI disturbances; optional domain skills amplify task repertoires. Shared-tab conflicts are attenuated through documented serialized use or separate browser lanes. Loss of connection escalates to diagnostic/recovery and sometimes user Chrome approval; account/MFA/consent ambiguity escalates to the user. These are ordinary operation and coordination paths rather than a demonstrated metasystem identity/strategic decision loop.

## Evidence gaps

- Semantic claims are based on primary-source inspection of pinned code and supported operating documentation, not a live multi-agent Chrome integration run.
- The separately packaged Browser Use host product may implement organizational mechanisms outside the declared Browser Harness distribution; those require a distinct boundary assessment, not implicit upgrading of this row.
- Open unmerged third-party PRs (for example [#911](https://github.com/browser-use/browser-harness/pull/911), [#842](https://github.com/browser-use/browser-harness/pull/842) and [#1034](https://github.com/browser-use/browser-harness/pull/1034)) are not counted as shipped functionality at the pinned `main`.
- Maintainer domain-skill decisions are evidenced, but no credible in-runtime S5 ownership/return path was found after checking shipped modes. The negative result is scoped to this boundary rather than a statement about the company.

## Reassessment conclusion

Under Profile `0.2.4` and Methodology `0.3.8`, the current pinned first-party distribution still supports `A C — — — —` at `8ec26f6974015a78eaf5494fe35bb9ba1f6b3598`. The accepted vector is unchanged from the prior `afbcc381b963040c19627d788e40c7e7663171ee` review, but the current assessment now accounts for shipped recording/video features, domain-skill governance boundary, and the updated negative-state absence-scope and first-party reachability requirements. This is a new-ref `reassessed-unchanged` result; immutable generation provenance is preserved.
