---
harness_id: agent-harness-kit
project_name: Agent Harness Kit
repository: https://github.com/enmanuelmag/agent-harness-kit
review_ref: 25edd77efd4e046bfc8fd232c406759f2b48caef
reviewed_at: 2026-10-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Agent Harness Kit

## Review boundary

- System in focus: the installed AHK project workflow: generated agent roles plus task/action/health MCP, in its supported provider hosts.
- Purpose and identity: deliver explicitly scoped software tasks through attributable role work and verified completion.
- Relevant environment: project code/specifications, native health commands, database lifecycle state, external provider agents and current dependency documentation.
- Standard-distribution boundary: npm CLI/materializer, packaged role templates and MCP server; credit the concrete Claude Code generated composition as the positive reachability witness.
- Credited operating / distribution surfaces: src/core/materializer/agent-templates, ClaudeCodeMaterializer, delegation-guidance, task health/execution policy, database claims and MCP tools.
- Adjacent first-party surfaces excluded from ownership: root .agents/.codex development agents, this repository's own plans/reports/tests/CI and dashboard demonstrations do not supply product ownership.
- First-party operating / deployment modes considered: installed tracked lead→explorer→optional consultant→builder→reviewer flow; blocked/repair modes and lightweight read-only skills; other provider materializers inspected for role restrictions.
- Recursion level: one installed project contribution workflow with operational role units; no organization-wide governance inferred.
- Reviewed revision: `25edd77efd4e046bfc8fd232c406759f2b48caef`.
- Observation date: 2026-10-27.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

ahk init materializes native agents/skills and MCP settings. In the Claude Code distribution, scaffolding writes five named role files and selects lead as the project default. Lead chooses/claims one task, reads health and dependency state, supplies bounded handoffs, delegates, responds to reviewer blocks and requests final completion. Builder owns implementation; explorer/consultant supply analysis; reviewer owns ordinary acceptance verification. MCP/database logic atomically claims tasks, records actions/handoffs, executes server-owned health and binds results to claim generation/run tokens; blocked mode refuses builder actions until an audited bounded repair is opened. Configured native health is required rather than a canned success. Materializers expose different enforcement strength: Codex no-write roles are explicitly prose-only, not an OS guarantee. Provider engines execute the concrete first-party roles rather than donating an assessed VSM vector.

## Operational model

Installed role instructions confer ordinary discretion over evidence, implementation and correction inside authorized task scope. Lead can diagnose failed whole-project health and select bounded repair scope, control which role may act and reassign the builder after findings. Deterministic claim, health and action gates enforce decisions; they are separated from lead's organizational judgment. Reviewer is a distinct role but remains the prescribed ordinary acceptance stage, so separation by name/context alone is not counted as complementary audit.

## S1 — Operations

