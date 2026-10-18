---
harness_id: opensre
project_name: OpenSRE
repository: https://github.com/Tracer-Cloud/opensre
review_ref: dac688001e0e92b0356807176bb2162e3cd69843
reviewed_at: 2026-09-18
generated_profile_version: 0.2.2
generated_assessment_procedure_version: 0.3.1
profile_version: 0.2.2
assessment_procedure_version: 0.3.1
assessment_changed_at: 2026-09-18
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# OpenSRE

## Review boundary

- System in focus: OpenSRE's first-party production SRE agent runtime / `AgentSession` incident-response loop at pinned revision `dac688001e0e92b0356807176bb2162e3cd69843`.
- Purpose and identity: answer production questions and investigate incidents by collecting operational evidence, reasoning across connected systems, producing evidence-linked diagnoses and optionally taking/remediating actions.
- Relevant environment: production infrastructure, logs/metrics/traces/deploys, runbooks, incident-management/communication systems, model providers, operators and integration APIs.
- Standard-distribution boundary: first-party runtime, prompt/skill contracts, session state, tool/integration layer and approval/required-input surfaces. External model providers/infrastructure systems remain environment/dependencies. The repository's e2e training/evaluation environment is not treated as part of the production operational organization.
- First-party operating/deployment modes considered: interactive shell, headless CLI, in-process Python `AgentSession`, connected tools/integrations and approval-gated write/remediation actions.
- Recursion level: one OpenSRE incident-response agent organization. Connected coding agents/fleet members or external services are not automatically S1 units at this boundary.
- Reviewed revision: `dac688001e0e92b0356807176bb2162e3cd69843`.
- Observation date: 2026-09-18.
- Generated/current Profile / Methodology: `0.2.2` / `0.3.1`.

## Repository architecture

OpenSRE's production loop fetches correlated logs, metrics, traces and recent deployments, optionally masks sensitive identifiers, reasons through hypotheses in a tool-calling loop, produces an evidence-linked answer, suggests or optionally executes remediation and can post a summary to operational communication systems. Sessions are persistent/resumable and can be driven interactively, headlessly or from Python.

Write/external-side-effect tools can require explicit authority. In headless mode such tools are denied unless allowlisted for that invocation (or explicitly bypassed); when the agent needs a user decision, it can return structured `needs_input` and resume the same session after the reply. These are real safety/authority paths, but the assessment does not promote them to S3/S5 without evidence that the underlying question is whole-system current control or identity/ultimate policy.

## Primary evidence

- [`README.md`](https://github.com/Tracer-Cloud/opensre/blob/dac688001e0e92b0356807176bb2162e3cd69843/README.md) — production incident-response loop, AgentSession boundary, evidence gathering/reasoning, optional remediation and integrations.
- [`docs/headless-cli.mdx`](https://github.com/Tracer-Cloud/opensre/blob/dac688001e0e92b0356807176bb2162e3cd69843/docs/headless-cli.mdx) — per-invocation tool authorization, denied write/side-effect tools, resumable structured human input and returned-session closure.
- [`AGENTS.md`](https://github.com/Tracer-Cloud/opensre/blob/dac688001e0e92b0356807176bb2162e3cd69843/AGENTS.md) — human-owned system-prompt/skill boundary; used as governance evidence but not promoted to runtime S5 by itself.

## Operational model

The SRE agent is the primary S1 unit: it autonomously chooses which operational evidence to gather, which hypotheses to test and which read actions/tools to invoke in order to diagnose the incident/question. Optional write/remediation actions remain constrained by explicit authorization. Connected tools and 60+ integrations expand the environment/repertoire; they are not themselves additional S1 units or metasystem functions.

## S1 — Operations

- State: `A`.
- Function: autonomously investigate production questions/incidents and produce evidence-backed diagnoses, recommendations and permitted operational actions.
- Disturbance / variety regulated: distributed operational failures, noisy/correlated telemetry, recent deployments/configuration, runbook constraints and hypothesis uncertainty.
- Decisive decision or feedback right: the agent chooses evidence-gathering/tool actions, hypotheses and diagnostic reasoning within its authorized tool boundary.
- Decision owner: model-driven OpenSRE agent actor.
- Supporting / enforcement mechanisms: AgentSession, integrations, session persistence, masking, tool registry and approval enforcement.
- Closure path: tool observations/evidence feed later agent reasoning and the final answer/remediation path changes or informs the incident environment.
- Basis / confidence: explicit + structural; high.

## S2 — Coordination

- State: `—`.
- Evidence aggregation across many integrations and local agent-fleet monitoring do not establish two or more operational S1 units with a concrete mutual interference/oscillation and a first-party coordination feedback loop. Tool routing and broad connectivity are not S2.
- Confidence: high.

## S3 — Inside-and-now control

- State: `—`.
- Optional remediation, session control and approval-gated write tools can alter production state, but the pinned distribution does not establish a distinct first-party regulator with a current whole-organization view and discretionary authority over shared resources, commitments or priorities across multiple S1 units.
- Human approval of a particular side-effecting tool is action-level authority, not by itself a parent-governed S3 loop. `needs_input` likewise can resolve ordinary task ambiguity rather than whole-system current control.
- Confidence: high.

## S3* — Complementary audit

- State: `—`.
- OpenSRE ships e2e incident tests/training/evaluation infrastructure, but that is an evaluation/growth environment rather than a runtime complementary audit channel inside the production AgentSession organization. Evidence-linked diagnosis and normal tool verification are part of S1 operation, not a separate independent audit loop.
- Confidence: high.

## S4 — Outside-and-then intelligence

- State: `—`.
- The agent responds to current production evidence and can consult runbooks/recent changes, but the pinned production boundary does not establish a persistent external-and-prospective intelligence function that models future environmental change, develops adaptation options and returns them into present organizational capability.
- Confidence: high.

## S5 — Policy and identity

- State: `—`.
- The system prompt/skills are explicitly human-owned and write-tool permissions can require operator authorization, but these facts are constraints/governance mechanisms. The reviewed runtime does not establish an identity/ultimate-policy issue → legitimate parent decision → returned organizational-policy closure at the declared recursion.
- Generic human ownership of prompts or approval of operational writes is therefore not `P`.
- Confidence: high.

## Recursion

External infrastructure/services and locally monitored coding agents remain environment/adjacent actors unless separately organized and assessed as viable child systems. OpenSRE's separate training/evaluation environment is not collapsed into the production runtime.

## Variety and escalation

Integrations amplify evidence/action variety while evidence correlation and masking attenuate it. Approval-gated writes and structured `needs_input` provide concrete operational escalation to a human, but the escalated matter must first satisfy a VSM S3/S4/S5 function before parent notation can apply; the pinned evidence does not establish that broader function.

## Evidence gaps

No positive metasystem state is inferred from tool count, incident-management vocabulary, remediation capability, human approvals or development-time governance rules without the function-specific whole-system/independence/prospective/identity closure required by the Profile.

## Admission conclusion

Canonical vector: `A — — — — —`.
