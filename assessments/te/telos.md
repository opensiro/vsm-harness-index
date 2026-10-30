---
harness_id: telos
project_name: Telos
repository: https://github.com/nevinshine/telos-runtime
review_ref: d430d61c9005f2ab5523ba2d41bdab574fcc314e
reviewed_at: 2026-10-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: excluded-no-agentic-vsm
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Telos

## Review boundary

- System in focus: the first-party Telos intent-based **security runtime** at `d430d61c9005f2ab5523ba2d41bdab574fcc314e`, not an unspecified AI agent protected by it.
- Purpose and identity: regulate process execution, network access and information flow for externally supplied agent/process workloads according to declared intent, taint and configured security policy.
- Relevant environment: operator-supplied processes and agents, natural-language intent declarations, browsers, DNS destinations, Linux syscalls, kernel eBPF/LSM, potentially hostile data and the optional local model used to classify ambiguous domains.
- Standard-distribution boundary: the shipped Cortex gRPC verifier/guardian, deterministic domain and execution classifiers, optional TinyLlama relevance classifier, policy configuration, persistent audit, Browser Eye, kernel/edge enforcement, and operating CLI. Telos is a guard for **other** agent processes; their task decision loops are external.
- Credited operating / distribution surfaces: `cortex/main.py`, `cortex/verifier.py`, `cortex/domain_intel.py`, `cortex/exec_intel.py`, `cortex/llm_verifier.py`, `cortex/guardian.py`, `cortex/config.py`, `cortex/audit.py`, `telos_core/src/bpf_lsm.c`, `telos_edge/src/xdp_filter.c`, `browser_eye/`, and `telos_cli.py`.
- Adjacent first-party surfaces excluded from ownership: the deliberately vulnerable `deploy/vulnerable_agent/agent_sim.py`, red-team and attack simulators, proof-of-concept demos, benchmark and verification scripts, repository CI, white paper, and maintainer/development activities. They are evidence of expected integration, not an autonomous production S1 inside Telos.
- First-party operating / deployment modes considered: Cortex with deterministic domain/exec intelligence; optional local LLM classifier on escalation; kernel/network enforcement with Browser Eye taint signals; CLI and configured security policy; demonstration agent process outside the production runtime.
- Recursion level: one deployed Telos security service protecting one or more external processes, rather than a larger organization that includes the protected agent and its operator.
- Reviewed revision: `d430d61c9005f2ab5523ba2d41bdab574fcc314e`.
- Observation date: 2026-10-29.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.7`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.7`.

## Repository architecture

The project ships a Linux security-control and enforcement stack. External processes declare a goal and planned network or execution actions over `TelosControl.DeclareIntent`. Cortex validates the PID/session, checks current taint and rate limits, invokes `IntentVerifier`, and sends allow/deny execution and network restrictions to the Go/eBPF layer. `Guardian` associates browser observations with PIDs and preserves taint state; the audit database records policy events. The operator configures sensitive paths, network rules and thresholds. Neither the gRPC server nor eBPF hooks choose the protected agent's goals, next actions or response to their tool observations.

`IntentVerifier` computes deterministic domain and binary classifications. For an ambiguous domain it can call a local `LLMVerifier`, which classifies *goal–domain relevance* and can persist that verdict for subsequent lookups. This is a narrow security judgment, not an agent that plans work, invokes its own tools, observes task results and chooses subsequent substantive actions. The fallback is absent when the optional model is unavailable. Persisted security verdicts are reactive enforcement data, not evidence of a prospective S4 capability-adaptation conversation.

The one file named an agent loop, `deploy/vulnerable_agent/agent_sim.py`, is explicitly a **simulation**: it requests an intent verdict and then reads shell commands from a human `input(...)` loop (or an explicitly supplied single command) and executes them. It has no LLM-generated task/action loop. `deploy/vulnerable_agent/redteam_suite.py` feeds predefined test scenarios into Cortex; it is validation of the guard, not operational AI agent ownership. The README describes Telos as a security runtime *for* autonomous agents, and the code confirms the supported subject is a protected external process rather than a bundled autonomous agent.

Primary pinned evidence:

- [README](https://github.com/nevinshine/telos-runtime/blob/d430d61c9005f2ab5523ba2d41bdab574fcc314e/README.md) — intent, eBPF/LSM and security-service identity.
- [Cortex gRPC service](https://github.com/nevinshine/telos-runtime/blob/d430d61c9005f2ab5523ba2d41bdab574fcc314e/cortex/main.py) — external intent input, verification, policy commit and process registration.
- [IntentVerifier](https://github.com/nevinshine/telos-runtime/blob/d430d61c9005f2ab5523ba2d41bdab574fcc314e/cortex/verifier.py) — deterministic security classification and optional LLM escalation.
- [LLMVerifier](https://github.com/nevinshine/telos-runtime/blob/d430d61c9005f2ab5523ba2d41bdab574fcc314e/cortex/llm_verifier.py) — bounded domain-relevance inference, not task act/observe recurrence.
- [Guardian](https://github.com/nevinshine/telos-runtime/blob/d430d61c9005f2ab5523ba2d41bdab574fcc314e/cortex/guardian.py) and [policy schema](https://github.com/nevinshine/telos-runtime/blob/d430d61c9005f2ab5523ba2d41bdab574fcc314e/cortex/config.py) — state, policy and owner/configuration split.
- [Simulated agent](https://github.com/nevinshine/telos-runtime/blob/d430d61c9005f2ab5523ba2d41bdab574fcc314e/deploy/vulnerable_agent/agent_sim.py) and [red-team fixture](https://github.com/nevinshine/telos-runtime/blob/d430d61c9005f2ab5523ba2d41bdab574fcc314e/deploy/vulnerable_agent/redteam_suite.py) — separate demonstration/test surfaces.

## Operational model

An external agent/process decides what it wants to do, sends intent and planned actions, and receives a security verdict. Telos classifies and enforces; the external agent remains responsible for its own actual task loop. An operator sets policy and deploys the guard. Under the counterfactual owner test, removing the external agent but keeping Cortex, policy, the optional relevance model, Browser Eye, audit DB and eBPF yields a security service that can inspect requests but cannot itself pursue an autonomous operational task in its environment. The demo's command prompt is human-driven. This fails the Index first-party autonomous S1 inclusion boundary. The following negative vector is bounded to this Telos distribution, not a universal claim about systems that integrate Telos.

## S1 — Operations

- State: —
- Function: no first-party autonomous agent work cell producing an environmental task outcome with a model/action/observation/next-choice loop is supplied.
- Disturbance / variety regulated: process behavior and suspect domains are regulated by security gates, while actual tasks and environment-facing agent decisions belong to protected external programs.
- Decisive decision or feedback right: choosing and revising substantive task actions after observations; Telos decides only whether a declared operation is permitted.
- Decision owner: external agent or human operating the process; the Telos security verdict belongs to deterministic rules and optionally a narrow model classifier.
- Supporting / enforcement mechanisms: Cortex gRPC, PID/session registry, taint, domain/exec scoring, kernel eBPF policy maps, audit and browser observations.
- Closure path: external process intent → Telos allow/deny → kernel enforcement → external process continues or is blocked. No first-party autonomous task-policy recurrence is returned within Telos.
- Why this is / is not agent-owned: an optional model can judge domain relevance but does not own goal formation, tool selection, substantive task action or observation-driven next-step selection. The only packaged agent simulator uses human shell input.
- Evidence: [Cortex](https://github.com/nevinshine/telos-runtime/blob/d430d61c9005f2ab5523ba2d41bdab574fcc314e/cortex/main.py), [verifier](https://github.com/nevinshine/telos-runtime/blob/d430d61c9005f2ab5523ba2d41bdab574fcc314e/cortex/verifier.py), [simulator](https://github.com/nevinshine/telos-runtime/blob/d430d61c9005f2ab5523ba2d41bdab574fcc314e/deploy/vulnerable_agent/agent_sim.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: Telos may be a valuable protective component in a wider autonomous agent organization; that wider system has a different ownership boundary.

### Absence scope

- Surfaces inspected: README, Cortex entry/verification/classification, optional model, Guardian, security policy, agent demo, red-team suite, CLI and enforcement/IPC tree.
- Plausible first-party paths checked: Cortex as a primary autonomous agent; optional relevance model as a task actor; PID-based agent registry as ownership; demo shell loop as a production agent loop.
- Why no material first-party path remains: the production path is a guard around externally initiated actions, the optional model makes a single security classification, and the demo action selection is explicitly human/test-driven.

## S2 — Coordination

- State: —
- Function: no S2 relation between distinct first-party autonomous operational S1 units is established.
- Disturbance / variety regulated: rate limiting, per-PID taint, locks and network rules regulate resource and process safety, not oscillation between two first-party autonomous S1 units.
- Decisive decision or feedback right: attenuation of identified inter-S1 interference with returned adjustment to each unit; no such first-party organizational decision is wired.
- Decision owner: operator rules and deterministic Cortex/Guardian enforcement for independent external processes.
- Supporting / enforcement mechanisms: per-PID rate limiter/locks, session map, shared domain DB and kernel maps.
- Closure path: Cortex applies safety restrictions to PIDs; no evidence of multiple first-party S1s negotiating or adapting their operations to resolve a concrete mutual interference.
- Why this is / is not agent-owned: multiple registered PIDs are external workloads, and safety serialization is not by itself an S2-specific autonomous coordination loop.
- Evidence: [Guardian](https://github.com/nevinshine/telos-runtime/blob/d430d61c9005f2ab5523ba2d41bdab574fcc314e/cortex/guardian.py), [Cortex](https://github.com/nevinshine/telos-runtime/blob/d430d61c9005f2ab5523ba2d41bdab574fcc314e/cortex/main.py).
- Basis: structural absence.
- Confidence: high.
- Caveats: a larger assembly of agents could use Telos policy to reduce collisions; that would need its own concrete S2 witness.

### Absence scope

- Surfaces inspected: PID/session registry, per-PID locks and rate limits, domain maps, agent simulator and multi-process API.
- Plausible first-party paths checked: multiple PIDs as S1 plurality; lock/queue as S2; shared taint as conflict regulation.
- Why no material first-party path remains: no two first-party autonomous S1 units, identified interference between them, S2-specific attenuating judgment, and feedback into their task decisions are shipped.

## S3 — Inside-and-now control

- State: —
- Function: no whole-system autonomous-operations control over first-party S1 commitments or priorities is established at this boundary.
- Disturbance / variety regulated: current security violations, policy expiry, taint and resource safety, rather than whole-system commitments of a Telos-owned agent organization.
- Decisive decision or feedback right: choosing/revising resource allocations, operational priorities or commitments for multiple first-party S1 units; not supplied.
- Decision owner: operator-authored policy for the constraint; Cortex/Guardian deterministically evaluate/enforce it; optional model judges isolated domain relevance.
- Supporting / enforcement mechanisms: fail-closed taint checks, policy maps, rate-limit timers, allow/deny/TTL and kill-like restrictions.
- Closure path: verified declared intent → restrictions installed on protected external PID → later calls permitted or denied. This is security enforcement of a selected policy, not Telos-owned S3 organizational regulation.
- Why this is / is not agent-owned: enforcement power and `Cortex` naming do not imply ownership of a whole-agent organization's current resource/commitment decisions.
- Evidence: [Cortex service](https://github.com/nevinshine/telos-runtime/blob/d430d61c9005f2ab5523ba2d41bdab574fcc314e/cortex/main.py), [policy](https://github.com/nevinshine/telos-runtime/blob/d430d61c9005f2ab5523ba2d41bdab574fcc314e/cortex/config.py).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: at a larger deployment boundary Telos restrictions might enforce a parent S3 decision, but enforcement does not transfer that decision right to Telos.

### Absence scope

- Surfaces inspected: Cortex request flow, policy config, Guardian, rate-limit and taint recovery, IPC/kernel updates and CLI lifecycle.
- Plausible first-party paths checked: central policy engine as S3; rate limiter and kill restrictions as S3; human operator settings as a first-party parent S3 mode.
- Why no material first-party path remains: no first-party autonomous S1 commitments or whole-system current management loop is present; static operator policy and deterministic enforcement do not supply the missing function/owner.

## S3* — Complementary audit

- State: —
- Function: no complementary audit of ordinary reporting by a Telos-owned autonomous S1 organization is supplied.
- Disturbance / variety regulated: taint and suspicious process behavior are monitored independently of protected external processes, but those processes are outside the declared Telos-owned S1 boundary.
- Decisive decision or feedback right: independently challenge an internal S1 performance/assurance claim and return findings into organizational control; not supplied for first-party S1.
- Decision owner: deterministic Browser Eye/Guardian and policy engine; tests and red-team fixtures exercise guard behavior in a separate evaluation boundary.
- Supporting / enforcement mechanisms: browser signals, audit SQLite, test scenarios and kernel telemetry.
- Closure path: browser/kernel observation → taint → enforcement against external PID; no first-party normal S1 report → complementary independently judged audit → corrective control return is established.
- Why this is / is not agent-owned: a security telemetry feed can be complementary evidence at a *wider protected-agent* boundary, but generic logging, tests and external-process taint are not a first-party S3* organizational audit of Telos S1.
- Evidence: [Guardian](https://github.com/nevinshine/telos-runtime/blob/d430d61c9005f2ab5523ba2d41bdab574fcc314e/cortex/guardian.py), [audit](https://github.com/nevinshine/telos-runtime/blob/d430d61c9005f2ab5523ba2d41bdab574fcc314e/cortex/audit.py), [red-team fixture](https://github.com/nevinshine/telos-runtime/blob/d430d61c9005f2ab5523ba2d41bdab574fcc314e/deploy/vulnerable_agent/redteam_suite.py).
- Basis: explicit + structural absence.
- Confidence: medium-high.
- Caveats: direct browser/LSM observation could form part of S3* for an external agent organization, not for the narrower Telos runtime assessed here.

### Absence scope

- Surfaces inspected: Browser Eye, Guardian taint bridge, audit trail, tests/red-team fixture, policy enforcement and Cortex reporting.
- Plausible first-party paths checked: Browser Eye as independent auditor; test suite as S3*; audit DB as S3*; kernel telemetry as complementary S1 truth.
- Why no material first-party path remains: these inspect/enforce external process behavior or validate Telos in test contexts; no autonomous first-party S1 ordinary claim and independently closed audit correction relation exists at this recursion.

## S4 — Outside-and-then intelligence

- State: —
- Function: no externally prospective adaptation conversation with present first-party autonomous operational capability is established.
- Disturbance / variety regulated: unknown domains and mismatches trigger current threat classification; they do not themselves drive future-oriented redesign of autonomous S1 capability.
- Decisive decision or feedback right: develop a future-relevant adaptation option and select its return into current organizational capability; no such path is supplied.
- Decision owner: optional local model makes single relevance verdicts; deterministic code can persist domain trust for later checks. Operator/developer owns broader policy/product changes.
- Supporting / enforcement mechanisms: SQLite domain verdict cache, seed watchlist, heuristics, LLM fallback and YAML policy.
- Closure path: unknown domain → LLM relevance judgment → persisted domain classification → future security lookups. This is reactive classification reuse, not outside-and-then options communicated with S3 and adopted as changed capability.
- Why this is / is not agent-owned: `self-learning` persistence does not by itself demonstrate S4 prospective intelligence; the model does not plan future adaptation or govern operational reconfiguration.
- Evidence: [verifier](https://github.com/nevinshine/telos-runtime/blob/d430d61c9005f2ab5523ba2d41bdab574fcc314e/cortex/verifier.py), [domain intelligence](https://github.com/nevinshine/telos-runtime/blob/d430d61c9005f2ab5523ba2d41bdab574fcc314e/cortex/domain_intel.py), [LLM](https://github.com/nevinshine/telos-runtime/blob/d430d61c9005f2ab5523ba2d41bdab574fcc314e/cortex/llm_verifier.py).
- Basis: structural absence.
- Confidence: high.
- Caveats: new threat classification can improve later blocking; that operational learning is not equivalent to a VSM S4 future strategy function.

### Absence scope

- Surfaces inspected: deterministic domain/exec intelligence, LLM relevance classifier, persisted verdicts, policy YAML, core/edge update logic and architecture docs.
- Plausible first-party paths checked: unknown-domain escalation as S4; persisted security verdicts as self-improvement; changing deny lists as adaptation; maintainers' roadmap as S4.
- Why no material first-party path remains: no first-party prospective external model → adaptation options → S3/current-capability return is wired in the reviewed standard distribution.

## S5 — Policy and identity

- State: —
- Function: no legitimate live identity/ultimate-policy decision closure for a first-party agent organization is established.
- Disturbance / variety regulated: operator-configured access, sensitive paths and model thresholds constrain security decisions, but do not constitute identity-level tension in a Telos-owned autonomous organization.
- Decisive decision or feedback right: resolve an actual identity/ultimate-policy matter at the declared recursion and return the authoritative decision into subsequent operation; no such path is present.
- Decision owner: external operator/developer authoring `policy.yaml` and config, not an internal S5 authority; runtime enforces the selected constraints.
- Supporting / enforcement mechanisms: Pydantic policy loader, YAML rules, auth token, kernel enforcement and CLI management.
- Closure path: configured constraints → validated load → subsequent security verdicts/enforcement. No identity/policy matter → legitimate parent authority → returned authoritative resolution of a Telos agent organization is evidenced.
- Why this is / is not agent-owned: static policy text and permission gates are not S5; human configuration is not automatically a function-specific parent-governed S5 loop.
- Evidence: [config schema](https://github.com/nevinshine/telos-runtime/blob/d430d61c9005f2ab5523ba2d41bdab574fcc314e/cortex/config.py), [policy YAML](https://github.com/nevinshine/telos-runtime/blob/d430d61c9005f2ab5523ba2d41bdab574fcc314e/cortex/policy.yaml), [CLI](https://github.com/nevinshine/telos-runtime/blob/d430d61c9005f2ab5523ba2d41bdab574fcc314e/telos_cli.py).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: the operator can maintain legitimate ultimate policy for their wider organization, but that is not a shipped first-party Telos S5 ownership path.

### Absence scope

- Surfaces inspected: policy schema/file, Cortex startup/auth, CLI, README/security prose, request permissions and simulated agent.
- Plausible first-party paths checked: YAML policy as S5; operator edits as parent S5; intent approval as ultimate policy; security violation escalation as identity judgment.
- Why no material first-party path remains: inspected paths govern operational permissions and load configuration, without a first-party identity-level issue and legitimate decisive-return closure at this recursion.

## Recursion

Telos protects external agent processes and can itself be a supporting mechanism within those agents' parent organization. The agent simulator is a test client, not an autonomous recursive S1. A distinct assessment of a deployed agent + Telos + human governance system could produce very different VSM results; this Index artifact assesses the repository-relative security runtime only.

## Variety and escalation

The guard attenuates a wide range of process/network/security variety via deterministic scoring, taint, locks, policy, model escalation and eBPF. The noteworthy decision-owner split is that external agents propose actions, an optional model supplies narrow domain relevance, operators determine policy, and Telos enforces. `ESCALATE` in [IntentVerifier](https://github.com/nevinshine/telos-runtime/blob/d430d61c9005f2ab5523ba2d41bdab574fcc314e/cortex/verifier.py) is a local policy classification/LLM fallback, not proof of a VSM S3/S4/S5 path or algedonic organizational signal. No live/offensive execution was performed for this review.

## Evidence gaps

- No first-party protected-agent deployment or action/observation loop is included in the declared repository-relative boundary; external agents' cognitive control would need an independently pinned assessment.
- TinyLlama relevance inference was assessed from source only; no model weights were downloaded or inference run, and no accuracy or runtime-determinism claim is made. Its documented input/output is sufficiently narrow to distinguish it from an autonomous task/action loop.
- The [red-team fixture](https://github.com/nevinshine/telos-runtime/blob/d430d61c9005f2ab5523ba2d41bdab574fcc314e/deploy/vulnerable_agent/redteam_suite.py) and demo source are adjacent and cannot donate task autonomy to production Telos; test results are not treated as organizational S3* evidence.
- The deployed [Cortex gRPC request path](https://github.com/nevinshine/telos-runtime/blob/d430d61c9005f2ab5523ba2d41bdab574fcc314e/cortex/main.py) consumes `natural_language_goal` and `planned_actions` supplied by its caller; it does not generate those actions or own the caller's observation-to-next-action loop.
- Negative states are bounded to shipped first-party operating paths inspected, not a claim that integration with Telos can never support a viable agent organization.

## Assessment summary

Telos is a security enforcement substrate *for* autonomous agents. It does not ship the first-party autonomous operational agent loop required for Index inclusion.

Its [optional model](https://github.com/nevinshine/telos-runtime/blob/d430d61c9005f2ab5523ba2d41bdab574fcc314e/cortex/llm_verifier.py) judges domain relevance on security escalation; the only bundled agent loop is a [human-input simulator](https://github.com/nevinshine/telos-runtime/blob/d430d61c9005f2ab5523ba2d41bdab574fcc314e/deploy/vulnerable_agent/agent_sim.py). Under Profile 0.2.4 / Methodology 0.3.7, the canonical disposition is `excluded-no-agentic-vsm` with `S1=— / S2=— / S3=— / S3*=— / S4=— / S5=—`.
