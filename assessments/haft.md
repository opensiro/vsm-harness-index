---
harness_id: haft
project_name: Haft
repository: https://github.com/m0n0x41d/haft
review_ref: 8a5f0384a10003bda7b2b65edc86f0f1a656a345
reviewed_at: 2026-10-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-04
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Haft

## Review boundary

- System in focus: Haft's shipped project-governance organization at frozen revision `8a5f0384a10003bda7b2b65edc86f0f1a656a345`: first-party host skills/procedures, MCP/CLI kernel, typed project artifact graph, code/project-memory reads, evidence/drift lifecycle and explicit authority gates.
- Purpose and identity: help AI-assisted engineering reason from versioned FPF source, persist reliance-bearing project memory, verify governed claims against reality, and keep binding project choices/execution authority with the human principal.
- Relevant environment: operator requests, repository/code state, external evidence/tests/metrics, current project records, supported coding-agent hosts, FPF source and artifact freshness/drift.
- Standard-distribution boundary: Haft skills, generated host carriers, MCP/CLI kernel and project ledger are inside. Claude Code/Codex/Grok/Hermes/Pi/etc. host implementations are external execution/inference dependencies; Haft receives credit only where its distributed skill/procedure plus kernel closes the organizational path. Separately operated runners executing WorkCommissions remain external.
- Credited operating / distribution surfaces: `README.md`; `internal/cli/skill/h-{reason,frame,explore,compare,decide,verify,commission}/SKILL.md`; Pi-adapted shipped skills; artifact/authority/refresh/query kernel surfaces; project ledger and typed-memory projections.
- Adjacent first-party surfaces excluded from ownership: repository-development CI/release/FPF-refresh maintenance; tests/fixtures; removed pre-v9 built-in executors; separately operated external runners; host-agent internals not supplied by Haft.
- First-party operating / deployment modes considered: installed Claude/Codex stable host integration; generic MCP host use; h-reason/frame/explore/compare; host-routed h-decide; h-verify; read-only h-status; manual h-commission authority grant.
- Recursion level: one Haft-governed engineering project is the focal organization. Agentic governance/reasoning work performed through shipped Haft skills is operational S1. The human principal is the parent authority for binding current choices/execution mandates.
- Reviewed revision: `8a5f0384a10003bda7b2b65edc86f0f1a656a345`.
- Observation date: 2026-10-04.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Haft v9 deliberately has no built-in coding-agent executor. Instead it publishes first-party skills into supported hosts and exposes a local kernel over MCP/CLI. The skills carry the reasoning procedure and define when/how to query FPF, frame problems, explore/compare alternatives, persist project records and verify decisions; the kernel validates typed artifacts, evidence, parity and authority boundaries and commits the resulting project graph.

This is not merely generic MCP storage. For example, `h-reason` explicitly reconstructs the current engineering concern, selects applicable source material, invokes only the capability currently justified, may autonomously establish minimum durable memory when a concrete receiving use exists, and routes resulting records through first-party Haft tools. The host model supplies inference, while Haft owns the role/procedure and durable feedback path.

Binding choice is intentionally parent-governed. `h-decide` may prepare/route a direct unambiguous operator request, but model-supplied arguments are not authority. The human principal's direct request is bound as a DecisionRecord and later governs downstream commissions, verification and code-context reads. WorkCommission creation is even stricter: `h-commission` is manual-only, creates bounded execution authority, and stops before external execution.

## Operational model

A supported host agent receives a Haft skill when the current engineering concern matches it. The skill reads project/source context, exercises model-backed judgment under Haft's procedure and uses Haft MCP/CLI sinks to create or update project artifacts when the receiving-use contract warrants persistence. Binding choices pause at the human authority boundary; the returned human decision is stored and thereafter constrains/recontextualizes subsequent agent work. Verification later gathers evidence from current reality and records a verdict against the earlier decision.

## S1 — Operations

