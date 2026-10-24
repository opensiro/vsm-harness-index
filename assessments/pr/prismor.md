---
harness_id: prismor
project_name: Prismor
repository: https://github.com/PrismorSec/prismor
review_ref: 4cdcfb62197e01da280e21b3f3534bb791109065
reviewed_at: 2026-10-10
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
status: included
autonomy_s1: A
autonomy_s2: ?
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: P
autonomy_s5: ?
---

# Prismor

## Review boundary

- System in focus: one deployed first-party Prismor runtime security control boundary protecting one or more configured coding agents and/or framework-managed agents, with hooks/proxy/MCP interceptors, policy engine, optional model-backed semantic security judge, event history and human-governed learning-policy update.
- Purpose and identity: prevent or flag unsafe agent actions, exfiltration and adversarial prompts, preserve audit evidence and enable future policy adjustment based on encountered security patterns.
- Relevant environment: external coding agents, tools/MCP servers, model requests and responses, untrusted files/web/tool results, per-agent IAM claims, local project and network infrastructure, human operator/security administrator.
- Standard-distribution boundary: installed Python `prismor` CLI, `prismor/runtime/` policy/interception/security-judgment path, optional supported semantic model guard, learning CLI and project policy, and supported local/organization policy configuration. External hosted Claude Code/Codex/LangGraph/... agent reasoning and tool execution are not imported as Prismor control cognition.
- Credited operating / distribution surfaces: `prismor/runtime/runtime.py`, `policy_engine.py`, installed hooks and MCP/proxy guard, opt-in semantic guard, `learning.py` and `cli.py` operator-accepted policy updates.
- Adjacent first-party surfaces excluded from ownership: samples/benchmark/research/training/CI/release/test files, unrelated threat assessments, external upstream coding agent proprietary reasoning/tool loop, external SIEM and human audit organizations not instantiated in this deployment.
- First-party operating / deployment modes considered: installed hooks and gateway on pre-action events, observe/enforce policy, supported model-backed semantic-guard mode with configured model/CLI, local human policy maintainer `prismor learn --apply`, optional audit receipts and admin-bound scopes.
- Recursion level: one Prismor-governed local project/workspace/security policy boundary around autonomous agent actors; the enterprise organization, multiple independent installations and open-source maintainer organization are different recursions.
- Reviewed revision: `4cdcfb62197e01da280e21b3f3534bb791109065`.
- Observation date: 2026-10-10.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

Prismor integrates at the tool/LLM/MCP event boundary. Installed CLI hooks or the local gateway intercept an external agent's requests and content, load a project/organization policy plus packaged base rules, and return an allow/warn/block/approval outcome that the host honors in the supported pre-action setting. `PolicyEngine` owns deterministic rule loading, precedence, effective enforcement mode and compiled matching; per-agent IAM, signed remote overlays and admin exceptions constrain one action or identity at a time. A separate semantic guard optionally dispatches ambiguous prompt-injection intent to a configured model-backed judge; the judgment is returned as security feedback. These are first-party Prismor paths even though the coding agents and model inference engines remain external.

Prismor also persists observed action/violation history and proposes new rules from repeated uncovered sensitive commands. `prismor learn` mines the recorded environment, but explicitly **does not auto-apply** a candidate; `prismor learn --apply ID` requires the human operator to select a rule. The CLI appends the accepted rule to the project YAML policy, and later policy-engine instances read the overlay. That is an evidenced prospective human-parent adaptation loop, not an autonomous model-governance loop.

