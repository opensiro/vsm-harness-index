---
harness_id: rum
project_name: Rum
repository: https://github.com/KAJdev/rum
review_ref: 9c00bdb35f2a55959d6e56bd0d27b9573aac6fdd
reviewed_at: 2026-10-10
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# Rum

## Review boundary

- System in focus: first-party Rust Rum terminal coding-agent, autonomous source/tool loop, separate read-only Explore child, TUI background jobs and optional post-push CI watcher.
- Purpose and identity: edit/investigate source projects using a model and tools, with optional independent CI failure feedback to the same coder.
- Relevant environment: user Git repository, local commands and tests, configured model provider, read-only research tasks, GitHub CI results, TUI/user steering and session history.
- Standard-distribution boundary: shipped Rum CLI/TUI/headless app, its native tool loop, read-only Explore and TUI CI watcher. Excludes external AI provider internals, hypothetical user-created agent teams, Rum project maintainer/CI machinery and packaged editor integrations as independent decision owners.
- Credited operating / distribution surfaces: src/main.rs, src/agent.rs, src/tools/dispatch.rs, src/tools/explore.rs, src/tui.rs, config and persistence; independent CI checks are user-repository external validators only, reachable through a first-party watcher.
- Adjacent first-party surfaces excluded from ownership: project-maintainer Github Actions and release CI, bundled app/editor/LSP tooling without independent organizational decisions, repo demos and other user-configured tool providers.
- First-party operating / deployment modes considered: interactive coding, headless print mode, parallel model-selected tools, read-only Explore assistant, background shell jobs, and configured interactive TUI GitHub Actions watcher after a successful git push.
- Recursion level: primary code-editing S1; a separately operating read-only investigation agent may serve it, but no first-party inter-S1 conflict regulation is established. Optional complementary CI checks are distinct from the model and must be externally configured.
- Reviewed revision: 9c00bdb35f2a55959d6e56bd0d27b9573aac6fdd.
- Observation date: 2026-10-10.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Rum ships its own Rust provider/tool coding loop. The model requests read/edit/write/bash/search/LSP and other tools, the runtime executes and streams actual results into the same conversation, then the model continues or ends. Tool calls may run in parallel without creating independent coding S1 units. Its read-only Explore tool launches a separately prompted model with read/bash/web actions and returns a researched report to the parent; task delegation and research handoff alone do not establish S2 coordination over actual competing S1 activities.

A source-specific complementary CI-feedback connector is shipped in the interactive TUI, subject to a material pushed-ref identity limitation. After a successful bash tool result, `src/tui.rs` checks whether the command *text contains* `git push`; it does not parse the actual push destination/ref or verify that a push occurred. When scheduled, `ci_watch` later obtains local `git rev-parse HEAD` from the working directory and queries `gh run list --commit <that-local-HEAD>`; **the watcher does not establish that this SHA equals the commit/ref actually pushed**. In the conditional case where local HEAD is the pushed commit and independently configured GitHub Actions checks exist, failed-job logs can return through a first-party TUI feedback bridge to the same coder. External CI workflows belong to the user's repository and require configuration; mere test status transport does not establish an autonomous Rum audit-judgment owner or guaranteed repair. This narrows the evidence for the currently accepted `S3*=C` and preserves that historical grade for separate Index owner adjudication under [#1381](https://github.com/opensiro/vsm-harness-index/issues/1381).

The file editor, LSP, session branches, compaction, operator interventions and asynchronous command jobs are substantial usability mechanisms without separately evidenced S3 whole-current management or strategic S4/identity S5 governance. CI failure signalling is complementary feedback and does not automatically upgrade S3.

