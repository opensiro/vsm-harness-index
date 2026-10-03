---
harness_id: defenseclaw
project_name: DefenseClaw
repository: https://github.com/cisco-ai-defense/defenseclaw
review_ref: 85029e57e9094debd9366a7d5a9f7e6d5c3ef6fc
reviewed_at: 2026-10-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-04
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# DefenseClaw

## Review boundary

- System in focus: the first-party DefenseClaw security-governance runtime at frozen revision `85029e57e9094debd9366a7d5a9f7e6d5c3ef6fc`, including the Go guardrail gateway, local/remote scanners, optional model-backed LLM Judge, policy finalization, native connector hooks, admission/enforcement, audit persistence and operator CLI.
- Purpose and identity: inspect agent prompts, completions, tool calls/results and install/runtime assets; make enforceable security decisions; block, confirm, alert or allow according to current evidence and policy while preserving durable audit evidence.
- Relevant environment: user intent, current and recent tool calls, prompt/completion/tool-result content, installed skills/plugins/MCPs, remote AI Defense verdicts, local detector findings, connector/session identity, operator policy and runtime health.
- Standard-distribution boundary: DefenseClaw gateway, hook adapters, Judge, scanners, policy/enforcement, audit store and CLI are inside. OpenClaw/Claude Code/Codex/Cursor/other protected agent reasoning loops are external; Cisco AI Defense cloud inspection is an external evidence/decision service in managed mode and is not borrowed to establish OSS autonomous ownership where the local model-backed Judge already closes the claimed path.
- Credited operating / distribution surfaces: `internal/gateway/{guardrail,llm_judge,inspect,decision,tool_policy_lookup,asset_policy_runtime}.go`; `internal/enforce/*`; `internal/audit/*`; `cli/defenseclaw/enforce/*`; `cli/defenseclaw/{guardrail,openclaw_guardrail,llm,audit_actions}.py`; native connector hooks.
- Adjacent first-party surfaces excluded from ownership: benchmark/LLM-judge evaluation corpora; test suites; observability dashboards/exporters; contributor/release tooling; protected-agent internals; managed Cisco cloud internals; docs-only future work.
- First-party operating / deployment modes considered: local/open-source guardrail gateway with optional LLM Judge; native connector hook enforcement; asset admission/runtime enforcement; observe/action modes; local policy/rule packs; audit/evidence persistence; managed mode only as a boundary contrast.
- Recursion level: one DefenseClaw-protected agent session/security-governance organization. Individual safety classifications are S1 operations; bounded session intent/recent-tool context supports current whole-session S3 supervision.
- Reviewed revision: `85029e57e9094debd9366a7d5a9f7e6d5c3ef6fc`.
- Observation date: 2026-10-04.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

DefenseClaw combines deterministic local detectors, optional Cisco AI Defense inspection, an optional model-backed LLM Judge and OPA/fallback policy finalization. Its native connector hooks place this machinery on the execution boundary: tool-call and message content are inspected, a `ToolInspectVerdict` carries `block`, `confirm`, `alert` or `allow`, and action mode preserves the enforceable action consumed by hook scripts/connector handlers.

The LLM Judge is first-party runtime code rather than an external host-agent function. It classifies prompt injection, PII/exfiltration and tool-call risk through a configured model provider. For tool calls it maintains bounded per-session context: the latest user intent plus recent tool events are incorporated into the next judge sample. This makes a later safety decision sensitive to the current trajectory rather than only the isolated call.

DefenseClaw also has rich audit storage, scanners, alerts and observability. Those surfaces preserve and expose complementary evidence, but the inspected standard paths do not show an independent audit judgment automatically or authoritatively returning findings into current control. Policy/rule reload is operator/config driven rather than an autonomous external-prospective adaptation loop.

Primary evidence:

- [`internal/gateway/llm_judge.go`](https://github.com/cisco-ai-defense/defenseclaw/blob/85029e57e9094debd9366a7d5a9f7e6d5c3ef6fc/internal/gateway/llm_judge.go)
- [`internal/gateway/inspect.go`](https://github.com/cisco-ai-defense/defenseclaw/blob/85029e57e9094debd9366a7d5a9f7e6d5c3ef6fc/internal/gateway/inspect.go)
- [`internal/gateway/guardrail.go`](https://github.com/cisco-ai-defense/defenseclaw/blob/85029e57e9094debd9366a7d5a9f7e6d5c3ef6fc/internal/gateway/guardrail.go)
- [`internal/gateway/decision.go`](https://github.com/cisco-ai-defense/defenseclaw/blob/85029e57e9094debd9366a7d5a9f7e6d5c3ef6fc/internal/gateway/decision.go)
- [`cli/defenseclaw/enforce/admission.py`](https://github.com/cisco-ai-defense/defenseclaw/blob/85029e57e9094debd9366a7d5a9f7e6d5c3ef6fc/cli/defenseclaw/enforce/admission.py)
- [`internal/audit/store.go`](https://github.com/cisco-ai-defense/defenseclaw/blob/85029e57e9094debd9366a7d5a9f7e6d5c3ef6fc/internal/audit/store.go)
- [`README.md`](https://github.com/cisco-ai-defense/defenseclaw/blob/85029e57e9094debd9366a7d5a9f7e6d5c3ef6fc/README.md)

## Operational model

A protected connector supplies prompt, completion, tool-call/result or asset context. DefenseClaw gathers local findings and configured external inspection evidence, optionally invokes the model-backed Judge, merges/finalizes the evidence through policy, and returns an enforceable verdict. In action mode native hooks can prevent the protected operation. For tool calls, Judge context carries the bounded user intent and prior same-session calls into the next decision.

## S1 — Operations

- State: A
- Function: make contextual security judgments over protected agent traffic/actions and close those judgments into the execution boundary.
- Disturbance / variety regulated: prompt injection, PII/secret exfiltration, unsafe or destructive tool activity, ambiguous tool-call chains, malicious capabilities/assets and benign cases that static matching alone cannot distinguish reliably.
- Decisive decision or feedback right: classify the current protected content/action using the model-backed Judge and contribute a semantic verdict that policy can turn into `allow`, `alert`, `confirm` or `block`.
- Decision owner: the first-party LLM Judge role in configured open-source/local Judge mode; deterministic scanners and policy constrain/merge its judgment.
- Supporting / enforcement mechanisms: local pattern scanner; rule packs; OPA/fallback policy; asset policy; Cisco inspection when configured; connector hooks; audit persistence; fail modes.
- Closure path: protected prompt/tool/result arrives → local evidence and optional Judge classification are produced → guardrail/policy finalizes the verdict → action-mode connector/hook returns an enforceable block/confirm/allow result → the protected operation proceeds or is stopped.
- Boundary reachability: `LLMJudge`, `GuardrailInspector`, inspect endpoints and native connector enforcement are shipped runtime surfaces; the operator configures the model/provider but does not need to invent the safety role or execution feedback loop.
- Why this is / is not agent-owned: without the Judge model, deterministic and external lanes remain, but the first-party runtime loses its contextual semantic classification over ambiguous prompt/tool content. The model-backed role therefore owns real S1 discretion in that supported mode.
- Evidence: [`internal/gateway/llm_judge.go`](https://github.com/cisco-ai-defense/defenseclaw/blob/85029e57e9094debd9366a7d5a9f7e6d5c3ef6fc/internal/gateway/llm_judge.go); [`internal/gateway/guardrail.go`](https://github.com/cisco-ai-defense/defenseclaw/blob/85029e57e9094debd9366a7d5a9f7e6d5c3ef6fc/internal/gateway/guardrail.go); [`internal/gateway/inspect.go`](https://github.com/cisco-ai-defense/defenseclaw/blob/85029e57e9094debd9366a7d5a9f7e6d5c3ef6fc/internal/gateway/inspect.go).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: protected-agent task reasoning is outside the boundary. Managed-enterprise mode can assign authoritative enforcement to the external Cisco AI Defense service; the positive local state is based on the shipped open-source Judge mode, not inherited cloud ownership.

## S2 — Coordination

- State: —
- Function: no material same-recursion inter-S1 coordination function is established.
- Disturbance / variety regulated: multiple detector lanes and protected connectors exist, but detector aggregation is one safety-decision pipeline rather than coordination among distinct autonomous operational S1 units.
- Decisive decision or feedback right: not established for an interference-specific relation among distinct same-recursion S1 units.
- Decision owner: not established as a first-party S2 owner.
- Supporting / enforcement mechanisms: verdict merging; per-connector policy; hook routing; asset-policy resolution; scanner-source arbitration.
- Closure path: evidence from several lanes is merged into one safety verdict; no separate inter-S1 disturbance→coordination response→changed S1 behavior loop was found.
- Why this is / is not agent-owned: routing and arbitration among detector outputs are not S2 without distinct operational units and an evidenced mutual interference.
- Evidence: [`internal/gateway/guardrail.go`](https://github.com/cisco-ai-defense/defenseclaw/blob/85029e57e9094debd9366a7d5a9f7e6d5c3ef6fc/internal/gateway/guardrail.go); [`internal/gateway/asset_policy_runtime.go`](https://github.com/cisco-ai-defense/defenseclaw/blob/85029e57e9094debd9366a7d5a9f7e6d5c3ef6fc/internal/gateway/asset_policy_runtime.go).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: a higher-level fleet/security platform may coordinate multiple agents, but that recursion is not DefenseClaw's local safety pipeline.

### Absence scope

- Surfaces inspected: scanner/Judge merge, per-connector policy, native hooks, asset runtime policy, audit/observability and connector registry.
- Plausible first-party paths checked: multi-connector operation; detector arbitration; HILT/confirmation; asset registries; hook routing.
- Why no material first-party path remains: the plurality is lanes and protected clients around one safety-control service, not distinct first-party S1 units with an actual interaction disturbance.

## S3 — Inside-and-now control

- State: A
- Function: supervise the current protected session trajectory and intervene in the next tool action using a bounded whole-session view.
- Disturbance / variety regulated: harmful multi-step tool chains, mismatch between current user intent and later tool activity, risk that emerges only across successive actions, and current security findings that should stop or escalate the next operation.
- Decisive decision or feedback right: judge the next tool call with the current session's user intent and recent tool-call sequence, then feed the resulting security action into the execution hook.
- Decision owner: the model-backed LLM Judge in the configured tool-injection/current-session mode, constrained by guardrail policy and deterministic evidence.
- Supporting / enforcement mechanisms: `toolJudgeSessionContext`; `ObserveSessionPrompt`; bounded recent-call history; `RunToolJudge`; guardrail merge/finalization; action-mode hook enforcement.
- Closure path: authenticated session prompt records current intent → successive tool calls accumulate bounded session history → next call is judged against intent + prior calls + current arguments → policy emits block/confirm/allow → native hook changes the next current operation.
- Boundary reachability: session context and Judge methods are wired into the production gateway/hook inspection path, and action-mode verdicts are consumed by shipped connector hooks.
- Why this is / is not agent-owned: the current-session supervisory distinction comes from the model's interpretation of intent plus trajectory; deterministic machinery supplies state/enforcement but cannot reproduce the same contextual judgment after the model is removed.
- Evidence: [`internal/gateway/llm_judge.go`](https://github.com/cisco-ai-defense/defenseclaw/blob/85029e57e9094debd9366a7d5a9f7e6d5c3ef6fc/internal/gateway/llm_judge.go); [`internal/gateway/inspect.go`](https://github.com/cisco-ai-defense/defenseclaw/blob/85029e57e9094debd9366a7d5a9f7e6d5c3ef6fc/internal/gateway/inspect.go).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the session context is deliberately bounded and in-memory; this is current safety control, not durable strategic adaptation.
- Whole-system current view: latest bounded user intent plus up to the configured bounded recent same-session tool events and the proposed current tool call, combined with current detector/policy evidence.
- Current-control decision scope: whether the next protected tool operation may proceed, should alert/require confirmation, or must be blocked now.

## S3* — Complementary audit

- State: —
- Function: durable audit, finding/correlation stores, scans and observability supply complementary evidence but do not establish a closed independent audit judgment returning directly into current control.
- Disturbance / variety regulated: historical findings, runtime decisions, correlations, inventory and security evidence can expose conditions not visible from one current hook decision.
- Decisive decision or feedback right: not established as a first-party complementary auditor whose finding itself enters a mandatory/authoritative current-control feedback path.
- Decision owner: operator/external security workflow for follow-up; audit code primarily records, queries, correlates and exports evidence.
- Supporting / enforcement mechanisms: audit store; finding lifecycle; correlation; observability exporters; CLI audit/findings actions; scans; alerts.
- Closure path: runtime/security evidence → durable audit/findings surfaces → operator/external workflow may change policy/configuration; the standard runtime does not show the independent audit finding itself closing the subsequent control transition.
- Why this is / is not agent-owned: an extensive evidence plane is not sufficient for S3* when the return-to-control decision remains external.
- Evidence: [`internal/audit/store.go`](https://github.com/cisco-ai-defense/defenseclaw/blob/85029e57e9094debd9366a7d5a9f7e6d5c3ef6fc/internal/audit/store.go); [`internal/audit/correlation_v8.go`](https://github.com/cisco-ai-defense/defenseclaw/blob/85029e57e9094debd9366a7d5a9f7e6d5c3ef6fc/internal/audit/correlation_v8.go); [`cli/defenseclaw/audit_actions.py`](https://github.com/cisco-ai-defense/defenseclaw/blob/85029e57e9094debd9366a7d5a9f7e6d5c3ef6fc/cli/defenseclaw/audit_actions.py).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: external SOC/managed workflows can close a complementary audit loop at a parent recursion; that ownership is not imported.

### Absence scope

- Surfaces inspected: audit store/lifecycle, finding/correlation state, audit export/actions, scan persistence, observability dashboards/exporters, alert acknowledgement and runtime enforcement.
- Plausible first-party paths checked: finding→policy mutation; correlation→automatic block; audit action→guardrail change; scanner result→runtime-disable; SOC dashboard→control.
- Why no material first-party path remains: runtime scanners directly participating in the normal gate are routine production checks; the distinct durable audit plane does not itself own a closed findings→current-control judgment path.

## S4 — Outside-and-then intelligence

- State: —
- Function: no autonomous first-party external-and-prospective adaptation loop is established.
- Disturbance / variety regulated: changing threat patterns, connector versions, policy/rule packs, registries and cloud inspection capabilities can affect future security posture.
- Decisive decision or feedback right: not established for autonomously developing and selecting a future capability adaptation from external change.
- Decision owner: operator/maintainer/configuration for rule-pack, policy, registry and connector changes.
- Supporting / enforcement mechanisms: policy reload; local-pattern overrides; registry sync; connector compatibility data; scanner updates; managed remote inspection.
- Closure path: external/operator updates policy/rules/configuration → DefenseClaw reloads/applies them → later runtime decisions change; no autonomous environment-model→adaptation-option→return loop closes.
- Why this is / is not agent-owned: hot reload and registry/policy synchronization implement chosen adaptations; they do not autonomously choose them from prospective environmental analysis.
- Evidence: [`internal/gateway/guardrail.go`](https://github.com/cisco-ai-defense/defenseclaw/blob/85029e57e9094debd9366a7d5a9f7e6d5c3ef6fc/internal/gateway/guardrail.go); [`cli/defenseclaw/enforce/policy.py`](https://github.com/cisco-ai-defense/defenseclaw/blob/85029e57e9094debd9366a7d5a9f7e6d5c3ef6fc/cli/defenseclaw/enforce/policy.py).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: model-backed runtime classification adapts the current verdict to context but does not create durable future capability by itself.

### Absence scope

- Surfaces inspected: policy/rule reload, registries, connector version contracts, scanner/benchmark corpus, LLM Judge, cloud inspection integration and audit correlations.
- Plausible first-party paths checked: automatic rule learning; benchmark→runtime policy promotion; finding→rule generation; registry refresh; model/provider change; threat-intel adaptation.
- Why no material first-party path remains: located updates are operator/config/maintainer selected or current-request classification. No autonomous prospective option-development and capability-return loop was found.

## S5 — Policy and identity

- State: —
- Function: policy engines, allow/block registries, HILT settings and fail modes enforce ordinary security policy without identity/ultimate-policy closure.
- Disturbance / variety regulated: admissible assets, severity actions, runtime enforcement posture, confirmation requirements, scanner/fail modes and connector restrictions.
- Decisive decision or feedback right: not established for an identity- or ultimate-policy-level issue at this recursion.
- Decision owner: operator/administrator/configuration supplies the policy; DefenseClaw interprets and enforces it.
- Supporting / enforcement mechanisms: OPA/Rego; policy bundles; asset policy; manual allow/block lists; HILT; fallback profiles; admission rules.
- Closure path: externally selected security policy → first-party evaluation/enforcement → later protected operation.
- Why this is / is not agent-owned: strong policy enforcement and final veto authority over ordinary actions do not themselves constitute S5 identity governance.
- Evidence: [`internal/gateway/guardrail.go`](https://github.com/cisco-ai-defense/defenseclaw/blob/85029e57e9094debd9366a7d5a9f7e6d5c3ef6fc/internal/gateway/guardrail.go); [`cli/defenseclaw/enforce/admission.py`](https://github.com/cisco-ai-defense/defenseclaw/blob/85029e57e9094debd9366a7d5a9f7e6d5c3ef6fc/cli/defenseclaw/enforce/admission.py).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: enterprise governance may place DefenseClaw inside an S5 process at a higher recursion; that parent authority is outside the assessed system.

### Absence scope

- Surfaces inspected: OPA/policy finalization, admission policy, HILT, allow/block/quarantine lists, runtime asset policy, fail modes and managed-mode authority split.
- Plausible first-party paths checked: policy changes; HILT confirmation; default-deny assets; managed/local authority choice; security posture profiles.
- Why no material first-party path remains: these mechanisms apply ordinary security constraints selected by an operator/parent. No identity/ultimate-policy dispute reaches and returns from a first-party ultimate authority.

## Recursion

The focal recursion is DefenseClaw as a security-governance organization protecting an external agent session. Safety classification is S1; session-level trajectory supervision is S3. The protected agent's coding/task operation and higher-level enterprise governance are separate systems.

## Variety and escalation

Local patterns cheaply attenuate known risk; the Judge amplifies regulatory variety for semantic and multi-step cases. Policy can escalate to confirmation/HILT or block. Durable evidence/observability supports external security workflows. No autonomous durable learning/adaptation path comparable to ClawKeeper's learned-pattern hot reload was found at this frozen revision.

## Evidence gaps

No evidence gap requires `?`. The main boundary distinction is explicit: DefenseClaw is an enforcement/evidence layer. Positive autonomy is limited to its own model-backed safety judgment and current-session supervision, not the protected agent's reasoning or enterprise policy authority.

**Vector:** A · — · A · — · — · —