Architectural evidence: [README.md](https://github.com/PrismorSec/prismor/blob/4cdcfb62197e01da280e21b3f3534bb791109065/README.md); [hooks.py](https://github.com/PrismorSec/prismor/blob/4cdcfb62197e01da280e21b3f3534bb791109065/prismor/runtime/hooks.py); [runtime.py](https://github.com/PrismorSec/prismor/blob/4cdcfb62197e01da280e21b3f3534bb791109065/prismor/runtime/runtime.py); [policy_engine.py](https://github.com/PrismorSec/prismor/blob/4cdcfb62197e01da280e21b3f3534bb791109065/prismor/runtime/policy_engine.py); [mcp_gateway.py](https://github.com/PrismorSec/prismor/blob/4cdcfb62197e01da280e21b3f3534bb791109065/prismor/runtime/mcp_gateway.py); [proxy.py](https://github.com/PrismorSec/prismor/blob/4cdcfb62197e01da280e21b3f3534bb791109065/prismor/runtime/proxy.py); [semantic-guard.md](https://github.com/PrismorSec/prismor/blob/4cdcfb62197e01da280e21b3f3534bb791109065/docs/semantic-guard.md); [semantic_guard.py](https://github.com/PrismorSec/prismor/blob/4cdcfb62197e01da280e21b3f3534bb791109065/prismor/runtime/semantic_guard.py); [learning.py](https://github.com/PrismorSec/prismor/blob/4cdcfb62197e01da280e21b3f3534bb791109065/prismor/runtime/learning.py); [cli.py](https://github.com/PrismorSec/prismor/blob/4cdcfb62197e01da280e21b3f3534bb791109065/prismor/runtime/cli.py); [learning.md](https://github.com/PrismorSec/prismor/blob/4cdcfb62197e01da280e21b3f3534bb791109065/docs/learning.md).

## Operational model

Each supported external agent continues to choose and execute its own task-level coding/tool behavior. The first-party Prismor security detector instead enacts its local purpose by inspecting agent-facing actions/content and deciding security outcomes; the optional model-backed semantic guard owns some discretionary detection choices. The deterministic policy engine supplies most blocking/recording mechanisms. Cross-agent visibility, identity-specific access restrictions, signed trails, attestations and policy configuration are assessed as such rather than promoted to S2/S3/S3*/S5 without function-specific organizational proof. A local human explicitly promotes learned detection rules to influence future execution.

## S1 — Operations

- State: A
- Function: produce bounded security judgments on incoming agent actions and tool/model messages through Prismor's first-party event/semantic guard and enforce/warn decision path.
- Disturbance / variety regulated: malicious prompts, evolving shell/tool/API payloads, ambiguous injection variants and sensitive-resource access that could redirect executing coding agents.
- Decisive decision or feedback right: the configured semantic-guard model evaluates ambiguous intent when pre-screen confidence falls into its model-calling region; ordinary rule matches also produce deterministic verdicts.
- Decision owner: the model-backed semantic security judge called by Prismor's packaged semantic-guard integration for the narrow uncertainty zone; the external CLI/provider supplies inference, not an imported programming-agent manager.
- Supporting / enforcement mechanisms: heuristic pre-screen, rule compiler, hook adapters and MCP/LLM proxy, configured observe/enforce modes, rule mode resolution and action withholding.
- Closure path: agent sends a pending action/tool-content event → first-party Prismor hook/adapter applies guard and may seek a model verdict → allow/warn/block reaches the hook or proxy → external agent continues, sees warning, or does not receive blocked tool action/result.
- Boundary reachability: semantic-guard mode is shipped and documented in Prismor's standard install and is directly integrated into its runtime evaluation path; native coding agents remain separately running S1 consumers of the verdict.
- Why this is / is not agent-owned: for ambiguous paraphrased attacks the configured judge actually chooses a context-sensitive verdict; deterministic rule gates by themselves cannot be counted as this agent-owned decision. This credits Prismor's specific shipped model-judge path rather than the coding agent's proprietary cognition.
- Evidence: [README.md](https://github.com/PrismorSec/prismor/blob/4cdcfb62197e01da280e21b3f3534bb791109065/README.md); [semantic-guard.md](https://github.com/PrismorSec/prismor/blob/4cdcfb62197e01da280e21b3f3534bb791109065/docs/semantic-guard.md); [semantic_guard.py](https://github.com/PrismorSec/prismor/blob/4cdcfb62197e01da280e21b3f3534bb791109065/prismor/runtime/semantic_guard.py); [runtime.py](https://github.com/PrismorSec/prismor/blob/4cdcfb62197e01da280e21b3f3534bb791109065/prismor/runtime/runtime.py); [policy_engine.py](https://github.com/PrismorSec/prismor/blob/4cdcfb62197e01da280e21b3f3534bb791109065/prismor/runtime/policy_engine.py); [hooks.py](https://github.com/PrismorSec/prismor/blob/4cdcfb62197e01da280e21b3f3534bb791109065/prismor/runtime/hooks.py); [mcp-gateway.md](https://github.com/PrismorSec/prismor/blob/4cdcfb62197e01da280e21b3f3534bb791109065/docs/mcp-gateway.md)
- Basis: explicit + structural.
- Confidence: medium-high for installed model-backed guard mode.
- Caveats: The model check is optional / provider-dependent; the default heuristic-only mode is deterministic and should not be misreported as A. An LLM judge's text classification is a narrow S1 security operation, not autonomous coding. No model-backed live test was performed.

## S2 — Coordination

- State: ?
- Function: stabilize interference or oscillation *between distinct operational agent units*; no positive, specifically evidenced inter-S1 attenuation path was established.
- Disturbance / variety regulated: multiple agents might act on shared workspace files, tools or credentials, but a specific conflicting pair plus coordination return is not evidenced merely by per-agent IAM.
- Decisive decision or feedback right: Prismor can block per-identity actions under individual least-privilege rules; there is no established joint-activity interference decision or negotiation right.
- Decision owner: configured human/admin for IAM policy; deterministic engine for per-event enforcement. Distinct agent S2 coordinator unknown.
- Supporting / enforcement mechanisms: per-identity profiles, tool allow/deny restrictions, protected policy floor and MCP gateway event checks.
- Closure path: individual agent request → IAM/policy decision → allow/deny returns to that agent; an inter-agent conflict-specific regulation and return across two S1 units is unverified.
- Boundary reachability: IAM and gateway ship, but that does not by itself meet S2 function evidence.
- Why this is / is not agent-owned: security guardrails for each actor and global permissions are not automatically coordination between two operational actors.
- Distinct S1 units: multiple protected external agent instances can share a machine/project, but their common workspace alone is topology not a witness.
- Inter-S1 disturbance: potential competing writes/access to shared resources; no exact evidence tying an interference class to mutual adjustment rather than isolated policy screening.
- Attenuating coordination relation: per-agent security restrictions exist but a specific inter-S1 conflict-damping mechanism is unresolved.
- Feedback into subsequent S1 behaviour: each agent receives a local allow/deny; a coordination result feeding both S1s remains unestablished.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: not established; avoid treating IAM, static policy or enforcement coverage as S2 merely due to multiple agents.
- Evidence: [iam.py](https://github.com/PrismorSec/prismor/blob/4cdcfb62197e01da280e21b3f3534bb791109065/prismor/runtime/iam.py); [iam.md](https://github.com/PrismorSec/prismor/blob/4cdcfb62197e01da280e21b3f3534bb791109065/docs/iam.md); [mcp_gateway.py](https://github.com/PrismorSec/prismor/blob/4cdcfb62197e01da280e21b3f3534bb791109065/prismor/runtime/mcp_gateway.py); [policy_engine.py](https://github.com/PrismorSec/prismor/blob/4cdcfb62197e01da280e21b3f3534bb791109065/prismor/runtime/policy_engine.py); [mcp-gateway.md](https://github.com/PrismorSec/prismor/blob/4cdcfb62197e01da280e21b3f3534bb791109065/docs/mcp-gateway.md)
- Basis: structural + unresolved.
- Confidence: medium in insufficiency.
- Caveats: `?` is not a negative; targeted multi-agent disturbance proof could support S2 in a future assessment.

## S3 — Inside-and-now control

- State: ?
- Function: regulate aggregate current operational commitments and resources of a protected agent organization, beyond applying event-level safety policy.
- Disturbance / variety regulated: risky running sessions, blocked agent actions, resource/permission incidents and policy violations.
- Decisive decision or feedback right: operators can configure policies, pause enforcement and inspect events; no whole-current allocation / intervention authority with an evidenced portfolio view and return path was reconstructed.
- Decision owner: human/admin for individual policy/approval decisions; deterministic event path applies constraints. A legitimate whole-system S3 owner remains unproven.
- Supporting / enforcement mechanisms: agent inventory, per-session dashboard, approval paths, policy precedence, pause commands and telemetry.
- Closure path: individual event violation can be blocked/approved; there is no demonstrated separate whole-system S3 decision over shared commitments/priorities and feedback to multiple S1s.
- Boundary reachability: governance console and CLI are shipped; positive S3 cannot be inferred from their existence.
- Why this is / is not agent-owned: a policy classifier, static block rule and human step-up approval of a single action are not whole-current resource steering.
- Whole-system current view: inventory/dashboard may aggregate sessions but lacks documented whole-current commitment bargaining within this boundary.
- Current-control decision scope: observable per-session rights and aggregate security posture do not prove real system-wide current resource tradeoffs.
- Evidence: [README.md](https://github.com/PrismorSec/prismor/blob/4cdcfb62197e01da280e21b3f3534bb791109065/README.md); [policy_engine.py](https://github.com/PrismorSec/prismor/blob/4cdcfb62197e01da280e21b3f3534bb791109065/prismor/runtime/policy_engine.py); [modes.py](https://github.com/PrismorSec/prismor/blob/4cdcfb62197e01da280e21b3f3534bb791109065/prismor/runtime/modes.py); [dashboard.md](https://github.com/PrismorSec/prismor/blob/4cdcfb62197e01da280e21b3f3534bb791109065/docs/dashboard.md); [policy-layers-and-exemptions.md](https://github.com/PrismorSec/prismor/blob/4cdcfb62197e01da280e21b3f3534bb791109065/docs/policy-layers-and-exemptions.md)
- Basis: structural + unresolved.
- Confidence: medium in uncertainty.
- Caveats: no standalone P merely because an operator can approve a tool, edit policy or pause blocking.

## S3* — Complementary audit

- State: ?
- Function: independent complementary inquiry into underlying operational reality, challenging routine reports and returning a corrective decision.
- Disturbance / variety regulated: untruthful or incomplete activity claims and tampered evidence of agent behavior.
- Decisive decision or feedback right: signed audit data and generated attestations support downstream verification but do not themselves exercise an independent organizational audit judgment.
- Decision owner: independent qualified auditor and corrective decision loop not verified in a standard live distribution.
- Supporting / enforcement mechanisms: hash-chain signed trail, SIEM receipt exports, host discovery, attestation bundles and replayable event histories.
- Closure path: tamper-evident evidence may be exported/verified; a distinct independent sampled/probing verdict feeding corrective instructions to agents remains unproven.
- Boundary reachability: trail verification and attestation are shipped; merely being cryptographically independently checkable does not guarantee an enacted S3* organizational feedback loop.
- Why this is / is not agent-owned: cryptographic verification is a deterministic evidence-integrity check, not itself an independent AI audit reviewer.
- Claim being audited: an agent complied with configured security policy and its recorded actions match reality.
- Ordinary reporting path: session event logs, policy verdicts and dashboard summaries.
- Complementary access path: signed audit chain, receipts, host-discovery and attestation verification.
- Independence boundary: separate access is possible, but a live independent audit owner and corrective closure are not established.
- Who acts on findings: outside auditor/admin may act; no documented first-party automatic independent returned action established.
- Evidence: [audit.py](https://github.com/PrismorSec/prismor/blob/4cdcfb62197e01da280e21b3f3534bb791109065/prismor/runtime/audit.py); [attestation-bundle.md](https://github.com/PrismorSec/prismor/blob/4cdcfb62197e01da280e21b3f3534bb791109065/docs/attestation-bundle.md); [store.py](https://github.com/PrismorSec/prismor/blob/4cdcfb62197e01da280e21b3f3534bb791109065/prismor/runtime/store.py); [dashboard.md](https://github.com/PrismorSec/prismor/blob/4cdcfb62197e01da280e21b3f3534bb791109065/docs/dashboard.md)
- Basis: structural + unresolved.
- Confidence: medium in insufficient closure evidence.
- Caveats: S3* is not marked absent; audit trail may support later independent audit processes, but signing ≠ organizational audit.

## S4 — Outside-and-then intelligence

- State: P
- Function: adapt the security posture of later agent work to newly observed uncovered/evasive command patterns across runtime sessions.
- Disturbance / variety regulated: future exploitation or harmful action patterns not covered by the current rule set, learned from past operating-environment incidents and false positives.
- Decisive decision or feedback right: a legitimate human operator chooses whether a mined rule candidate should become a project policy rule; the program proposes/records but does not unilaterally choose and deploy a new rule.
- Decision owner: local project policy owner/operator acting in the supported `prismor learn --apply ID` mode. No independent autonomous S4 rule-promotion right is evidenced.
- Supporting / enforcement mechanisms: session event database, `mine_patterns` normalized pattern grouping and threshold, proposal confidence/support metadata, saved candidate queue and acceptance CLI, new YAML policy.
- Closure path: recent agent environment events populate `prismor.db` → learn identifies recurring uncovered sensitive commands and potential evasion → operator reviews prospective candidate → `learn --apply` writes project policy `.prismor/policy.yaml` → subsequent PolicyEngine loads that overlay and changes later agent action evaluation.
- Boundary reachability: learning analysis, candidate persistence, operator apply/reject CLI and policy-engine project overlay are all shipped paths, not development examples. Human decision participates within the first-party provided operating mode.
- Why this is / is not agent-owned: a deterministic miner scores prospective detections but cannot autonomously approve deployment; removal of the human leaves candidates only. Parent governance closes S4, not autonomous A.
- External distinction: uncaptured/evasive operations in the agent-facing environment reveal prospective security threats beyond the current rule repertoire.
- Future / prospective distinction: the choice is a revised future detector to govern later events, not simple historical log viewing or immediate incident intervention.
- Adaptation option generated: new learned rule for repeatedly uncovered sensitive command pattern or proposed refinement.
- Path back into current capability / S3: accepted rule in project policy alters the policy engine's later allow/warn/block findings; the accepted learned rules generally start as warn rules, not automatic block.
- Evidence: [learning.md](https://github.com/PrismorSec/prismor/blob/4cdcfb62197e01da280e21b3f3534bb791109065/docs/learning.md); [learning.py](https://github.com/PrismorSec/prismor/blob/4cdcfb62197e01da280e21b3f3534bb791109065/prismor/runtime/learning.py); [cli.py](https://github.com/PrismorSec/prismor/blob/4cdcfb62197e01da280e21b3f3534bb791109065/prismor/runtime/cli.py); [policy_engine.py](https://github.com/PrismorSec/prismor/blob/4cdcfb62197e01da280e21b3f3534bb791109065/prismor/runtime/policy_engine.py); [runtime.py](https://github.com/PrismorSec/prismor/blob/4cdcfb62197e01da280e21b3f3534bb791109065/prismor/runtime/runtime.py)
- Basis: explicit + structural.
- Confidence: medium for human-approved prospective security-rule update.
- Caveats: Not continuous automatic learning. This P is bounded to local policy-owner-approved rule adaptation; routine telemetry and history alone do not suffice. Future adaptation to model capabilities or enterprise strategy is not claimed.

## S5 — Policy and identity

- State: ?
- Function: settle the protected organization's constitutive purpose and ultimate legitimate policy, not just execute tool restrictions or user authorization.
- Disturbance / variety regulated: ultimate governance disputes about agent purpose, final organizational priorities or authority boundaries.
- Decisive decision or feedback right: org/project policies, IAM role creation, exemptions and signed security floors govern actions; a separate identity/ultimate-policy issue and deciding parent-return loop was not reconstructed.
- Decision owner: admins/operators choose configured permissions and compliance controls; S5-level ultimate organizational authority unresolved.
- Supporting / enforcement mechanisms: signed organization overlays, IAM, per-agent profiles, exceptions, admin approvals, authentication and non-overridable floor.
- Closure path: security policy/exemption decisions constrain tools, but no evidenced constitutive identity issue → legitimate ultimate decision → return shaping organizational purpose.
- Boundary reachability: real supported security administration paths are installed, but presence of rules and auth does not imply S5.
- Why this is / is not agent-owned: hardcoded safety floor and human access management cannot create autonomous S5 by themselves.
- Identity / ultimate-policy issue: not established beyond ordinary enforcement or rule acceptance.
- Ultimate authority in each claimed mode: none established for positive S5; human config owner is not automatically the ultimate recursion.
- Return-to-operation path: selected permissions return to tool checks, but ultimate identity/purpose closure was not proven.
- Evidence: [policy-layers-and-exemptions.md](https://github.com/PrismorSec/prismor/blob/4cdcfb62197e01da280e21b3f3534bb791109065/docs/policy-layers-and-exemptions.md); [policy_engine.py](https://github.com/PrismorSec/prismor/blob/4cdcfb62197e01da280e21b3f3534bb791109065/prismor/runtime/policy_engine.py); [iam.py](https://github.com/PrismorSec/prismor/blob/4cdcfb62197e01da280e21b3f3534bb791109065/prismor/runtime/iam.py); [iam.md](https://github.com/PrismorSec/prismor/blob/4cdcfb62197e01da280e21b3f3534bb791109065/docs/iam.md); [README.md](https://github.com/PrismorSec/prismor/blob/4cdcfb62197e01da280e21b3f3534bb791109065/README.md)
- Basis: structural + unresolved.
- Confidence: medium in insufficiency.
- Caveats: human approval to adapt future security rules belongs to the bounded S4 claim, not automatically S5.

## Distributed OSS parent arrangement

Individual developers/operators maintaining unrelated Prismor installations do not constitute one product-runtime parent organization. Enterprise admins may distribute signed rule overlays to managed devices, but those enforcement/configuration paths do not independently establish S3 or S5 at the local workspace recursion.

## Self-hosted and non-human modes

Prismor can secure external autonomous coding agents locally without a continuously present human for individual events, and configured model-assisted semantic guard may make independent security judgments. A distinct **human-approved** prospective S4 mode is supported through `learn --apply` and policy reload. No simultaneous S4=A mode is claimed: automatic detection does not autonomously promote learned rules.

## Recursion

The assessed security boundary surrounds one project's agent-facing runtime operation, not every higher-level organization whose policies it may receive. Agent actors' native reasoning remains an adjacent substrate, while Prismor's own security decision and adaptive policy surface is the reviewed first-party organization.

## Variety and escalation

Heuristics and model-assisted guard absorb diverse local security input; deterministic engine/IAM/deny-wins policy attenuates forbidden actions; operator is asked to approve exceptions and may accept future detection-rule options. Audit chains preserve evidence for independent consumers without implying an enacted S3* reviewer. Signed remote policy is an external organizational input, not a self-evident S5 policy-identity owner.

## Evidence gaps

- Verify an installed external coding-agent/hook and model-backed semantic guard end-to-end to measure S1 A judgment reachability; this assessment reviews pinned source/config and supported deployment wiring, not a provider-backed run.
- Confirm any actual cross-S1 collision regulation, beyond ordinary per-actor least privilege, before upgrading S2 from `?`.
- Establish a true whole-current portfolio authority or independent corrective audit pathway before upgrading S3 or S3*.
- S4=P is narrowly anchored to learned rule candidate → named operator acceptance → later policy application; no autonomous learning-policy promotion or strategic organizational foresight is asserted.
- Do not infer S5 from signed rule floors, identity credentials or human admin consoles absent a concrete identity/ultimate-policy issue and authoritative returned closure.
