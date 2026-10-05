---
harness_id: clawkeeper
project_name: ClawKeeper
repository: https://github.com/SafeAI-Lab-X/ClawKeeper
review_ref: 69db077317bd8a89777c7670295539ed93145f46
reviewed_at: 2026-10-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-04
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: A
autonomy_s5: —
---

# ClawKeeper

## Review boundary

- System in focus: the first-party ClawKeeper safety middleware and optional Watcher at frozen revision `69db077317bd8a89777c7670295539ed93145f46`, including Judge/guard chains, Watcher intent/history supervision, host adapters, security scanners, learned-pattern synthesis/store/hot reload, and enforcement callbacks.
- Purpose and identity: regulate tool-using agent execution by deciding whether proposed actions are safe to allow, require operator attention, or deny; improve future guard coverage when contextual Watcher decisions expose deterministic blind spots.
- Relevant environment: user intent, proposed tool calls, recent tool-call trajectories, tool results, credentials/files/URLs, hostile or injected content, supported host-agent callbacks, and recurring attack/bypass patterns.
- Standard-distribution boundary: `clawkeeper_core`, shipped adapters, HTTP core and optional Watcher daemon are inside. Hermes/OpenClaw/other host-agent reasoning loops and their task semantics are external; external OpenAI-compatible inference supplies Watcher model execution but does not donate unrelated host VSM functions.
- Credited operating / distribution surfaces: `README.md`; `clawkeeper_core/judge.py`; `clawkeeper_core/guards/*`; `clawkeeper_core/adapters/hermes.py`; `clawkeeper_core/watcher/{agent,tools,policy,learner,reload,daemon}.py`; `clawkeeper_core/{audit,scanner,maintenance,server}.py`.
- Adjacent first-party surfaces excluded from ownership: legacy snapshots; repository-development red-team tests/benchmarks; host-agent internals; operator dashboards that only expose findings; upstream-sharing endpoint infrastructure; external model/provider internals.
- First-party operating / deployment modes considered: deterministic Judge/guards; Hermes adapter pre-tool enforcement; HTTP Judge; optional model-backed Watcher; per-session Watcher history/intent; learned-pattern self-improvement; on-demand audit/scanners and maintenance endpoints.
- Recursion level: one ClawKeeper-protected agent session is the focal organization. Individual safety decisions are operational S1; Watcher trajectory supervision is whole-session current control. The protected coding agent remains an external operating system.
- Reviewed revision: `69db077317bd8a89777c7670295539ed93145f46`.
- Observation date: 2026-10-04.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

ClawKeeper is inserted between an external tool-using agent and its tools. Deterministic pre-tool guards inspect commands, paths, scripts and URLs. The Hermes adapter registers a first-party `pre_tool_call` hook so a blocking finding actually skips tool execution. The optional Watcher adds model-backed contextual judgment: it receives the stated intent, recent calls, deterministic findings and the proposed call, emits `allow|ask|deny`, passes that proposal through a deterministic post-filter, and feeds `deny/ask` back into the host's pre-tool hook.

The Watcher also closes a durable adaptation path. When it confidently catches a dangerous call that all deterministic guards missed, it asks the model to synthesize a narrow regex, validates that regex against benign commands, stores the candidate, and immediately hot-reloads it into the live deterministic guard layer. Future tool calls are therefore regulated by a capability learned from an observed external bypass.

Primary evidence:

