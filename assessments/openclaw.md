---
harness_id: openclaw
project_name: OpenClaw
repository: https://github.com/openclaw/openclaw
review_ref: 387da5edaa9d6c6cfcfc15e167fe2e46d8647d86
reviewed_at: 2026-09-16
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
last_checked_ref: 387da5edaa9d6c6cfcfc15e167fe2e46d8647d86
last_checked_at: 2026-09-16
assessment_changed_at: 2026-09-16
last_reassessment_round: R2
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C(P)
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# OpenClaw

## Review boundary
OpenClaw at the pinned revision as the trusted local gateway/control plane plus configured assistant harness plugins and the first-party system-agent setup/control surface. The OpenClaw Foundation and model providers are outside the runtime system-in-focus.

## Repository architecture
One Gateway manages sessions, tools, events, channels and device nodes for a personal or team deployment. Agent harnesses/models are plugins. The architecture explicitly separates trusted gateway, untrusted execution and deterministic policy. Agent-visible session tools expose cross-session messaging, status/history, subagent lifecycle and bounded responsibility/session management. The current system-agent additionally exposes host-scoped whole-deployment status/configuration surfaces and persistent setup/control mutations whose execution is bound to exact operator approval.

## Primary evidence
- `docs/concepts/session-tool.md`: agents can inspect session state/history, message authorized parent/child/sibling sessions, spawn/cancel subagents, patch visible sessions, assign responsibility and manage session lifecycle; these remain first-party constructor paths rather than a default closed autonomous coordination/control policy.
- `src/agents/tools/system-agent-tool.ts` at `387da5edaa9d6c6cfcfc15e167fe2e46d8647d86`: the host-owned system-agent surface can inspect deployment status/models/agents/channels/config/gateway/audit state and propose persistent mutations including model/config, agent/team, gateway and plugin changes. Persistent operations require an exact staged operation hash, host-observed explicit user approval and a matching approved retry; the host applies the accepted mutation, validates/audits it and returns failures for a fresh proposal.
- commit `387da5edaa9d6c6cfcfc15e167fe2e46d8647d86`: approved configuration writes now use the canonical config writer and return validation failures for corrective proposals, preserving explicit approval and write-authority checks.
- `docs/gateway/heartbeat.md` and `docs/concepts/dreaming.md`: periodic turns and memory consolidation advance current goals/context, but neither establishes external-and-prospective S4 intelligence.

## Operational model
A configured assistant/harness performs S1 work. Cross-session messaging plus lifecycle/status controls expose constructor paths for coordination and current-operation regulation. Separately, the system-agent exposes a parent-governed current-control mode: the system can surface whole-deployment current state, formulate a concrete persistent control mutation, pause on the exact proposal, receive explicit operator approval through the host, apply that exact mutation through the canonical writer/control path, and continue under the changed configuration.

## S1 — Operations
`A`: a standard configured assistant autonomously uses model/harness tools toward user work. Confidence: high.

## S2 — Coordination
`C`: authorized sibling/parent/child messaging and session ownership/lifecycle tools provide a concrete constructor path for operational agents to exchange coordination information and regulate responsibility, but no standard agent-owned anti-oscillation policy is closed out of the box. Confidence: high.

## S3 — Inside-and-now control
`C(P)`: the existing agent-visible status/history, lifecycle, ownership, spawn/cancel and model-selection surfaces remain a material S3 constructor path without a stock autonomous whole-system regulator. In addition, the first-party system-agent closes a distinct parent-governed S3 mode: it exposes current whole-deployment state, proposes concrete model/config/team/gateway/plugin control changes, binds the decisive mutation to exact operator approval, and returns the approved change through canonical writers/control operations into subsequent runtime behavior. The parent mode is therefore independently complete while autonomous S3 ownership still requires composition. Confidence: high.

## S3* — Complementary audit
`—`: audit facts, telemetry, security controls and transcript inspection are observability/enforcement surfaces; no distinct sufficiently independent autonomous complementary-audit path is supplied in the reviewed standard distribution.

## S4 — Outside-and-then intelligence
`—`: heartbeats, cron, external triggers, dreaming and system-agent repair/setup concern current operation or maintenance; they do not establish a distinct external-and-prospective adaptation function whose options feed back into present capability.

## S5 — Policy and identity
`—`: operator approval of configuration/setup mutations is not by itself identity or ultimate-policy closure. Security, visibility, pairing and tool policy remain operator/runtime configured, but the reviewed evidence does not reconstruct an S5-specific identity/policy issue reaching legitimate ultimate authority and returning as an authoritative identity/policy decision. The S3 parent mode must not be promoted to S5 merely because the operator has final say over a current-control mutation.

## Recursion, variety, escalation
Team deployments, subagents and device nodes expand reach but are not automatically recursive viable systems. The system-agent approval path demonstrates explicit parent ownership for selected current-control decisions; it does not establish parent ownership for unrelated VSM functions.