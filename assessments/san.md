---
harness_id: san
project_name: San
repository: https://github.com/genai-io/san
review_ref: dd1b41882472fb76ce38dc3f88107deffc2e73bc
reviewed_at: 2026-09-25
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-25
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# San

## Review boundary

- System in focus: one first-party San interactive coding session at pinned revision `dd1b41882472fb76ce38dc3f88107deffc2e73bc`, including the standard reason→act→observe agent loop, durable/resumable session state, tool/permission machinery, optional AutoPilot copilot, bounded subagents, inspector/replay, and enabled self-learning surfaces.
- Purpose and identity: help a user complete software-engineering and related terminal work through an autonomous model/tool loop, with optional mission-level unattended continuation and first-party extensions for permissions, skills, memory, subagents, inspection and learning.
- Relevant environment: the user/operator, working repository/filesystem, shell/tool results, model/provider services, MCP/plugin integrations, project/user instructions and external systems reached through tools.
- Standard-distribution boundary: first-party San core loop, app/session wiring, AutoPilot mode, permission reviewer, subagent executor, transcript store, inspector/replay and self-learning machinery at the frozen revision. External model providers, MCP servers, plugins, user-authored skills and repository-development CI remain environment or adjacent systems.
- Credited operating / distribution surfaces: normal interactive session; persisted/resumed session; AutoPilot permission posture and mission steering; model-callable tools; bounded subagents; read-only inspector/replay; optional self-learning via `Evolve`.
- Adjacent first-party surfaces excluded from ownership: San's own tests/CI/release process; development-only fixtures; static documentation and package names where no runtime closure is wired; user-authored policy/persona content considered as constraints/configuration rather than automatic S5.
- First-party operating / deployment modes considered: ordinary interactive loop; AutoPilot mode with turn-end/kick/recovery steering; subagent execution; inspector server/replay; enabled self-learning with agent-triggered `Evolve`.
- Recursion level: the assessed organization is one San coding session. The long-lived main model/tool loop is the primary S1 unit. One-shot subagents are bounded delegated workers and are not promoted to independent S1 units at the parent recursion without additional viability/coordination evidence.
- Reviewed revision: `dd1b41882472fb76ce38dc3f88107deffc2e73bc`.
- Observation date: 2026-09-25.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

San's core runtime closes a standard model→tool→feedback loop: model output can request tools, San executes those actions under first-party permission/tool machinery, appends observations/results to the conversation, and continues model reasoning against the changed environment. Session/transcript machinery makes that operational state durable and resumable.

AutoPilot adds a distinct autonomous control actor above the ordinary work loop. In AutoPilot mode, a separate configured LLM judge receives the mission plus bounded recent session evidence after a clean turn, resumable step-limit/truncation stop, mission kick or recoverable failure. It chooses a structured `continue`, `done`, or hand-back outcome. A `continue` decision must include the next instruction; San visibly submits that instruction back into the main agent as the next user-style message. `done` retires the mission, while an unresolved human-only decision hands control back. This is credited as S3 because it regulates the current session's mission-level commitment and continuation on behalf of the whole session rather than merely executing the local tool step.

San also contains two surfaces that look like higher VSM functions by name but do not satisfy the Profile at this boundary. The permission `reviewer` is a pre-action judge for allow/escalate decisions and is not complementary audit of operational truth. The `inspector` is explicitly localhost-only and read-only: it exposes raw append-only transcripts, live tail and deterministic replay state, but no autonomous audit judgment or first-party feedback path from inspector findings into runtime control was established. Self-learning is substantive—after the main model explicitly calls `Evolve`, a restricted background fork reviews the completed turn and may write durable memory or agent-created skills used by future sessions—but the reviewed loop is retrospective experience consolidation, not an externally/prospectively oriented S4 conversation.

Primary evidence:

