---
harness_id: dashclaw
project_name: DashClaw
repository: https://github.com/ucsandman/DashClaw
review_ref: c6754674f98b73bba73046687c683e9bf685851c
reviewed_at: 2026-10-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-04
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: C
autonomy_s3_star: —
autonomy_s4: C(P)
autonomy_s5: —
---

# DashClaw

## Review boundary

- System in focus: the first-party DashClaw governance runtime at frozen revision `c6754674f98b73bba73046687c683e9bf685851c`, including the guard/risk engine, supported enforcement hooks and governed execution seams, approvals/grants, active-plan/deviation control, predictive-risk model path, calibration controller, policy-tuning proposals, audit/evidence persistence, enforcement-liveness probe and posture findings.
- Purpose and identity: place an enforceable governance layer between autonomous agents and consequential actions, preserving policy, approval, evidence and execution claims while adapting interruption posture from observed outcomes.
- Relevant environment: proposed agent actions, executable acts and derived evidence, agent/action history, active plans, policy state, approvals/denials, operator judgments, external verdict providers, hook/runtime health and enforcement-seam failures.
- Standard-distribution boundary: DashClaw server/API, guard/risk/policy runtime, first-party hooks/plugins, SDK/MCP governance paths, approval/calibration/tuning surfaces and liveness probes are inside. Claude Code, Codex, OpenClaw, Hermes and other protected agent reasoning loops are external; development/dogfood agents under `.claude/` and `.agents/` are adjacent and are not credited.
- Credited operating / distribution surfaces: `app/lib/guard/*`; `app/lib/predictive-risk.ts`; `app/lib/policy-tuning/engine.ts`; `app/api/policies/proposals/route.ts`; `app/api/approvals/[actionId]/route.ts`; `hooks/enforcement_liveness_probe.py`; `app/lib/enforcement-liveness.ts`; supported hook/plugin execution seams.
- Adjacent first-party surfaces excluded from ownership: maintainer/development agents; planning/spec documents where not wired; tests/benchmarks; marketing/demo fixtures; protected-agent reasoning; external policy providers; operator UI where it only displays state.
- First-party operating / deployment modes considered: guard API and record/claim path; mechanical pre-tool enforcement hooks; optional predictive-risk LLM; active/relief calibration controller; plan authorization/deviation control; human approvals; policy-tuning proposal/apply flow; enforcement-liveness probes.
- Recursion level: one DashClaw-governed agent/session organization. Individual governance verdicts are S1 operations; the active plan/current governance envelope is the current S3 control level; calibration and tuning alter future governance capability.
- Reviewed revision: `c6754674f98b73bba73046687c683e9bf685851c`.
- Observation date: 2026-10-04.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

DashClaw's guard path evaluates a proposed action against server-derived evidence, policy, predictive history, external verdicts, approvals/grants, calibration and plan-deviation checks, then persists an auditable decision and can close it into mechanical hook enforcement. The decision lattice is tighten-only up to an absolute block, with explicit bounded downgrades for authorized grants/calibration.

The optional predictive-risk lane is model-backed. For sufficiently high server-side risk with history available, DashClaw sends recent executed behavior for the same agent/action type to a configured model. The model returns a bounded `-20..+20` risk adjustment and reasoning; that adjustment is folded into the guard score before policy evaluation and can therefore change whether a current action is interrupted.

DashClaw also contains a closed learning/control path. Human allow/deny resolutions are ingested as calibration labels. A deterministic controller updates the persisted interruption threshold and per-agent evidence state; active/relief mode uses that state on later guard calls to raise or relieve `require_approval`. Separately, the policy-tuning engine derives evidence-backed future policy changes from observed interruption/approval outcomes, but deliberately does not auto-apply them: an admin applies the proposed patch through the policy route.

Primary evidence:

