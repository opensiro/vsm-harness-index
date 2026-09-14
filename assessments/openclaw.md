---
harness_id: openclaw
project_name: OpenClaw
repository: https://github.com/openclaw/openclaw
review_ref: 697bce4c40a5e80993adc62d26ce660943e0865e
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: —
---

# OpenClaw

## Review boundary
OpenClaw at the pinned revision as the trusted local gateway/control plane plus configured assistant harness plugins. The OpenClaw Foundation and model providers are outside the runtime system-in-focus.

## Repository architecture
One Gateway manages sessions, tools, events, channels and device nodes for a personal or team deployment. Agent harnesses/models are plugins. The architecture explicitly separates trusted gateway, untrusted execution and deterministic policy; pairing/sandbox/security remain operator-configured.

## Primary evidence
- `README.md`: gateway/control-plane architecture, swappable harness plugins, team deployment, channels/tools/skills/nodes, deterministic policy and security controls.

## Operational model
A configured assistant/harness performs S1 work. Gateway routing, session isolation and deterministic policy are supporting control mechanisms rather than autonomous agent-owned metasystem functions.

## S1 — Operations
`A`: a standard configured assistant autonomously uses model/harness tools toward user work. Confidence: high.

## S2 — Coordination
`—`: multiple channels/sessions/team deployment do not establish an agent-owned anti-oscillation relation among autonomous S1 units.

## S3 — Inside-and-now control
`?`: the Gateway is a deterministic/human-operated control plane; no autonomous S3 actor is verified.

## S3* — Complementary audit
`?`: telemetry/logging/security surfaces do not establish sufficiently independent autonomous audit.

## S4 — Outside-and-then intelligence
`?`: external channels/tools do not establish prospective adaptation.

## S5 — Policy and identity
`—`: security/policy is explicitly deterministic/operator-configured; no agent owns ultimate policy or identity closure.

## Recursion, variety, escalation
Team deployments and device nodes expand reach but are not automatically recursive viable systems.