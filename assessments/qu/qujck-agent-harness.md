---
harness_id: qujck-agent-harness
project_name: agent-harness
repository: https://github.com/qujck/harness
review_ref: 9a2fc16d1cc26070114ae6e908107cf211e0c99e
reviewed_at: 2026-10-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C(P)
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# agent-harness

## Review boundary

- System in focus: a configured project using qujck's installed workflow kit with subscription-backed Claude Code sessions; not the template's own development team.
- Purpose and identity: deliver feature tickets through attributable coding work and controlled integration.
- Relevant environment: project repositories, parallel worker sessions, GitHub/Jira, PostgreSQL ticket store, model subscription usage and human project owner.
- Standard-distribution boundary: shipped scripts, role documents, ledger adapter, Claude hooks and optional team launcher/dashboard; project commands, owner and live role sessions must be configured.
- Credited operating / distribution surfaces: developer role plus agent-spawn's explicit role/AGENTS/init/claim prompt; ticket-conflict primitives; function-specific delivery-lead and reviewer construction instructions; owner budget return path.
- Adjacent first-party surfaces excluded from ownership: template repository's historical PROGRESS/DECISIONS entries, its test fixtures/CI and originating project's unported head-of-testing/tester prompts. Historical owner quotations are template rules, not evidence of a running assessed organization.
- First-party operating / deployment modes considered: configured developer launch; manually commissioned delivery-lead and optional code-reviewer sessions; operator budget adjustments; agent-agnostic manual scripts. Bare unconfigured kit is not a running agent.
- Recursion level: one configured delivery team with developer ticket episodes as S1 units.
- Reviewed revision: 9a2fc16d1cc26070114ae6e908107cf211e0c99e
- Observation date: 2026-10-29
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

Shell scripts initialize project stacks, enforce identity/verification/handoff, and manage a PostgreSQL or Jira ledger. feature-ticket creates remote branch locks; team/agent-spawn starts Claude Code in a named worktree with the developer prompt and watches its claim. The optional lead reads the ledger and controls routing/team size; reviewer guidance separates raw-code judgment from the author. Non-worker role launch lines open Claude and then require the operator to paste/read the role, initialize it and connect the team's messaging. The shipped roster contains only a retired example. This bounds higher-function claims to intentional constructors, not a deployed self-starting organization.

## Operational model

An installed developer receives its ticket and uses the external Claude runtime as the explicitly supported inference/tool host for the first-party role. The harness supplies the task/identity/claim/handoff arrangement rather than borrowing an unrelated private agent. The lead/reviewer roles need commissioning and an effective communication/authority setup. Deterministic gates never become the discretionary owners.

## S1 — Operations

