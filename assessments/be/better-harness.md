---
harness_id: better-harness
project_name: Better Harness
repository: https://github.com/QoderAI/better-harness
review_ref: b605532fcf1014bcb48d3e6940a5bc64e80cddd5
reviewed_at: 2026-11-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: ?
autonomy_s4: P
autonomy_s5: —
---

# Better Harness

## Review boundary

- System in focus: the first-party Better Harness coding-agent-workflow inspection and improvement procedure installed into a supported coding-agent host, not the host coding agent's unrelated work.
- Purpose and identity: review a project's coding-agent work loop, distinguish supported workflow deficiencies from missing evidence, issue a validated findings report, and support bounded improvements.
- Relevant environment: project changes and history, coding-agent session traces, installed rules/skills/hooks, developer requests, host-specific permissions and available report formats.
- Standard-distribution boundary: the published `/better-harness` host-invoked Skill, bundled JavaScript evidence/analysis/render/repair commands and their documented supported host adapters; external host agent and model execute the packaged instructions but their unrelated abilities are not borrowed.
- Credited operating / distribution surfaces: [`skills/better-harness/SKILL.md`](https://github.com/QoderAI/better-harness/blob/b605532fcf1014bcb48d3e6940a5bc64e80cddd5/skills/better-harness/SKILL.md), its [finding-bound repair](https://github.com/QoderAI/better-harness/blob/b605532fcf1014bcb48d3e6940a5bc64e80cddd5/skills/better-harness/references/finding-bound-fix.md), [host invocation documentation](https://github.com/QoderAI/better-harness/blob/b605532fcf1014bcb48d3e6940a5bc64e80cddd5/README.md), and the [`scripts/` evidence and report implementations](https://github.com/QoderAI/better-harness/tree/b605532fcf1014bcb48d3e6940a5bc64e80cddd5/scripts).
- Adjacent first-party surfaces excluded from ownership: the repository's development AGENTS.md, ADRs, documentation site, CI, demos, fixture reports, internal development controls, and external coding-agent hosts' own task loops.
- First-party operating / deployment modes considered: interactive analysis via supported Claude/Codex/Qoder/Cursor/Copilot and other documented hosts, inline or durable report, operator-invoked finding-bound repair, optional independently evaluated post-fix status. No claim that the package autonomously starts itself or controls unrelated host sessions.
- Recursion level: one installed review/improvement work cell within the operator's coding-workflow organization.
- Reviewed revision: `QoderAI/better-harness@b605532fcf1014bcb48d3e6940a5bc64e80cddd5` (MIT distribution).
- Observation date: 2026-11-04.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The distributed Skill resolves a selected host/workspace and a bounded evidence bundle. Deterministic JavaScript collectors normalize session/project/asset evidence. Three context-separated read-only AI analysis passes inspect different evidence lanes; a lead AI agent reconciles findings, chooses severity and a support track, then produces a report passed through deterministic validation/rendering. Repair is a separate scoped, operator-invoked route with workspace/revision/target checks and optional fresh post-fix evaluation. Reports and finding revisions persist as files. The product does **not** ship its own model runtime or unattended scheduler for the analytical process. The host provides model inference, tools and subagent execution; the first-party Skill specifies the decisions and limits. [README](https://github.com/QoderAI/better-harness/blob/b605532fcf1014bcb48d3e6940a5bc64e80cddd5/README.md), [Skill](https://github.com/QoderAI/better-harness/blob/b605532fcf1014bcb48d3e6940a5bc64e80cddd5/skills/better-harness/SKILL.md), [architecture boundary](https://github.com/QoderAI/better-harness/blob/b605532fcf1014bcb48d3e6940a5bc64e80cddd5/docs/ARCHITECTURE.md).

## Operational model

The review's operational outcome is an evidence-bounded, actionable diagnosis of the installed coding-workflow system, or an authorized bounded repair. The specialist AI evidence passes and lead agent make task-specific judgments under the packaged workflow; collectors, report writers, host plug-in metadata and validations are support. The host coding agent's normal code-production work is an adjacent operational system, not evidence of additional Better Harness VSM functions. The operator selects work scope and a prospective repair to execute. No central OSS-project maintainer authority is imported into an installed review instance.

## S1 — Operations

- State: A
- Function: produce evidence-backed diagnostic findings and, in a separate authorized route, a bounded repair outcome.
- Disturbance / variety regulated: divergent project/session/asset evidence, uncertain provenance and differing workflow failure causes.
- Decisive decision or feedback right: three specialist AI passes judge candidate findings in distinct lanes; the lead AI decides the final supported findings, severity, score and output narrative.
- Decision owner: the host-executed AI specialists and lead, following the first-party packaged Skill. Host inference/tool delivery is support, not an independent Better Harness policy owner.
- Supporting / enforcement mechanisms: read-only evidence bundle, deterministic analyzers, scope limits, output schema, renderer and revision checks.
- Closure path: evidence bundle → specialist results → lead reconciliation and report judgment → validated report and optional bounded repair result.
- Boundary reachability: the published Skill explicitly directs host agents to run the three passes and lead reconciliation in ordinary installed host invocation; it is not merely a development example.
- Why this is / is not agent-owned: content judgment depends on AI discretion over findings and fixes, not on the JavaScript collectors alone.
- Evidence: [Skill Steps 1–4](https://github.com/QoderAI/better-harness/blob/b605532fcf1014bcb48d3e6940a5bc64e80cddd5/skills/better-harness/SKILL.md), [README host routes](https://github.com/QoderAI/better-harness/blob/b605532fcf1014bcb48d3e6940a5bc64e80cddd5/README.md).
- Basis: explicit.
- Confidence: high.
- Caveats: host inference and permissions must be configured; this is the installed Better Harness review work cell, not an independently booting agent runtime.

## S2 — Coordination

- State: —
- Function: no established inter-S1 oscillation-regulation function at this review-cell boundary.
- Disturbance / variety regulated: no specific destructive cross-specialist interference is shown; specialists deliberately receive non-overlapping read-only evidence.
- Decisive decision or feedback right: none shown for a coordination decision that changes subsequent specialist behavior.
- Decision owner: not established.
- Supporting / enforcement mechanisms: the Skill's parallel launch and evidence partitioning are scheduling/isolation, and lead reconciliation is terminal report judgment.
- Closure path: no inter-S1 feedback loop beyond collecting independent answers into the lead report.
- Why this is / is not agent-owned: parallel execution and deduplicating similar findings do not establish a specific S2 disturbance-and-feedback relationship.
- Evidence: [independent evidence passes and restrictions](https://github.com/QoderAI/better-harness/blob/b605532fcf1014bcb48d3e6940a5bc64e80cddd5/skills/better-harness/SKILL.md).
- Basis: structural.
- Confidence: medium.
- Caveats: this is not a claim that host coding agents can never coordinate in another product mode.

### Absence scope

- Surfaces inspected: installed Skill, specialist briefs, lead reconciliation, host invocation and first-party report/repair route.
- Plausible first-party paths checked: parallel specialist launch, distinct evidence lanes, merge/deduplication instructions and later repair status.
- Why no material first-party path remains: no documented contention/oscillation among specialists with a coordination decision returned to alter their subsequent operation; they finish read-only lanes and the lead synthesizes output.

## S3 — Inside-and-now control

- State: A
- Function: current whole-report control over the three evidence lanes and acceptance of their work on behalf of the diagnostic task.
- Disturbance / variety regulated: incomplete or inconsistent specialist evidence, unsupported claims, scope overruns and duplicate/conflated findings could undermine the whole review outcome.
- Decisive decision or feedback right: the lead AI accepts/defer/merges specialist findings, fixes final severity and scores, selects one support track, and stops or narrows publication on evidence failure.
- Decision owner: the review's AI lead; validators enforce the prescribed result structure and the host executes commands.
- Supporting / enforcement mechanisms: bundle lane status, quality gates, `findings.json` validation, renderer and hard cap on evidence specialists.
- Closure path: cross-lane status and findings reach the lead → agent selects admissible current commitments and their priority → only reconciled findings are rendered or execution is stopped.
- Boundary reachability: these lead rights are mandatory in Step 3 of the distributed Skill's normal analysis mode.
- Why this is / is not agent-owned: the lead chooses material accept/reject/priority judgments; code guards do not precompute which real findings deserve inclusion.
- Whole-system current view: one bundle with three lane states plus lead facts, then all specialist candidates at reconciliation.
- Current-control decision scope: acceptance, severity, support-track and report-level commitment—not control of the operator's unrelated coding tasks.
- Evidence: [Skill Steps 2–4](https://github.com/QoderAI/better-harness/blob/b605532fcf1014bcb48d3e6940a5bc64e80cddd5/skills/better-harness/SKILL.md), [findings quality gate](https://github.com/QoderAI/better-harness/blob/b605532fcf1014bcb48d3e6940a5bc64e80cddd5/skills/better-harness/references/findings-review.md).
- Basis: explicit.
- Confidence: medium.
- Caveats: the whole-system boundary is the review cell; report acceptance should not be confused with general parent governance of all coding agents.

## S3* — Complementary audit

- State: ?
- Function: a plausible independent post-fix check of a repair claim, but the complementary-access boundary is not fully established from the shipped instructions alone.
- Disturbance / variety regulated: the repair-performing lead may overclaim that a reported finding has been fixed.
- Decisive decision or feedback right: a fresh read-only agent may judge `verified`, `partial` or `blocked` from the pre-fix finding, actual outputs, changed paths, native validation and refreshed integrity envelope.
- Decision owner: a separately instantiated agent for the post-fix verdict, when supported; the deterministic recorder stores it.
- Supporting / enforcement mechanisms: versioned finding lock, target topology binding, asset integrity collector and unchanged pre-fix baseline.
- Closure path: independent verdict can update `Repair Progress`, while efficacy scores require later comparable episodes.
- Why this is / is not agent-owned: an AI verdict exists, but the reviewer receives lead-provided bounded inputs, is forbidden to rescan the project, and can be omitted on delegation failure; it is unresolved whether its evidence access is materially complementary to ordinary repair reporting.
- Evidence: [finding-bound repair / Reassess the Repair Independently](https://github.com/QoderAI/better-harness/blob/b605532fcf1014bcb48d3e6940a5bc64e80cddd5/skills/better-harness/references/finding-bound-fix.md).
- Basis: explicit for the route, unknown for independent complementary access.
- Confidence: low.
- Caveats: no independent S3* audit is inferred from ordinary specialist decomposition, validators or host subagent naming alone.

## S4 — Outside-and-then intelligence

- State: P
- Function: prepare prospective improvements to the project-facing coding-agent workflow, with operator-controlled adoption of a selected repair.
- Disturbance / variety regulated: evolving project needs, repeated session friction, missing rules/assets and changing operational evidence can make the existing workflow ineffective.
- Decisive decision or feedback right: the lead develops prioritized options; the parent operator selects and invokes an actual repair against an authorized project/finding, delimiting the adoption decision.
- Decision owner: operator/parent for the adoption decision; AI lead for option formation and scoped repair implementation, with deterministic tools checking target/expected revision.
- Supporting / enforcement mechanisms: session/project/asset evidence collectors, repair callback, workspace topology and revision guards.
- Closure path: observed project/session mismatches → agent-generated future improvements → operator invokes a finding-bound repair → host AI edits the authorized target → validators and recorded outputs inform later work.
- Boundary reachability: both diagnostic findings with repair actions and callback-based bounded repair are first-party installed Skill routes; no external repository maintainer workflow is borrowed.
- Why this is / is not agent-owned: the agent generates prospective options but the decisive commitment to change the live work environment is parent-selected in the evidenced finding-bound route.
- External distinction: observed project changes, session outcomes and host agent assets rather than only an internal current subtask plan.
- Future / prospective distinction: findings specify an improved workflow/asset and verifiable future operating outcome.
- Adaptation option generated: bounded project/agent-asset repair and a prioritized expected output.
- Path back into current capability / S3: applied local instructions/assets and recorded repair status influence subsequent host-agent sessions; later comparable task episodes, not same-run scores, measure effectiveness.
- Evidence: [README workflow and improvement route](https://github.com/QoderAI/better-harness/blob/b605532fcf1014bcb48d3e6940a5bc64e80cddd5/README.md), [Skill Step 3/5](https://github.com/QoderAI/better-harness/blob/b605532fcf1014bcb48d3e6940a5bc64e80cddd5/skills/better-harness/SKILL.md), [finding-bound repair](https://github.com/QoderAI/better-harness/blob/b605532fcf1014bcb48d3e6940a5bc64e80cddd5/skills/better-harness/references/finding-bound-fix.md).
- Basis: explicit and structural.
- Confidence: medium.
- Caveats: reports alone are proposals; no automatic adoption, causal improvement or unattended future sensing is claimed. This `P` is a supported operator-selected adaptation path, not generic task approval.

## S5 — Policy and identity

- State: —
- Function: no shipped operational identity/ultimate-policy adjudication loop at this review-cell recursion.
- Disturbance / variety regulated: user-selected scope, risk and permission restrictions remain outer constraints, not an identified unresolved identity tension.
- Decisive decision or feedback right: no such in-boundary right evidenced.
- Decision owner: no agentic or first-party parent S5 closure established.
- Supporting / enforcement mechanisms: Skill's fixed guardrails, stop conditions, permission scoping and CLI validation.
- Closure path: no identity-level issue → legitimate parent decision → returned policy path is supplied; ordinary human choice of report scope or fix does not qualify.
- Why this is / is not agent-owned: static instructions constrain review actions without giving an actor an ultimate-policy decision process.
- Evidence: [Skill scope and guardrails](https://github.com/QoderAI/better-harness/blob/b605532fcf1014bcb48d3e6940a5bc64e80cddd5/skills/better-harness/SKILL.md), [repair authority boundary](https://github.com/QoderAI/better-harness/blob/b605532fcf1014bcb48d3e6940a5bc64e80cddd5/skills/better-harness/references/finding-bound-fix.md).
- Basis: structural.
- Confidence: medium.
- Caveats: product developers may make policy decisions in a separate repository-governance system, excluded from this installed review cell.

### Absence scope

- Surfaces inspected: packaged Skill, review/repair protocols, host installation and scope controls, developer architecture documentation.
- Plausible first-party paths checked: outer authority resolution, human callback, stop/escalation instructions, fixed privacy/permission gates, project governance documents.
- Why no material first-party path remains: the first-party runtime exposes task authorization and policy enforcement but no identity/ultimate-policy issue, legitimate S5 adjudication, and returned governing decision at the declared recursion.

## Distributed OSS parent arrangement

The authors and contributors maintain the source repository. Its development governance and CI are outside this installed review work cell, and do not supply S3/S4/S5 ownership here. The relevant parent mode for S4 is the local operator selecting a concrete adaptation and returning it through a first-party finding-bound repair route.

## Self-hosted and non-human modes

The analysis mode is hosted inside a separately installed coding-agent product. The host supplies AI inference and tool/subagent execution; Better Harness supplies the first-party decision procedure. No provider-independent standalone daemon or automatic cross-user organization is credited.

## Recursion

Specialist evidence passes are bounded operational subcells under one lead-controlled diagnostic task. Nothing in their read-only individual briefs establishes complete independently viable recursive organizations. The operator's full coding workflow is the parent context, not an assessed second recursion.

## Variety and escalation

The bundle limits evidence window/provider/workspace and records missing lanes; the lead halts or downgrades confidence when required evidence is unavailable. Repair uses exact target/revision scope and can refuse stale callbacks. These are useful constraints and escalations, not by themselves S5 or an algedonic channel.

## Evidence gaps

- Complementary audit: the independent post-fix reviewer has a fresh context but receives bounded lead-curated evidence and cannot rescan the project. A direct complementary raw-evidence path and audit judgment independence sufficient for S3* remain unresolved; hence `?` rather than assuming `A` or a definitive `—`.
- Actual outcomes: no host-specific execution or model quality success is claimed from documentation/source alone. The file describes first-party supported behavior, not independent empirical verification of improved productivity.
