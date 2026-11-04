---
harness_id: metaorcha
project_name: Metaorcha
repository: https://github.com/solvent-labs-org/metaorcha
review_ref: 8dd8bb23b95339bb32bb2c12d23d03fb94ad1c6d
reviewed_at: 2026-11-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Metaorcha

## Review boundary

- System in focus: Metaorcha's installable open-source **MetaBot** local agent runner, particularly its bundled `metabot ask` / ladder and configured multi-agent Code Desks `office` modes, operating one user task. This is the concrete user-facing standard distribution emphasized in the repository's primary README.
- Purpose and identity: use signed-in external coding agents or a configured local model server to perform controlled coding work, with explicit tool gating, signed receipts, isolated desk branches, configurable independent advisors and operator selection of finished work.
- Relevant environment: the user's task and repository, local CLI engines/models, optional MCP connections, execution logs, branch diffs, acceptance checks, human permissions, available money/turn budgets, task-specific office configuration and desk outputs.
- Standard-distribution boundary: `uv tool install orcha-metabot` with its published CLI/runner, engine bridge, `office.yaml` loader, desk execution, optional advisors, budget/approval gate and signed receipt verifier. The connected Claude/Codex/Cursor or local OpenAI-compatible model provides the first-party supported operational agent decision actor; its unrelated platform functions are not borrowed.
- Credited operating / distribution surfaces: [top-level README](https://github.com/solvent-labs-org/metaorcha/blob/8dd8bb23b95339bb32bb2c12d23d03fb94ad1c6d/README.md), [MetaBot operating modes](https://github.com/solvent-labs-org/metaorcha/blob/8dd8bb23b95339bb32bb2c12d23d03fb94ad1c6d/apps/metabot/README.md), [office model](https://github.com/solvent-labs-org/metaorcha/blob/8dd8bb23b95339bb32bb2c12d23d03fb94ad1c6d/apps/metabot/src/metabot/office.py), [desk/advisor runner](https://github.com/solvent-labs-org/metaorcha/blob/8dd8bb23b95339bb32bb2c12d23d03fb94ad1c6d/apps/metabot/src/metabot/office_run.py), and [advisor behavior tests](https://github.com/solvent-labs-org/metaorcha/blob/8dd8bb23b95339bb32bb2c12d23d03fb94ad1c6d/apps/metabot/tests/test_office_advisor.py).
- Adjacent first-party surfaces excluded from ownership: the repository's separately deployed gateway/superagent/planning-discovery distributed service platform, SDK scaffolding and attestation playground, development AGENTS.md, CI/tests/roadmap as autonomous actors, independently installed external Code Desks runtime, and the user's vendor account's unrelated behavior. These are documented sibling products/authoring surfaces, not silently imported into the MetaBot task-cell assessment.
- First-party operating / deployment modes considered: direct `metabot ask`/`chat`, fallback ladder with checks, scheduled user-defined routines, configured Code Desks relay/fan offices and opt-in `--advisors`, read-only reviewers and office `--until-checks` loops, operator `desks pick`; local/OpenAI-compatible or signed-in external engine. No claim that a default office exists without the user/configured `office.yaml` and role files.
- Recursion level: one local MetaBot task/office instance with operational desk subunits and a supervising user, not Metaorcha OSS project governance.
- Reviewed revision: `solvent-labs-org/metaorcha@8dd8bb23b95339bb32bb2c12d23d03fb94ad1c6d` (Apache-2.0).
- Observation date: 2026-11-04.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

MetaBot drives supported external coding-agent CLIs or a configured model endpoint, applies a local gate to the tool calls it can observe, and signs local run journals/receipts. It supplies a model ladder with execution checks and a configurable multi-agent office. An `office.yaml` declares desks/roles, engine selection, optional `advises` reviewers and trusted acceptance commands. In a relay each desk gets its own Git worktree/branch based on the preceding desk's result; a fan runs bounded copies from one base. The first-party runner creates and cleans desk worktrees, passes earlier outputs in a new desk's inbox, runs optional checks/rounds and offers resulting branches to the user. A configured advisor is a separate model run in a detached read-only worktree at the actual reviewed commit; it sees the target's raw changes, judges what is wrong/missing, and its advice is delivered to later desks and the user. Offline signature verification establishes integrity of claimed records, **not** actual correctness or independent auditing of the task. [MetaBot README](https://github.com/solvent-labs-org/metaorcha/blob/8dd8bb23b95339bb32bb2c12d23d03fb94ad1c6d/apps/metabot/README.md), [office implementation](https://github.com/solvent-labs-org/metaorcha/blob/8dd8bb23b95339bb32bb2c12d23d03fb94ad1c6d/apps/metabot/src/metabot/office_run.py).

## Operational model

The user submits a task or starts a configured office. Individual model agents investigate/modify code in desk worktrees and return results; the runner captures diffs and run receipts. Model-capable advisors separately inspect what a prior desk actually changed. The local human operator sets office roles, acceptance gates, run bounds, selects desks and eventually picks one completed branch for the current checkout. The office execution order, retry-on-failed-checks and cryptographic verification are mostly predefined mechanisms, not autonomous management policy. This assessment distinguishes agent S1 work and independent advisory audit from parent-user current whole-office control.

## S1 — Operations

- State: A
- Function: perform coding and other bounded requested work through supported coding-agent/model engines, including several independent implementation desks when an office is configured.
- Disturbance / variety regulated: varied coding tasks, source context, failed tool calls, failing tests and alternative implementation approaches.
- Decisive decision or feedback right: invoked model agents independently choose task-specific tool calls, code changes and responses to actual results within their configured roles and permits.
- Decision owner: each run's Claude/Codex/Cursor/local-model agent, launched in the first-party MetaBot `ask` or office execution path; MetaBot supplies execution/gating and provenance.
- Supporting / enforcement mechanisms: engine adapters, per-call authorization, worktree/branch isolation, role files, bounded turns/cost, signed receipts and checks.
- Closure path: user/office task → a supported model agent receives current project and role → agent reads/edits/executes → real tool/result feedback → model continuation and output on its own task branch.
- Boundary reachability: README and CLI expose installed `metabot ask` and `metabot office run`, with model engines and real worktree execution; no test-only actor is needed for the claim.
- Why this is / is not agent-owned: source-dependent coding choices are made by model agents; the gate, branch-copy routine and receipt signer cannot themselves decide a bug fix.
- Evidence: [MetaBot engines and tool operation](https://github.com/solvent-labs-org/metaorcha/blob/8dd8bb23b95339bb32bb2c12d23d03fb94ad1c6d/apps/metabot/README.md), [office runner](https://github.com/solvent-labs-org/metaorcha/blob/8dd8bb23b95339bb32bb2c12d23d03fb94ad1c6d/apps/metabot/src/metabot/office_run.py), [office tests](https://github.com/solvent-labs-org/metaorcha/blob/8dd8bb23b95339bb32bb2c12d23d03fb94ad1c6d/apps/metabot/tests/test_office_run.py).
- Basis: explicit and structural.
- Confidence: high.
- Caveats: users must configure/sign into engines, supply an office file for multi-desk mode and grant writes where appropriate; CLI local runs are not evidence of remote multi-tenant deployment.

## S2 — Coordination

- State: —
- Function: no distinct agent-owned inter-S1 disturbance-regulation and return loop established for concurrently active desks.
- Disturbance / variety regulated: several desks can produce conflicting alternatives against the same repository, but the shipped response is separate worktrees/branches and later comparison or parent selection.
- Decisive decision or feedback right: no material shipped agent authority to sense competing *ongoing* desk interference and return an attenuation decision to adjust those desks' subsequent operation.
- Decision owner: predefined relay/fan topology, isolated branches and final operator selection; individual advisors inspect completed work rather than coordinate simultaneous interference.
- Supporting / enforcement mechanisms: desk-specific worktrees, capped fan, relay handoff/inbox, branch comparison, trusted checks, budget gates.
- Closure path: isolated fan/relay alternatives → subsequent desk may compare or operator picks an outcome; a specific inter-operational oscillation feedback loop is not demonstrated.
- Why this is / is not agent-owned: branch isolation and passing completed results are valuable safety/hand-off mechanisms, but do not suffice for a separately accountable S2 coordinator.
- Evidence: [office modes and fan/relay semantics](https://github.com/solvent-labs-org/metaorcha/blob/8dd8bb23b95339bb32bb2c12d23d03fb94ad1c6d/apps/metabot/README.md), [office runner](https://github.com/solvent-labs-org/metaorcha/blob/8dd8bb23b95339bb32bb2c12d23d03fb94ad1c6d/apps/metabot/src/metabot/office_run.py).
- Basis: structural.
- Confidence: medium.
- Caveats: a user-authored desk prompt could instruct coordination, but that is not a function-specific first-party S2 agent loop in the inspected distribution.

### Absence scope

- Surfaces inspected: desk model and runner, relay/fan branch topology, advice delivery, checks-driven rounds, budget/concurrency limits and picks.
- Plausible first-party paths checked: multiple active desks, competing alternatives, inbox handoffs, advisor findings, failed checks and user branch selection.
- Why no material first-party path remains: these are isolated alternatives, sequential downstream review or fixed retry, without an agent-owned decision returned to regulate interference among multiple still-operating S1 cells.

## S3 — Inside-and-now control

- State: P
- Function: parent-user whole-office task control over roles, execution shape, acceptance constraints and adoption of completed work in the current checkout.
- Disturbance / variety regulated: differing desk work, unacceptable results, trust/cost limitations, conflicting output branches and risk of automatically committing an unaccepted candidate.
- Decisive decision or feedback right: the operator chooses which desks and modes run, supplies trusted checks and run limits, reviews the results/receipts/advisor outputs and selects a particular finished branch with `metabot desks pick` for staging into the real checkout.
- Decision owner: the legitimate human operator of the local office; MetaBot's CLI/UI is the current-control actuator and desk agents are supervised operations, not independent whole-office priority owners.
- Supporting / enforcement mechanisms: `office.yaml`, `office check/trust/run`, per-desk result statuses, signed office seal, local page and `desks list/pick`, deterministic checks/round limits.
- Closure path: operator-visible whole-office run and competing branch outcomes → operator chooses desk scope/acceptance and final branch to pick → MetaBot runs the selected commitments or stages the chosen branch into the real worktree → next current operation builds on that outcome.
- Boundary reachability: the installed MetaBot CLI documents and implements `office run --desks/--fan/--until-checks` and `desks pick` with local user authority; this is not inferred from OSS maintainer governance.
- Why this is / is not agent-owned: models produce each desk's work but the precommitted office shape and decisive choice of the actual branch for the current checkout remain the user's; machine checks cannot replace that discretionary adoption judgment.
- Whole-system current view: the configured office, its selected desk/copy roster, run status, advice, checked receipts, candidate branches and completion offers shown through CLI/UI.
- Current-control decision scope: task-wide resource/commitment choice (desks, fan, cost/rounds, trusted acceptance gates) and which candidate becomes current workspace work, not the repository owner's ultimate project identity.
- Evidence: [office user controls and pick semantics](https://github.com/solvent-labs-org/metaorcha/blob/8dd8bb23b95339bb32bb2c12d23d03fb94ad1c6d/apps/metabot/README.md), [office result/offer and runner](https://github.com/solvent-labs-org/metaorcha/blob/8dd8bb23b95339bb32bb2c12d23d03fb94ad1c6d/apps/metabot/src/metabot/office_run.py), [office command controls](https://github.com/solvent-labs-org/metaorcha/blob/8dd8bb23b95339bb32bb2c12d23d03fb94ad1c6d/apps/metabot/src/metabot/office_commands.py).
- Basis: explicit and structural.
- Confidence: medium.
- Caveats: `P` here is specific to an explicitly configured multi-desk office. Generic per-tool approval alone would not qualify; user control of whole current desk commitments and returned branch adoption establishes the bounded parent mode. No separately closed autonomous S3 office manager is claimed.

## S3* — Complementary audit

- State: A
- Function: independently review an operating desk's actual code changes and return corrective advice to later desks and the office owner.
- Disturbance / variety regulated: a build desk can produce incorrect, incomplete or overclaimed work that its own completion report fails to reveal.
- Decisive decision or feedback right: a separately launched, role-configured read-only advisor agent inspects the target desk's actual committed worktree/diff, judges what is wrong or missing and formulates advice about what to change.
- Decision owner: the advisor's independent model/engine session, not the builder or receipt verifier; the operator decides whether to select the branch and later desks receive the advice.
- Supporting / enforcement mechanisms: `advises` mapping in `office.yaml`, detached read-only worktree, `git diff` with actual base, separate run/receipt, `.metabot/inbox` output and CLI advice display.
- Closure path: builder's final commit/report → separate advisor opened on real builder worktree with raw diff access → advisor judgment written as a separate artifact → later desk receives the advice in its own inbox and operator sees it before picking results.
- Boundary reachability: `metabot office run` supports first-party configured advisor desks and automatic post-build review; tests exercise the detached worktree, read-only protection and advice delivered to the next desk and user.
- Why this is / is not agent-owned: the advisor model, in a separate session, decides which defects matter; deterministic signed receipts, checks and worktree snapshots merely preserve evidence and transfer the findings.
- Claim being audited: a completed builder desk's source changes and claimed task correctness.
- Ordinary reporting path: the builder's own answer and branch/receipt.
- Complementary access path: advisor's separate detached worktree at the builder's committed HEAD, with raw file reads and `git diff` against the builder's prior base.
- Independence boundary: distinct desk role, fresh engine invocation and read-only worktree that cannot alter/commit the builder's code; it is launched after the target finishes rather than reusing the builder's claim as truth.
- Who acts on findings: downstream desk receives the persisted advice in its work inbox; the human office owner sees the same advice while deciding which candidate to adopt.
- Evidence: [advisor prompt with raw diff and read-only requirement](https://github.com/solvent-labs-org/metaorcha/blob/8dd8bb23b95339bb32bb2c12d23d03fb94ad1c6d/apps/metabot/src/metabot/office_run.py), [advisor model configuration](https://github.com/solvent-labs-org/metaorcha/blob/8dd8bb23b95339bb32bb2c12d23d03fb94ad1c6d/apps/metabot/src/metabot/office.py), [test: advice delivered to later desk and person](https://github.com/solvent-labs-org/metaorcha/blob/8dd8bb23b95339bb32bb2c12d23d03fb94ad1c6d/apps/metabot/tests/test_office_advisor.py).
- Basis: explicit and structural.
- Confidence: medium.
- Caveats: advisor is an opt-in supported office configuration, not the default `metabot ask`; its advice is not a mandatory veto and its empirical correctness is not measured. Cryptographic receipt validity is **not** the S3* judgment.

## S4 — Outside-and-then intelligence

- State: —
- Function: no shipped future-environment sensing and operational-capability adaptation closure at the local task/office recursion.
- Disturbance / variety regulated: future engine availability, model quality and new tasks may require different capability, but configuration and fallback operate on the present user request.
- Decisive decision or feedback right: no separate agent with a supported future-focused adaptation judgment and adoption path into the office's standing capability established.
- Decision owner: operator for installed engines, office roles, routines and future configuration; ladder uses specified current-task success/failure conditions.
- Supporting / enforcement mechanisms: model roster, current-task ladder/fallback, schedule-triggered routines, source plugins and operator config.
- Closure path: no evidenced prospective outside/then intelligence → adaptation proposal → authorized changed current capability path.
- Why this is / is not agent-owned: retries, model escalation when a test fails, scheduled goal execution and manual configuration do not themselves constitute strategic sensing and capability adaptation.
- Evidence: [ladder and routines](https://github.com/solvent-labs-org/metaorcha/blob/8dd8bb23b95339bb32bb2c12d23d03fb94ad1c6d/apps/metabot/README.md), [roster](https://github.com/solvent-labs-org/metaorcha/blob/8dd8bb23b95339bb32bb2c12d23d03fb94ad1c6d/apps/metabot/README.md).
- Basis: structural.
- Confidence: medium.
- Caveats: a human may revise future office configuration based on experience, but that separately governed prospective loop was not evidenced as a first-party task-cell function.

### Absence scope

- Surfaces inspected: model ladder, role/roster selection, scheduled routines, office re-runs, user-configured engines and plugins.
- Plausible first-party paths checked: adaptive fallback after failure, cost-based model routing, future timed tasks, plugin upgrades and creation of office role definitions.
- Why no material first-party path remains: inspected decisions concern current run recovery or explicit user configuration; none carries an evidenced external-prospective adaptation loop into revised standing capability.

## S5 — Policy and identity

- State: —
- Function: no identity/ultimate-policy issue resolution closed at this local MetaBot office recursion.
- Disturbance / variety regulated: risk of destructive tool calls, private data exposure and untrusted engines/skills calls for permissions, but these are operating policy constraints.
- Decisive decision or feedback right: no actor is shown adjudicating the ultimate identity/purpose of the office and returning authoritative policy; user approves/denies individual risk categories and sets fixed gate rules.
- Decision owner: operator outside the operational agent cell for task permissions; local gate and signed journal enforce/capture provided authorizations.
- Supporting / enforcement mechanisms: read/write/destructive gate, yes/no challenge, signing key, per-connection policies, audit receipt and trusted checks.
- Closure path: operator-configured scope and per-call permission → enforced execute/refuse → signed report; no explicit identity-level dispute and returned whole-office governing policy path.
- Why this is / is not agent-owned: prompts, user gates, receipts and code-of-conduct are not a runtime ultimate-policy body.
- Evidence: [gate/permissions and receipts](https://github.com/solvent-labs-org/metaorcha/blob/8dd8bb23b95339bb32bb2c12d23d03fb94ad1c6d/apps/metabot/README.md), [control mechanisms](https://github.com/solvent-labs-org/metaorcha/blob/8dd8bb23b95339bb32bb2c12d23d03fb94ad1c6d/apps/metabot/src/metabot/control.py).
- Basis: structural.
- Confidence: medium.
- Caveats: separate deployed Metaorcha platform governance specifications and public OSS project policy are outside the selected MetaBot task-cell boundary.

### Absence scope

- Surfaces inspected: local execution gate, office configuration, trust checks, engine/connection setup, receipts and user UI.
- Plausible first-party paths checked: destructive approvals, private model routing, office owner picks, signed provenance, governance specs for separate service platform.
- Why no material first-party path remains: enforcement and task-level owner decisions do not form a genuine identity/ultimate-policy adjudication and returned policy-closure loop within the assessed office.

## Distributed OSS parent arrangement

MetaBot is installed locally by independent users. Each operator configures desks, engines, gates, office runs and resulting work selection; their agents do not share a public management plane. Maintainer governance of source code and the repository's separate distributed service platform are not imported into a local office run. The `P` S3 claim belongs to this local human-owned office, not the OSS organization.

## Self-hosted and non-human modes

The local OpenAI-compatible engine or signed-in coding agents can operate within MetaBot's first-party CLI loop; ordinary `ask` does not require a separate office. The configured office can contain multiple agent engines and independent advisors. The system deliberately does not commit or push to the user's main branch automatically; `desks pick` is a parent-owned result-selection mechanism.

## Recursion

Each desk is a bounded operational unit; advisers have a separate evidence-judgment role and own no code edits. Office configuration, parent result selection and checks define a task-local recursion. No claim is made that every individual desk or the receipt verifier is itself a complete viable organization.

## Variety and escalation

The run gate mediates risky tools, checks and ladder triggers respond to failed work with bounded retries, and individual runs/seals are cryptographically bound to their recorded evidence. These channels reduce risk and preserve provenance; they do not verify that work truly happened or is correct. The advisor supplies a distinct complementary source-code review path, while the operator chooses the ultimately adopted work.

## Evidence gaps

- Positive S3* concerns only offices with an explicitly configured advisor; a plain direct `metabot ask` has no such independent review. A downstream desk may receive advice without being forced to obey it.
- The assessed system is the separately installable first-party MetaBot product. The repository also contains a distinct container/service platform (`services/superagent`, planning-discovery, gateway), whose deployment and autonomy must not be silently composed with this local CLI office without a different system boundary.
- No live authenticated Claude/Codex/Cursor run or real user Git-worktree session was executed by this assessment; primary runtime instructions, implementation, and tests establish the documented paths, not empirical success rates.