- State: A
- Function: implement an assigned feature ticket to a reviewed terminal disposition.
- Disturbance / variety regulated: task-specific source/test uncertainty and failures.
- Decisive decision or feedback right: choose investigation, edits and repairs within a ticket.
- Decision owner: model-backed developer session under the shipped role.
- Supporting / enforcement mechanisms: tmux/Claude launcher, identity environment, isolated worktree, ledger, verification and handoff scripts.
- Closure path: spawn passes read-role/init/claim instructions and ticket; developer decides actions, consumes tests/review and completes/parks/releases the record.
- Boundary reachability: team/agent-spawn.sh builds an actual claude command and first prompt, including the shipped developer role, rather than only describing an aspirational agent.
- Why this is / is not agent-owned: the model chooses the implementation; launcher/gates enforce mechanics. Standard installation supplies commands/credentials, not a newly invented S1 actor policy.
- Evidence: [team/agent-spawn.sh](https://github.com/qujck/harness/blob/9a2fc16d1cc26070114ae6e908107cf211e0c99e/team/agent-spawn.sh); [docs/roles/developer.md](https://github.com/qujck/harness/blob/9a2fc16d1cc26070114ae6e908107cf211e0c99e/docs/roles/developer.md); [AGENTS.md](https://github.com/qujck/harness/blob/9a2fc16d1cc26070114ae6e908107cf211e0c99e/AGENTS.md)
- Basis: structural
- Confidence: medium-high
- Caveats: Source-relative ownership/reachability finding; no live model or effectiveness test.

## S2 — Coordination

- State: C
- Function: attenuate concurrent duplicate ownership and shared-checkout corruption.
- Disturbance / variety regulated: two developer ticket units claim the same ticket or mutate the same checkout.
- Decisive decision or feedback right: accept one claim, refuse the competing claimant and return it to another ticket; isolate each writer.
- Decision owner: developer/lead coordination policy must be composed with first-party conflict-response primitives.
- Supporting / enforcement mechanisms: atomic remote Git branch claim, ledger claim, identity/live-marker checks and per-agent worktrees.
- Closure path: feature-ticket claim rejection explicitly tells the loser to choose another ticket; init refuses an occupied checkout and names isolation remedy.
- Boundary reachability: the installed developer's prompt invokes claim/init before work; these are S2-specific paths in executable first-party scripts.
- Why this is / is not agent-owned: C reflects supplied collision response with autonomous coordinating actors/communication still commissioned; neither a push lock nor a generic mailbox is an agent.
- Evidence: [scripts/feature-ticket.sh](https://github.com/qujck/harness/blob/9a2fc16d1cc26070114ae6e908107cf211e0c99e/scripts/feature-ticket.sh); [scripts/init.sh](https://github.com/qujck/harness/blob/9a2fc16d1cc26070114ae6e908107cf211e0c99e/scripts/init.sh); [docs/roles/developer.md](https://github.com/qujck/harness/blob/9a2fc16d1cc26070114ae6e908107cf211e0c99e/docs/roles/developer.md)
- Basis: structural
- Confidence: medium-high
- Caveats: Source-relative ownership/reachability finding; no live model or effectiveness test.
- Distinct S1 units: parallel developer sessions owning different or competing tickets.
- Inter-S1 disturbance: duplicate claim race and same-checkout corruption are explicitly documented and refused.
- Attenuating coordination relation: single accepted remote lock/ledger holder and separate writer worktrees.
- Feedback into subsequent S1 behaviour: losing claimant must select another ticket; occupied-checkout init refuses progress until isolation/legitimate handoff.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: claim refusal targets a concrete shared-work race and returns a changed work-selection condition.

## S3 — Inside-and-now control

- State: C(P)
- Function: regulate the current team's queue, work allocation, team size and shared account commitments.
- Disturbance / variety regulated: idle/blocked workers, ready-work demand, red main and current budget/capacity pressure.
- Decisive decision or feedback right: base constructor: commission a lead with queue/routing/spawn/bench authority; parent mode: owner authorizes off-budget/current-capacity exceptions or revises weekly plan.
- Decision owner: base C: configured delivery-lead actor/communication/authority arrangement; P: legitimate local project owner.
- Supporting / enforcement mechanisms: ledger/frontier, team panel/context publisher, budget calculation, spawn/bench and owner-word records.
- Closure path: lead instructions connect current record → routing/team changes; owner budget answer is returned verbatim or through approve/adjust, altering subsequent spawn acceptance.
- Boundary reachability: lead role plus onboarding launch-line procedure is an intentional first-party constructor; owner-approved budget flags/adjustment scripts are actually consumed by spawning. Non-worker launch requires manual role commissioning; it is not graded autonomous A.
- Why this is / is not agent-owned: telemetry and hard cap do not choose staffing. A lead's missing commissioning prevents A, while the explicit local owner resource judgment supplies the distinct parent loop.
- Evidence: [docs/roles/delivery-lead.md](https://github.com/qujck/harness/blob/9a2fc16d1cc26070114ae6e908107cf211e0c99e/docs/roles/delivery-lead.md); [scripts/agent-onboard.sh](https://github.com/qujck/harness/blob/9a2fc16d1cc26070114ae6e908107cf211e0c99e/scripts/agent-onboard.sh); [team/agents-budget.sh](https://github.com/qujck/harness/blob/9a2fc16d1cc26070114ae6e908107cf211e0c99e/team/agents-budget.sh); [team/agent-spawn.sh](https://github.com/qujck/harness/blob/9a2fc16d1cc26070114ae6e908107cf211e0c99e/team/agent-spawn.sh)
- Basis: structural
- Confidence: medium-high
- Caveats: Source-relative ownership/reachability finding; no live model or effectiveness test.
- Whole-system current view: lead reads team ledger claims/frontier, red-main state and cross-session context/account usage.
- Current-control decision scope: shared staffing/model allocation, routing, budget exceptions and current work priorities within the owner's envelope.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | commissioned delivery-lead actor | ready/idle/blocked team and ledger | lead routes or changes staffing once connected | [docs/roles/delivery-lead.md](https://github.com/qujck/harness/blob/9a2fc16d1cc26070114ae6e908107cf211e0c99e/docs/roles/delivery-lead.md) |
| Parent (`P`) | local project owner | off-budget start/cap or plan revision | quoted owner words / approve-adjust return to spawn acceptance | [team/agents-budget.sh](https://github.com/qujck/harness/blob/9a2fc16d1cc26070114ae6e908107cf211e0c99e/team/agents-budget.sh); [team/agent-spawn.sh](https://github.com/qujck/harness/blob/9a2fc16d1cc26070114ae6e908107cf211e0c99e/team/agent-spawn.sh) |

## S3* — Complementary audit

- State: C
- Function: independently challenge developer completion/correctness claims from original change evidence and return findings to delivery control.
- Disturbance / variety regulated: developer report or green routine checks miss a substantive defect.
- Decisive decision or feedback right: judge defects separately from authorship and decide how findings affect held/reworked PRs.
- Decision owner: a separately commissioned code-reviewer actor judges; delivery lead acts; neither is supplied as an active default session.
- Supporting / enforcement mechanisms: separate role/session/worktree, raw PR diff/code/tests, durable line comments and lead-directed messages.
- Closure path: reviewer posts verified line findings before messaging lead; lead decides holds and routes repair; moved commits return for review.
- Boundary reachability: code-reviewer.md and onboarding role/launch instructions expose the specific independent raw-artifact and corrective-routing path, but commissioning/host messaging/authority must still be composed.
- Why this is / is not agent-owned: C is specific independent judgment/feedback construction, not an automatic grade for tests or labels. The separate role cannot write fixes, merge or take author direction; routine mandatory testing alone is not credited.
- Evidence: [docs/roles/code-reviewer.md](https://github.com/qujck/harness/blob/9a2fc16d1cc26070114ae6e908107cf211e0c99e/docs/roles/code-reviewer.md); [docs/roles/delivery-lead.md](https://github.com/qujck/harness/blob/9a2fc16d1cc26070114ae6e908107cf211e0c99e/docs/roles/delivery-lead.md); [scripts/agent-onboard.sh](https://github.com/qujck/harness/blob/9a2fc16d1cc26070114ae6e908107cf211e0c99e/scripts/agent-onboard.sh)
- Basis: structural
- Confidence: medium-high
- Caveats: Source-relative ownership/reachability finding; no live model or effectiveness test.
- Claim being audited: developer's completed PR implements ticket requirements without defects.
- Ordinary reporting path: developer handover/test readings and CI to the lead.
- Complementary access path: reviewer reads original ticket/diff/code/tests and sibling callers to falsify the claim.
- Independence boundary: separate session/role; no code writes, no author-to-reviewer routing; judgment belongs to reviewer, corrective acceptance to lead.
- Who acts on findings: lead decides hold/repair and developer revises, with reviewer re-engaged after new commits.

## S4 — Outside-and-then intelligence

- State: —
- Function: no supplied externally prospective adaptation dialogue with current capability.
- Disturbance / variety regulated: changing future technology/user environment.
- Decisive decision or feedback right: no function-specific prospective adaptation judgment established.
- Decision owner: none established; process-improvement holder has current pipeline duties.
- Supporting / enforcement mechanisms: process records, trials, pipeline measurements and role rules.
- Closure path: internal pipeline improvement/record rulings are not a demonstrated outside-and-then capability loop.
- Why this is / is not agent-owned: roles and measurements do not by themselves establish S4; positive/parent alternatives were checked first.
- Evidence: [docs/roles/process-improvement.md](https://github.com/qujck/harness/blob/9a2fc16d1cc26070114ae6e908107cf211e0c99e/docs/roles/process-improvement.md); [METHOD.md](https://github.com/qujck/harness/blob/9a2fc16d1cc26070114ae6e908107cf211e0c99e/METHOD.md); [docs/roles/delivery-lead.md](https://github.com/qujck/harness/blob/9a2fc16d1cc26070114ae6e908107cf211e0c99e/docs/roles/delivery-lead.md)
- Basis: structural
- Confidence: medium-high
- Caveats: Source-relative ownership/reachability finding; no live model or effectiveness test.

### Absence scope

- Surfaces inspected: process-improvement and lead terms, measurement method, pipeline runbook and configuration.
- Plausible first-party paths checked: trials/falsifiers, reason-expiry/re-ask rules, owner process approval and queueing improvements.
- Why no material first-party path remains: These regulate present delivery process; no supplied external/future model, adaptation option owner and return into current capability closes S4. An arbitrary future process ticket is not a shipped path.

## S5 — Policy and identity

- State: —
- Function: no runtime ultimate identity-policy adjudication path at the configured team boundary established.
- Disturbance / variety regulated: identity/ultimate-policy conflict between operations and adaptation.
- Decisive decision or feedback right: owner's product/budget permissions and standing rules do not alone specify identity-level closure.
- Decision owner: no qualifying S5 decision arrangement established.
- Supporting / enforcement mechanisms: AGENTS, dated owner words, DECISIONS and role permissions.
- Closure path: ordinary task/resource/process decisions return through the lead; no distinct ultimate-policy tension and resolution-return arrangement supplied.
- Why this is / is not agent-owned: budget authority is S3 here; prompts, configuration and generic owner final say are not promoted to S5.
- Evidence: [AGENTS.md](https://github.com/qujck/harness/blob/9a2fc16d1cc26070114ae6e908107cf211e0c99e/AGENTS.md); [docs/roles/delivery-lead.md](https://github.com/qujck/harness/blob/9a2fc16d1cc26070114ae6e908107cf211e0c99e/docs/roles/delivery-lead.md); [docs/roles/process-improvement.md](https://github.com/qujck/harness/blob/9a2fc16d1cc26070114ae6e908107cf211e0c99e/docs/roles/process-improvement.md)
- Basis: structural
- Confidence: medium-high
- Caveats: Source-relative ownership/reachability finding; no live model or effectiveness test.

### Absence scope

- Surfaces inspected: role authority chains, AGENTS owner escalation, reason-expiry and decision-record rules.
- Plausible first-party paths checked: product questions to owner, invasive-action consent, budget exceptions and changes to process rules.
- Why no material first-party path remains: These are ordinary operational/permission channels. No identity-policy issue → legitimate ultimate authority → governing operational settlement is supplied at the reviewed team recursion; historical template owner quotes are not a live S5 witness.

## Distributed OSS parent arrangement

The configured local project owner owns budget exceptions and revisions, returned via quoted words and recorded adjustments to subsequent spawning. This is a local team S3 parent mode, not governance of qujck's public development organization or S5 authority.

## Self-hosted and non-human modes

Local tmux/Claude and ledger deployment is supported. No model task, account usage probe or production service was executed for this assessment. Retired/example roster entries do not prove a live non-human organization.

## Recursion

Ticket workers have local discretion but no separately established full metasystem. A worktree or process is not recursive viability.

## Variety and escalation

Identity provenance, remote claim locks and isolated worktrees reduce concurrent corruption; budget telemetry and idle/waiting hooks bring current team constraints to a lead. Notifications alone do not own S3. Owner budget answers alter admissible future starts; ordinary completion, reviewer and owner channels remain distinct.

## Evidence gaps

No live configured team was observed. The missing head-of-testing.md and tester.md referenced by AGENTS are not credited; a real whole-system audit by those roles remains unverified. The code-reviewer path used below is present but must be separately commissioned and connected. Generic messaging instructions assume host support, and operator words are a procedural authorization record rather than cryptographic identity enforcement.
