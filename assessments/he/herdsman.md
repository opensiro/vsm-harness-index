---
harness_id: herdsman
project_name: herdsman
repository: https://github.com/jirathip-dev/herdsman
review_ref: efd970e817c2021439c5415739e695f4af119b1d
reviewed_at: 2026-11-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# herdsman

## Review boundary

- System in focus: one installed herdsman Rust fleet conductor, its configured GitHub-issue queues, isolated coding/review lanes, append-only event log, drive loop, hard merge gates and human owner interface.
- Purpose and identity: carry bounded software changes from issue to tested/reviewed integration while making agent actions, capacity, refusals and owner decisions accountable.
- Relevant environment: evolving GitHub issues and PR heads, failing CI, cross-branch collisions, host load and storage, remote agent runners, human approvals and fleet resource constraints.
- Standard-distribution boundary: `herdsman` CLI/core/server, `fleet.toml`, herdr lanes and first-party role prompts/hooks, logged state, drive/timer and phone board. External Claude/Hermes/dsh engines, herdr substrate, GitHub and cloud provisioning are dependencies; their independent organizations are not credited.
- Credited operating / distribution surfaces: [README supported CLI and gates](https://github.com/jirathip-dev/herdsman/blob/efd970e817c2021439c5415739e695f4af119b1d/README.md), [architecture and event log](https://github.com/jirathip-dev/herdsman/blob/efd970e817c2021439c5415739e695f4af119b1d/docs/architecture.md), [staged pipeline](https://github.com/jirathip-dev/herdsman/blob/efd970e817c2021439c5415739e695f4af119b1d/docs/pipeline.md), [agent lanes](https://github.com/jirathip-dev/herdsman/blob/efd970e817c2021439c5415739e695f4af119b1d/docs/lanes.md), [drive implementation](https://github.com/jirathip-dev/herdsman/blob/efd970e817c2021439c5415739e695f4af119b1d/crates/core/src/drive.rs).
- Adjacent first-party surfaces excluded from ownership: example demo/cache data, CI/tests used to validate herdsman itself, UI themes and snapshots, development cap-history, and contributor governance of the upstream OSS project rather than the installed fleet.
- First-party operating / deployment modes considered: single-host or multi-host lanes, timers/kicks/fast drive, custom pipeline, Claude and Hermes implementer/reviewer roles and dsh beta, host admission, conflict preview, owner-only asks/answers and manual board intervention.
- Recursion level: a configured fleet overseeing multiple issue-level operational cells; the roles within each issue do not each show an independent complete S3–S5 metasystem.
- Reviewed revision: `efd970e817c2021439c5415739e695f4af119b1d`.
- Observation date: 2026-11-04.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The core stores each fleet's lifecycle in an append-only event log and reconstructs issue/queue state from it. An installed `drive` pass uses the queue, snapshots, GitHub PR/CI state and resource gates to spawn an implementer; a pushed head causes a distinct reviewer lane; a verdict pins the reviewed head; passing CI and merge policy allow integration. FAIL sends findings back to an implementation round; conflict/behind sends an update round; exhausted limits or owner topics park for human action. The server exposes a phone board with pause, answers, approvals and lane status. Host admission, isolated worktrees, the lane hook and custom pipeline remain first-party deterministic controls around model-using coding agents. [Architecture](https://github.com/jirathip-dev/herdsman/blob/efd970e817c2021439c5415739e695f4af119b1d/docs/architecture.md); [drive](https://github.com/jirathip-dev/herdsman/blob/efd970e817c2021439c5415739e695f4af119b1d/docs/lanes.md); [merge gate](https://github.com/jirathip-dev/herdsman/blob/efd970e817c2021439c5415739e695f4af119b1d/crates/core/src/gate.rs).

## Operational model

The herdsman constructor selects the next lifecycle step and enforces queue, capacity, review, branch and authority limits. Within a lane, the configured external agent model has actual scoped coding or adversarial review choices: an implementer reads an issue brief and changes code/tests; an isolated reviewer inspects the diff against acceptance criteria, reruns checks and records PASS/FAIL. Herdr and models execute the roles, but the implemented fleet role wiring, event feedback and refusal paths belong to herdsman. The project expressly disclaims an AI orchestrator: automatic portfolio transitions are deterministic, not evidence of an agent-governed S3. [Role boundary](https://github.com/jirathip-dev/herdsman/blob/efd970e817c2021439c5415739e695f4af119b1d/docs/pipeline.md); [implementation mandate](https://github.com/jirathip-dev/herdsman/blob/efd970e817c2021439c5415739e695f4af119b1d/roles/impl.md); [review mandate](https://github.com/jirathip-dev/herdsman/blob/efd970e817c2021439c5415739e695f4af119b1d/roles/rev.md).

## S1 — Operations

- State: A
- Function: configured coding agent lanes implement and repair requested changes; separately tasked review agents exercise real task-specific judgment on code/tests.
- Disturbance / variety regulated: new issue requirements, unknown codebase state, implementation errors, test failures and review findings.
- Decisive decision or feedback right: choose which code and tests to change, what fixes to make and how to respond with evidence to reviewer findings within the owner-authorized issue.
- Decision owner: model-based implementer and, for their bounded verification output, reviewer roles launched under the fleet pipeline; the deterministic `drive` merely chooses when to launch the next stage.
- Supporting / enforcement mechanisms: herdr worktree/pane spawn, issue brief, role prompts, profile hooks, PR cache, head-pinned verdicts and event log.
- Closure path: issue queued → implementer writes/tests/pushes change → reviewer evaluates exact head → FAIL returns findings to fix lane or PASS and green CI lead through merge gate → code reaches integration branch.
- Boundary reachability: `drive` and timers launch the roles by supported fleet settings, and the named default pipeline wires their outputs back to future steps; this is not a unit-test-only role.
- Why this is / is not agent-owned: code edits, targeted tests and adversarial judgments require meaningful agent choices; herdsman's hard transition and merge checks are constructor enforcement, not additional autonomous S1 judgment.
- Evidence: [role instructions](https://github.com/jirathip-dev/herdsman/blob/efd970e817c2021439c5415739e695f4af119b1d/roles/impl.md), [spawn source](https://github.com/jirathip-dev/herdsman/blob/efd970e817c2021439c5415739e695f4af119b1d/crates/core/src/spawn.rs), [pipeline](https://github.com/jirathip-dev/herdsman/blob/efd970e817c2021439c5415739e695f4af119b1d/docs/pipeline.md).
- Basis: documented supported operation plus pinned role and spawn wiring.
- Confidence: high for model role construction, bounded for outcomes without a provider-backed run in this review.
- Caveats: no agent executes without an installed, authenticated external harness and herdr; no unattended intelligence is attributed to the Rust scheduler itself.

## S2 — Coordination

- State: C
- Function: first-party conflict preview, serial integration gate and isolated lane worktrees attenuate specific interference among concurrently coding issue units.
- Disturbance / variety regulated: two issue agents editing overlapping files or branches cause rejected merges, overwrite/ordering hazards and repeated updates against the integration branch.
- Decisive decision or feedback right: detect file-level collisions with `git merge-tree`, show the specific conflicting paths, order ready PRs, enforce required serial groups and return the losing lane to update its branch before another reviewed merge.
- Decision owner: first-party deterministic `overlap`, `drive`, `gate` and serial-group rules; no model has a standing right to settle portfolio-wide branch conflicts by changing these policies.
- Supporting / enforcement mechanisms: isolated worktrees, cached head-pair collision preview, `HEADS-UP` prompts, exact-head verdicts, serial gate and update rounds with bounded retry.
- Closure path: conflicting concurrent heads → warning/serial ordering and first merge → implementer of later head receives update instruction and incorporates integration → fresh reviewer verdict and CI → next eligible merge.
- Boundary reachability: the installed `drive` calls overlap preview before action ordering, and the supported conflict/behind path actively spawns an update role.
- Why this is / is not agent-owned: concrete cross-issue contention is treated, but collision detection and merge precedence are coded invariants, not an autonomous S2 decision owner; this is `C`.
- Distinct S1 units: independently running implementer lanes for different issue worktrees in the same configured fleet.
- Inter-S1 disturbance: overlapping file edits and stale branch ancestry can make otherwise valid S1 output conflict at integration.
- Attenuating coordination relation: file-level preview and first-ready ordering, strict serial marking, integration update and mandatory fresh review.
- Feedback into subsequent S1 behaviour: later implementer gets exact conflicting paths/updated integration instructions, edits its work and pushes a changed head for another review.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the relation recognizes actual write-set/merge interference between independent S1 agents and closes that conflict through a change in what the later agent does.
- Evidence: [overlap source](https://github.com/jirathip-dev/herdsman/blob/efd970e817c2021439c5415739e695f4af119b1d/crates/core/src/overlap.rs), [drive conflicts and ordering](https://github.com/jirathip-dev/herdsman/blob/efd970e817c2021439c5415739e695f4af119b1d/crates/core/src/drive.rs), [lane conflict/update contract](https://github.com/jirathip-dev/herdsman/blob/efd970e817c2021439c5415739e695f4af119b1d/docs/lanes.md).
- Basis: directly implemented collision-specific runtime path and prompt feedback.
- Confidence: high for structural conflict attenuation; no claim of perfect prediction or autonomous negotiation.
- Caveats: an early heads-up is advisory and does not lock all overlapping files; a first reviewed merge may still force an update round.

## S3 — Inside-and-now control

- State: P
- Function: the human fleet owner sees the live issue/lane/host portfolio and can pause or resume a fleet, intervene in blocked work and decide current resource and merge envelopes.
- Disturbance / variety regulated: excessive concurrent lanes, host pressure, stalled fixes, owner questions and unwanted work on active issues.
- Decisive decision or feedback right: use the phone board/CLI to pause or resume, move/park an issue, answer owner asks, extend review rounds or grant the narrow owner override without bypassing exact-head review and CI.
- Decision owner: fleet owner/operator. `drive` computes the next mechanically valid transition, but does not set purpose/priorities as an AI metasystem.
- Supporting / enforcement mechanisms: live status, board and need-you cards, logged pause/decision events, queue moves, host admission and owner-only intervention controls.
- Closure path: operator inspects current state → changes fleet pause/queue/decision or permitted round limit → next drive/kick reads event state and changes or withholds operational lane work.
- Boundary reachability: `pause`, `resume`, `ask`, `answer` and board actions are shipped CLI/server paths and `drive` reads the same event log, not aspirational UI only.
- Why this is / is not agent-owned: the human selects priorities and discretionary intervention; programmed drive and resource thresholds do not upgrade to S3 A.
- Whole-system current view: board shows queue, pipeline, lanes, host load, waiting and `needs-you` across a fleet.
- Current-control decision scope: current issue order, which work waits or proceeds, review rounds, host/cost envelope and capacity within configured policy.
- Evidence: [owner board and drive behavior](https://github.com/jirathip-dev/herdsman/blob/efd970e817c2021439c5415739e695f4af119b1d/docs/lanes.md), [live host control](https://github.com/jirathip-dev/herdsman/blob/efd970e817c2021439c5415739e695f4af119b1d/docs/hosts.md), [pause/answer implementation](https://github.com/jirathip-dev/herdsman/blob/efd970e817c2021439c5415739e695f4af119b1d/crates/core/src/lib.rs).
- Basis: explicit human command path and recorded return to scheduler.
- Confidence: high for supported owner mode; model-directed supervisor not established.
- Caveats: UI requires a running server/paired device; same control also exists through CLI.

## S3* — Complementary audit

- State: A
- Function: independent, adversarial reviewer agents inspect implementation code and objective acceptance evidence outside the implementer's self-report.
- Disturbance / variety regulated: plausible but incorrect implementation claims, tests proving only mocks, leaked secrets and unreviewed scope changes.
- Decisive decision or feedback right: read the actual diff and criteria, independently rerun tests and return a head-specific PASS/FAIL with blocking findings that the implementer must address.
- Decision owner: a separately launched read-only reviewer model in a distinct lane and role/profile; `verdict` and CI checks merely enforce validity and preserve its findings.
- Supporting / enforcement mechanisms: dedicated reviewer worktree, read-only pre-tool hook, `verdict.md` with reviewed 40-hex head and tests checked, exact-head gate and fresh check-round spawn.
- Closure path: implementation PR head → reviewer inspects raw code/tests/criteria independently → head-pinned verdict and findings → implementer fix or approved integration → new head invalidates prior verdict and is independently reviewed again.
- Boundary reachability: default and custom pipelines include independent `check` stages, distinct from `build`, with verified role constraints and `drive` spawns on pushed heads.
- Why this is / is not agent-owned: adversarial technical judgment belongs to a distinct model role that can reject claims, not a boolean test wrapper or the implementer's own confirmation.
- Claim being audited: implementation actually meets issue acceptance criteria and tests/PR description prove it.
- Ordinary reporting path: implementer diff, test report and PR claim.
- Complementary access path: independent checkout/diff, direct tests and head evidence against the original issue brief.
- Independence boundary: reviewer role is prohibited from writing code, commits, pushes and PR comments, uses its own lane and verifies the actual current head; the same external harness vendor may still provide both models.
- Who acts on findings: the subsequent implementer fix lane; herdsman's event/gate machine blocks merge until fresh PASS and green CI.
- Evidence: [reviewer role](https://github.com/jirathip-dev/herdsman/blob/efd970e817c2021439c5415739e695f4af119b1d/roles/rev.md), [review stage isolation](https://github.com/jirathip-dev/herdsman/blob/efd970e817c2021439c5415739e695f4af119b1d/docs/pipeline.md), [verdict source](https://github.com/jirathip-dev/herdsman/blob/efd970e817c2021439c5415739e695f4af119b1d/crates/core/src/gate.rs).
- Basis: mandatory shipped review workflow and access separation.
- Confidence: high for implemented audit path; reviewer accuracy not measured here.
- Caveats: separate role/worktree provides process and tool isolation, not external institutional independence; no live paid provider review was performed in this assessment.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party prospective outside-environment interpretation and return into enduring fleet capability changes was established.
- Disturbance / variety regulated: new coding models, repository ecosystems, infrastructure economics and future workloads might eventually require adaptation.
- Decisive decision or feedback right: no internal future-environment option selection and promotion right evidenced; host choices and code paths are bounded to present work/load.
- Decision owner: not established for a separate S4 loop; fleet configuration and infrastructure upgrade choices remain with humans.
- Supporting / enforcement mechanisms: host-history sampling, cost ceiling, `doctor`, backlog, context prompts and issue queue.
- Closure path: observed present host pressure can deny a lane or start a configured cloud overflow host, but no projected external future becomes a selected enduring fleet strategy returned to implementation.
- Why this is / is not agent-owned: capacity observation is near-term S3/operational admission, and repository improvement by contributors is outside the installed fleet recursion.
- Evidence: [host placement and budget](https://github.com/jirathip-dev/herdsman/blob/efd970e817c2021439c5415739e695f4af119b1d/docs/hosts.md), [architecture and scope](https://github.com/jirathip-dev/herdsman/blob/efd970e817c2021439c5415739e695f4af119b1d/docs/architecture.md).
- Basis: bounded negative source review of shipped operating modes.
- Confidence: medium-high for missing S4 closure in the reviewed modes.
- Caveats: future model/host choice by the operator is possible but not credited as installed autonomous S4.

### Absence scope

- Surfaces inspected: `drive`, host placement/overflow, account/model selection, event history, remote host bootstrap, pipeline configuration and role prompts.
- Plausible first-party paths checked: host-history trends, auto cloud overflow, model/profile switching, round retries, issue queue intake and automated remote updates.
- Why no material first-party path remains: these enforce current load, maintain compatibility or complete already-scoped issues; none independently discovers a future environment, proposes a strategic capability change and returns the selected option to a durable new policy.

## S5 — Policy and identity

- State: —
- Function: no first-party loop was established that brings an identity- or ultimate-policy-level issue to legitimate authority and returns the binding result to govern the fleet as a coherent organization.
- Disturbance / variety regulated: changing the fleet's ultimate mission, reconciling external future adaptation with current obligations, or revising the constitutional distribution of authority could require such a loop.
- Decisive decision or feedback right: the owner may edit `fleet.toml` and decide scoped owner asks, but no shipped identity-level agenda or decision-return path was evidenced beyond those task and administration actions.
- Decision owner: not established for S5 at the declared fleet recursion; ultimate responsibility remains with the human owner outside the demonstrated herdsman function.
- Supporting / enforcement mechanisms: owner/routine ask classifier, `OWNER_TOPIC` refusal, no-default owner answer, protected branches, command hooks, limit settings and fleet configuration.
- Closure path: owner decisions are returned to individual tasks and settings bind future runs, but there is no demonstrated loop from an organization-level identity dispute through deliberation to a revised ultimate charter applied by the fleet.
- Boundary reachability: task-level owner asks and configuration commands are shipped; their existence is not by itself S5 closure.
- Why this is / is not agent-owned: approval for secrets, cost or scope during a single implementation may be important safety governance without constituting identity/policy-level VSM S5.
- Evidence: [owner/routine decision contract](https://github.com/jirathip-dev/herdsman/blob/efd970e817c2021439c5415739e695f4af119b1d/docs/lanes.md), [ask/answer code](https://github.com/jirathip-dev/herdsman/blob/efd970e817c2021439c5415739e695f4af119b1d/crates/core/src/lib.rs), [fleet policy and gate](https://github.com/jirathip-dev/herdsman/blob/efd970e817c2021439c5415739e695f4af119b1d/docs/pipeline.md).
- Basis: bounded negative first-party review, distinguishing task authorization from ultimate-policy closure.
- Confidence: medium-high for this scoped absence; an independently organized human governance layer is not ruled out.
- Caveats: this does not deny that an operator can govern or change herdsman outside the built fleet workflow.

### Absence scope

- Surfaces inspected: owner asks and defaults, pause/queue actions, protected-branch and command hooks, fleet configuration, pipeline rules and host budget controls.
- Plausible first-party paths checked: exceptional `--kind owner` questions about scope/secrets/production, persistent fleet config edits, owner-only host decisions and review-round overrides.
- Why no material first-party path remains: each path addresses current task authority, safety enforcement or direct operator configuration, without a evidenced identity-level agenda, legitimate adjudication and binding revised organizational policy returned through a single S5 loop.

## Distributed OSS parent arrangement

The herdsman software's GitHub maintainer organization is outside the installed multi-issue fleet. A user-configured fleet owner has a first-party S3(P) path through the CLI/config/board and retains safety/policy authority, but that alone does not satisfy the S5 identity-level test. Upstream OSS contributors and external model vendors are not promoted to fleet-level S5.

## Self-hosted and non-human modes

herdsman can drive a fleet unattended with a timer and owner-defined rules, but an owner ask stops rather than silently defaults. Model agents perform S1 and review decisions; fixed code handles coordination and stage progression. An owner-configured no-human-run period does not produce S3/S5 A, and the retained parent authority alone is insufficient to claim S5(P).

## Recursion

Issue-level build/check lanes are differentiated operational cells within the fleet. The queue/pipeline has one supervisory closure, not proof that every child agent independently carries a viable five-function organization. Multiple fleet blocks share the conductor but do not establish a novel higher-tier autonomous S5.

## Variety and escalation

Role prompts and configurable harnesses amplify implementation and scrutiny variety. Queue, host admission, worktree segregation, collision preview, exact-head review/CI and refusal hooks attenuate it. Repeated review failures, dangerous asks or exhausted rounds escalate to `needs-human`; owner intervention is logged and returned to the relevant lane, not inferred from a mere notification.

## Evidence gaps

- Pinned README, documentation, Rust runtime and role prompts reviewed; no authenticated Claude/Hermes or remote host was run, so observed execution quality and process isolation under every provider remain unverified.
- S2 file-collision preview is a constructor path with a real write-conflict target, but does not guarantee zero cross-lane interference or autonomous coordination.
- S3* independence is a fresh role/worktree/tool separation inside one configured workflow, not an external auditor's guarantee.
- Owner asks and standing fleet config establish important human authority but not an independent identity-level S5 closure path at this recursion.