- State: A
- Function: perform FPF-aware project-governance reasoning such as framing a current problem, exploring/comparing alternatives, recording warranted project memory, or checking a governed concern through a shipped Haft capability.
- Disturbance / variety regulated: ambiguous engineering questions, alternative sets, code/project context, source-pattern applicability, evidence/freshness state and reliance requirements requiring contextual rather than fixed decisions.
- Decisive decision or feedback right: the model-backed Haft role decides which evidence/source distinctions are relevant, which current capability applies, what bounded result follows and what minimum non-binding record should be produced when the skill's persistence contract is satisfied.
- Decision owner: the host model executing Haft's first-party distributed skill/procedure.
- Supporting / enforcement mechanisms: generated skills/instruction carriers; MCP tools; artifact graph; project ledger; FPF source/query; typed memory; kernel validators and structured errors.
- Closure path: operator/current project concern → first-party Haft skill is invoked → model-backed role reads source/project evidence and performs the skill procedure → Haft tool/kernel validates and, where justified, persists the result → later project reads/reasoning consume that returned artifact/state.
- Boundary reachability: stable Claude/Codex integrations install the actual Haft skills and MCP server into supported hosts; the procedure and artifact-return path are shipped by Haft rather than authored downstream.
- Why this is / is not agent-owned: removing the host model while retaining the kernel leaves validation/storage but removes the contextual reasoning that selects/applies source and constructs the project result. Removing Haft while retaining the host removes the specific role/procedure and project-governance closure being assessed.
- Evidence: [`README.md`](https://github.com/m0n0x41d/haft/blob/8a5f0384a10003bda7b2b65edc86f0f1a656a345/README.md); [`internal/cli/skill/h-reason/SKILL.md`](https://github.com/m0n0x41d/haft/blob/8a5f0384a10003bda7b2b65edc86f0f1a656a345/internal/cli/skill/h-reason/SKILL.md); [`internal/cli/skill/h-frame/SKILL.md`](https://github.com/m0n0x41d/haft/blob/8a5f0384a10003bda7b2b65edc86f0f1a656a345/internal/cli/skill/h-frame/SKILL.md); [`internal/cli/skill/h-compare/SKILL.md`](https://github.com/m0n0x41d/haft/blob/8a5f0384a10003bda7b2b65edc86f0f1a656a345/internal/cli/skill/h-compare/SKILL.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: Haft is not credited with semantic coding execution performed by external coding agents/runners; S1 here is the first-party governance/reasoning operation that Haft intentionally supplies.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 coordination function was established.
- Disturbance / variety regulated: multiple hosts/sessions may share one project ledger, but no standard Haft path was found in which distinct same-recursion S1 units create an interaction conflict/oscillation and an autonomous Haft coordinator chooses a response.
- Decisive decision or feedback right: not established at S2.
- Decision owner: not established as a first-party S2 owner.
- Supporting / enforcement mechanisms: checked project ledger; authority records; artifact graph; host parity; code/project-memory reads; commissions.
- Closure path: deterministic consistency/authority checks can constrain several host sessions, but no inter-S1 coordination judgment loop was found.
- Why this is / is not agent-owned: shared records and concurrency-safe persistence do not themselves establish S2.
- Evidence: [`README.md`](https://github.com/m0n0x41d/haft/blob/8a5f0384a10003bda7b2b65edc86f0f1a656a345/README.md); [`internal/cli/skill/h-reason/SKILL.md`](https://github.com/m0n0x41d/haft/blob/8a5f0384a10003bda7b2b65edc86f0f1a656a345/internal/cli/skill/h-reason/SKILL.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: an external engineering organization can coordinate multiple agents through Haft records, but its coordinator is outside this boundary.

### Absence scope

- Surfaces inspected: host integrations; shared ledger/memory; authority graph; skills; commissions; status/coverage/drift interfaces.
- Plausible first-party paths checked: multi-host shared memory, commission concurrency, code-graph indexing, artifact reconciliation and host parity.
- Why no material first-party path remains: located mechanisms synchronize or constrain shared state but do not establish an autonomous function-specific response to a concrete cross-S1 interference.

## S3 — Inside-and-now control

- State: P
- Function: maintain a project-wide current governance view and close binding choices/execution-authority changes through the legitimate human principal.
- Disturbance / variety regulated: active/superseded/stale decisions, unresolved project problems, drift/evidence debt, specification gates, open commissions and current operations that would otherwise rely on ambiguous or unauthorized commitments.
- Decisive decision or feedback right: bind or supersede a current project choice, grant/narrow/decline a bounded WorkCommission, or resolve a material human gate before the affected operation proceeds.
- Decision owner: the human principal/operator in the parent-governed mode.
- Supporting / enforcement mechanisms: `h-status` project cockpit; Human Gate Brief contract; host-routed `h-decide`; DecisionRecords; manual `h-commission`; authority provenance; project/kernel gates.
- Closure path: Haft exposes current project decision/drift/commission/spec state → a skill presents the exact current gate/options when a binding choice is required → human principal makes the authoritative choice → supported host route or manual commission path binds it → DecisionRecord/WorkCommission becomes governing project state read/enforced by later Haft operations.
- Boundary reachability: the status/gate/decision/commission paths are shipped host integration and kernel contracts; the parent does not need to build a separate governance database or effect sink.
- Why this is / is not agent-owned: agents may analyze options and recommend, but Haft explicitly rejects model-supplied authority and retains the decisive current-control right at the human principal; therefore the published state is `P`, not `A`.
- Evidence: [`README.md`](https://github.com/m0n0x41d/haft/blob/8a5f0384a10003bda7b2b65edc86f0f1a656a345/README.md); [`packages/haft-pi/skills/h-status/SKILL.md`](https://github.com/m0n0x41d/haft/blob/8a5f0384a10003bda7b2b65edc86f0f1a656a345/packages/haft-pi/skills/h-status/SKILL.md); [`internal/cli/skill/h-decide/SKILL.md`](https://github.com/m0n0x41d/haft/blob/8a5f0384a10003bda7b2b65edc86f0f1a656a345/internal/cli/skill/h-decide/SKILL.md); [`internal/cli/skill/h-commission/SKILL.md`](https://github.com/m0n0x41d/haft/blob/8a5f0384a10003bda7b2b65edc86f0f1a656a345/internal/cli/skill/h-commission/SKILL.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: not every DecisionRecord is a whole-system intervention. The positive witness is the project cockpit + explicit material gate/authority path that governs whether affected current operation may proceed.
- Whole-system current view: compact project status spans active problems/decisions/notes, evidence freshness/drift, commissions, spec lifecycle, coverage and current authority surfaces.
- Current-control decision scope: binding current project choices and bounded execution authority at material gates, including whether affected work may proceed and under what scope/evidence envelope.

## S3* — Complementary audit

- State: A
- Function: independently challenge a recorded decision/claim against current operational reality and feed the verdict back into its lifecycle.
- Disturbance / variety regulated: a previously bound decision may have drifted, evidence may have decayed, predictions may fail, or current tests/metrics/logs/code may contradict the recorded claim.
- Decisive decision or feedback right: the model-backed `h-verify` role chooses and executes discriminating evidence probes, interprets them against declared observables/thresholds, and records an evidence-backed accepted/partial/failed measurement verdict.
- Decision owner: the autonomous host model executing Haft's first-party `h-verify` procedure.
- Supporting / enforcement mechanisms: exact DecisionRecord recovery; baselines; affected-file drift; Bash/Read/Grep/Glob probes; evidence carriers; congruence/evidence expiry fields; kernel requirement that evidence precede measure.
- Closure path: recorded decision/predictions → h-verify recovers exact claim/baseline → role gathers current tests/metrics/log/code evidence → attaches evidence and measurement verdict → lifecycle/drift state changes and subsequent reliance, reopen/supersede/hold decisions consume that audit result.
- Boundary reachability: `h-verify` is shipped in the stable host integration and uses first-party kernel evidence/measure/refresh surfaces.
- Why this is / is not agent-owned: deterministic drift and evidence gates support the audit, but the semantic selection/interpretation of real-world probes and verdict is assigned to the model-backed verification role.
- Evidence: [`internal/cli/skill/h-verify/SKILL.md`](https://github.com/m0n0x41d/haft/blob/8a5f0384a10003bda7b2b65edc86f0f1a656a345/internal/cli/skill/h-verify/SKILL.md); [`README.md`](https://github.com/m0n0x41d/haft/blob/8a5f0384a10003bda7b2b65edc86f0f1a656a345/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: deterministic stale/drift flags alone would be observability; S3* is credited to the separate evidence-against-reality verification procedure and returned verdict.
- Claim being audited: a bound DecisionRecord's declared claims/predictions and continued validity in the current project.
- Ordinary reporting path: DecisionRecord, affected-file baseline, implementation/project state and the original rationale/predictions.
- Complementary access path: h-verify performs current tests, metrics, log scans and code probes, attaches external/current evidence and checks drift/freshness against the recorded claim.
- Independence boundary: verification uses current reality/evidence rather than accepting the decision's own rationale or status; kernel enforces evidence-before-verdict and preserves the historical claim.
- Who acts on findings: subsequent agent work and the human principal consume accepted/partial/failed, drift and freshness results; material reopen/supersede/waiver choices remain parent-governed.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party runtime loop was established that senses external/future change, develops project adaptation options and returns a selected adaptation into current capability.
- Disturbance / variety regulated: evidence expiry, code drift and project-memory change are mainly internal/current governance signals; FPF upstream refresh is repository/product maintenance rather than the assessed project runtime.
- Decisive decision or feedback right: not established at S4.
- Decision owner: not established.
- Supporting / enforcement mechanisms: evidence decay; drift events; source query; FPF refresh tooling; project-memory reconciliation.
- Closure path: not applicable at S4.
- Why this is / is not agent-owned: learning/memory/staleness and source-refresh maintenance do not by themselves constitute external-and-prospective organizational intelligence.
- Evidence: [`README.md`](https://github.com/m0n0x41d/haft/blob/8a5f0384a10003bda7b2b65edc86f0f1a656a345/README.md); [`packages/haft-pi/skills/h-status/SKILL.md`](https://github.com/m0n0x41d/haft/blob/8a5f0384a10003bda7b2b65edc86f0f1a656a345/packages/haft-pi/skills/h-status/SKILL.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: a host agent can use Haft to reason about future/external concerns, but generic reasoning capability is not a shipped autonomous S4 loop.

### Absence scope

- Surfaces inspected: evidence decay/drift/reconciliation, project memory, FPF source/query/refresh, status, spec lifecycle and host skills.
- Plausible first-party paths checked: source refresh, stale-decision review, typed-memory update, code drift, future project reasoning.
- Why no material first-party path remains: inspected runtime paths react to current/internal project evidence or provide general reasoning; no autonomous outside-environment model develops durable adaptation options and closes them into present S3.

## S5 — Policy and identity

- State: —
- Function: explicit human authority and policy boundaries are strong, but no dedicated identity/ultimate-policy closure for the project organization was established.
- Disturbance / variety regulated: binding decisions and WorkCommissions may be highly consequential, yet they remain bounded project choices/authority grants rather than necessarily identity-level disputes.
- Decisive decision or feedback right: no first-party identity/ultimate-policy issue → legitimate ultimate authority → governing return loop was established.
- Decision owner: not established at S5.
- Supporting / enforcement mechanisms: human-authority provenance, DecisionRecords, WorkCommissions, spec lifecycle gates and kernel authority checks.
- Closure path: not applicable at S5.
- Why this is / is not agent-owned: preserving the human principal's authority does not automatically turn every human decision into S5.
- Evidence: [`internal/cli/skill/h-decide/SKILL.md`](https://github.com/m0n0x41d/haft/blob/8a5f0384a10003bda7b2b65edc86f0f1a656a345/internal/cli/skill/h-decide/SKILL.md); [`internal/cli/skill/h-commission/SKILL.md`](https://github.com/m0n0x41d/haft/blob/8a5f0384a10003bda7b2b65edc86f0f1a656a345/internal/cli/skill/h-commission/SKILL.md); [`README.md`](https://github.com/m0n0x41d/haft/blob/8a5f0384a10003bda7b2b65edc86f0f1a656a345/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: a particular downstream organization might use Haft DecisionRecords for identity policy; that use is not a standard first-party S5 function by itself.

### Absence scope

- Surfaces inspected: authority model, h-decide, h-commission, specs, governance mode, human gates and project identity/profile records.
- Plausible first-party paths checked: binding DecisionRecords, commission grants, profile changes, spec lifecycle gates and human-principal constraints.
- Why no material first-party path remains: these mechanisms establish authority provenance and bounded choices; none specifically reconstructs an identity/ultimate-policy tension and return-to-operation loop at the assessed project recursion.

## Recursion

The focal organization is one Haft-governed engineering project. Model-backed Haft skills perform governance/reasoning operations inside supported host agents. The human principal remains the parent authority for material binding choices and execution mandates. External coding runners are not absorbed into the boundary.

## Variety and escalation

Haft amplifies reasoning variety through FPF-aware model roles and project/code memory while attenuating unsafe governance variety with typed artifacts, parity/evidence gates and explicit authority provenance. Material binding questions escalate to the human principal. Later verification can challenge recorded claims with fresh evidence before subsequent work relies on them.

## Evidence gaps

No evidence gap requires `?`. The main boundary is deliberate: Haft's first-party distributed skills are credited where they define and close a governance role through Haft's kernel, while generic host-agent coding behavior and external runners remain outside.

**Vector:** A · — · P · A · — · —