- [`app/lib/guard/evaluate.ts`](https://github.com/ucsandman/DashClaw/blob/c6754674f98b73bba73046687c683e9bf685851c/app/lib/guard/evaluate.ts)
- [`app/lib/guard/evaluate.checks.ts`](https://github.com/ucsandman/DashClaw/blob/c6754674f98b73bba73046687c683e9bf685851c/app/lib/guard/evaluate.checks.ts)
- [`app/lib/predictive-risk.ts`](https://github.com/ucsandman/DashClaw/blob/c6754674f98b73bba73046687c683e9bf685851c/app/lib/predictive-risk.ts)
- [`app/lib/guard/calibration.ts`](https://github.com/ucsandman/DashClaw/blob/c6754674f98b73bba73046687c683e9bf685851c/app/lib/guard/calibration.ts)
- [`app/lib/guard/calibration-feedback.ts`](https://github.com/ucsandman/DashClaw/blob/c6754674f98b73bba73046687c683e9bf685851c/app/lib/guard/calibration-feedback.ts)
- [`app/lib/policy-tuning/engine.ts`](https://github.com/ucsandman/DashClaw/blob/c6754674f98b73bba73046687c683e9bf685851c/app/lib/policy-tuning/engine.ts)
- [`app/api/policies/proposals/route.ts`](https://github.com/ucsandman/DashClaw/blob/c6754674f98b73bba73046687c683e9bf685851c/app/api/policies/proposals/route.ts)
- [`hooks/enforcement_liveness_probe.py`](https://github.com/ucsandman/DashClaw/blob/c6754674f98b73bba73046687c683e9bf685851c/hooks/enforcement_liveness_probe.py)

## Operational model

A protected agent submits an action plus executable evidence through a supported DashClaw seam. The server derives risk/evidence, optionally applies a model-backed predictive adjustment, evaluates policy and current plan/deviation state, and returns/persists an enforceable verdict. A `require_approval` can be resolved by an attributable human principal and retried/claimed through the governed path. Those adjudications feed the persistent calibration controller used by future decisions.

## S1 — Operations

- State: A
- Function: make a context-sensitive governance/risk judgment for a proposed agent action and close it into an enforceable allow/warn/approval/block outcome.
- Disturbance / variety regulated: heterogeneous action risk, executed-behavior history, evidence/declared-intent mismatch, prompt injection, protected paths, spend/data/system impact, external verdicts and ambiguous high-stakes actions that deterministic policy alone may not distinguish well.
- Decisive decision or feedback right: in predictive-risk mode, interpret recent executed behavior for the current agent/action type and choose a bounded semantic risk adjustment that can change the guard's final intervention.
- Decision owner: the model-backed predictive-risk role in the supported opt-in mode; deterministic guard/policy machinery combines and enforces its result.
- Supporting / enforcement mechanisms: server risk/evidence classification; local policies; predictive statistics; external verdict phase; grants; approvals; hook/plugin seams; action/decision persistence; execution claims.
- Closure path: proposed action → server evidence/risk + optional model assessment → adjusted risk and policy evaluation → final guard verdict → mechanical hook/governed-execution seam allows, interrupts or blocks → outcome/decision is recorded.
- Boundary reachability: predictive-risk execution is called directly from the production `evaluateGuard` path when enabled and sufficiently high-risk; supported hooks and governed execution paths consume the resulting guard decision.
- Why this is / is not agent-owned: removing the model leaves deterministic/statistical governance but removes the semantic interpretation of executed history that can move the current risk score and therefore the intervention. The autonomous role owns real operational discretion in this mode.
- Evidence: [`app/lib/predictive-risk.ts`](https://github.com/ucsandman/DashClaw/blob/c6754674f98b73bba73046687c683e9bf685851c/app/lib/predictive-risk.ts); [`app/lib/guard/evaluate.external.ts`](https://github.com/ucsandman/DashClaw/blob/c6754674f98b73bba73046687c683e9bf685851c/app/lib/guard/evaluate.external.ts); [`app/lib/guard/evaluate.ts`](https://github.com/ucsandman/DashClaw/blob/c6754674f98b73bba73046687c683e9bf685851c/app/lib/guard/evaluate.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the model lane is opt-in and budget/deadline bounded; the published state reflects a supported first-party mode, not every deployment. Protected-agent task reasoning is outside the boundary.

## S2 — Coordination

- State: —
- Function: no material same-recursion inter-S1 coordination function was established.
- Disturbance / variety regulated: multiple agents, policies and fleet records can coexist, but the runtime evidence reviewed does not establish distinct first-party autonomous S1 units whose interaction creates a specific conflict or oscillation addressed by a DashClaw coordination relation.
- Decisive decision or feedback right: not established at S2.
- Decision owner: not established as a first-party S2 owner.
- Supporting / enforcement mechanisms: agent identity/fleet attribution; scoped policies; plans; queues; grants; separation-of-duties rules; shared decision/action stores.
- Closure path: these mechanisms govern individual/fleet actions but no specific inter-S1 disturbance→coordination choice→changed S1 behavior loop was established.
- Why this is / is not agent-owned: fleet visibility, routing, shared state and separation rules are insufficient without the required interference witness.
- Evidence: [`app/lib/guard/evaluate.ts`](https://github.com/ucsandman/DashClaw/blob/c6754674f98b73bba73046687c683e9bf685851c/app/lib/guard/evaluate.ts); [`README.md`](https://github.com/ucsandman/DashClaw/blob/c6754674f98b73bba73046687c683e9bf685851c/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: downstream organizations can use DashClaw to govern multiple agents; their coordination topology is not automatically DashClaw S2.

### Absence scope

- Surfaces inspected: fleet/agent identity, policies, plans, approvals, grants, guard evaluation, workflows and supported hooks.
- Plausible first-party paths checked: multi-agent policy scoping; plan ownership; fleet controls; approval separation of duties; shared budgets and interruption limits.
- Why no material first-party path remains: no concrete same-recursion S1 interference relation plus S2-specific feedback loop was found.

## S3 — Inside-and-now control

- State: C
- Function: regulate the current governed agent/session against its active operating envelope, including current plan, org halt/pause state, grants and deviation policy.
- Disturbance / variety regulated: current actions can deviate from an authorized live plan, cross active organizational constraints, exhaust interruption/approval allowances, or occur while the organization is halted/paused.
- Decisive decision or feedback right: deterministically compare the next action with current live-plan/current-governance state and raise, preserve or relieve the current intervention before execution.
- Decision owner: first-party constructor/runtime logic; no autonomous supervisory model is required for the S3 path itself.
- Supporting / enforcement mechanisms: live-plan lookup and plan-step grants; deviation classifier/response policy; org halt; approval pause; interruption budget; operator grants; action/execution claims; hook enforcement.
- Closure path: current plan/governance state + proposed action → deterministic current-control checks/deviation classification → warn/require-approval/block or bounded relief → governed execution seam changes the next operation → action/decision state feeds later current checks.
- Boundary reachability: the plan/deviation and current-governance passes execute inside the shipped guard hot path and their verdict changes are returned through supported enforcement seams.
- Why this is / is not agent-owned: removing the optional model leaves materially the same plan-conformance/current-control transition. The S3 organizational discretion is therefore constructor-owned rather than autonomous-agent-owned.
- Evidence: [`app/lib/guard/evaluate.ts`](https://github.com/ucsandman/DashClaw/blob/c6754674f98b73bba73046687c683e9bf685851c/app/lib/guard/evaluate.ts); [`app/lib/guard/evaluate.checks.ts`](https://github.com/ucsandman/DashClaw/blob/c6754674f98b73bba73046687c683e9bf685851c/app/lib/guard/evaluate.checks.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: an isolated human approval is not separately promoted to parent S3; the positive witness is the shipped whole-current-envelope controller.
- Whole-system current view: current org halt/pause and policy/grant state, the agent's current live plan/authorized steps, the proposed action and current deviation/risk evidence.
- Current-control decision scope: whether the next current operation remains inside the active plan/governance envelope or must be interrupted/blocked/reviewed before proceeding.

## S3* — Complementary audit

- State: —
- Function: an independent enforcement-liveness probe supplies complementary reality access, but its finding does not itself close a first-party audit-judgment→current-control loop.
- Disturbance / variety regulated: the decision ledger can claim blocks while a broken hook seam actually lets actions execute; the probe independently tests the installed seam by attempting a synthetic held action and observing whether a witness file exists.
- Decisive decision or feedback right: not established as a closed audit decision that automatically or authoritatively changes subsequent current governance.
- Decision owner: probe verdict is deterministic and first-party; remediation/control choice remains with an operator or subsequent external workflow.
- Supporting / enforcement mechanisms: `enforcement_liveness_probe.py`; per-seam liveness records; posture findings; setup/coverage surfaces; live canary and silent-lane witnesses.
- Closure path: independent synthetic action → real hook seam → witness observation → held/executed/unprovable record → posture finding; the standard path stops at surfacing/remediation guidance rather than feeding the finding directly into current guard authority.
- Why this is / is not agent-owned: the alternative access is unusually strong, but Methodology requires findings to inform subsequent control through a closed path; evidence display alone remains insufficient.
- Evidence: [`hooks/enforcement_liveness_probe.py`](https://github.com/ucsandman/DashClaw/blob/c6754674f98b73bba73046687c683e9bf685851c/hooks/enforcement_liveness_probe.py); [`app/lib/enforcement-liveness.ts`](https://github.com/ucsandman/DashClaw/blob/c6754674f98b73bba73046687c683e9bf685851c/app/lib/enforcement-liveness.ts); [`app/lib/posture/findings.ts`](https://github.com/ucsandman/DashClaw/blob/c6754674f98b73bba73046687c683e9bf685851c/app/lib/posture/findings.ts).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: an operator can act on the finding, but that manual follow-up is not a standard closed S3* ownership mode here.

### Absence scope

- Surfaces inspected: enforcement-liveness probe, live canary, silent-lane witness, audit/decision evidence, replay/posture findings and remediation surfaces.
- Plausible first-party paths checked: probe failure→automatic halt; liveness finding→guard escalation; canary failure→policy change; replay discrepancy→current block.
- Why no material first-party path remains: complementary evidence is produced and surfaced, but a distinct closed feedback transition from that audit finding into subsequent current control was not established.

## S4 — Outside-and-then intelligence

- State: C(P)
- Function: adapt future interruption/governance capability from observed operator outcomes and longer-window policy performance.
- Disturbance / variety regulated: systematic false interruptions, dangerous misses, persistent agent denial patterns, policies that humans repeatedly override, ineffective/dead policy rules and changing observed governance needs.
- Decisive decision or feedback right: in the base mode, deterministically update the persistent calibrated interruption threshold/evidence state from human adjudications; in the parent mode, decide whether an evidence-backed policy-tuning proposal should be applied to future policy.
- Decision owner: base mode is first-party constructor/controller logic; parent mode is an attributable human admin applying the proposed policy patch.
- Supporting / enforcement mechanisms: calibration-state store and CAS; approval/miss/review label ingestion; calibrated controller; tuning statistics/proposals; policy PATCH route; evidence windows and proposal fingerprints.
- Closure path: external operator judgment/outcome history → persisted calibration/tuning evidence → threshold or policy adaptation option → calibrated controller/policy store changes → subsequent guard decisions use the changed capability.
- Boundary reachability: approval resolution directly feeds calibration ingestion and later guard evaluation reads that state; policy proposals are generated by shipped server routes and applied through the first-party admin policy path.
- Why this is / is not agent-owned: neither adaptation mode requires autonomous model judgment. The automatic base path is deterministic constructor-owned; the distinct policy-change path deliberately reserves the decisive adaptation decision to a parent human.
- Evidence: [`app/lib/guard/calibration-feedback.ts`](https://github.com/ucsandman/DashClaw/blob/c6754674f98b73bba73046687c683e9bf685851c/app/lib/guard/calibration-feedback.ts); [`app/lib/guard/calibration.ts`](https://github.com/ucsandman/DashClaw/blob/c6754674f98b73bba73046687c683e9bf685851c/app/lib/guard/calibration.ts); [`app/lib/guard/evaluate.checks.ts`](https://github.com/ucsandman/DashClaw/blob/c6754674f98b73bba73046687c683e9bf685851c/app/lib/guard/evaluate.checks.ts); [`app/lib/policy-tuning/engine.ts`](https://github.com/ucsandman/DashClaw/blob/c6754674f98b73bba73046687c683e9bf685851c/app/lib/policy-tuning/engine.ts); [`app/api/policies/proposals/route.ts`](https://github.com/ucsandman/DashClaw/blob/c6754674f98b73bba73046687c683e9bf685851c/app/api/policies/proposals/route.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: generic feedback storage is not credited; the positive witness is the durable future-facing threshold/policy change that returns into later governance.
- External distinction: human allow/deny/miss judgments and observed policy interruption outcomes distinguish where the deployed governance posture mismatches the operator/environment.
- Future / prospective distinction: the calibration threshold and tuning proposal govern later actions, not merely the adjudicated episode.
- Adaptation option generated: a revised calibrated threshold/evidence state in base mode; evidence-backed `raise_risk_threshold`/keep/dead-policy proposals in parent mode.
- Path back into current capability / S3: calibration state is read by `runCalibrationController` on later guard calls; accepted policy proposal patches alter the policy set read by later current-control decisions.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | deterministic calibration controller | resolved human adjudication / reviewed miss or warn supplies an external label | persisted threshold/e-process state → later `runCalibrationController` raises or relieves interruptions | `calibration-feedback.ts`, `calibration.ts`, `evaluate.checks.ts` |
| Parent (`P`) | attributable human admin | evidence-backed policy-tuning proposal from longer-window interruption/approval outcomes | admin applies the proposal through policy update → later guard calls load the changed policy | `policy-tuning/engine.ts`, `/api/policies/proposals`, policy admin route |

## S5 — Policy and identity

- State: —
- Function: no material identity/ultimate-policy closure is established in the runtime boundary.
- Disturbance / variety regulated: policies, grants, approvals, risk posture and human ratification constrain operational governance, but they concern ordinary action/policy tuning rather than organizational identity or supreme policy.
- Decisive decision or feedback right: not established for an identity-level dispute at the assessed recursion.
- Decision owner: operator/admin for ordinary policy; runtime enforces returned constraints.
- Supporting / enforcement mechanisms: guard policies; human approvals; grants; admin roles; charter/maintainer documents; halt and policy modes.
- Closure path: ordinary policy/configuration selected by operator → DashClaw enforcement → later agent operation; no separate identity/ultimate-policy matter→ultimate authority→returned governance loop was found.
- Why this is / is not agent-owned: a human-held charter and strong policy enforcement do not establish runtime S5 when the actual decisions are operational safety/tuning choices.
- Evidence: [`README.md`](https://github.com/ucsandman/DashClaw/blob/c6754674f98b73bba73046687c683e9bf685851c/README.md); [`app/lib/guard/evaluate.ts`](https://github.com/ucsandman/DashClaw/blob/c6754674f98b73bba73046687c683e9bf685851c/app/lib/guard/evaluate.ts).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: repository maintainer governance is adjacent first-party governance and is not borrowed into runtime ownership.

### Absence scope

- Surfaces inspected: human approvals, policy admin, grants, halt state, policy modes, charter/maintainer material, runtime identity and plans.
- Plausible first-party paths checked: policy ratification; org halt; admin approval; charter constraints; plan authorization; policy modes.
- Why no material first-party path remains: these paths regulate ordinary operations or development governance. No identity/ultimate-policy issue is routed through a legitimate runtime ultimate authority and returned as S5 governance.

## Recursion

The focal recursion is DashClaw's governance organization around one protected autonomous-agent/session context. Guard verdicts are operational S1. Current plan/governance-envelope regulation is S3. Future interruption/policy adaptation is S4. The protected agent's own task operation remains external.

## Variety and escalation

DashClaw attenuates common risk with deterministic evidence/policy and escalates uncertain/high-risk actions to approval or block. Predictive LLM scoring amplifies semantic variety for high-stakes history-sensitive cases. Current plan/deviation control restricts operational drift. Human outcomes then feed calibration and policy-tuning loops so future interruption posture can change without treating every approval as S5.

## Evidence gaps

No evidence gap requires `?`. S3* is deliberately conservative: the independent liveness probe supplies excellent alternative access to reality but does not itself close a mandatory findings-to-current-control transition.

**Vector:** A · — · C · — · C(P) · —
