---
harness_id: agentharness-ruby
project_name: AgentHarness (Ruby)
repository: https://github.com/viamin/agent-harness
review_ref: cda07ca157db1e51b6e7687820a96601432f8fb1
reviewed_at: 2026-10-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# AgentHarness (Ruby)

## Review boundary

- System in focus: the shipped Ruby gem's provider/transport/orchestration support layer, not the independently installed coding-agent processes it invokes.
- Purpose and identity: normalize coding-agent CLI/model transport, installation/runtime configuration, failure handling and usage reporting.
- Relevant environment: Ruby consumers, Claude/Codex/Cursor/Gemini and other external agent CLIs, model endpoints, containers, quotas and user credentials.
- Standard-distribution boundary: lib/, bin/ and documented gem API; deterministic conductor/provider management, execution adapters, conversation storage and extension/subagent translation.
- Credited operating / distribution surfaces: lib/agent_harness.rb, providers/base.rb, orchestration/, transport/executor, configuration, extensions/skills, dependency updater and provider adapters.
- Adjacent first-party surfaces excluded from ownership: spec/, release/audit/contributor scripts, vendored installation artifacts and package-development governance. External CLIs, their model/tool loops and provider internals do not donate ownership.
- First-party operating / deployment modes considered: orchestrated and direct CLI requests; direct chat/streaming; executor/container overrides; configured extensions, skills/MCP/subagents; callbacks and dependency-version selection.
- Recursion level: one Ruby support-library installation. External coding agents are separate operational systems.
- Reviewed revision: `viamin/agent-harness@cda07ca157db1e51b6e7687820a96601432f8fb1`, frozen intake #2412 / controller #2413.
- Observation date: 2026-10-30.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[README.md](https://github.com/viamin/agent-harness/blob/cda07ca157db1e51b6e7687820a96601432f8fb1/README.md) documents a unified interface and configured fallback. [lib/agent_harness/orchestration/conductor.rb](https://github.com/viamin/agent-harness/blob/cda07ca157db1e51b6e7687820a96601432f8fb1/lib/agent_harness/orchestration/conductor.rb) retries and changes providers according to error classes; [lib/agent_harness/orchestration/provider_manager.rb](https://github.com/viamin/agent-harness/blob/cda07ca157db1e51b6e7687820a96601432f8fb1/lib/agent_harness/orchestration/provider_manager.rb) follows configured fallback chains and health/rate-limit state. [lib/agent_harness/providers/base.rb](https://github.com/viamin/agent-harness/blob/cda07ca157db1e51b6e7687820a96601432f8fb1/lib/agent_harness/providers/base.rb) prepares native CLI execution and parses responses; its send_chat_message performs one transport call, adds usage metadata and returns. [lib/agent_harness/conversation.rb](https://github.com/viamin/agent-harness/blob/cda07ca157db1e51b6e7687820a96601432f8fb1/lib/agent_harness/conversation.rb) stores caller-provided messages. Skills/extensions and subagent definitions translate into provider instructions/tool definitions; they do not instantiate an independently deciding first-party work cell. DependencyUpdater resolves caller-registered releases with deterministic cooldown/version selection.

## Operational model

Recommended canonical disposition: **excluded-no-agentic-vsm**. This is a substantive executable integration layer, but no first-party autonomous operational decision/action loop was established. Imported CLI autonomy is outside the repository boundary; a model response or parsed tool-call schema does not supply the missing returned tool-action loop. For the proposed artifact all six states are bounded absence findings; exclusion is finalized only by a separate transaction.

## S1 — Operations

- State: —
- Function: No first-party autonomous operational cell is supplied; native coding work belongs to invoked external CLIs.
- Disturbance / variety regulated: provider/request errors, capability configuration and execution signals; tested for the specific organizational function above.
- Decisive decision or feedback right: no qualifying first-party autonomous or function-specific constructor/parent closure established.
- Decision owner: consumer/developer configuration and deterministic library code; native agent choices remain outside this boundary.
- Supporting / enforcement mechanisms: Provider wrappers, direct chat and extension/tool translation are the plausible candidates.
- Closure path: Conductor sends a prompt to a selected provider; Base invokes an external process or returns one transport response. Chat tool-call metadata is returned without a shipped iterative tool-execution agent.
- Why this is / is not agent-owned: removing an external coding agent leaves transport/orchestration machinery; the library does not replace that agent's operational decisions.
- Evidence: [lib/agent_harness/providers/base.rb](https://github.com/viamin/agent-harness/blob/cda07ca157db1e51b6e7687820a96601432f8fb1/lib/agent_harness/providers/base.rb); [lib/agent_harness/orchestration/conductor.rb](https://github.com/viamin/agent-harness/blob/cda07ca157db1e51b6e7687820a96601432f8fb1/lib/agent_harness/orchestration/conductor.rb)
- Basis: structural
- Confidence: high
- Caveats: bounded distribution-level finding, not a claim that a downstream consumer cannot build an agent organization.

### Absence scope

- Surfaces inspected: lib/agent_harness/providers/base.rb, lib/agent_harness/orchestration/conductor.rb, README documented modes and the lib/spec tree.
- Plausible first-party paths checked: Provider wrappers, direct chat and extension/tool translation are the plausible candidates.
- Why no material first-party path remains: Conductor sends a prompt to a selected provider; Base invokes an external process or returns one transport response. Chat tool-call metadata is returned without a shipped iterative tool-execution agent.

## S2 — Coordination

- State: —
- Function: Provider switching does not establish coordination among distinct first-party S1 cells.
- Disturbance / variety regulated: provider/request errors, capability configuration and execution signals; tested for the specific organizational function above.
- Decisive decision or feedback right: no qualifying first-party autonomous or function-specific constructor/parent closure established.
- Decision owner: consumer/developer configuration and deterministic library code; native agent choices remain outside this boundary.
- Supporting / enforcement mechanisms: Fallback, rate limits, executor isolation and subagent translation were tested as possible coordination.
- Closure path: These protect request/provider state and translate external-agent configuration; no first-party interacting work cells with a specific regulated inter-S1 conflict are instantiated.
- Why this is / is not agent-owned: removing an external coding agent leaves transport/orchestration machinery; the library does not replace that agent's operational decisions.
- Evidence: [lib/agent_harness/orchestration/provider_manager.rb](https://github.com/viamin/agent-harness/blob/cda07ca157db1e51b6e7687820a96601432f8fb1/lib/agent_harness/orchestration/provider_manager.rb); [lib/agent_harness/sub_agent_translator.rb](https://github.com/viamin/agent-harness/blob/cda07ca157db1e51b6e7687820a96601432f8fb1/lib/agent_harness/sub_agent_translator.rb)
- Basis: structural
- Confidence: high
- Caveats: bounded distribution-level finding, not a claim that a downstream consumer cannot build an agent organization.

### Absence scope

- Surfaces inspected: lib/agent_harness/orchestration/provider_manager.rb, lib/agent_harness/sub_agent_translator.rb, README documented modes and the lib/spec tree.
- Plausible first-party paths checked: Fallback, rate limits, executor isolation and subagent translation were tested as possible coordination.
- Why no material first-party path remains: These protect request/provider state and translate external-agent configuration; no first-party interacting work cells with a specific regulated inter-S1 conflict are instantiated.

## S3 — Inside-and-now control

- State: —
- Function: Deterministic request-level availability management is supplied without a first-party agent-owned or S3-specific constructor current-control loop.
- Disturbance / variety regulated: provider/request errors, capability configuration and execution signals; tested for the specific organizational function above.
- Decisive decision or feedback right: no qualifying first-party autonomous or function-specific constructor/parent closure established.
- Decision owner: consumer/developer configuration and deterministic library code; native agent choices remain outside this boundary.
- Supporting / enforcement mechanisms: Conductor status/metrics, circuit breakers, fallback and callbacks expose health/usage.
- Closure path: Configured priorities and fallback chains determine selection. Callbacks report switches; the package does not compose a discretionary whole-organization regulator or close a parent intervention loop.
- Why this is / is not agent-owned: removing an external coding agent leaves transport/orchestration machinery; the library does not replace that agent's operational decisions.
- Evidence: [lib/agent_harness/orchestration/conductor.rb](https://github.com/viamin/agent-harness/blob/cda07ca157db1e51b6e7687820a96601432f8fb1/lib/agent_harness/orchestration/conductor.rb); [lib/agent_harness/orchestration/provider_manager.rb](https://github.com/viamin/agent-harness/blob/cda07ca157db1e51b6e7687820a96601432f8fb1/lib/agent_harness/orchestration/provider_manager.rb); [lib/agent_harness/configuration.rb](https://github.com/viamin/agent-harness/blob/cda07ca157db1e51b6e7687820a96601432f8fb1/lib/agent_harness/configuration.rb)
- Basis: structural
- Confidence: high
- Caveats: bounded distribution-level finding, not a claim that a downstream consumer cannot build an agent organization.

### Absence scope

- Surfaces inspected: lib/agent_harness/orchestration/conductor.rb, lib/agent_harness/orchestration/provider_manager.rb, lib/agent_harness/configuration.rb, README documented modes and the lib/spec tree.
- Plausible first-party paths checked: Conductor status/metrics, circuit breakers, fallback and callbacks expose health/usage.
- Why no material first-party path remains: Configured priorities and fallback chains determine selection. Callbacks report switches; the package does not compose a discretionary whole-organization regulator or close a parent intervention loop.

## S3* — Complementary audit

- State: —
- Function: No complementary agentic audit arrangement is supplied.
- Disturbance / variety regulated: provider/request errors, capability configuration and execution signals; tested for the specific organizational function above.
- Decisive decision or feedback right: no qualifying first-party autonomous or function-specific constructor/parent closure established.
- Decision owner: consumer/developer configuration and deterministic library code; native agent choices remain outside this boundary.
- Supporting / enforcement mechanisms: Health probes, token/usage accounting, provider parsing and repository audit disposition were inspected.
- Closure path: Availability/usage checks are routine operational reporting; specs and AUDIT_DISPOSITION.md belong to package development, not an independent audit actor with returned current control.
- Why this is / is not agent-owned: removing an external coding agent leaves transport/orchestration machinery; the library does not replace that agent's operational decisions.
- Evidence: [lib/agent_harness/provider_health_check.rb](https://github.com/viamin/agent-harness/blob/cda07ca157db1e51b6e7687820a96601432f8fb1/lib/agent_harness/provider_health_check.rb); [lib/agent_harness/orchestration/metrics.rb](https://github.com/viamin/agent-harness/blob/cda07ca157db1e51b6e7687820a96601432f8fb1/lib/agent_harness/orchestration/metrics.rb); [AUDIT_DISPOSITION.md](https://github.com/viamin/agent-harness/blob/cda07ca157db1e51b6e7687820a96601432f8fb1/AUDIT_DISPOSITION.md)
- Basis: structural
- Confidence: high
- Caveats: bounded distribution-level finding, not a claim that a downstream consumer cannot build an agent organization.

### Absence scope

- Surfaces inspected: lib/agent_harness/provider_health_check.rb, lib/agent_harness/orchestration/metrics.rb, AUDIT_DISPOSITION.md, README documented modes and the lib/spec tree.
- Plausible first-party paths checked: Health probes, token/usage accounting, provider parsing and repository audit disposition were inspected.
- Why no material first-party path remains: Availability/usage checks are routine operational reporting; specs and AUDIT_DISPOSITION.md belong to package development, not an independent audit actor with returned current control.

## S4 — Outside-and-then intelligence

- State: —
- Function: No external-and-prospective agent adaptation loop is supplied.
- Disturbance / variety regulated: provider/request errors, capability configuration and execution signals; tested for the specific organizational function above.
- Decisive decision or feedback right: no qualifying first-party autonomous or function-specific constructor/parent closure established.
- Decision owner: consumer/developer configuration and deterministic library code; native agent choices remain outside this boundary.
- Supporting / enforcement mechanisms: Runtime provider discovery, dependency release registry/cooldown, skills/extensions and fallback were considered.
- Closure path: The dependency updater selects eligible versions from caller-registered release metadata using deterministic age/version rules; it does not model future environments, develop options and negotiate present capability. No supported parent adaptation return is wired.
- Why this is / is not agent-owned: removing an external coding agent leaves transport/orchestration machinery; the library does not replace that agent's operational decisions.
- Evidence: [lib/agent_harness/dependency_updater.rb](https://github.com/viamin/agent-harness/blob/cda07ca157db1e51b6e7687820a96601432f8fb1/lib/agent_harness/dependency_updater.rb); [lib/agent_harness/release_registry.rb](https://github.com/viamin/agent-harness/blob/cda07ca157db1e51b6e7687820a96601432f8fb1/lib/agent_harness/release_registry.rb); [lib/agent_harness/extensions.rb](https://github.com/viamin/agent-harness/blob/cda07ca157db1e51b6e7687820a96601432f8fb1/lib/agent_harness/extensions.rb)
- Basis: structural
- Confidence: high
- Caveats: bounded distribution-level finding, not a claim that a downstream consumer cannot build an agent organization.

### Absence scope

- Surfaces inspected: lib/agent_harness/dependency_updater.rb, lib/agent_harness/release_registry.rb, lib/agent_harness/extensions.rb, README documented modes and the lib/spec tree.
- Plausible first-party paths checked: Runtime provider discovery, dependency release registry/cooldown, skills/extensions and fallback were considered.
- Why no material first-party path remains: The dependency updater selects eligible versions from caller-registered release metadata using deterministic age/version rules; it does not model future environments, develop options and negotiate present capability. No supported parent adaptation return is wired.

## S5 — Policy and identity

- State: —
- Function: No runtime identity/ultimate-policy authority loop is supplied.
- Disturbance / variety regulated: provider/request errors, capability configuration and execution signals; tested for the specific organizational function above.
- Decisive decision or feedback right: no qualifying first-party autonomous or function-specific constructor/parent closure established.
- Decision owner: consumer/developer configuration and deterministic library code; native agent choices remain outside this boundary.
- Supporting / enforcement mechanisms: Configuration DSL, tool/skill permissions, extension instructions, subagent translations and OSS maintainer policy were checked.
- Closure path: These are authored inputs, validation and transport rules; no identity-level matter reaches a legitimate runtime parent and returns as an authoritative operational decision.
- Why this is / is not agent-owned: removing an external coding agent leaves transport/orchestration machinery; the library does not replace that agent's operational decisions.
- Evidence: [lib/agent_harness/configuration.rb](https://github.com/viamin/agent-harness/blob/cda07ca157db1e51b6e7687820a96601432f8fb1/lib/agent_harness/configuration.rb); [lib/agent_harness/extensions.rb](https://github.com/viamin/agent-harness/blob/cda07ca157db1e51b6e7687820a96601432f8fb1/lib/agent_harness/extensions.rb); [lib/agent_harness/sub_agent_translator.rb](https://github.com/viamin/agent-harness/blob/cda07ca157db1e51b6e7687820a96601432f8fb1/lib/agent_harness/sub_agent_translator.rb)
- Basis: structural
- Confidence: high
- Caveats: bounded distribution-level finding, not a claim that a downstream consumer cannot build an agent organization.

### Absence scope

- Surfaces inspected: lib/agent_harness/configuration.rb, lib/agent_harness/extensions.rb, lib/agent_harness/sub_agent_translator.rb, README documented modes and the lib/spec tree.
- Plausible first-party paths checked: Configuration DSL, tool/skill permissions, extension instructions, subagent translations and OSS maintainer policy were checked.
- Why no material first-party path remains: These are authored inputs, validation and transport rules; no identity-level matter reaches a legitimate runtime parent and returns as an authoritative operational decision.

## Distributed OSS parent arrangement

Package maintainer/contributor authority is outside the assessed deployed library. Configuration callbacks do not establish project-level or local parent S3/S4/S5 closure.

## Self-hosted and non-human modes

Direct and orchestrated self-hosted use retain the external CLI/model boundary. Custom provider registration or arbitrary extension callbacks are not themselves a shipped organizational actor.

## Recursion

Multiple providers and translated subagents are configuration/transport topology; no recursively viable first-party operational system is established.

## Variety and escalation

Typed errors, bounded retries, authentication failure return, quota/circuit state and provider-switch events expose and attenuate transport variety. They do not alone establish algedonic signalling or agent-owned regulation.

## Evidence gaps

Exact-ref static source and specs reviewed; no Ruby executable is installed on the inspection host, so native Ruby tests were not run. No external coding CLI, model/provider or paid task was executed. This operational limitation does not leave a specific unexamined first-party agent loop: the documented direct chat and CLI paths were traced to return boundaries.
