---
harness_id: cmcp
project_name: cMCP
repository: https://github.com/agentrust-io/cmcp
review_ref: f8743e013786b094caaa70c336519834e73c74d5
reviewed_at: 2026-09-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-24
status: excluded-no-agentic-vsm
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# cMCP

## Review boundary

- System in focus: the first-party cMCP Confidential MCP Runtime at pinned revision `f8743e013786b094caaa70c336519834e73c74d5`, including the MCP gateway/proxy, Cedar policy evaluation, catalog/provenance checks, TEE attestation, session/audit state, response inspection, kill switch, TRACE Claim production and offline verification surfaces.
- Purpose and identity: mediate an external agent's MCP tool traffic through a confidential, attestable policy-enforcement boundary that can allow, deny, redact, rate-limit, audit and prove what happened without trusting the governed process or operator.
- Relevant environment: the governed external agent/MCP client and its model/reasoning loop, upstream MCP servers/tools, policy authors/operators, Agent Manifest issuers, hardware/TEE providers, trust anchors, auditors/verifiers and downstream services.
- Standard-distribution boundary: repository-owned `cmcp_runtime` gateway/proxy/policy/session/audit/inspection/attestation code and `cmcp_verify` verification library are inside. The model-driven agent that chooses tasks/tool calls and upstream tool-server application logic are outside.
- Credited operating / distribution surfaces: `README.md`; `STATUS.md`; `src/cmcp_runtime/runtime_gateway.py`; `src/cmcp_runtime/mcp/proxy.py`; `src/cmcp_runtime/policy/evaluator.py`; `src/cmcp_runtime/kill_switch.py`; `src/cmcp_runtime/agent_manifest.py`; shipped session/audit/inspection/TEE paths.
- Adjacent first-party surfaces excluded from ownership: repository tests/CI, governance documents, fuzzing/benchmarks and roadmap capabilities not marked shipped in `STATUS.md`. Future semantic-intent alignment and other explicitly unimplemented features are not credited.
- First-party operating / deployment modes considered: enforcing/advisory/silent gateway modes, hardware-attested and explicit software-development mode, HTTP/SSE and shipped stdio upstream transport, optional Agent Manifest binding, signed policy hot reload, kill-switch enforcement and offline claim verification.
- Recursion level: the cMCP governance gateway itself as admitted to organizational/control batch #407. The external governed agent can be part of a wider composed agent organization, but its autonomous reasoning/action ownership is not imported into this repository-relative first-party boundary.
- Reviewed revision: `f8743e013786b094caaa70c336519834e73c74d5`.
- Observation date: 2026-09-24.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

cMCP's own architecture fixes the ownership boundary clearly: `Agent -> cMCP Runtime -> Cedar Policy Engine (TEE) -> Tool`. The external agent decides to make an MCP tool call; cMCP intercepts that already-selected action, evaluates it against measured/configured policy and catalog constraints, optionally blocks/redacts it, forwards permitted requests to upstream MCP servers, inspects responses, and commits the resulting evidence into a tamper-evident audit/TRACE path.

`CMCPProxy` describes the network topology as `Agent Host (MCP client) -> CMCPProxy -> cMCP runtime gateway (policy + scanning) -> upstream MCP servers`. Its standard tool-call path checks catalog identity, Cedar authorization, rate limits and dangerous parameters, records evidence, then transports an allowed invocation. `MCPGateway` is explicitly a fail-closed allowlist/response enforcement surface: it checks tool names, parameter patterns, per-agent call budgets and response threats. None of these components generates the agent's objective, decides that a tool should be called in service of that objective, or runs a model/tool reasoning loop.

The policy layer is strong and intentionally isolated. `PolicyEvaluator` loads a measured Cedar bundle and returns/raises ALLOW/DENY/STEP_UP/DEFER-style decisions according to configured enforcement mode. Signed hot reload, policy-key revocation, attestation and Agent Manifest binding make those controls harder to tamper with; they do not transfer authorship of ultimate policy or operational objectives to the gateway. `STATUS.md` is particularly explicit that semantic intent alignment (AARM R3) and semantic distance from intent (R7) are not implemented; the latter is deliberately not approximated because it would require a model.

The runtime also exposes operational safeguards: a kill switch deterministically blocks an agent identity when configured deny-rate thresholds are reached, and operators can explicitly block/unblock identities. Session lifecycle, audit chains, TRACE Claims and offline verification preserve evidence. The standalone execution registry is even more explicit about its status: it is a storage foundation, "not wired into the gateway", and repeat reservations never authorize invocation.

