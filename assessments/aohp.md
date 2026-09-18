---
harness_id: aohp
project_name: AOHP
repository: https://github.com/aohp-os/aohp
review_ref: b8ab9e98a2bd51f7fbd01a95d3b45dca078c5884
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

# AOHP

## Review boundary

- System in focus: the AOHP OS-level agent harness as documented and distributed from `aohp-os/aohp` at pinned revision `b8ab9e98a2bd51f7fbd01a95d3b45dca078c5884`.
- Purpose and identity: make agents first-class OS actors that compose personalized services through system APIs, CLIs and GUI applications while the OS supplies background execution, memory and information-flow/security machinery.
- Relevant environment: Android applications and system services, user intents, GUI/API/CLI resources, sensitive data, external model/agent implementations and the human user.
- Standard-distribution boundary: the runnable AOHP/AOSP integration and first-party project contracts represented by this repository. Stock Android, separately assessed external agent frameworks such as OpenClaw, external model providers and generated user-defined apps are not credited as inherited organizational functions.
- First-party operating/deployment modes considered: user-defined apps backed by agents, direct agent execution over OS services, parallel background interaction, cross-app memory and security/consent enforcement.
- Recursion level: one AOHP-equipped operating-system agent organization. A generated user-defined application is a separate candidate system-in-focus.
- Reviewed revision: `b8ab9e98a2bd51f7fbd01a95d3b45dca078c5884`.
- Observation date: 2026-09-18.
- Generated/current Profile / Methodology: `0.2.2` / `0.3.1`.

## Repository architecture

AOHP is presented as a runnable AOSP fork and OS-level agent harness rather than a conventional application-layer agent library. Agents act under user intent and compose services from APIs, CLIs and GUI applications. AOHP adds parallel background interaction, OS-managed cross-app memory and fine-grained information-flow tracking with sandboxed sensitive values. Its security tests establish deterministic enforcement such as vault references, fail-closed unsupported access and user consent for sensitive transfers/payment confirmation.

The assessment separates those strong OS mechanisms from VSM ownership. Scheduling, taint tracking, sandboxing and consent gates show enforceable boundaries; they do not by themselves prove an S2/S3/S5 decision owner at the declared recursion.

## Primary evidence

- [`README.md`](https://github.com/aohp-os/aohp/blob/b8ab9e98a2bd51f7fbd01a95d3b45dca078c5884/README.md) — explicit OS-level harness boundary, first-class agent actors, user-defined applications, agent service composition, parallel background execution, cross-app memory and information-flow/consent behaviour.

## Operational model

The operational outcome is execution of personalized user intents through agent-driven composition of OS/application capabilities. Maintainer evidence explicitly assigns agents the role of first-class actors that perceive/plan/act over those capabilities, while AOHP provides the system substrate and security envelope. The benchmark example using OpenClaw is not used to inherit OpenClaw's own metasystem functions; it only demonstrates that AOHP's first-party environment can host autonomous agent execution.

## S1 — Operations

- State: `A`.
- Function: enact user-requested service outcomes through model-driven agents operating across application/system capabilities.
- Disturbance / variety regulated: heterogeneous apps/interfaces, user intent, GUI/API/CLI state, cross-app information and task-specific environmental changes during execution.
- Decisive decision or feedback right: the agent actor chooses task actions/service-composition steps under the user's intent.
- Decision owner: autonomous AI agent actor hosted by the AOHP harness.
- Supporting / enforcement mechanisms: OS APIs/CLIs/GUI access, background execution, memory, sandboxed sensitive values and information-flow tracking.
- Closure path: agent choices invoke OS/application actions, observations return through the harness and subsequent agent behaviour responds until the requested service outcome is produced.
- Why agent-owned: AOHP explicitly places agents as first-class operating actors; deterministic OS mechanisms execute/constrain rather than replace the agent's task decisions.
- Basis / confidence: explicit + structural; high.

## S2 — Coordination

- State: `—`.
- AOHP supports parallel background interaction and shared OS resources, but the pinned repository evidence does not identify distinct S1 units plus a specific inter-S1 interference/oscillation and a corresponding coordination feedback path. OS scheduling, sandboxing and information-flow enforcement are not promoted merely because they can constrain concurrent actors.
- Confidence: medium-high.

## S3 — Inside-and-now control

- State: `—`.
- The OS can enforce permissions, information-flow constraints, background execution and user-consent gates, but no distinct first-party actor is evidenced with a whole-system current view plus discretionary authority over shared operational resources, commitments or priorities.
- Sensitive-transfer/payment consent is an action-level authorization mechanism; it does not establish a whole-system S3 parent loop.
- Confidence: high.

## S3* — Complementary audit

- State: `—`.
- Security-oriented test cases and information-flow metadata validate/enforce the product's security model, but no independent runtime audit actor/path is shown challenging ordinary S1/S3 reporting and returning corrective findings into current control.
- Confidence: high.

## S4 — Outside-and-then intelligence

- State: `—`.
- Personalization and cross-app memory can improve task context, but the pinned boundary does not establish an externally and prospectively oriented intelligence loop that models future environmental change, develops adaptation options and returns them into current organizational capability.
- Confidence: high.

## S5 — Policy and identity

- State: `—`.
- User intent and consent are important authority inputs, and AOHP's security policies constrain execution. However, the cited paths concern task/sensitive-action authorization rather than an identity- or ultimate-policy-level issue reaching legitimate parent authority and returning to govern the organization as a whole.
- Static/security enforcement is therefore not promoted to S5 or `P`.
- Confidence: high.

## Recursion

Generated user-defined apps and external agent frameworks can contain their own organizational structures, but each is a separate system-in-focus requiring separate evidence.

## Variety and escalation

AOHP amplifies operational repertoire by exposing APIs, CLIs, GUIs and cross-app memory to agents while attenuating security variety through taint tracking, sandboxed values, fail-closed access and user consent. These mechanisms are recorded as support/enforcement unless a VSM-specific decision owner and closure are separately established.

## Evidence gaps

The AOHP project spans AOSP source trees fetched through first-party manifests outside this repository. This assessment deliberately does not infer additional VSM functions from unpinned sibling source repositories; positive mappings rely on the pinned repository's explicit standard-distribution description.

## Admission conclusion

Canonical vector: `A — — — — —`.
