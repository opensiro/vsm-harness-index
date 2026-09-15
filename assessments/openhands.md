---
harness_id: openhands
project_name: OpenHands
repository: https://github.com/OpenHands/OpenHands
review_ref: 28464621d879e3e9b3ceeae9d70a71d96da6212d
reviewed_at: 2026-09-15
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# OpenHands

## Review boundary
OpenHands/Agent Canvas at the pinned revision. The repository is the user-facing control center; canonical agent behavior is explicitly split into first-party `software-agent-sdk`, client and automation repositories, so functionality owned outside this repository is not silently attributed to Agent Canvas itself.

## Repository architecture
Agent Canvas runs the OpenHands coding agent out of the box, connects to multiple agent backends and provides conversations, local-stack orchestration and automation/control surfaces. The pinned architecture states that Agent Canvas selects and supervises backends, the Agent Server/SDK decides what the coding agent runs, and the automation service decides when conversations are dispatched.

## Primary evidence
- `README.md`: Agent Canvas is a developer control center; it runs OpenHands out of the box, can switch among local/remote/cloud agent backends, and exposes scheduled/webhook automations.
- `README.md`, repository-boundary table: `OpenHands/OpenHands` owns the frontend/control center/backend selection/local-stack orchestration; `software-agent-sdk` owns canonical agents/tools/conversations/workspaces/events; `OpenHands/automation` owns scheduling, webhooks, run history and dispatch.
- `src/api/agent-server-adapter.ts`: adapts operator/conversation settings, backend identity, model/tool configuration, child-conversation plumbing and Agent Server capabilities into the Canvas surface. These are runtime/control integrations rather than an autonomous metasystem regulator.

## Operational model
A running coding agent/conversation is S1. Canvas selects, configures and observes those operational loops, while automation dispatch controls when work starts. The decisive control plane remains application/operator owned.

## S1 — Operations
`A`: the standard product runs an autonomous OpenHands coding agent that executes workspace/tool actions through the first-party Agent Server. Confidence: high.

## S2 — Coordination
`—`: multiple backends, conversations, child-conversation plumbing and automation dispatch are deployment/routing mechanisms, not an autonomous anti-oscillation/shared-resource coordination function among peer S1 units.

## S3 — Inside-and-now control
`—`: the control center exposes operator/runtime controls and settings; no reviewed path gives an autonomous superior agent whole-system resource, priority and commitment authority.

## S3* — Complementary audit
`—`: confirmation/security/review surfaces constrain or expose operational work, but no distinct autonomous complementary-audit agent is established at this repository boundary.

## S4 — Outside-and-then intelligence
`—`: schedules, webhooks and external integrations trigger current operations; they do not form a prospective environment-intelligence loop shaping future organizational adaptation.

## S5 — Policy and identity
`—`: backend/model/tool/security choices and ultimate task authority remain operator/application configured.

## Recursion, variety, escalation
Multiple Agent Servers/backends and child conversations are deployment/composition topology, not evidence of recursively viable systems.