- State: A
- Function: produce scoped implementation and evidence-backed task outcomes.
- Disturbance / variety regulated: unknown project structure, incomplete requirements, code failures and unmet acceptance conditions.
- Decisive decision or feedback right: choose implementation steps, inspections, tests and corrective code changes within the handoff.
- Decision owner: installed builder and analysis role agents for their bounded operational outcomes.
- Supporting / enforcement mechanisms: provider tool loop, generated roles, canonical handoffs, action records, filesystem and native commands.
- Closure path: builder reads context, changes code, observes tests, fixes failures and records result; reviewer feedback returns through lead for further implementation.
- Boundary reachability: ClaudeCodeMaterializer writes concrete named agent files and MCP/default-lead setup from packaged templates.
- Why this is / is not agent-owned: agent discretion selects actual changes; lifecycle storage and health gates alone cannot implement them.
- Evidence: [src/core/materializer/claude-code.ts](https://github.com/enmanuelmag/agent-harness-kit/blob/25edd77efd4e046bfc8fd232c406759f2b48caef/src/core/materializer/claude-code.ts), [src/core/materializer/agent-templates/builder.md](https://github.com/enmanuelmag/agent-harness-kit/blob/25edd77efd4e046bfc8fd232c406759f2b48caef/src/core/materializer/agent-templates/builder.md), [src/core/materializer/agent-templates/lead.md](https://github.com/enmanuelmag/agent-harness-kit/blob/25edd77efd4e046bfc8fd232c406759f2b48caef/src/core/materializer/agent-templates/lead.md).
- Basis: structural.
- Confidence: medium-high, bounded source inspection.
- Caveats: Static supported-path assessment; no live model/provider execution or effectiveness claim.

## S2 — Coordination

- State: C
- Function: prevent duplicate task ownership and conflicting overlapping role work.
- Disturbance / variety regulated: two sessions claiming the same pending task, or dependent role work advancing before its prerequisite handoff.
- Decisive decision or feedback right: accept exclusive task claim, deny competing claim and return a different eligible task path; keep dependent implementation waiting for prior role result.
- Decision owner: claim exclusivity/ordering policy is developer-selected deterministic support; an autonomous inter-unit coordinating decision/authority arrangement beyond the installed fixed discipline is not established.
- Supporting / enforcement mechanisms: transactional claim, assigned_to/status feedback, canonical handoffs and provider-specific wait guidance.
- Closure path: failed claim returns task_already_claimed and lead must select another pending task; dependent role waits alter subsequent execution.
- Boundary reachability: tasks.claim is shipped MCP, backed by HarnessDB.claimTask transaction; lead Step 3 and packaged delegation guidance consume returned claim and completion state.
- Why this is / is not agent-owned: a function-specific enforced coordination path exists, but the autonomous coordination right is not inferred from fixed rejection/sequence execution.
- Distinct S1 units: independently launched project task sessions and delegated operational roles.
- Inter-S1 disturbance: duplicate execution of one task and conflicting dependent work before shared context is ready.
- Attenuating coordination relation: exclusive claim with rejection feedback, one-task discipline and required predecessor result/handoff.
- Feedback into subsequent S1 behaviour: a busy task is skipped rather than stolen; dependent role cannot responsibly start without canonical input.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the claim explicitly excludes competing owners; waiting is tied to dependent shared-work interference rather than generic message delivery.
- Evidence: [src/core/db.ts](https://github.com/enmanuelmag/agent-harness-kit/blob/25edd77efd4e046bfc8fd232c406759f2b48caef/src/core/db.ts), [src/core/mcp-tools.ts](https://github.com/enmanuelmag/agent-harness-kit/blob/25edd77efd4e046bfc8fd232c406759f2b48caef/src/core/mcp-tools.ts), [src/core/materializer/agent-templates/lead.md](https://github.com/enmanuelmag/agent-harness-kit/blob/25edd77efd4e046bfc8fd232c406759f2b48caef/src/core/materializer/agent-templates/lead.md), [src/core/materializer/delegation-guidance.ts](https://github.com/enmanuelmag/agent-harness-kit/blob/25edd77efd4e046bfc8fd232c406759f2b48caef/src/core/materializer/delegation-guidance.ts).
- Basis: structural.
- Confidence: medium-high, bounded source inspection.
- Caveats: C is bounded to supplied exclusion/feedback primitives. It does not claim autonomous shared-resource arbitration or correctness under every provider.

## S3 — Inside-and-now control

- State: A
- Function: maintain current project/workflow cohesion through health-constrained repair and corrective role assignment.
- Disturbance / variety regulated: whole-project health fails, existing commitments cannot safely proceed, or review contradicts implementation readiness.
- Decisive decision or feedback right: diagnose the current failure, define a bounded repair reason/scope, authorize the builder through repair mode, and choose corrective reassignment before closure.
- Decision owner: installed lead agent within user-authorized task scope.
- Supporting / enforcement mechanisms: server-owned health, task modes, action-denial policy, logged repair scope, claims and handoffs.
- Closure path: claim health failure blocks implementation; lead selects bounded repair, MCP records the mode/scope, builder acts under that constraint, reviewer/fresh final health determine whether closure is admissible.
- Boundary reachability: lead Orient explicitly instructs tasks.repair.begin before assigning bounded health-failure implementation; installed MCP exposes repair and execution policy gates.
- Why this is / is not agent-owned: lead chooses diagnosis, scope and corrective assignment; deterministic health and denial enforce those choices without becoming their owner.
- Whole-system current view: project-native health plus active/pending task state, role results, dependency changes and acceptance evidence for the installed workflow.
- Current-control decision scope: current operational constraints, accountable role commitments and exception recovery on behalf of the project workflow.
- Evidence: [src/core/materializer/agent-templates/lead.md](https://github.com/enmanuelmag/agent-harness-kit/blob/25edd77efd4e046bfc8fd232c406759f2b48caef/src/core/materializer/agent-templates/lead.md), [src/core/task-health.ts](https://github.com/enmanuelmag/agent-harness-kit/blob/25edd77efd4e046bfc8fd232c406759f2b48caef/src/core/task-health.ts), [src/core/task-execution-policy.ts](https://github.com/enmanuelmag/agent-harness-kit/blob/25edd77efd4e046bfc8fd232c406759f2b48caef/src/core/task-execution-policy.ts), [src/core/mcp-tools.ts](https://github.com/enmanuelmag/agent-harness-kit/blob/25edd77efd4e046bfc8fd232c406759f2b48caef/src/core/mcp-tools.ts), [src/core/db.ts](https://github.com/enmanuelmag/agent-harness-kit/blob/25edd77efd4e046bfc8fd232c406759f2b48caef/src/core/db.ts).
- Basis: structural.
- Confidence: medium-high, bounded source inspection.
- Caveats: One task at a time and actual project authorization limit the decision envelope. Health scripts are operator-supplied; no global portfolio optimization or ultimate authority is inferred.

## S3* — Complementary audit

- State: —
- Function: no separate complementary operational audit is established.
- Disturbance / variety regulated: reviewer checks current task acceptance as ordinary production QA.
- Decisive decision or feedback right: reviewer reads files/tests and can block, but this is the normal mandatory delivery check; health is the normal lifecycle gate.
- Decision owner: no separate complementary audit owner supplied at this boundary.
- Supporting / enforcement mechanisms: role restrictions, reviewer verdicts, action evidence, native health and diagnostic history access.
- Closure path: ordinary reviewer→lead→builder feedback exists, without a distinct complementary audit path beyond routine production reporting/acceptance.
- Why this is / is not agent-owned: independent role/context is evidence of ordinary review separation, not by itself a complementary S3* mandate.
- Evidence: [src/core/materializer/agent-templates/reviewer.md](https://github.com/enmanuelmag/agent-harness-kit/blob/25edd77efd4e046bfc8fd232c406759f2b48caef/src/core/materializer/agent-templates/reviewer.md), [src/core/materializer/agent-templates/lead.md](https://github.com/enmanuelmag/agent-harness-kit/blob/25edd77efd4e046bfc8fd232c406759f2b48caef/src/core/materializer/agent-templates/lead.md), [src/core/task-health.ts](https://github.com/enmanuelmag/agent-harness-kit/blob/25edd77efd4e046bfc8fd232c406759f2b48caef/src/core/task-health.ts), [src/core/materializer/agent-restrictions.ts](https://github.com/enmanuelmag/agent-harness-kit/blob/25edd77efd4e046bfc8fd232c406759f2b48caef/src/core/materializer/agent-restrictions.ts).
- Basis: structural.
- Confidence: medium-high, bounded source inspection.
- Caveats: Static supported-path assessment; no live model/provider execution or effectiveness claim.

### Absence scope

- Surfaces inspected: packaged lead/builder/reviewer workflows, history/diagnostic access, role restrictions and server health.
- Plausible first-party paths checked: reviewer raw-file/test checks, action-history audit/diagnosis reads, final health and blockers.
- Why no material first-party path remains: all supplied paths are routine acceptance or optional diagnosis; no distinct sampled/adversarial/reconciliatory operational audit loop is wired into the installed organization.

## S4 — Outside-and-then intelligence

- State: —
- Function: no externally prospective adaptation of the harness's capability is established.
- Disturbance / variety regulated: dependency facts and requested project work, not a separate future capability/environment model.
- Decisive decision or feedback right: consultant investigates versions and required changes for the current task; upgrade notices and doctor report installed state.
- Decision owner: no S4-specific adaptation owner established.
- Supporting / enforcement mechanisms: dependency snapshot/check, current-documentation research, plan handoffs, maintenance commands and cached version notices.
- Closure path: task advice can change the approved implementation plan, but no outside-and-then harness capability adaptation conversation is supplied.
- Why this is / is not agent-owned: research-as-task and operator-selected upgrades are not automatically S4.
- Evidence: [src/core/materializer/agent-templates/lead.md](https://github.com/enmanuelmag/agent-harness-kit/blob/25edd77efd4e046bfc8fd232c406759f2b48caef/src/core/materializer/agent-templates/lead.md), [src/core/materializer/agent-templates/builder.md](https://github.com/enmanuelmag/agent-harness-kit/blob/25edd77efd4e046bfc8fd232c406759f2b48caef/src/core/materializer/agent-templates/builder.md), [README.md](https://github.com/enmanuelmag/agent-harness-kit/blob/25edd77efd4e046bfc8fd232c406759f2b48caef/README.md).
- Basis: structural.
- Confidence: medium-high, bounded source inspection.
- Caveats: Static supported-path assessment; no live model/provider execution or effectiveness claim.

### Absence scope

- Surfaces inspected: lead research/dependency rules, installed workflow and README maintenance/doctor/migration modes.
- Plausible first-party paths checked: external documentation/compatibility advice, dependency upgrades, model preferences, doctor and generated-skill migration.
- Why no material first-party path remains: the shipped paths address current task design or explicitly selected maintenance; none develops prospective harness adaptation options with a corresponding current-control return loop.

## S5 — Policy and identity

- State: —
- Function: no runtime identity/ultimate-policy closure is established.
- Disturbance / variety regulated: approved project/task scope and permission synchronization.
- Decisive decision or feedback right: human approval controls specifications, implementation authorization and selected maintenance, not a supplied identity-level dispute resolution path.
- Decision owner: no runtime S5 owner established; initial project/user policy remains externally selected.
- Supporting / enforcement mechanisms: role red lines, provider permissions, config, document approvals and repair scope logs.
- Closure path: no identity/policy issue→legitimate ultimate authority→authoritative returned policy loop found.
- Why this is / is not agent-owned: ordinary task approvals and permission acknowledgments do not become S5.
- Evidence: [README.md](https://github.com/enmanuelmag/agent-harness-kit/blob/25edd77efd4e046bfc8fd232c406759f2b48caef/README.md), [src/core/materializer/agent-templates/lead.md](https://github.com/enmanuelmag/agent-harness-kit/blob/25edd77efd4e046bfc8fd232c406759f2b48caef/src/core/materializer/agent-templates/lead.md), [src/core/materializer/agent-restrictions.ts](https://github.com/enmanuelmag/agent-harness-kit/blob/25edd77efd4e046bfc8fd232c406759f2b48caef/src/core/materializer/agent-restrictions.ts).
- Basis: structural.
- Confidence: medium-high, bounded source inspection.
- Caveats: Static supported-path assessment; no live model/provider execution or effectiveness claim.

### Absence scope

- Surfaces inspected: specification/authorization workflow, lead instructions, provider restrictions and configuration ownership.
- Plausible first-party paths checked: use-case/spec approvals, permission-sync acknowledgment, health repair authorization and user-owned generated-file changes.
- Why no material first-party path remains: these govern bounded work/configuration; no explicit ultimate-policy/identity matter and returned authoritative decision path is shipped.

## Distributed OSS parent arrangement

No root development agent or maintainer authority is imported into the installed customer project. Local human authorization is inspected per function and does not establish organization-level parent notation.

## Self-hosted and non-human modes

Supported provider materializers package the workflow. Claude Code supplies the concrete credited role reachability; Codex prose-only no-write restrictions are disclosed rather than represented as enforced isolation. Generic operator approvals do not establish a P mode.

## Recursion

Five roles and nested provider subagents do not establish five recursively viable systems. The assessed boundary remains the installed project workflow.

## Variety and escalation

Claim collisions return to selection; health failure enters blocked diagnosis or bounded repair; review findings return to implementation; missing MCP or unclear blockers stop for human resolution. These paths are not automatically algedonic or ultimate-policy channels.

## Evidence gaps

No live provider task or production database deployment was executed. Source paths establish the packaged workflow, not effectiveness or security. Native TypeScript suite availability is recorded in the run receipt; role enforcement varies by provider.