Counterfactual owner test: remove the external agent/MCP client while leaving the entire cMCP gateway, Cedar policies, catalog, TEE, response scanners, kill switch, audit chain, verification library and configured upstream servers intact. The remaining system can validate policy, attest itself, expose/verify evidence and enforce constraints on hypothetical calls, but it does not receive a user objective, choose a substantive action, issue a model-selected tool call, interpret the result and decide the next action. Operational S1 remains outside the assessed first-party boundary.

Under Methodology `0.3.6`, the presence of strong governance or enforcement around an external agent does not satisfy first-party autonomous S1 admission. The proposed terminal outcome is therefore `excluded-no-agentic-vsm` rather than an included constructor vector.

Primary evidence:

- [`README.md`](https://github.com/agentrust-io/cmcp/blob/f8743e013786b094caaa70c336519834e73c74d5/README.md) — product identity and explicit Agent → gateway → policy → Tool topology.
- [`STATUS.md`](https://github.com/agentrust-io/cmcp/blob/f8743e013786b094caaa70c336519834e73c74d5/STATUS.md) — source of truth for shipped versus unimplemented capabilities, including semantic-intent limits.
- [`src/cmcp_runtime/mcp/proxy.py`](https://github.com/agentrust-io/cmcp/blob/f8743e013786b094caaa70c336519834e73c74d5/src/cmcp_runtime/mcp/proxy.py) — first-party MCP interception/transport and enforcement path.
- [`src/cmcp_runtime/runtime_gateway.py`](https://github.com/agentrust-io/cmcp/blob/f8743e013786b094caaa70c336519834e73c74d5/src/cmcp_runtime/runtime_gateway.py) — allowlist, call-budget, dangerous-parameter and response scanning controls.
- [`src/cmcp_runtime/policy/evaluator.py`](https://github.com/agentrust-io/cmcp/blob/f8743e013786b094caaa70c336519834e73c74d5/src/cmcp_runtime/policy/evaluator.py) — Cedar decision/enforcement mode path.
- [`src/cmcp_runtime/kill_switch.py`](https://github.com/agentrust-io/cmcp/blob/f8743e013786b094caaa70c336519834e73c74d5/src/cmcp_runtime/kill_switch.py) — deny-rate and operator block enforcement.
- [`src/cmcp_runtime/execution/registry.py`](https://github.com/agentrust-io/cmcp/blob/f8743e013786b094caaa70c336519834e73c74d5/src/cmcp_runtime/execution/registry.py) — explicitly non-production execution-correlation storage primitive.
- [`src/cmcp_runtime/agent_manifest.py`](https://github.com/agentrust-io/cmcp/blob/f8743e013786b094caaa70c336519834e73c74d5/src/cmcp_runtime/agent_manifest.py) — external agent identity/intent binding evidence rather than an internal agent actor.

## S1 — Operations

- State: —
- Function: no first-party autonomous operational decision/action loop is established inside the cMCP gateway boundary.
- Disturbance / variety regulated: cMCP regulates whether externally selected tool actions are permitted and whether their responses are safe to return, while the substantive task variety and action selection belong to the external agent.
- Decisive decision or feedback right: choose what objective to pursue, whether/which tool to invoke, how to interpret its result, and what substantive action follows.
- Decision owner: the external governed agent/MCP client, not a first-party cMCP autonomous actor.
- Supporting / enforcement mechanisms: catalog allowlist, Cedar policies, TEE measurement, call budgets, parameter/response scanning, session state, upstream transports, kill switch and audit/claim machinery.
- Closure path: external agent selects tool call → cMCP evaluates/enforces/transports the call → upstream returns result → cMCP inspects/enforces response → result or denial returns to the external agent → external agent decides the next substantive action.
- Boundary reachability: removing the external agent leaves no first-party model/tool reasoning loop or other autonomous actor that can originate and pursue an operational objective.
- Why this is / is not agent-owned: cMCP owns enforcement decisions over proposed actions; it does not own the operational action-selection loop whose calls it governs.
- Evidence: [`README.md`](https://github.com/agentrust-io/cmcp/blob/f8743e013786b094caaa70c336519834e73c74d5/README.md); [`src/cmcp_runtime/mcp/proxy.py`](https://github.com/agentrust-io/cmcp/blob/f8743e013786b094caaa70c336519834e73c74d5/src/cmcp_runtime/mcp/proxy.py); [`src/cmcp_runtime/runtime_gateway.py`](https://github.com/agentrust-io/cmcp/blob/f8743e013786b094caaa70c336519834e73c74d5/src/cmcp_runtime/runtime_gateway.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: a separately assessed composed system containing both an autonomous agent and cMCP may establish S1 for that wider boundary; this assessment does not inherit the adjacent agent actor.

### Absence scope

- Surfaces inspected: README/STATUS architecture, gateway proxy, runtime enforcement, policy evaluation, execution registry, session/audit controls, Agent Manifest binding and kill switch.
- Plausible first-party paths checked: gateway itself as agent; response scanner as agent feedback loop; kill switch as operational controller; execution registry as runtime; Agent Manifest intent as goal ownership.
- Why no material first-party path remains: all shipped model-independent paths receive, constrain, transport or attest an action selected elsewhere. The only semantic-intent comparison that might approach autonomous judgment is explicitly unimplemented.

## S2 — Coordination

- State: —
- Function: no first-party S2 coordination function is established because the declared boundary contains no population of first-party autonomous S1 operational units whose interaction disturbance is being attenuated.
- Disturbance / variety regulated: sessions, tool calls and upstream servers can contend for resources or violate policy, but those are gateway/security concerns rather than evidenced oscillation/conflict among distinct internal S1 units.
- Decisive decision or feedback right: no S2-specific autonomous coordination judgment is established.
- Decision owner: none established at the first-party boundary.
- Supporting / enforcement mechanisms: per-session call budgets, session isolation, upstream pooling rules, lifecycle drains, execution correlation and catalog constraints.
- Closure path: mechanisms serialize/constrain requests but do not close a function-specific inter-S1 disturbance → coordination decision → changed later S1 behaviour loop inside cMCP.
- Why this is / is not agent-owned: generic multiplexing, rate limits and session state are not promoted to S2 without an internal S1 interaction witness.
- Evidence: [`src/cmcp_runtime/mcp/proxy.py`](https://github.com/agentrust-io/cmcp/blob/f8743e013786b094caaa70c336519834e73c74d5/src/cmcp_runtime/mcp/proxy.py); [`src/cmcp_runtime/runtime_gateway.py`](https://github.com/agentrust-io/cmcp/blob/f8743e013786b094caaa70c336519834e73c74d5/src/cmcp_runtime/runtime_gateway.py).
- Basis: structural negative search.
- Confidence: high.
- Caveats: a wider deployment with multiple governed agents can use cMCP as shared policy infrastructure, but that does not make the gateway's transport/rate-limiting machinery an internal autonomous S2 function.

### Absence scope

- Surfaces inspected: session lifecycle, per-agent call budgets, upstream transport pooling/isolation, catalog/provenance state, kill switch and execution registry.
- Plausible first-party paths checked: rate limiting; shared upstream servers; session drain/rotation; deny-rate aggregation; execution correlation.
- Why no material first-party path remains: no concrete interaction-generated disturbance among distinct first-party S1 units and no S2-specific autonomous feedback path were found.

## S3 — Inside-and-now control

- State: —
- Function: cMCP strongly constrains current external-agent actions, but no first-party autonomous whole-system current-control function over an internal S1 organization is established.
- Disturbance / variety regulated: forbidden tools/arguments, excessive call rates, deny-rate anomalies, stale/invalid policy or attestation state, unsafe responses and upstream drift/provenance conditions.
- Decisive decision or feedback right: policy rules and configured thresholds deterministically decide whether a proposed action is allowed/denied/redacted/blocked; no autonomous manager chooses current priorities, commitments, allocation or interventions for an internal operational whole.
- Decision owner: policy authors/operators own the substantive configured constraints; deterministic gateway machinery enforces them.
- Supporting / enforcement mechanisms: Cedar evaluator, catalog, response scanner, kill-switch threshold, session lifecycle, fail-closed startup/runtime checks and transport gates.
- Closure path: externally selected call arrives → configured/deterministic checks permit or block → decision changes whether the external action proceeds; this is enforcement over an adjacent agent, not autonomous S3 ownership of internal operations.
- Why this is / is not agent-owned: hard blocking authority is enforcement authority, not evidence that an autonomous actor owns whole-system current-control discretion.
- Evidence: [`src/cmcp_runtime/policy/evaluator.py`](https://github.com/agentrust-io/cmcp/blob/f8743e013786b094caaa70c336519834e73c74d5/src/cmcp_runtime/policy/evaluator.py); [`src/cmcp_runtime/kill_switch.py`](https://github.com/agentrust-io/cmcp/blob/f8743e013786b094caaa70c336519834e73c74d5/src/cmcp_runtime/kill_switch.py); [`STATUS.md`](https://github.com/agentrust-io/cmcp/blob/f8743e013786b094caaa70c336519834e73c74d5/STATUS.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: cMCP may implement an important governance/control role in a wider agent organization. The negative state is about autonomous S3 ownership at the declared repository-relative boundary, not about enforcement strength.

### Absence scope

- Surfaces inspected: Cedar decisions, enforcement modes, kill switch, policy reload/revocation, session lifecycle, catalog drift/provenance and runtime gateway gates.
- Plausible first-party paths checked: policy engine as manager; kill switch as S3; policy hot reload as current control; session lifecycle as manager; response blocking as intervention.
- Why no material first-party path remains: each path enforces pre-authored rules or lifecycle invariants and lacks an autonomous whole-system decision owner over internal S1 operations.

## S3* — Complementary audit

- State: —
- Function: cMCP supplies extensive audit, attestation and verification evidence, but no qualifying complementary audit of a first-party S1 operational reality is established at this boundary.
- Disturbance / variety regulated: policy decisions or audit records might be tampered with, runtime identity might differ from the approved artifact, upstream provenance may drift, and a verifier may need evidence independent of the operator.
- Decisive decision or feedback right: cMCP records/signs/attests execution evidence and its verifier appraises signatures, hashes, chains and platform claims; these checks validate governance evidence rather than independently challenge an internal S1 claim/result through a corrective organizational feedback loop.
- Decision owner: deterministic attestation/verification code and external auditors/verifiers; no first-party autonomous S3* actor over internal operations.
- Supporting / enforcement mechanisms: hash-chained audit log, TRACE Claim, TEE-bound signing key, offline verifier, catalog/provenance verification, Agent Manifest binding and response inspection.
- Closure path: tool/governance event → first-party evidence is committed → verifier can appraise authenticity/consistency; no internally owned independent audit judgment over first-party S1 reality returns into corrective internal operation because first-party S1 is absent.
- Why this is / is not agent-owned: cryptographic independence from the operator is strong evidence integrity, but S3* is an organizational function, not a synonym for audit log/attestation/verification.
- Evidence: [`README.md`](https://github.com/agentrust-io/cmcp/blob/f8743e013786b094caaa70c336519834e73c74d5/README.md); [`STATUS.md`](https://github.com/agentrust-io/cmcp/blob/f8743e013786b094caaa70c336519834e73c74d5/STATUS.md); [`src/cmcp_runtime/mcp/proxy.py`](https://github.com/agentrust-io/cmcp/blob/f8743e013786b094caaa70c336519834e73c74d5/src/cmcp_runtime/mcp/proxy.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: in a wider composed system, cMCP's tamper-resistant evidence and independent verifier can be important supporting material for an S3* design; that separate system boundary would need its own audit-function reconstruction.

### Absence scope

- Surfaces inspected: audit chain, TRACE Claim, offline verification, TEE attestation, Agent Manifest verification, server provenance, catalog drift, response inspection and policy-decision evidence.
- Plausible first-party paths checked: verifier as S3*; TEE isolation as independent audit; server provenance as complementary channel; response scanner as audit; Agent Manifest verification as operational challenge.
- Why no material first-party path remains: inspected paths prove/configure/enforce security and provenance properties of gateway-mediated calls but do not independently challenge a first-party operational S1 result and return that judgment into corrective internal operation.

## S4 — Outside-and-then adaptation

- State: —
- Function: no autonomous outside-and-future sensing/adaptation loop that persistently changes cMCP organizational capability is established.
- Disturbance / variety regulated: policy bundles, signing keys, catalogs, trust anchors, provider support and configuration can evolve, and the runtime can detect/reload approved policy changes.
- Decisive decision or feedback right: what new policy/version/trust anchor/capability should be adopted is decided by external authors/operators; hot reload verifies and installs authorized artifacts rather than autonomously generating/adopting adaptation options.
- Decision owner: external policy/configuration/governance authorities, not a first-party autonomous S4 actor.
- Supporting / enforcement mechanisms: signed policy hot reload, version monotonicity, key revocation/successor handling, catalog/provenance checks, attestation refresh and status/roadmap evidence.
- Closure path: external authority authors/signs change → cMCP verifies and installs/uses it → later calls follow changed constraints. The prospective adaptation judgment originates outside the first-party runtime.
- Why this is / is not agent-owned: secure policy update is a strong adaptation transport/enforcement path, but the system does not itself sense outside/future conditions, formulate alternatives and choose persistent organizational change.
- Evidence: [`STATUS.md`](https://github.com/agentrust-io/cmcp/blob/f8743e013786b094caaa70c336519834e73c74d5/STATUS.md); [`src/cmcp_runtime/policy/evaluator.py`](https://github.com/agentrust-io/cmcp/blob/f8743e013786b094caaa70c336519834e73c74d5/src/cmcp_runtime/policy/evaluator.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: signed hot reload provides a useful constructor/support surface for externally governed adaptation, but Methodology does not award S4 from update capability alone without the function-specific adaptation judgment loop.

### Absence scope

- Surfaces inspected: policy hot reload/revocation, attestation refresh, catalog/provenance drift, STATUS roadmap, configuration and Agent Manifest binding.
- Plausible first-party paths checked: policy reload as learning; provenance drift as external sensing; key succession as adaptation; roadmap/provider expansion as S4.
- Why no material first-party path remains: sensing/checking is present, but option generation and decisive persistent adaptation remain externally authored.

## S5 — Policy / identity

- State: —
- Function: cMCP enforces policy and binds identity evidence but does not establish an autonomous or qualifying parent-governed identity/ultimate-policy decision loop at the declared runtime boundary.
- Disturbance / variety regulated: which tools/actions are permitted, which policy artifacts/issuer keys are trusted, what agent identity/declared intent is bound, and which enforcement mode applies.
- Decisive decision or feedback right: policy bundles, trust anchors, manifests, conformance profile and enforcement configuration are supplied/signed by external authorities; cMCP verifies and enforces them rather than deciding organizational identity/ultimate policy.
- Decision owner: external policy authors/operators/manifest issuers/trust authorities.
- Supporting / enforcement mechanisms: Cedar policy bundle, signed hot reload, Agent Manifest binding, trust anchors, enforcement modes, attestation and kill switch.
- Closure path: external authority defines/signs identity/policy constraints → cMCP verifies/binds/enforces them → subsequent gateway behavior changes. This does not by itself establish the required identity-level parent-governance function; the runtime is an enforcement membrane for supplied policy.
- Why this is / is not agent-owned: a component named policy engine does not become S5; the relevant ultimate-policy choice remains outside the runtime and no evidenced S5 deliberation/escalation/return topology is supplied.
- Evidence: [`src/cmcp_runtime/agent_manifest.py`](https://github.com/agentrust-io/cmcp/blob/f8743e013786b094caaa70c336519834e73c74d5/src/cmcp_runtime/agent_manifest.py); [`src/cmcp_runtime/policy/evaluator.py`](https://github.com/agentrust-io/cmcp/blob/f8743e013786b094caaa70c336519834e73c74d5/src/cmcp_runtime/policy/evaluator.py); [`STATUS.md`](https://github.com/agentrust-io/cmcp/blob/f8743e013786b094caaa70c336519834e73c74d5/STATUS.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: cMCP can enforce a parent's ultimate policy in a wider organization, but the mere existence of externally supplied policy/configuration is insufficient to publish `S5=P` for this gateway boundary without an evidenced S5 matter/authority/return loop.

### Absence scope

- Surfaces inspected: Cedar policy authorship/enforcement, signing keys/revocation, Agent Manifest intent/identity binding, conformance profiles, trust anchors, kill switch and operator controls.
- Plausible first-party paths checked: policy engine as S5; signed policy issuer as parent S5; manifest intent as organizational identity; operator block/unblock as ultimate authority.
- Why no material first-party path remains: the repository verifies and enforces externally supplied identity/policy facts, but does not establish an identity/ultimate-policy organizational decision loop at the declared first-party recursion.

## Terminal outcome

`excluded-no-agentic-vsm`.

cMCP is a substantive, technically strong governance/enforcement runtime. The exclusion is narrower: it intentionally governs an external agent's selected MCP actions and does not itself supply the autonomous operational decision/action loop required for S1 inclusion. Strong Cedar enforcement, TEE isolation, kill-switch control, audit/attestation and verification therefore remain supporting governance functions at this repository-relative boundary rather than an included VSM autonomy vector.

## Evidence boundaries / caveats

- No VSM function is inferred from terms such as `policy`, `gateway`, `runtime`, `audit`, `verification`, `kill switch`, `agent manifest`, `decision` or `control plane`.
- Deterministic allow/deny/redact/threshold decisions are separated from autonomous organizational discretion.
- Cryptographic/TEE independence is treated as evidence-integrity/security architecture, not automatically as S3* organizational independence.
- External policy authorship and Agent Manifest issuer intent are not imported as first-party S5 ownership.
- Explicitly unimplemented semantic-intent capabilities in `STATUS.md` are not promoted from roadmap/design text.
- A composed system containing an autonomous agent plus cMCP is a separate system-in-focus and requires its own evidence.