Source evidence: [src/agent.rs](https://github.com/KAJdev/rum/blob/9c00bdb35f2a55959d6e56bd0d27b9573aac6fdd/src/agent.rs); [src/tools/explore.rs](https://github.com/KAJdev/rum/blob/9c00bdb35f2a55959d6e56bd0d27b9573aac6fdd/src/tools/explore.rs); [src/main.rs](https://github.com/KAJdev/rum/blob/9c00bdb35f2a55959d6e56bd0d27b9573aac6fdd/src/main.rs); [src/tui.rs](https://github.com/KAJdev/rum/blob/9c00bdb35f2a55959d6e56bd0d27b9573aac6fdd/src/tui.rs); [src/tools/dispatch.rs](https://github.com/KAJdev/rum/blob/9c00bdb35f2a55959d6e56bd0d27b9573aac6fdd/src/tools/dispatch.rs).

## Operational model

The coder autonomously owns S1. Conditional external CI may supply complementarily sourced failed-check logs that Rum returns to the coder, but the watcher looks up runs for **local HEAD at watch time**, not a verified pushed ref. No separately autonomous Rum audit decision, guaranteed repair, inter-S1 conflict regulator or whole-current task supervisor is credited.

## S1 — Operations

- State: A
- Function: Native autonomous coding with actual read/write/edit and shell actions.
- Disturbance / variety regulated: Changing project code, user task needs, tool errors and observed test results.
- Decisive decision or feedback right: Model selects coding actions and next work after actual tool evidence.
- Decision owner: First-party Rum Agent invoking configured inference as the operational actor.
- Supporting / enforcement mechanisms: Tool dispatcher, streamed results, conversation history, shell/file/search tools.
- Closure path: Task → model tool calls → native file/shell execution → returned result → further model choice/finish.
- Boundary reachability: Rum TUI and print binary instantiate its own Agent, and code tools execute on real user files; the external model is inference, not an imported harness.
- Why this is / is not agent-owned: The model has contingent action discretion; the runtime executes and guards it.
- Evidence: [src/agent.rs](https://github.com/KAJdev/rum/blob/9c00bdb35f2a55959d6e56bd0d27b9573aac6fdd/src/agent.rs); [src/tools/dispatch.rs](https://github.com/KAJdev/rum/blob/9c00bdb35f2a55959d6e56bd0d27b9573aac6fdd/src/tools/dispatch.rs); [src/tools/file.rs](https://github.com/KAJdev/rum/blob/9c00bdb35f2a55959d6e56bd0d27b9573aac6fdd/src/tools/file.rs); [src/tools/bash.rs](https://github.com/KAJdev/rum/blob/9c00bdb35f2a55959d6e56bd0d27b9573aac6fdd/src/tools/bash.rs); [src/main.rs](https://github.com/KAJdev/rum/blob/9c00bdb35f2a55959d6e56bd0d27b9573aac6fdd/src/main.rs).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: Evidence is limited to the pinned first-party supported operating boundary.

## S2 — Coordination

- State: —
- Function: No supported conflict-damping relation among distinct independent operational S1 units.
- Disturbance / variety regulated: A research child and parent coder are distinct task participants, but no specific competing operation or destabilizing conflict is managed.
- Decisive decision or feedback right: Primary model delegates read-only exploration and gets its report; no inter-S1 coordination judgment exists.
- Decision owner: No S2-specific first-party decision owner.
- Supporting / enforcement mechanisms: Read-only Explore agent, parallel native tools, user messages and session forks.
- Closure path: Research findings and tool outputs return to parent coding decisions; this is delegation/inquiry rather than feedback that attenuates S1-to-S1 conflict.
- Why this is / is not agent-owned: An agent count, parallel tool tasks and simple research result exchange are insufficient for S2.
- Evidence: [src/tools/explore.rs](https://github.com/KAJdev/rum/blob/9c00bdb35f2a55959d6e56bd0d27b9573aac6fdd/src/tools/explore.rs); [src/tools/dispatch.rs](https://github.com/KAJdev/rum/blob/9c00bdb35f2a55959d6e56bd0d27b9573aac6fdd/src/tools/dispatch.rs); [src/agent.rs](https://github.com/KAJdev/rum/blob/9c00bdb35f2a55959d6e56bd0d27b9573aac6fdd/src/agent.rs); [src/main.rs](https://github.com/KAJdev/rum/blob/9c00bdb35f2a55959d6e56bd0d27b9573aac6fdd/src/main.rs).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: Evidence is limited to the pinned first-party supported operating boundary.

### Absence scope

- Surfaces inspected: Explore tool's read-only child, parent model/tool loop, parallel tool dispatcher, session branching and background jobs.
- Plausible first-party paths checked: Cross-S1 source-write conflicts or oscillation, a coordination owner and feedback influencing separate operational units.
- Why no material first-party path remains: Explore child performs independent read-only inquiry and returns data; no material disturbance/attenuation relationship between multiple S1 units is implemented.

## S3 — Inside-and-now control

- State: —
- Function: No independent whole-current commitment/prioritization decision owner spanning multiple active coding S1 operations.
- Disturbance / variety regulated: Tool jobs, queue updates, CI run statuses and cancellation are local execution contingencies.
- Decisive decision or feedback right: Runtime tracks events and human may stop/steer; no discretionary whole-current allocation manager.
- Decision owner: One coder with deterministic runtime and user, rather than separate S3 governor.
- Supporting / enforcement mechanisms: Background job feed, CI watch status, cancellation control, editor and LSP events.
- Closure path: Jobs signal completion or failures to the primary coder, but there is no aggregate supervisory decision returned to multiple S1 operating cells.
- Why this is / is not agent-owned: Monitoring jobs or CI is not whole-current management merely by being a control surface.
- Evidence: [src/main.rs](https://github.com/KAJdev/rum/blob/9c00bdb35f2a55959d6e56bd0d27b9573aac6fdd/src/main.rs); [src/tui.rs](https://github.com/KAJdev/rum/blob/9c00bdb35f2a55959d6e56bd0d27b9573aac6fdd/src/tui.rs); [src/agent.rs](https://github.com/KAJdev/rum/blob/9c00bdb35f2a55959d6e56bd0d27b9573aac6fdd/src/agent.rs).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: Evidence is limited to the pinned first-party supported operating boundary.

### Absence scope

- Surfaces inspected: TUI job watcher, model/user control channels, session lifecycle, CI watch, tool concurrency and LSP event processing.
- Plausible first-party paths checked: Aggregate current resource/priority decisions across active separate S1 cells, legitimate operator or autonomous current manager, returned interventions.
- Why no material first-party path remains: The shipped event loop reports/interrupts work but does not own a system-wide discretionary resource or current-commitment decision.

## S3* — Complementary audit

- State: C
- Function: First-party optional TUI constructor can convey failed configured CI checks selected by local-HEAD lookup back to the coding S1 for possible correction; identity of the *pushed* ref is not checked.
- Disturbance / variety regulated: Coding results could fail independent tests, builds or safety checks even when the coder judged them successful.
- Decisive decision or feedback right: Repository-configured external GitHub Actions checks produce their own conclusions/logs; Rum transports failures from `gh` runs selected by **local HEAD** to the coding agent, which may decide a repair. This selection does not bind the actual pushed SHA.
- Decision owner: The configured external repository CI/check policy supplies the candidate complementary outcome. `gh` is retrieval/transport, **not** a discretionary auditor; the concrete source of independently owned audit judgment depends on the external workflow configuration. Rum's Rust watcher exposes the feedback constructor but does not autonomously own that judgment.
- Supporting / enforcement mechanisms: TUI pending_ci_watch after git push, main.rs ci_watch, gh run list --commit, gh run view --log-failed, TUI job event and queued user messages.
- Closure path: Bash tool exits zero with command text containing `git push` → TUI requests a watch (not necessarily a verified push) → watcher reads local `HEAD` and polls CI for that SHA → available failed logs may be retrieved → TUI injects only matching failure summaries into the model's next input/queue → model may repair and re-push. No pushed-ref match, successful-check return, or repair is guaranteed.
- Boundary reachability: The supported interactive TUI calls the watcher after *successful bash commands whose argument text contains* `git push`. Actual push completion/ref and local-HEAD equivalence are not verified; available failed-log summaries can reach `user_tx` or the queued agent input. This is shipped runtime code, not demo-only.
- Why this is / is not agent-owned: Appropriately configured external CI can contradict the coder's own account, and Rum has a function-specific feedback constructor, but independently configured checks, `gh`, an eligible matching local HEAD and failure logs remain external/conditional. The original `C` classification is not upgraded; this narrowly conditional constructor interpretation received an attributable, non-independent Index S1 source-first semantic disposition in #1381, and the remaining publication/verification gates are distinct.
- Evidence: [src/tui.rs](https://github.com/KAJdev/rum/blob/9c00bdb35f2a55959d6e56bd0d27b9573aac6fdd/src/tui.rs); [src/main.rs](https://github.com/KAJdev/rum/blob/9c00bdb35f2a55959d6e56bd0d27b9573aac6fdd/src/main.rs); [src/agent.rs](https://github.com/KAJdev/rum/blob/9c00bdb35f2a55959d6e56bd0d27b9573aac6fdd/src/agent.rs).
- Basis: structural + explicit.
- Confidence: medium.
- Caveats: Only in interactive TUI with an exit-zero bash command containing `git push`, authenticated `gh`, independently configured project checks **and a matching local HEAD**. A successful `echo git push` can trigger a watch; pushing another ref can select the wrong commit. Missing failed logs prevent model injection, and repair is not guaranteed.

- Claim being audited: Coder changes whose **local HEAD selected by the watcher** may have external check failures; equivalence to the most recently pushed ref is unverified.
- Ordinary reporting path: Exit-zero bash tool output/command text (which need not prove an actual push) and local code/tool results.
- Complementary access path: Authenticated `gh` retrieves external GitHub Actions runs/logs by the *watched local HEAD SHA*; this is not an identity-verified receipt for the actual pushed ref.
- Independence boundary: GitHub Actions workflows/runners are outside Rum/model and can supply distinct project checks where configured; whether their policy represents an independently controlled audit judgment is case- and workflow-specific, not proven by the watcher alone.
- Who acts on findings: The coding agent receives failure findings in a subsequent input and decides possible repairs.

## S4 — Outside-and-then intelligence

- State: —
- Function: No organizational future-environment appraisal and capability renewal authority.
- Disturbance / variety regulated: Future model ecosystem and project needs would require prospective adaptation beyond the current coding task.
- Decisive decision or feedback right: Read-only Explore and web research gather information, but do not enact binding strategic capability change.
- Decision owner: No first-party S4 decision owner.
- Supporting / enforcement mechanisms: Explore, web tools, persisted session notes, prompt files and user model selection.
- Closure path: Research and stored notes may inform one coding task, not a strategy decision returning as altered organizational capabilities.
- Why this is / is not agent-owned: Research tools and saved prompts are not standalone outside-and-then strategic regulation.
- Evidence: [src/tools/explore.rs](https://github.com/KAJdev/rum/blob/9c00bdb35f2a55959d6e56bd0d27b9573aac6fdd/src/tools/explore.rs); [src/config.rs](https://github.com/KAJdev/rum/blob/9c00bdb35f2a55959d6e56bd0d27b9573aac6fdd/src/config.rs); [src/agent.rs](https://github.com/KAJdev/rum/blob/9c00bdb35f2a55959d6e56bd0d27b9573aac6fdd/src/agent.rs).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: Evidence is limited to the pinned first-party supported operating boundary.

### Absence scope

- Surfaces inspected: Explore/web tools, system/project prompts, compaction, persistence, model and UI configuration.
- Plausible first-party paths checked: Prospective external intelligence, generation/selection of strategic alternatives and return to operational capability.
- Why no material first-party path remains: The shipped mechanisms inform a current task or configure a model, with no autonomous strategic adaptation decision/feedback loop.

## S5 — Policy and identity

- State: —
- Function: No constitutive identity/ultimate-policy governance decision and authoritative return.
- Disturbance / variety regulated: Tool access, cancellation, fixed read-only Explore rights and human preferences constrain individual tasks, not highest-purpose conflicts.
- Decisive decision or feedback right: User determines prompts/model and cancels, deterministic rules enforce read-only child tools.
- Decision owner: User and tool guard rather than an S5 actor or eligible complete parent policy mode.
- Supporting / enforcement mechanisms: System prompt, AGENTS.md/CLAUDE.md, tool allowlists, auth/model config and TUI cancellation.
- Closure path: Settings and policy may alter next action, but no legitimate ultimate-purpose policy choice is deliberated and returned to govern the operating organization.
- Why this is / is not agent-owned: A human prompt, fixed permission rule or repo maintainer practice does not establish S5.
- Evidence: [src/config.rs](https://github.com/KAJdev/rum/blob/9c00bdb35f2a55959d6e56bd0d27b9573aac6fdd/src/config.rs); [src/tools/explore.rs](https://github.com/KAJdev/rum/blob/9c00bdb35f2a55959d6e56bd0d27b9573aac6fdd/src/tools/explore.rs); [src/main.rs](https://github.com/KAJdev/rum/blob/9c00bdb35f2a55959d6e56bd0d27b9573aac6fdd/src/main.rs).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: Evidence is limited to the pinned first-party supported operating boundary.

### Absence scope

- Surfaces inspected: Local prompts, model config, read-only tools, user steering, persistence and package governance boundary.
- Plausible first-party paths checked: Highest-order identity policy tension, legitimate deciding actor, ratification and binding policy return.
- Why no material first-party path remains: Shipped paths modify local task permissions and prompts, with no distinct legitimate ultimate-governance decision and closure.

## Distributed OSS parent arrangement

Rum's own maintainer/release CI is external to an installed coding session. A user repository's separately configured GitHub Actions check may supply complementary evidence; Rum owns the conditional feedback connector, not that check's policy or discretionary judgment. The locally queried SHA is not guaranteed to equal the last pushed ref.

## Self-hosted and non-human modes

Primary coding and read-only Explore are operational first-party modes. The accepted `S3*=C` witness is restricted to configured interactive TUI with a relevant successful push whose checked-out local HEAD matches the pushed revision and available CI failure logs. Headless print, missing CI/`gh`/logs, nonmatching pushed ref, or text-only false push detection do not establish that same complementary return path.

## Recursion

One coding project is served by a primary code-editing S1, with optional read-only Explore research. There is no established S2 conflict stabilizer. Independent checks can send complementary audit results through the TUI, but are not a separate native coding S1 or autonomous Rum auditor.

## Variety and escalation

Code/tool failures inform subsequent coding choices. Failed externally sourced CI logs can inform coding when the TUI's local-HEAD watch matches the pushed revision; the watcher itself cannot prove that relation. They do not establish whole-current S3 or future S4 management.

## Evidence gaps

- S3* constructor mode requires externally configured checks, authenticated `gh`, appropriate local-HEAD/pushed-ref alignment and available failure logs. The shipped watcher does not verify a real push or pushed ref. Independence, audit quality, and eventual repair are not established by the constructor alone; #1381 retains the owner adjudication.
- The read-only Explore child exists but no first-party inter-S1 conflict damping is evidenced; parallel tool calls are not autonomous code-work cells.
- No benchmark capability or efficacy is inferred from README descriptions or static code structure.
