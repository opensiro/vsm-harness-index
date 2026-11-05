---
harness_id: ai-chassis
project_name: ai-chassis
repository: https://github.com/sergeiwallace/ai-chassis
review_ref: ea39de12db1308c2a46ac7ffab38ead14ce39aaf
reviewed_at: 2026-11-05
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# ai-chassis

## Review boundary

- System in focus: the public Apache-2.0 `ai-chassis` installation composed into an operator's local fleet of Claude Code/Codex coding-agent sessions and multiple Git repositories.
- Purpose and identity: reusable session configuration, skills, worktree isolation, job persistence, cross-session handoff, Git integration and audit evidence for concurrent coding agents.
- Relevant environment: competing edits and launches, context exhaustion, disjoint remote machines, stale worktrees, unreviewed changes, lost task/review state and multiple Git integration targets.
- Standard-distribution boundary: the first-party installed `ai-chassis` CLI/package, published `SKILL.md` procedures, scripts, templates and opt-in local job supervisor / messaging / Git-review mechanisms at the pinned public revision. External Claude Code/Codex sessions must be separately installed and authenticated.
- Credited operating / distribution surfaces: [public installation and mode inventory](https://github.com/sergeiwallace/ai-chassis/blob/ea39de12db1308c2a46ac7ffab38ead14ce39aaf/README.md), [Python package entry point](https://github.com/sergeiwallace/ai-chassis/blob/ea39de12db1308c2a46ac7ffab38ead14ce39aaf/pyproject.toml), [CLI composition and apply](https://github.com/sergeiwallace/ai-chassis/blob/ea39de12db1308c2a46ac7ffab38ead14ce39aaf/src/ai_chassis/cli.py), [job supervisor](https://github.com/sergeiwallace/ai-chassis/blob/ea39de12db1308c2a46ac7ffab38ead14ce39aaf/src/ai_chassis/job_supervisor.py), [message-board skill](https://github.com/sergeiwallace/ai-chassis/blob/ea39de12db1308c2a46ac7ffab38ead14ce39aaf/skills/message-board/SKILL.md), [Git reviewer](https://github.com/sergeiwallace/ai-chassis/blob/ea39de12db1308c2a46ac7ffab38ead14ce39aaf/scripts/git_review.py) and [audit packet construction](https://github.com/sergeiwallace/ai-chassis/blob/ea39de12db1308c2a46ac7ffab38ead14ce39aaf/scripts/review_packet.py).
- Adjacent first-party surfaces excluded from ownership: maintainer's explicitly unpublished private harness and history, future roadmap modules/services, release/CI safety tests, fixture-only proofs, uninstalled sample configuration, independent provider model internals, external `hlg` reviewer program and unverified user-specific Firstmate/Chief deployments.
- First-party operating / deployment modes considered: `ai-chassis init/plan/apply/doctor`; installed Claude/Codex agent plus published skills and rules; linked worktree per job; optional launched local job supervisor; message transport ladder; optional multi-repo `git-review`; constructed review packets/audit receipts. Unpublished roadmap features are not credited.
- Recursion level: the installed local fleet/worktree set owned by one user/organization, not the private multi-machine maintainer installation or independent governance of every upstream provider.
- Reviewed revision: `ea39de12db1308c2a46ac7ffab38ead14ce39aaf`.
- Observation date: 2026-11-05.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The published Python CLI composes shared context modules and per-machine overlays into local Claude/Codex sessions; it is a harness around externally supplied LLM coding agents, not its own model. Shipped skills describe spec approval, worktree/Git review, validated commits, durable cross-session handoffs, quality checks and shadow-Codex launch correlation. `job_supervisor` maintains an authoritative local job ledger, starts detached commands only from linked worktrees, prevents duplicate request-key creation and supports terminal-result claim/ack. The message-board procedure resolves one transport rung, refuses duplicate handoff across rungs, and treats received content as non-authoritative. `git_review` performs multi-repository inventory and can proof-check configured ship/merge actions against conservative policy before integration and readback. Evidence utilities can construct an exact Git-diff/test-result review packet and validate typed audit-receipt events. All require their own supported operator configuration and do not turn hypothetical private fleet components into credited first-party owners. [README](https://github.com/sergeiwallace/ai-chassis/blob/ea39de12db1308c2a46ac7ffab38ead14ce39aaf/README.md); [skills](https://github.com/sergeiwallace/ai-chassis/tree/ea39de12db1308c2a46ac7ffab38ead14ce39aaf/skills); [job supervisor](https://github.com/sergeiwallace/ai-chassis/blob/ea39de12db1308c2a46ac7ffab38ead14ce39aaf/src/ai_chassis/job_supervisor.py).

## Operational model

The human/operator supplies requests and configures which agents may act, in which worktrees and with what integration policy. Model-backed Claude/Codex sessions perform coding S1 work and invoke installed skills. First-party code implements specific coordination, evidence and multi-repo current-control *constructors*, but does not ship an independent AI supervisor that owns the fleet's final cross-project commitments. The public `quality-check` skill names external `hlg review`; since `hlg` is not supplied as a first-party decision owner, any independent model review obtained through it is not silently credited. [Public release limits](https://github.com/sergeiwallace/ai-chassis/blob/ea39de12db1308c2a46ac7ffab38ead14ce39aaf/README.md#status); [quality review skill](https://github.com/sergeiwallace/ai-chassis/blob/ea39de12db1308c2a46ac7ffab38ead14ce39aaf/skills/quality-check/SKILL.md).

## S1 — Operations

- State: A
- Function: externally installed Claude Code/Codex coding-agent sessions work on assigned repository tasks using first-party shared context, skills, tools and linked worktrees.
- Disturbance / variety regulated: code changes, errors and command/test observations within individual software tasks.
- Decisive decision or feedback right: a configured AI coding agent selects implementation, tool invocations and revisions after inspecting source and feedback; scripts constrain provenance and filesystem/Git operations.
- Decision owner: active Claude/Codex model-backed coding session in the documented assembled mode; external provider internals not automatically credited above task level.
- Supporting / enforcement mechanisms: per-machine context composer, installed skills (`spec`, `commit`, `quality-check`, `shadow-codex-launch`), Git/worktree helpers and provenance commits.
- Closure path: human/controller assigns a repository task → installed coding agent reads the composed context and uses tools in its linked worktree → model adapts to observed source/tests → writes/commits work with provenance → review/merge or rework returns into later agent work.
- Boundary reachability: the project ships installation and context-application CLI and actual `SKILL.md` entry points for Claude/Codex tools, explicitly assembling these available external agents; no proprietary private engine is required to run the published subset.
- Why this is / is not agent-owned: the live model chooses code and tool steps, unlike the deterministic provenance, commit and job-ledger checks.
- Evidence: [README usage and supported sessions](https://github.com/sergeiwallace/ai-chassis/blob/ea39de12db1308c2a46ac7ffab38ead14ce39aaf/README.md); [public CLI composition](https://github.com/sergeiwallace/ai-chassis/blob/ea39de12db1308c2a46ac7ffab38ead14ce39aaf/src/ai_chassis/cli.py); [planning skill](https://github.com/sergeiwallace/ai-chassis/blob/ea39de12db1308c2a46ac7ffab38ead14ce39aaf/skills/spec/SKILL.md); [validated commit skill](https://github.com/sergeiwallace/ai-chassis/blob/ea39de12db1308c2a46ac7ffab38ead14ce39aaf/skills/commit/SKILL.md).
- Basis: supported first-party agent integration and task feedback.
- Confidence: medium-high for assembled decision structure.
- Caveats: `ai-chassis` is not a model server; the actual provider and its private decision logic remain external, and no paid-provider E2E was run.

## S2 — Coordination

- State: C
- Function: worktree admission, idempotent job tracking and unique result claims prevent some inter-session collisions and duplicate work or handoff effects.
- Disturbance / variety regulated: two coding sessions operating in the same Git worktree, duplicate job submissions, competing terminal result claimants and repeated cross-host message sends.
- Decisive decision or feedback right: worktree/owner/transport choices are configured or selected by an operator/agent; the first-party supervisor rejects invalid main-worktree launch and conflicting result claims and idempotently returns the existing job ID.
- Decision owner: deterministic first-party coordination constructor, not a model that negotiates or revises conflict policy across S1 units.
- Supporting / enforcement mechanisms: `require_linked_worktree`, `Ledger.create_idempotent`, locked `claim`, job status/ack, worktree naming and one-transport message-board route.
- Closure path: incoming work is checked against linked worktree and request key → invalid/duplicate work is refused or bound to existing job; separate terminal claimants cannot both own the fresh result → sender resolves one handoff transport and receives corresponding status → later S1 work uses the non-duplicated job/message outcome.
- Boundary reachability: the Python `job_supervisor` has a runnable `daemon/submit/status/claim/ack` CLI, and the installed `message-board` SKILL names concrete transport and delivery procedures for working sessions; these are not mere roadmap diagrams.
- Why this is / is not agent-owned: a function-specific interference attenuation path exists, but the inter-S1 decision policy is configured and enforced by code. Additional autonomous coordination and guaranteed semantic non-conflict are not established.
- Distinct S1 units: independently running coding agents bound to separate linked worktrees, and possible peer sessions on another host.
- Inter-S1 disturbance: duplicate job starts/result claims and shared working-tree edits would corrupt attribution or overwrite another agent's work.
- Attenuating coordination relation: separate linked worktree admission, idempotency keys and exclusive claim with freshness checks; the transport ladder prevents duplicate handoff across channels.
- Feedback into subsequent S1 behaviour: duplicate submit returns the original job instead of starting another; rejected claim refuses a second consumer; incompatible source tree cannot launch; a completed handoff gives a single actionable receipt.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: source-level conflict checks forbid simultaneous incompatible owner claims and duplicated launches, not merely pass text or schedule tasks.
- Evidence: [job supervisor worktree and lock checks](https://github.com/sergeiwallace/ai-chassis/blob/ea39de12db1308c2a46ac7ffab38ead14ce39aaf/src/ai_chassis/job_supervisor.py#L45-L73); [idempotent submit and claim](https://github.com/sergeiwallace/ai-chassis/blob/ea39de12db1308c2a46ac7ffab38ead14ce39aaf/src/ai_chassis/job_supervisor.py#L893-L925); [exclusive result claim](https://github.com/sergeiwallace/ai-chassis/blob/ea39de12db1308c2a46ac7ffab38ead14ce39aaf/src/ai_chassis/job_supervisor.py#L1109-L1133); [message-board transport contract](https://github.com/sergeiwallace/ai-chassis/blob/ea39de12db1308c2a46ac7ffab38ead14ce39aaf/skills/message-board/SKILL.md).
- Basis: released runtime mechanisms with first-party ownership boundaries.
- Confidence: medium-high for narrow duplication/claim interference.
- Caveats: no generalized agent-authored negotiation or automatic resolution of competing code edits is supplied; worktrees isolate rather than semantically merge changes.

## S3 — Inside-and-now control

- State: C
- Function: the published cross-repository review/integration constructor inventories present fleet Git work, determines admissible ship/merge paths under explicit configured policy and returns readback status.
- Disturbance / variety regulated: multiple pending branches and worktrees, missing or stale integration evidence, unauthorized merge requests and uncertain work ownership across repositories.
- Decisive decision or feedback right: an authorized operator/repository policy must specify eligible integration paths; source code computes applicable candidates and refutes or executes eligible current integration. No first-party autonomous portfolio owner is shipped.
- Decision owner: current operator/configured repository merge policy, supported by deterministic first-party multi-repo decision-and-feedback constructor; code does not acquire independent organizational authority.
- Supporting / enforcement mechanisms: `git_review` multi-repository discovery/inventory, `ship_merge` preflight, `execute_merge`, exact terminal readback, job status and `status-update` skill.
- Closure path: review runs over registered repositories and active worktrees → inventories candidate work and current status → configured opt-in proof allows/refuses/queues integration → any authorized action is executed → authoritative merge readback updates current review/reclamation behavior.
- Boundary reachability: `scripts/git_review.py` is published alongside the CLI-installed checkout and the shipped `/git-review` procedure explicitly invokes it to inspect and act; no private Chief/Firstmate live runtime is borrowed.
- Why this is / is not agent-owned: the first-party path is specific to fleet-level current integration, not merely a task-local merge button, but its decision rights are configured and the actual adapting agent/parent supervisor is not established as an autonomous owner at this fleet boundary; hence constructor `C` only.
- Whole-system current view: `git_review.run` discovers repositories from its configured projects root/registry and reports branches, worktrees, stashes, candidate merges and failures with a fleet-wide workflow state.
- Current-control decision scope: which current branch/worktree work may be shipped or merged, which evidence/owners block integration and whether a follow-up reclamation is safe; no claim over broad business budgets or strategy.
- Evidence: [full multi-repo review procedure](https://github.com/sergeiwallace/ai-chassis/blob/ea39de12db1308c2a46ac7ffab38ead14ce39aaf/skills/git-review/SKILL.md); [Git reviewer orchestration and readback](https://github.com/sergeiwallace/ai-chassis/blob/ea39de12db1308c2a46ac7ffab38ead14ce39aaf/scripts/git_review.py#L86-L308); [status-update current-view procedure](https://github.com/sergeiwallace/ai-chassis/blob/ea39de12db1308c2a46ac7ffab38ead14ce39aaf/skills/status-update/SKILL.md).
- Basis: first-party specific review/ship-merge constructor.
- Confidence: medium; only narrow Git integration current-control is established.
- Caveats: no independent continuous AI chief is included in this claim; human consent on one code edit or PR alone would not justify `P` for the whole fleet, and deterministic merge proofs are support rather than autonomous decision rights.

## S3* — Complementary audit

- State: C
- Function: a first-party review/audit packet and provenance-receipt constructor supplies separately read Git/test evidence for a reviewer, with typed audit findings and bounded closure checks.
- Disturbance / variety regulated: accepting an author's unverified claim that an implementation meets scope and has passed checks.
- Decisive decision or feedback right: an explicitly invoked reviewer may inspect actual Git diff/test artifacts and return findings; first-party scripts require well-formed evidence and record disputed/open versus closed findings. No independent auditor model is bundled as an authority.
- Decision owner: first-party audit-path constructor and user-supplied distinct reviewer; no automatic independent model verdict or fully autonomous S3* owner proven.
- Supporting / enforcement mechanisms: `review_packet.push_diff` reads exact ratcheted Git range, supplies acceptance criteria/analyzer/test evidence; `audit_receipt` holds typed `audit/fix/halt/terminal` event records and computes closure state; `quality-check` requests external review with read-only Git fallback.
- Closure path: author claims completed work → first-party code builds review packet from *actual Git diff*, test result and ratchet findings rather than author prose → separately designated reviewer can return findings → typed event ledger marks issues open, fixed or needing another review; integration proceeds only through separately authorized Git policy/readback. This is an optional assembled check, not a guaranteed global merge gate.
- Boundary reachability: `scripts/review_packet.py` is a runnable CLI that opens Git itself; `scripts/audit_receipt.py` has executable `state`/`render` commands; published `/quality-check` invokes review/fallback, allowing construction of the path without undocumented private helpers.
- Why this is / is not agent-owned: independent evidence is available to a distinct reviewer, but reviewer selection, critical judgment and enforcement into all merges require further composition. The first-party **function-specific** constructor is present (`C`), not an autonomous first-party `A` auditor.
- Claim being audited: a coding agent's proposed change satisfies acceptance criteria and reported checks.
- Ordinary reporting path: agent-produced completion summary and proposed commit/PR.
- Complementary access path: raw repository Git diff of attested range plus separate analyzer findings and test result, structurally validated against typed audit events.
- Independence boundary: raw Git/test access does not depend solely on author's narrative; however the nominated model reviewer, external `hlg` executable, analyzer and test runner may be separate/outside this public distribution.
- Who acts on findings: a reviewing agent/operator processes issues and chooses rework or policy-authorized merge; the constructor records `open-blocking`, `fixed`, `deferred` and terminal outcomes for follow-up.
- Evidence: [review packet raw Git range and test data](https://github.com/sergeiwallace/ai-chassis/blob/ea39de12db1308c2a46ac7ffab38ead14ce39aaf/scripts/review_packet.py#L10-L76); [audit receipt typed state](https://github.com/sergeiwallace/ai-chassis/blob/ea39de12db1308c2a46ac7ffab38ead14ce39aaf/scripts/audit_receipt.py); [quality-check caveat](https://github.com/sergeiwallace/ai-chassis/blob/ea39de12db1308c2a46ac7ffab38ead14ce39aaf/skills/quality-check/SKILL.md).
- Basis: source-first constructed independent observation path.
- Confidence: medium-low for real deployed independent reviewer closure; high that raw Git/test packet code exists.
- Caveats: `hlg review` is an external requirement, not included in the credited surfaces; no claim of mandatory, independent reviewer execution or soundness of all audit verdicts.

## S4 — Outside-and-then intelligence

- State: —
- Function: no shipped fleet-level environmental/future intelligence loop is shown that selects and integrates an adaptation to current capability.
- Disturbance / variety regulated: provider, project and market changes can be studied by individual agents, but there is no first-party S4 adaptation authority at fleet recursion.
- Decisive decision or feedback right: missing; the human can edit context and install skills, while `persist` can record user-supplied conventions.
- Decision owner: no first-party separate S4 owner established.
- Supporting / enforcement mechanisms: extensible skills/config, `persist`, roadmap and repo-level planning templates.
- Closure path: no future-environment analysis → adaptation choice → changed operating capability loop is shipped.
- Why this is / is not agent-owned: retaining working conventions and writing a spec for a requested task are current work or operator customization, not S4 environmental adaptation.
- Evidence: [published roadmap and feature limits](https://github.com/sergeiwallace/ai-chassis/blob/ea39de12db1308c2a46ac7ffab38ead14ce39aaf/README.md#roadmap); [persist skill](https://github.com/sergeiwallace/ai-chassis/blob/ea39de12db1308c2a46ac7ffab38ead14ce39aaf/skills/persist/SKILL.md); [spec skill](https://github.com/sergeiwallace/ai-chassis/blob/ea39de12db1308c2a46ac7ffab38ead14ce39aaf/skills/spec/SKILL.md).
- Basis: bounded structural negative.
- Confidence: medium-high.
- Caveats: a human can compose a capable future-monitoring agent using the tools, but the composition is not demonstrated at this public revision.

### Absence scope

- Surfaces inspected: README roadmap/released modules, shared configuration, built-in skill list, scheduler/job and review paths.
- Plausible first-party paths checked: `persist` durable conventions, repo status updates, specs/architecture skill and optional later modules described in roadmap.
- Why no material first-party path remains: none ships a closed outside/future distinction, adaptation judgment and return into fleet capability; private roadmap and ad hoc tasks are not credited.

## S5 — Policy and identity

- State: —
- Function: no identity-level governance loop resolving ultimate-purpose or conflicting final policy matters is first-party operationally closed.
- Disturbance / variety regulated: competing ultimate commitments or exceptional mission disagreements do not become a routed S5 matter in the installed agent fleet.
- Decisive decision or feedback right: human-configured install profiles, Git merge opt-in and dangerous-action checks set constraints, but do not enact identity-policy issue adjudication.
- Decision owner: legitimate human and host repository authorities for out-of-band policy; no separate first-party S5 decision chain credited.
- Supporting / enforcement mechanisms: context rules, approvals, protected secrets/provenance gates and merge policy config.
- Closure path: policy settings constrain present actions; no policy conflict is elevated to a legitimate final authority, resolved and fed back as a new collective decision.
- Why this is / is not agent-owned: a safety default or sign-off gate has no deliberated identity question and no ultimate organizational authority loop.
- Evidence: [shared rules](https://github.com/sergeiwallace/ai-chassis/tree/ea39de12db1308c2a46ac7ffab38ead14ce39aaf/projects-wide-session-config/rules); [explicit spec approval](https://github.com/sergeiwallace/ai-chassis/blob/ea39de12db1308c2a46ac7ffab38ead14ce39aaf/skills/spec/SKILL.md); [Git integration policy](https://github.com/sergeiwallace/ai-chassis/blob/ea39de12db1308c2a46ac7ffab38ead14ce39aaf/scripts/git_review.py#L90-L166).
- Basis: bounded structural negative.
- Confidence: medium-high.
- Caveats: permissioned human policy control exists outside the audit's claimed S5 operational loop; an external CI branch-protection mechanism is not acquired as a first-party S5 owner.

### Absence scope

- Surfaces inspected: installation/config/CLI, policy rules, spec and commit skills, multi-repo merge gates, job supervisor and audit packets.
- Plausible first-party paths checked: human approval, Git opt-in policy, immutable provenance, merge ratchets, governance documents and private-harness roadmap.
- Why no material first-party path remains: these gate task execution and project integration without surfacing and resolving an exceptional identity/ultimate-policy issue through legitimate authority and return to fleet operations.

## Recursion

The installation can compose separate session contexts across machines and repositories, but each separate provider session performs S1 work under its own external agent runtime. The credited S2 and S3 paths concern local/conventionally registered fleet jobs and Git work; they do not demonstrate that the unrelated operator-maintained private system or all contributor machines share a complete organizational metasystem. The public released boundary must be re-evaluated if new roadmap modules become genuinely wired and shipped.

## Variety and escalation

Per-machine overlays, worktree isolation, idempotent submissions, exclusive claims and typed audit receipts attenuate operational uncertainty. Unsafe job launches, missing Git proof and unreviewed work are refused; report/readback makes the refusal visible. Human plan approval, potential task repair and cross-project integration remain contingent on configured operators and third-party session models. No independent spontaneous future-strategy or identity-policy decision has been imported from the maintainer's private fleet.

## Evidence gaps

- Source was reviewed at pinned public commit. `uv run --offline pytest -q` could not initialize because `ruff==0.17.3` was absent from the local dependency cache; no upstream full-suite pass is claimed. `python -m compileall -q src/ai_chassis scripts` succeeded.
- Private enterprise/fleet components and original development history are explicitly out of scope; no authority or S3/S4/S5 decision is inferred from their mention in README or source comments.
- The local `job_supervisor` and raw-diff audit packet are proven first-party executable constructors, but no fully configured multi-machine operation or independent reviewer-model E2E was observed.
- S3 is deliberately narrow `C`: a configured multi-repository current integration controller, not an independent AI chief or a completed parent-governed fleet S3.
