---
harness_id: openclaw
project_name: OpenClaw
repository: https://github.com/openclaw/openclaw
review_ref: 697bce4c40a5e80993adc62d26ce660943e0865e
reviewed_at: 2026-09-15
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# OpenClaw

## Review boundary
OpenClaw at the pinned revision as the trusted local gateway/control plane plus configured assistant harness plugins. The OpenClaw Foundation and model providers are outside the runtime system-in-focus.

## Repository architecture
One Gateway manages sessions, tools, events, channels and device nodes for a personal or team deployment. Agent harnesses/models are plugins. The architecture explicitly separates trusted gateway, untrusted execution and deterministic policy; pairing/sandbox/security remain operator-configured. Agent-visible session tools additionally expose cross-session messaging, status/history, subagent lifecycle and bounded responsibility/session management.

## Primary evidence
- `README.md`: gateway/control-plane architecture, swappable harness plugins, team deployment, channels/tools/skills/nodes, deterministic policy and security controls.
- `docs/concepts/session-tool.md`: agents can inspect session state/history, message authorized parent/child/sibling sessions, spawn/cancel subagents, patch visible sessions, assign responsibility and manage session lifecycle; these are first-party constructor paths rather than a default closed coordination/control policy.
- `docs/gateway/heartbeat.md` and `docs/concepts/dreaming.md`: periodic turns and memory consolidation advance current goals/context, but neither establishes external-and-prospective S4 intelligence.

## Operational model
A configured assistant/harness performs S1 work. Cross-session messaging plus lifecycle/status controls expose first-party building blocks for coordination and current-operation regulation, but the standard distribution does not close those tools into a general agent-owned S2/S3 policy. Gateway enforcement and ultimate policy remain deterministic/operator-owned.

## S1 — Operations
`A`: a standard configured assistant autonomously uses model/harness tools toward user work. Confidence: high.

## S2 — Coordination
`C`: authorized sibling/parent/child messaging and session ownership/lifecycle tools provide a concrete constructor path for operational agents to exchange coordination information and regulate responsibility, but no standard agent-owned anti-oscillation policy is closed out of the box. Confidence: high.

## S3 — Inside-and-now control
`C`: an agent can inspect current sessions/status/history and exercise lifecycle, ownership, spawn/cancel and model-selection controls over visible sessions. Those are material current-control decision rights from which S3 can be composed, but the stock harness does not supply a whole-system regulator that autonomously bargains resources/priorities across operations. Confidence: medium-high.

## S3* — Complementary audit
`—`: execution-audit facts, telemetry, security controls and transcript inspection are observability/enforcement surfaces; no distinct sufficiently independent autonomous audit path is supplied in the reviewed standard distribution.

## S4 — Outside-and-then intelligence
`—`: heartbeats, cron, external triggers and dreaming react to events or consolidate memory; they do not model external future change, develop adaptation options and couple those options back to present control.

## S5 — Policy and identity
`—`: security, visibility, pairing and tool policy are explicitly deterministic/operator-configured; no agent owns legitimate ultimate policy or identity closure.

## Recursion, variety, escalation
Team deployments, subagents and device nodes expand reach but are not automatically recursive viable systems.