- [`README.md`](https://github.com/SafeAI-Lab-X/ClawKeeper/blob/69db077317bd8a89777c7670295539ed93145f46/README.md)
- [`clawkeeper_core/watcher/agent.py`](https://github.com/SafeAI-Lab-X/ClawKeeper/blob/69db077317bd8a89777c7670295539ed93145f46/clawkeeper_core/watcher/agent.py)
- [`clawkeeper_core/watcher/learner.py`](https://github.com/SafeAI-Lab-X/ClawKeeper/blob/69db077317bd8a89777c7670295539ed93145f46/clawkeeper_core/watcher/learner.py)
- [`clawkeeper_core/watcher/reload.py`](https://github.com/SafeAI-Lab-X/ClawKeeper/blob/69db077317bd8a89777c7670295539ed93145f46/clawkeeper_core/watcher/reload.py)
- [`clawkeeper_core/adapters/hermes.py`](https://github.com/SafeAI-Lab-X/ClawKeeper/blob/69db077317bd8a89777c7670295539ed93145f46/clawkeeper_core/adapters/hermes.py)
- [`clawkeeper_core/watcher/policy.py`](https://github.com/SafeAI-Lab-X/ClawKeeper/blob/69db077317bd8a89777c7670295539ed93145f46/clawkeeper_core/watcher/policy.py)
- [`clawkeeper_core/audit.py`](https://github.com/SafeAI-Lab-X/ClawKeeper/blob/69db077317bd8a89777c7670295539ed93145f46/clawkeeper_core/audit.py)

## Operational model

A host proposes a tool call. ClawKeeper first runs deterministic guards; when the Watcher is enabled it additionally evaluates the action against the session's stated intent and recent trajectory. The final safety decision is enforced before tool execution. High-confidence Watcher catches missed by deterministic guards can be generalized into learned guard patterns and loaded into the running process.

## S1 — Operations

- State: A
- Function: make a contextual safety decision for a proposed tool action and close that decision into the host execution boundary.
- Disturbance / variety regulated: benign versus malicious or drifted shell/filesystem/network/tool actions, prompt-injection consequences, credential access/exfiltration chains, contextual false positives and bypasses that require intent/history-sensitive judgment.
- Decisive decision or feedback right: choose `allow`, `ask`, or `deny` for the proposed action after interpreting current intent, recent trajectory and deterministic evidence.
- Decision owner: the model-backed Watcher role in the enabled Watcher mode; deterministic guards/post-filter constrain and can override that decision.
- Supporting / enforcement mechanisms: deterministic guard chain; Watcher prompt; post-filter; session history; host adapter; pre-tool hook; HTTP Watcher client.
- Closure path: host proposes tool call → deterministic findings + intent/history reach Watcher → model-backed safety proposal → deterministic post-filter → adapter returns block/allow result → host skips or proceeds with the tool operation.
- Boundary reachability: the Watcher daemon/client and host adapter are shipped first-party integration surfaces; downstream users configure a model endpoint but do not need to invent the safety role or enforcement feedback path.
- Why this is / is not agent-owned: without the Watcher model, deterministic guards still enforce known patterns but cannot make the same contextual judgment over intent and recent trajectory. The model therefore owns the open-ended safety discretion in this first-party mode.
- Evidence: [`clawkeeper_core/watcher/agent.py`](https://github.com/SafeAI-Lab-X/ClawKeeper/blob/69db077317bd8a89777c7670295539ed93145f46/clawkeeper_core/watcher/agent.py); [`clawkeeper_core/watcher/tools.py`](https://github.com/SafeAI-Lab-X/ClawKeeper/blob/69db077317bd8a89777c7670295539ed93145f46/clawkeeper_core/watcher/tools.py); [`clawkeeper_core/watcher/policy.py`](https://github.com/SafeAI-Lab-X/ClawKeeper/blob/69db077317bd8a89777c7670295539ed93145f46/clawkeeper_core/watcher/policy.py); [`clawkeeper_core/adapters/hermes.py`](https://github.com/SafeAI-Lab-X/ClawKeeper/blob/69db077317bd8a89777c7670295539ed93145f46/clawkeeper_core/adapters/hermes.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: host-agent task reasoning is not credited. S1 is ClawKeeper's own safety operation, not the external coding operation.

## S2 — Coordination

- State: —
- Function: no material same-recursion inter-S1 coordination function was established.
- Disturbance / variety regulated: multiple guard modules and external tool calls coexist, but they are stages/inputs in one safety path rather than distinct autonomous S1 units whose interaction produces an evidenced interference.
- Decisive decision or feedback right: not established at S2.
- Decision owner: not established as a first-party S2 owner.
- Supporting / enforcement mechanisms: ordered guard chains; deterministic strictest-wins post-filter; per-session history; adapter routing.
- Closure path: guard findings are combined inside one safety decision path; no separate inter-S1 conflict→coordination→changed S1-behavior loop is evidenced.
- Why this is / is not agent-owned: aggregation, routing and arbitration among guard outputs do not by themselves establish S2.
- Evidence: [`clawkeeper_core/watcher/policy.py`](https://github.com/SafeAI-Lab-X/ClawKeeper/blob/69db077317bd8a89777c7670295539ed93145f46/clawkeeper_core/watcher/policy.py); [`clawkeeper_core/watcher/tools.py`](https://github.com/SafeAI-Lab-X/ClawKeeper/blob/69db077317bd8a89777c7670295539ed93145f46/clawkeeper_core/watcher/tools.py).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: coordination among external agents protected by one deployment would belong to that host organization unless independently closed by ClawKeeper.

### Absence scope

- Surfaces inspected: guard chain, Watcher, session history, post-filter, adapters, server, scans and maintenance.
- Plausible first-party paths checked: deterministic-vs-Watcher arbitration; several protected sessions; guard ordering; host routing.
- Why no material first-party path remains: the plurality is component/stage plurality inside one safety controller, not distinct same-recursion S1 units with a concrete interaction disturbance.

## S3 — Inside-and-now control

- State: A
- Function: supervise the current protected agent trajectory as a whole and intervene in the next tool action when its relation to intent/history or current risk becomes unsafe.
- Disturbance / variety regulated: multi-step drift, attack chains that become suspicious only across recent calls, mismatch between stated intent and proposed action, current deterministic findings and accumulated session context.
- Decisive decision or feedback right: at each proposed tool call, use session-level intent and recent-call state to permit the current trajectory to continue, require escalation, or halt the action before execution.
- Decision owner: the model-backed Watcher role, subject to stricter deterministic post-filter vetoes.
- Supporting / enforcement mechanisms: bounded per-session history; remembered intent; deterministic findings; Watcher prompt; fail-safe; post-filter; blocking pre-tool hook.
- Closure path: current session intent + recent tool history + proposed next action → Watcher whole-session safety judgment → deny/ask/allow → host pre-tool enforcement changes the next operation → the call is appended to session history for the following current-control decision.
- Boundary reachability: Watcher history, evaluator, client and Hermes `pre_tool_call` enforcement are shipped and wired as a supported optional ClawKeeper mode.
- Why this is / is not agent-owned: deterministic rules can veto known hardline cases, but contextual current-trajectory intervention depends on model judgment over the whole recent session. Removing the model removes that discretionary supervisory choice.
- Evidence: [`clawkeeper_core/watcher/agent.py`](https://github.com/SafeAI-Lab-X/ClawKeeper/blob/69db077317bd8a89777c7670295539ed93145f46/clawkeeper_core/watcher/agent.py); [`clawkeeper_core/watcher/tools.py`](https://github.com/SafeAI-Lab-X/ClawKeeper/blob/69db077317bd8a89777c7670295539ed93145f46/clawkeeper_core/watcher/tools.py); [`clawkeeper_core/adapters/hermes.py`](https://github.com/SafeAI-Lab-X/ClawKeeper/blob/69db077317bd8a89777c7670295539ed93145f46/clawkeeper_core/adapters/hermes.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: this is safety current-control over the protected session, not task prioritization for the external host agent.
- Whole-system current view: stated intent, bounded recent tool-call trajectory, proposed next call and current deterministic guard findings for the protected session.
- Current-control decision scope: whether the session may execute the proposed next tool action, must ask/escalate, or must block it now.

## S3* — Complementary audit

- State: —
- Function: on-demand audit and scanners provide materially different evidence, but no standard first-party feedback path automatically or authoritatively closes those findings back into current control.
- Disturbance / variety regulated: configuration weaknesses, dangerous skills, historical log patterns and control-catalogue findings can be detected outside the routine pre-tool path.
- Decisive decision or feedback right: not established as a closed S3* audit judgment that necessarily returns into subsequent current regulation.
- Decision owner: audit findings are deterministic; remediation requires a separate operator/client invocation of maintenance or manual action.
- Supporting / enforcement mechanisms: `/v1/audit`; log/skill scanners; finding scores; `harden`; rollback; next-step recommendations.
- Closure path: audit/scanner reads independent state/history → returns findings/recommendations; any transition into `harden` or manual remediation is a separate external action, so the required findings→control closure is not first-party-complete.
- Why this is / is not agent-owned: the evidence path is complementary, but observability plus an optional separate remediation API is insufficient to credit a closed S3* function.
- Evidence: [`clawkeeper_core/audit.py`](https://github.com/SafeAI-Lab-X/ClawKeeper/blob/69db077317bd8a89777c7670295539ed93145f46/clawkeeper_core/audit.py); [`clawkeeper_core/scanner.py`](https://github.com/SafeAI-Lab-X/ClawKeeper/blob/69db077317bd8a89777c7670295539ed93145f46/clawkeeper_core/scanner.py); [`clawkeeper_core/maintenance.py`](https://github.com/SafeAI-Lab-X/ClawKeeper/blob/69db077317bd8a89777c7670295539ed93145f46/clawkeeper_core/maintenance.py); [`clawkeeper_core/server.py`](https://github.com/SafeAI-Lab-X/ClawKeeper/blob/69db077317bd8a89777c7670295539ed93145f46/clawkeeper_core/server.py).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: a host/operator composition can close this loop; that external composition is not credited to ClawKeeper alone.

### Absence scope

- Surfaces inspected: audit control catalogue, log scanner, skill scanner, harden/rollback, server endpoints, dashboard-facing findings.
- Plausible first-party paths checked: audit→harden; scanner→policy; historical-event scan→Watcher; audit finding→automatic current blocking.
- Why no material first-party path remains: audit/scanner findings are returned as reports and recommendations. No standard shipped path makes those findings themselves trigger or govern subsequent current-control decisions without an external invocation.

## S4 — Outside-and-then intelligence

- State: A
- Function: learn a new future-facing deterministic guard from an observed external attack/bypass pattern and return it into live safety capability.
- Disturbance / variety regulated: novel malicious commands or close variants that evade the existing deterministic guard repertoire but are recognized contextually by the Watcher.
- Decisive decision or feedback right: generalize a confidently detected bypass into a candidate regex/guard target and decide whether it is specific enough to become a persistent future guard.
- Decision owner: the model-backed Watcher synthesis role generates the adaptation; deterministic validation rejects invalid, duplicate or benign-overmatching candidates before activation.
- Supporting / enforcement mechanisms: high-confidence missed-guard trigger; synthesis prompt; benign corpus; regex compilation; `LearnedPatternStore`; guard-target classification; hot-reload bridge; optional upstream fingerprint sharing.
- Closure path: external proposed call bypasses deterministic guards → Watcher denies/asks with high confidence → model synthesizes a generalized pattern → validation/persistence accepts it → `apply_learned_patterns()` mutates live guard rules → future calls are regulated by the new capability.
- Boundary reachability: learning, persistence and hot reload are called directly by the shipped Watcher evaluator when the trigger condition holds; no downstream glue is required beyond enabling Watcher mode.
- Why this is / is not agent-owned: generic memory is not credited; the positive witness is the model's prospective generalization of a newly observed threat into a reusable guard option that is automatically returned to present capability.
- Evidence: [`clawkeeper_core/watcher/agent.py`](https://github.com/SafeAI-Lab-X/ClawKeeper/blob/69db077317bd8a89777c7670295539ed93145f46/clawkeeper_core/watcher/agent.py); [`clawkeeper_core/watcher/learner.py`](https://github.com/SafeAI-Lab-X/ClawKeeper/blob/69db077317bd8a89777c7670295539ed93145f46/clawkeeper_core/watcher/learner.py); [`clawkeeper_core/watcher/reload.py`](https://github.com/SafeAI-Lab-X/ClawKeeper/blob/69db077317bd8a89777c7670295539ed93145f46/clawkeeper_core/watcher/reload.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: optional upstream sharing is not needed for the local S4 closure; the credited loop is local learning from externally presented attack variety.
- External distinction: an action that passed all current deterministic guards but is judged dangerous by the contextual Watcher.
- Future / prospective distinction: the synthesized regex is explicitly required to match the observed command and close variants, so it is a guard for future related actions rather than a record of the single episode.
- Adaptation option generated: a model-generated candidate pattern plus target guard class and confidence, bounded by benign-corpus and regex validation.
- Path back into current capability / S3: accepted candidates are persisted and immediately hot-reloaded into live deterministic guard modules used by subsequent pre-tool safety decisions.

## S5 — Policy and identity

- State: —
- Function: no material identity/ultimate-policy closure was established.
- Disturbance / variety regulated: safety policy, confirmation thresholds, guard rules and fail-safe behavior constrain execution but remain ordinary operational safety policy.
- Decisive decision or feedback right: not established for an identity- or ultimate-policy-level issue.
- Decision owner: configuration/operator for policy values; Watcher and deterministic guards apply those values within current safety operation.
- Supporting / enforcement mechanisms: default policy; deterministic hardline vetoes; config; guard rules; operator confirmation path.
- Closure path: not applicable at S5.
- Why this is / is not agent-owned: a safety filter or policy file does not become S5 merely because it has final veto power over ordinary tool calls.
- Evidence: [`clawkeeper_core/judge.py`](https://github.com/SafeAI-Lab-X/ClawKeeper/blob/69db077317bd8a89777c7670295539ed93145f46/clawkeeper_core/judge.py); [`clawkeeper_core/watcher/policy.py`](https://github.com/SafeAI-Lab-X/ClawKeeper/blob/69db077317bd8a89777c7670295539ed93145f46/clawkeeper_core/watcher/policy.py).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: a parent organization may treat some security policy as identity-level governance; that higher-recursion authority is not a first-party ClawKeeper function.

### Absence scope

- Surfaces inspected: Judge policy, Watcher post-filter, hardline rules, configuration, maintenance, state rule block and operator-confirmation paths.
- Plausible first-party paths checked: policy thresholds; `always/ask/deny` behavior; learned rules; state constitution; maintenance/rollback.
- Why no material first-party path remains: all located policy choices govern ordinary execution safety. No identity/ultimate-policy dispute is routed to a legitimate ultimate authority and returned as organizational policy.

## Recursion

The focal system is one ClawKeeper safety organization protecting one external agent session. Contextual safety decisions are S1 operations; Watcher history/intent supervision supplies S3 current control; learned-pattern synthesis supplies S4 adaptation. The external coding/task agent is not absorbed into this recursion.

## Variety and escalation

Deterministic guards attenuate known attack variety cheaply. The Watcher amplifies regulatory variety for contextual and multi-step threats and can escalate uncertainty to `ask`. Hardline deterministic findings override an unsafe model proposal. Novel bypasses can be converted into future deterministic coverage, reducing repeated dependence on expensive contextual judgment.

## Evidence gaps

No evidence gap requires `?` at the frozen revision. S3* is deliberately conservative: complementary audit evidence exists, but its return-to-control path remains externally invoked.

**Vector:** A · — · A · — · A · —