- [`internal/core/run.go`](https://github.com/genai-io/san/blob/dd1b41882472fb76ce38dc3f88107deffc2e73bc/internal/core/run.go) — production reason/act/observe model/tool execution loop.
- [`internal/agent/session.go`](https://github.com/genai-io/san/blob/dd1b41882472fb76ce38dc3f88107deffc2e73bc/internal/agent/session.go) and [`internal/agent/build.go`](https://github.com/genai-io/san/blob/dd1b41882472fb76ce38dc3f88107deffc2e73bc/internal/agent/build.go) — standard session/runtime composition and continuity.
- [`internal/app/autopilot.go`](https://github.com/genai-io/san/blob/dd1b41882472fb76ce38dc3f88107deffc2e73bc/internal/app/autopilot.go) — separate AutoPilot LLM judge, mission/session evidence, continuation/done/hand-back decisions and returned next-turn instruction.
- [`internal/reviewer/reviewer.go`](https://github.com/genai-io/san/blob/dd1b41882472fb76ce38dc3f88107deffc2e73bc/internal/reviewer/reviewer.go) — permission-review/steering judge inspected and not treated as S3* merely from naming.
- [`internal/subagent/executor.go`](https://github.com/genai-io/san/blob/dd1b41882472fb76ce38dc3f88107deffc2e73bc/internal/subagent/executor.go) — bounded one-shot subagent execution inspected for S2.
- [`internal/inspector/server.go`](https://github.com/genai-io/san/blob/dd1b41882472fb76ce38dc3f88107deffc2e73bc/internal/inspector/server.go) and [`internal/inspector/replay.go`](https://github.com/genai-io/san/blob/dd1b41882472fb76ce38dc3f88107deffc2e73bc/internal/inspector/replay.go) — read-only transcript viewer, live inspection and deterministic replay state.
- [`docs/packages/2-feature/inspector.md`](https://github.com/genai-io/san/blob/dd1b41882472fb76ce38dc3f88107deffc2e73bc/docs/packages/2-feature/inspector.md) — intended read-only inspector role.
- [`internal/selflearn/reviewer.go`](https://github.com/genai-io/san/blob/dd1b41882472fb76ce38dc3f88107deffc2e73bc/internal/selflearn/reviewer.go), [`internal/selflearn/prompts.go`](https://github.com/genai-io/san/blob/dd1b41882472fb76ce38dc3f88107deffc2e73bc/internal/selflearn/prompts.go) and [`docs/packages/2-feature/selflearn.md`](https://github.com/genai-io/san/blob/dd1b41882472fb76ce38dc3f88107deffc2e73bc/docs/packages/2-feature/selflearn.md) — agent-triggered post-turn learning, restricted review fork and future-session memory/skill writes.
- [`docs/concepts/harness-channels.md`](https://github.com/genai-io/san/blob/dd1b41882472fb76ce38dc3f88107deffc2e73bc/docs/concepts/harness-channels.md) — identity/policy/reminder channels and main/subagent context boundaries.

## Operational model

The main San agent owns open-ended work inside a durable session. It chooses model/tool actions, observes tool results and continues from those observations. Optional AutoPilot mode adds a separate LLM control loop that reviews mission and recent session evidence between turns and decides whether the organization should continue, finish or return control to the user. Other first-party mechanisms constrain permissions, delegate bounded work, expose transcripts/replay and optionally learn from prior completed turns.

## S1 — Operations

- State: A
- Function: transform user software-engineering/terminal objectives into repository, filesystem, command, research or other tool-mediated outcomes through a repeated reason→act→observe loop.
- Disturbance / variety regulated: changing repository/environment state, ambiguous task requirements, tool output/errors, model responses, permission outcomes, context pressure and user feedback.
- Decisive decision or feedback right: select substantive next model/tool actions and revise subsequent work from returned observations.
- Decision owner: the active San main agent model.
- Supporting / enforcement mechanisms: core run loop, tool registry, permissions/reviewer, session/transcript persistence, context management, provider adapters, skills/plugins/MCP and UI/runtime lifecycle.
- Closure path: user objective enters session → model reasons and selects action/tool → San executes under policy → observation/result returns into conversation → model chooses next action from changed evidence → task/environment state changes and the cycle continues.
- Boundary reachability: this is San's ordinary first-party interactive operating path, not a test-only or downstream composition.
- Why this is / is not agent-owned: removing the model leaves execution/policy machinery but removes the substantive choice of what work to do next and how to react to tool evidence.
- Evidence: [`internal/core/run.go`](https://github.com/genai-io/san/blob/dd1b41882472fb76ce38dc3f88107deffc2e73bc/internal/core/run.go); [`internal/agent/build.go`](https://github.com/genai-io/san/blob/dd1b41882472fb76ce38dc3f88107deffc2e73bc/internal/agent/build.go); [`internal/agent/session.go`](https://github.com/genai-io/san/blob/dd1b41882472fb76ce38dc3f88107deffc2e73bc/internal/agent/session.go).
- Basis: explicit + structural
- Confidence: high
- Caveats: model inference is external, but San supplies the standard first-party loop that repeatedly invokes that dependency and applies its decisions to the environment.

## S2 — Coordination

- State: —
- Function: no material first-party S2 relation is established at the assessed session recursion.
- Disturbance / variety regulated: no qualifying inter-S1 interference/oscillation witness is established.
- Decisive decision or feedback right: not established.
- Decision owner: none established for S2 at this boundary.
- Supporting / enforcement mechanisms: subagent charters, bounded child execution, task/background machinery, session boundaries and concurrency protections can isolate/delegate work but do not by themselves establish coordination.
- Closure path: not applicable; no reviewed path reconstructs distinct credited S1 units → concrete inter-S1 disturbance → S2-specific attenuation → feedback changing subsequent S1 behaviour.
- Distinct S1 units: the long-lived main session loop is the established S1. One-shot subagents are bounded delegated workers and are not credited as separate viable S1s at the parent recursion merely from process/session plurality.
- Inter-S1 disturbance: not established.
- Attenuating coordination relation: not established beyond generic delegation/isolation/execution boundaries.
- Feedback into subsequent S1 behaviour: not established for an S2-specific relation.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: it is deliberately not mapped as S2; the reviewed evidence supplies delegation and worker isolation, not the Profile's complete inter-S1 disturbance/attenuation witness.
- Why this is / is not agent-owned: no S2 function is established, so ownership classification does not proceed.
- Evidence: [`internal/subagent/executor.go`](https://github.com/genai-io/san/blob/dd1b41882472fb76ce38dc3f88107deffc2e73bc/internal/subagent/executor.go); [`docs/concepts/harness-channels.md`](https://github.com/genai-io/san/blob/dd1b41882472fb76ce38dc3f88107deffc2e73bc/docs/concepts/harness-channels.md).
- Basis: explicit + structural absence review
- Confidence: high
- Caveats: a wider deployment could organize multiple long-lived San sessions as distinct S1 units, but that would be a different system-in-focus requiring separate evidence.

### Absence scope

- Surfaces inspected: subagent executor, main/subagent context boundaries, task/background execution and session/runtime architecture.
- Plausible first-party paths checked: parent-to-subagent delegation, child-session execution, task routing and isolation/concurrency mechanisms.
- Why no material first-party path remains: the reviewed paths assign or isolate work; none establishes a concrete inter-S1 disturbance plus an S2-specific feedback relation at the chosen recursion.

## S3 — Inside-and-now control

- State: A
- Function: regulate the current San session's mission-level commitment and continuation between operational turns, deciding whether present work should continue autonomously, terminate as accomplished, or return to human authority.
- Disturbance / variety regulated: locally completed turns that leave the mission incomplete, step-limit/truncation stops, recoverable failures, uncertain next steps, completed missions and situations that genuinely require a human-only decision/access grant.
- Decisive decision or feedback right: choose `continue`, `done`, or hand-back and, for `continue`, author the concrete next instruction sent back to the main agent.
- Decision owner: the separate AutoPilot LLM judge/copot actor when AutoPilot mode is engaged.
- Supporting / enforcement mechanisms: persisted AutoPilot mission/config, recent-transcript/evidence renderer, continuation/recovery budgets, stop-reason gates, UI submit path and deterministic validation of structured decision states.
- Closure path: main S1 turn ends or stops resumably → AutoPilot receives mission plus recent whole-session evidence → AutoPilot chooses continue/done/hand-back → on continue its instruction is submitted as the next visible input to the main agent; on done the mission is retired; otherwise control returns to the user → subsequent current operation changes accordingly.
- Boundary reachability: AutoPilot is a first-party session mode wired through the San app and can be started/configured from the product rather than requiring downstream code.
- Whole-system current view: the controller receives the mission and bounded recent session evidence including conversation, compact summaries and tool outcomes, and is explicitly instructed to judge what is already accomplished from all supplied evidence rather than only the last turn.
- Current-control decision scope: the session's current commitment to unattended mission execution—continue with a new concrete step, stop as complete, or escalate control back to the human.
- Why this is / is not agent-owned: budgets/stop gates enforce safe boundaries, but they do not choose the mission-level continuation response or author the next instruction. Removing the AutoPilot model leaves those gates but removes the discretionary current-control judgment.
- Evidence: [`internal/app/autopilot.go`](https://github.com/genai-io/san/blob/dd1b41882472fb76ce38dc3f88107deffc2e73bc/internal/app/autopilot.go); [`internal/reviewer/reviewer.go`](https://github.com/genai-io/san/blob/dd1b41882472fb76ce38dc3f88107deffc2e73bc/internal/reviewer/reviewer.go).
- Basis: explicit + structural
- Confidence: high
- Caveats: the mapping is intentionally narrow to AutoPilot's mission-level current-control right; ordinary permission approval or the core reason→act→observe cycle are not separately counted as S3.

## S3* — Complementary audit

- State: —
- Function: no material first-party complementary-audit closure is established at the assessed session recursion.
- Disturbance / variety regulated: San exposes operational transcripts and replay state that could reveal mismatches, but no first-party independent audit judgment/control loop is established over those observations.
- Decisive decision or feedback right: not established.
- Decision owner: none established for S3* at this boundary.
- Supporting / enforcement mechanisms: append-only transcripts, integrity/digest-aware replay, localhost read-only inspector, records/live-tail/state APIs and a permission reviewer.
- Closure path: not applicable; the reviewed inspector path exposes operational reality but does not itself produce an independent corrective verdict that returns into runtime control. The permission reviewer acts before protected actions rather than auditing operational claims after/beside routine reporting.
- Claim being audited: no qualifying first-party audit claim/loop established.
- Ordinary reporting path: normal session messages/tool results/transcript records.
- Complementary access path: inspector/replay can reconstruct raw transcript/replay state independently of the rendered assistant narrative.
- Independence boundary: access is read-only and separate from the work loop, but access independence alone is insufficient without an audit judgment and feedback path.
- Who acts on findings: not established as a first-party S3* closure; a human can inspect/debug, but generic human observation is not enough for the Methodology's autonomous audit state.
- Why this is / is not agent-owned: no autonomous audit actor owns a complementary judgment. The pre-action permission reviewer owns a different function and is not reclassified as S3*.
- Evidence: [`internal/inspector/server.go`](https://github.com/genai-io/san/blob/dd1b41882472fb76ce38dc3f88107deffc2e73bc/internal/inspector/server.go); [`internal/inspector/replay.go`](https://github.com/genai-io/san/blob/dd1b41882472fb76ce38dc3f88107deffc2e73bc/internal/inspector/replay.go); [`docs/packages/2-feature/inspector.md`](https://github.com/genai-io/san/blob/dd1b41882472fb76ce38dc3f88107deffc2e73bc/docs/packages/2-feature/inspector.md); [`internal/reviewer/reviewer.go`](https://github.com/genai-io/san/blob/dd1b41882472fb76ce38dc3f88107deffc2e73bc/internal/reviewer/reviewer.go).
- Basis: explicit + structural absence review
- Confidence: high
- Caveats: the inspector is a strong constructor/debugging surface from which an auditor could be composed, but Methodology `0.3.6` does not award `C` until the S3* function itself is established.

### Absence scope

- Surfaces inspected: inspector HTTP server, transcript replay/integrity path, live stream, inspector documentation, permission reviewer and session transcript machinery.
- Plausible first-party paths checked: raw replay inspection, transcript-integrity reconstruction, live tail/debugging and pre-action permission review.
- Why no material first-party path remains: reviewed surfaces either expose evidence without independent audit judgment/return or judge whether a proposed action may proceed before execution. Neither closes complementary audit of operational reality.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party outside-and-then organizational adaptation loop is established at the assessed session recursion.
- Disturbance / variety regulated: not established as an external/prospective adaptation function.
- Decisive decision or feedback right: not established.
- Decision owner: none established for S4 at this boundary.
- Supporting / enforcement mechanisms: self-learning can be triggered by the main model via `Evolve`; after a clean turn a restricted background fork reviews the completed conversation and can write durable project memory or agent-created skills that affect future sessions.
- Closure path: not applicable for S4. The reviewed self-learning path closes retrospective experience consolidation into future memory/skills, but no first-party path reconstructs external/future-relevant sensing → development of adaptation options → S4 adaptation judgment → return into present capability/S3.
- Why this is / is not agent-owned: the main model autonomously decides when a turn is worth learning from and the review fork can decide what lesson/skill to write, but autonomy plus learning is not sufficient. The Profile explicitly excludes generic learning/self-improvement unless it participates in an external-and-prospective adaptation loop.
- Evidence: [`docs/packages/2-feature/selflearn.md`](https://github.com/genai-io/san/blob/dd1b41882472fb76ce38dc3f88107deffc2e73bc/docs/packages/2-feature/selflearn.md); [`internal/selflearn/reviewer.go`](https://github.com/genai-io/san/blob/dd1b41882472fb76ce38dc3f88107deffc2e73bc/internal/selflearn/reviewer.go); [`internal/selflearn/prompts.go`](https://github.com/genai-io/san/blob/dd1b41882472fb76ce38dc3f88107deffc2e73bc/internal/selflearn/prompts.go).
- Basis: explicit + structural absence review
- Confidence: high
- Caveats: self-learning materially changes future capability, so a wider organization that also supplies external/prospective sensing and adaptation selection could map differently; that wider S4 closure is not present at the frozen session boundary.

### Absence scope

- Surfaces inspected: `Evolve` trigger, post-turn reviewer, memory/skill write paths, future-session capability rebuild, skills/memory channels, AutoPilot and ordinary tool/research execution.
- Plausible first-party paths checked: retrospective lesson extraction, agent-created skill mutation, durable memory writes and ordinary environment/tool observations.
- Why no material first-party path remains: the reviewed learning loop is driven by completed internal operational experience, not a demonstrated model of changing external/future conditions that develops and returns adaptation options to present organizational capability.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy decision loop is established at the assessed session recursion.
- Disturbance / variety regulated: not established as an identity/ultimate-policy matter.
- Decisive decision or feedback right: not established.
- Decision owner: none established for S5 within the standard session boundary.
- Supporting / enforcement mechanisms: system-prompt identity/persona, rules, project/user memory, permission modes, AutoPilot mission/system prompt, reviewer decisions, skills and human approval constrain/configure operation but do not establish ultimate-policy closure.
- Closure path: not applicable; no reviewed first-party path shows an identity/ultimate-policy issue reaching legitimate ultimate authority and returning as authoritative policy governing subsequent San operation.
- Why this is / is not agent-owned: model actors operate inside configured identity, mission and permission boundaries; they are not shown exercising ultimate authority over those boundaries. Ordinary human permission or configuration edits likewise do not become S5 without an identity-level issue/decision/return loop.
- Evidence: [`docs/concepts/harness-channels.md`](https://github.com/genai-io/san/blob/dd1b41882472fb76ce38dc3f88107deffc2e73bc/docs/concepts/harness-channels.md); [`internal/app/autopilot.go`](https://github.com/genai-io/san/blob/dd1b41882472fb76ce38dc3f88107deffc2e73bc/internal/app/autopilot.go); [`internal/reviewer/reviewer.go`](https://github.com/genai-io/san/blob/dd1b41882472fb76ce38dc3f88107deffc2e73bc/internal/reviewer/reviewer.go).
- Basis: explicit + structural absence review
- Confidence: high
- Caveats: San deliberately exposes configurable identity/policy channels; Methodology `0.3.6` does not treat their existence as S5 without the identity/ultimate-policy function itself.

### Absence scope

- Surfaces inspected: system-prompt identity/rules channels, persona/policy configuration, project/user memory, permission reviewer, AutoPilot mission/system prompt, skill/memory mutation and human control paths.
- Plausible first-party paths checked: persona selection, policy/rules prompt composition, permission approval/escalation, AutoPilot mission retirement/hand-back, self-learning writes and user configuration changes.
- Why no material first-party path remains: these paths define constraints, task intent, permission posture or learned capability, but no current standard path elevates a genuine identity/ultimate-policy issue to a legitimate ultimate authority and returns its decision to govern subsequent operation.

## Distributed OSS parent arrangement

San is open source, but contributor/maintainer governance was not used to infer runtime parent ownership. The assessed recursion is one operating San session. Repository development/release decisions are adjacent unless a standard runtime return loop is established; no such parent S3/S4/S5 mode is claimed.

## Self-hosted and non-human modes

San is self-hosted and operator-supervised. The operator can change permissions, mission, persona/settings and take control back from AutoPilot, but these generic controls do not independently establish Methodology parent notation. S3 is credited to the autonomous AutoPilot mode; no separate qualifying parent-governed S3/S4/S5 closure is claimed.

## Recursion

The primary recursion is one long-lived San session. The main model/tool loop is S1; AutoPilot is a distinct metasystemic current-control actor over that session when enabled. One-shot subagents are bounded operations beneath the session and are not promoted to recursive viable systems or separate S1s without stronger evidence.

## Variety and escalation

San attenuates variety through permission modes, reviewer gates, context compaction, system/reminder channels, session persistence, subagent charters and bounded AutoPilot continuation/recovery budgets. Operational variety returns through tool results and conversation state. In AutoPilot mode, mission-level variety is transduced into `continue/done/hand-back`; human-only decisions and non-resumable states escalate back to the operator. Self-learning can amplify future response variety through durable memory/skills without being classified as S4 at this boundary.

## Evidence gaps

- No fresh runtime trace was executed inside this assessment environment; positive claims rely on pinned first-party source/docs and production wiring.
- S3 is intentionally narrow to the AutoPilot mission-level control loop; the core agent loop itself is not double-counted as S3.
- S3* remains absent despite strong read-only replay observability because no autonomous audit judgment plus corrective return path was established.
- S4 remains absent despite genuine autonomous self-learning because the reviewed path is retrospective operational learning rather than an external/prospective adaptation conversation.
- S2 remains absent because subagent plurality/delegation does not satisfy the Profile witness at the chosen recursion.
