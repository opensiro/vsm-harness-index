---
harness_id: repository-harness
project_name: Repository Harness
repository: https://github.com/hoangnb24/repository-harness
review_ref: 485fd4062be1c71b27c1c9e5585ac4cd2faa7e06
reviewed_at: 2026-10-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Repository Harness

## Review boundary

- System in focus: the current first-party `repository-harness` distribution at frozen revision `485fd4062be1c71b27c1c9e5585ac4cd2faa7e06`: the repository instruction/protocol payload, opt-in skills, Bash/PowerShell bootstrap and Rust `harness` core maintenance executable. Historical `harness-cli`/SQLite protocol v1 is explicitly end-of-life and absent from this source tree's build/install surface.
- Purpose and identity: turn an existing software repository into a navigable, evidence-aware, agent-ready workspace and safely install/update that guidance while preserving consumer-owned files and decisions.
- Relevant environment: an arbitrary consumer repository and its product authority, an independently selected external coding agent, user/operator decisions, GitHub releases, local files, merge conflicts and native repository validation.
- Standard-distribution boundary: first-party documentation and installed `AGENTS.md`, explicit-only `.agents/skills/*`, `harness` install/update/status/doctor CLI and its deterministic filesystem/provenance/merge/recovery code. External Codex/Claude/other host coding-agent/model/tool loops remain adjacent actors and cannot donate their S1 ownership to this repository.
- Credited operating / distribution surfaces: [README](https://github.com/hoangnb24/repository-harness/blob/485fd4062be1c71b27c1c9e5585ac4cd2faa7e06/README.md), [installed payload manifest](https://github.com/hoangnb24/repository-harness/blob/485fd4062be1c71b27c1c9e5585ac4cd2faa7e06/scripts/harness-install-files.txt), [Rust CLI](https://github.com/hoangnb24/repository-harness/blob/485fd4062be1c71b27c1c9e5585ac4cd2faa7e06/crates/harness/src/interface/cli.rs), [application update use case](https://github.com/hoangnb24/repository-harness/blob/485fd4062be1c71b27c1c9e5585ac4cd2faa7e06/crates/harness/src/application/service.rs), [embedded distribution](https://github.com/hoangnb24/repository-harness/blob/485fd4062be1c71b27c1c9e5585ac4cd2faa7e06/crates/harness/src/infrastructure/embedded_distribution.rs) and explicit invocation skills.
- Adjacent first-party surfaces excluded from ownership: release/CI/repository-development governance, developer-only evidence/test fixtures, historical archived `harness-cli` versions, consumer application runtime/commands/logs/credentials, independently hosted agents and their inference providers.
- First-party operating / deployment modes considered: fresh install, merge/override installation, status/doctor, previewed/normal self-update, human-resolved conflict continuation, optional explicitly invoked onboarding/audit/invariant/improvement skills, optional engineering-advice add-on. None provides an installed background task coordinator or model-backed agent runtime.
- Recursion level: a repository-scoped tooling/protocol layer, not an operating organization of first-party autonomous task performers. Consumer coding agents may themselves be systems at an adjacent recursion; their agency is not attributed to this payload.
- Reviewed revision: `485fd4062be1c71b27c1c9e5585ac4cd2faa7e06`, the immutable row 5 ref in [intake #2012](https://github.com/opensiro/vsm-harness-index/issues/2012) and [control #2013](https://github.com/opensiro/vsm-harness-index/issues/2013).
- Observation date: 2026-10-24.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The only active Rust binary is `harness`. Its CLI explicitly exposes `install`, `update`, `status` and `doctor`. `main.rs` composes an embedded distribution, filesystem state, Git three-way merger and latest release-candidate downloader. Application code computes managed-file diffs, validates hashes and paths, stages overlapping merge conflicts, records frozen resolution inputs and transaction journals, rolls back interrupted writes, and replaces a version-checked executable. These are substantive and valuable **deterministic maintenance operations**; none interprets an open-ended software task, chooses semantic tools/actions based on model observations or delegates autonomous workers. [Architecture](https://github.com/hoangnb24/repository-harness/blob/485fd4062be1c71b27c1c9e5585ac4cd2faa7e06/docs/ARCHITECTURE.md), [CLI](https://github.com/hoangnb24/repository-harness/blob/485fd4062be1c71b27c1c9e5585ac4cd2faa7e06/crates/harness/src/interface/cli.rs), [main](https://github.com/hoangnb24/repository-harness/blob/485fd4062be1c71b27c1c9e5585ac4cd2faa7e06/crates/harness/src/main.rs).

The shipped `AGENTS.md` shim and optional Markdown skills instruct *consumer* agents to navigate repositories, collect evidence, pause on uncertain policy and propose changes. Skills advertise `Use only when the user explicitly invokes` them. For instance, `$onboard-repository` requires an external session to inspect a target repository, and `$audit-onboarding-proposal` calls for a distinct external fresh session to make independent judgments. A script can validate evidence-capsule hashes but is not a standalone autonomous reviewer. The manifest embeds these prompts/scripts as data; installation expressly does not activate them. [Agent shim](https://github.com/hoangnb24/repository-harness/blob/485fd4062be1c71b27c1c9e5585ac4cd2faa7e06/scripts/agent-harness-block.md), [onboard skill](https://github.com/hoangnb24/repository-harness/blob/485fd4062be1c71b27c1c9e5585ac4cd2faa7e06/.agents/skills/onboard-repository/SKILL.md), [audit skill](https://github.com/hoangnb24/repository-harness/blob/485fd4062be1c71b27c1c9e5585ac4cd2faa7e06/.agents/skills/audit-onboarding-proposal/SKILL.md).

This is an unusually clear negative boundary: README says this project is **not** a task database, tracker, agent orchestrator or application runtime; `docs/HARNESS.md` denies background processes and supplies explicit-only skills; accepted decision 0027 removes its earlier SQLite protocol/control plane as an active product. A past binary retained in Git history cannot be imported into the frozen standard-distribution assessment. [README](https://github.com/hoangnb24/repository-harness/blob/485fd4062be1c71b27c1c9e5585ac4cd2faa7e06/README.md), [product model](https://github.com/hoangnb24/repository-harness/blob/485fd4062be1c71b27c1c9e5585ac4cd2faa7e06/docs/HARNESS.md), [EOL decision](https://github.com/hoangnb24/repository-harness/blob/485fd4062be1c71b27c1c9e5585ac4cd2faa7e06/docs/decisions/0027-end-protocol-v1-and-focus-repository-protocol.md).

## Operational model

A human installs `harness` into a particular consumer repository. The deterministic CLI installs a declared documentation/skill payload and keeps its exact upstream base under `.harness-core/`. A separately selected coding agent, if present, may read that guidance and make task-dependent judgments using its **own** execution engine. Updates compare the local base and new release; nonoverlapping edits are applied transactionally, while overlapping conflicts are frozen for human-directed resolution before `--continue`. The consumer owns application operation and verification. Remove the external coding-agent runtime counterfactually: installation, status, diagnostics and updates remain functional, but no first-party actor decides and completes an open-ended engineering request. [Install contract](https://github.com/hoangnb24/repository-harness/blob/485fd4062be1c71b27c1c9e5585ac4cd2faa7e06/docs/product/installation-profiles.md), [update](https://github.com/hoangnb24/repository-harness/blob/485fd4062be1c71b27c1c9e5585ac4cd2faa7e06/crates/harness/src/application/service.rs), [workflow](https://github.com/hoangnb24/repository-harness/blob/485fd4062be1c71b27c1c9e5585ac4cd2faa7e06/docs/WORKFLOW.md).

## S1 — Operations

- State: —
- Function: no first-party autonomous operational unit owns the open-ended consumer engineering task loop.
- Disturbance / variety regulated: repository uncertainty, missing capability, task ambiguity and behavior verification are discussed by installed instructions, while file drift, release integrity and merge conflicts are deterministically handled by updater code.
- Decisive decision or feedback right: interpret arbitrary task evidence, choose semantic engineering actions/tools, evaluate their effects, and revise/finish the consumer task.
- Decision owner: a separately supplied consumer coding agent and/or human user; `harness` itself follows CLI-selected deterministic file/install/update transitions.
- Supporting / enforcement mechanisms: repository-map instructions, optional skills, filesystem safeguards, checksums, three-way merge and transaction recovery.
- Closure path: human/host invokes installed instruction → external agent observes/decides/acts/revises → consumer environment supplies result; first-party updater separately closes a deterministic release-file maintenance process only.
- Boundary reachability: shipped CLI and Markdown skills are accessible, but no embedded model/tool-agent loop is installed, scheduled or started by them.
- Why this is / is not agent-owned: writing agent-facing instructions and safe automation does not make the independently hosted agent's consequential decisions first-party.
- Evidence: [README](https://github.com/hoangnb24/repository-harness/blob/485fd4062be1c71b27c1c9e5585ac4cd2faa7e06/README.md), [CLI commands](https://github.com/hoangnb24/repository-harness/blob/485fd4062be1c71b27c1c9e5585ac4cd2faa7e06/crates/harness/src/interface/cli.rs), [embedded payload](https://github.com/hoangnb24/repository-harness/blob/485fd4062be1c71b27c1c9e5585ac4cd2faa7e06/crates/harness/src/infrastructure/embedded_distribution.rs).
- Basis: explicit product boundary plus source-observed absence.
- Confidence: high.
- Caveats: an external agent using the supplied skill can be fully autonomous, but the reviewed artifact is a protocol component of that composed deployment.

### Absence scope

- Surfaces inspected: Rust CLI/main/application/embedded payload, Bash installer, installed AGENTS shim, skills and product/install guidance.
- Plausible first-party paths checked: `harness` command as S1; self-updater as autonomous agent; onboarding/encoding/improvement skills as agentic loop; retired SQLite `harness-cli` protocol.
- Why no material first-party path remains: current binary implements bounded deterministic maintenance, optional skills require an external consumer agent and explicit invocation, and the historical orchestrating product is no longer shipped.

## S2 — Coordination

- State: —
- Function: no shipped coordination function attenuates interference between **first-party autonomous S1 units** in an operating harness organization.
- Disturbance / variety regulated: different consumer agents or contributor workflows could conflict over files, but the installed core is not an executing multi-agent workforce.
- Decisive decision or feedback right: choose a coordination adjustment based on interference between distinct operating S1 workers and return it to them.
- Decision owner: consumer agents/humans for task coordination; deterministic Git three-way merge handles one installed core's file conflicts.
- Supporting / enforcement mechanisms: shared repository map, documentation conventions, merge conflict staging, optional human-directed skill instructions.
- Closure path: file conflict → updater stages BASE/LOCAL/UPSTREAM/RESOLVED for a human → user changes file and resumes update; no inter-S1 work-regulation loop.
- Boundary reachability: merge machinery is installed but acts on files/core provenance, not independently controlled S1 units.
- Why this is / is not agent-owned: repository synchronization is not proof of an agent-owned relation attenuating actual inter-worker interference; no distinct first-party S1 witness exists.
- Evidence: [architecture update transaction](https://github.com/hoangnb24/repository-harness/blob/485fd4062be1c71b27c1c9e5585ac4cd2faa7e06/docs/ARCHITECTURE.md), [workflow boundary](https://github.com/hoangnb24/repository-harness/blob/485fd4062be1c71b27c1c9e5585ac4cd2faa7e06/docs/WORKFLOW.md).
- Basis: structural absence, S2-specific function-first threshold.
- Confidence: high.
- Caveats: an external team of agents can coordinate using this repository; the team itself is not installed or controlled here.

### Absence scope

- Surfaces inspected: installed repo navigation, CLI update/merge logic, skills, installer and removed-protocol decision.
- Plausible first-party paths checked: file-merge as S2; shared repository truth as S2; reviewer skill handoff as coordination; retired protocol v1.
- Why no material first-party path remains: there are no distinct first-party operating autonomous workers, interference witness or S2-specific returned adjustment; remaining mechanisms are generic context, file safety or external-agent guidance.

## S3 — Inside-and-now control

- State: —
- Function: no whole-current autonomous or genuinely parent-governed management function controls the commitments/resources of first-party S1 operations.
- Disturbance / variety regulated: pending installation/update, version drift, interrupted transactions and unresolved file conflicts are represented and handled, but these are maintenance state, not whole-harness operational commitments.
- Decisive decision or feedback right: reprioritize operating units, resources, scope or constraints on behalf of the active organization from a whole-system view.
- Decision owner: absent inside reviewed distribution; human chooses whether to install/update and how to resolve semantic conflicts.
- Supporting / enforcement mechanisms: status/doctor, state manifests, update plans, candidate verification, rollback journals and `update --continue`.
- Closure path: user invokes command → deterministic installation/diagnostic/update transitions → report or conflict stage; on conflict a human supplies resolution before a later command. No whole-current operational correction returns to owned S1 agents.
- Boundary reachability: `harness` maintenance CLI and user-directed conflict continuation are supported; neither creates an autonomous/parent-owned S3 portfolio.
- Why this is / is not agent-owned: operator resolution of an updater file conflict is not parent S3 governance of an active operating organization.
- Evidence: [core app](https://github.com/hoangnb24/repository-harness/blob/485fd4062be1c71b27c1c9e5585ac4cd2faa7e06/crates/harness/src/application/service.rs), [self-update](https://github.com/hoangnb24/repository-harness/blob/485fd4062be1c71b27c1c9e5585ac4cd2faa7e06/crates/harness/src/application/self_update.rs).
- Basis: structural absence with parent-mode review.
- Confidence: high.
- Caveats: consumer application/workforce oversight could supply S3 in a separately composed system; the repository does not establish or operate it.

### Absence scope

- Surfaces inspected: update state machine, status/doctor, transaction recovery, release selection, explicit human conflict resolution and skill-guided planning.
- Plausible first-party paths checked: update manager as S3; operator-driven merge as S3=P; roadmap/product decisions as parent S3; guidance on planning as controller.
- Why no material first-party path remains: every supported path concerns deterministic core maintenance or adjacent consumer/repository-development decisions, not whole-current authority and return over first-party autonomous S1 operations.

## S3* — Complementary audit

- State: —
- Function: explicit audit skill and evidence validator exist, but no independently acting, first-party runtime auditor closes substantive corrective feedback on first-party S1 claims.
- Disturbance / variety regulated: inaccurate onboarding claims, missing source citations, capsule hashes, incorrect merge state and repository-proof gaps are recognized as problems.
- Decisive decision or feedback right: obtain complementary evidence independently of the acting worker, judge the claimed effect, and return a binding correction into subsequent S1 work.
- Decision owner: fresh external host-agent session/human per the opt-in audit skill, not an instantiated Repository Harness reviewer agent; scripts check deterministic evidence consistency.
- Supporting / enforcement mechanisms: `audit-onboarding-proposal` prompt, transcript hash/capsule checker, docs/tests and core doctor checks.
- Closure path: external producer produces proposal → separately requested external audit session verifies sources/patch → human may decide on edits; no shipped autonomous first-party audit executor or mandatory production-return controller.
- Boundary reachability: skill Markdown and validator are installed, but they run only when a user explicitly invokes them inside an independently supplied agent host.
- Why this is / is not agent-owned: detailed instructions for independent auditing are a construction aid, not a first-party independent actor or closed runtime audit function.
- Evidence: [audit skill](https://github.com/hoangnb24/repository-harness/blob/485fd4062be1c71b27c1c9e5585ac4cd2faa7e06/.agents/skills/audit-onboarding-proposal/SKILL.md), [evidence validator](https://github.com/hoangnb24/repository-harness/blob/485fd4062be1c71b27c1c9e5585ac4cd2faa7e06/.agents/skills/audit-onboarding-proposal/scripts/validate_evidence_capsule.py), [product evidence boundary](https://github.com/hoangnb24/repository-harness/blob/485fd4062be1c71b27c1c9e5585ac4cd2faa7e06/docs/HARNESS.md).
- Basis: structural absence; external-auditor separation.
- Confidence: high.
- Caveats: a consumer may legitimately pair two agents for auditing, but that pairing must be separately assessed as a composed organization.

### Absence scope

- Surfaces inspected: onboarding/audit skill contracts, capsule validator, updater doctor, docs/CI test checks and optional workflow instructions.
- Plausible first-party paths checked: audit skill as S3* actor; hashes as independent audit; CLI doctor as complementary inspector; repository CI as runtime S3*.
- Why no material first-party path remains: semantic audit judgment belongs to an external agent/human while first-party diagnostics are deterministic; CI is contributor evidence, not an installed corrective feedback organization.

## S4 — Outside-and-then intelligence

- State: —
- Function: the shipped core has no autonomous prospective environment-intelligence loop that selects and feeds back changes to its operating capabilities.
- Disturbance / variety regulated: new external repository patterns, release updates and process improvements could matter to future work.
- Decisive decision or feedback right: observe outside/future conditions, evaluate strategic capability alternatives and return a chosen adaptation to present operation.
- Decision owner: consumer/user or upstream maintainer; optional `$improve-harness` asks an external agent/user to compare an authorized baseline and fresh rerun.
- Supporting / enforcement mechanisms: optional improvement skill, accepted decision templates, latest-release fetch, version guards and update apply/recovery.
- Closure path: maintainer publishes a release or user requests improvement → deterministic CLI fetches/verifies/applies or external agent proposes intervention → future consumer instructions may change; the future-oriented judgment is external to the installed core.
- Boundary reachability: updater and explicit improvement skill are reachable, but the autonomous prospective sensing/option choice and returned strategic correction are not supplied first-party.
- Why this is / is not agent-owned: fetching latest release and running an explicitly requested improvement experiment do not transfer maintainer/external-agent adaptation judgment to `harness`.
- Evidence: [improve skill](https://github.com/hoangnb24/repository-harness/blob/485fd4062be1c71b27c1c9e5585ac4cd2faa7e06/.agents/skills/improve-harness/SKILL.md), [self-update](https://github.com/hoangnb24/repository-harness/blob/485fd4062be1c71b27c1c9e5585ac4cd2faa7e06/crates/harness/src/application/self_update.rs), [product model](https://github.com/hoangnb24/repository-harness/blob/485fd4062be1c71b27c1c9e5585ac4cd2faa7e06/docs/HARNESS.md).
- Basis: structural absence including parent-mode examination.
- Confidence: high.
- Caveats: a separately composed consumer agent could periodically research and improve repository guidance, but such a service is not shipped in the standard distribution.

### Absence scope

- Surfaces inspected: release/self-update policy, improvement skill, knowledge templates, decision history, guidance on learning and explicit skill activation.
- Plausible first-party paths checked: self-updater as adaptive S4; improve-harness skill as S4; maintainer roadmap as parent S4; advisory engineering-wisdom add-on.
- Why no material first-party path remains: updates implement externally chosen versions, the experiment requires external actor/invocation and evidence, and no supported installed outside-and-then choice/return loop exists.

## S5 — Policy and identity

- State: —
- Function: repository-authority guidance and safety rules constrain external agent work but do not constitute an operating organization's ultimate identity/policy resolution loop.
- Disturbance / variety regulated: invented application policy, unapproved changes, unsupported capability claims and ambiguous authority are addressed through instructions and human escalation.
- Decisive decision or feedback right: settle genuinely identity-level organizational choices and return authoritative policy to continuing operations.
- Decision owner: the owner of the consumer repository or a human product authority, not an autonomous first-party Harness S5 actor; no legitimate parent S5 decision-and-return loop for first-party S1 operations is established.
- Supporting / enforcement mechanisms: `AGENTS.md` authority instructions, `$encode-invariant` acceptance gate, `$onboard-repository` decision-required classes, immutable installed core provenance and safe updater.
- Closure path: external agent detects unclear consumer policy → stops and asks a human → user may approve particular edits → external agent acts; this is consumer-specific policy governance, not an installed S5 identity-dispute loop for the Repository Harness organization.
- Boundary reachability: guidance is available to consumer host agents; its normative user-decision behavior requires those separate agents and a consumer-side authority context.
- Why this is / is not agent-owned: respecting existing product authority and human permission is important but does not create first-party S5 ownership or an evidenced full S5=P closure at the selected recursion.
- Evidence: [workflow authority](https://github.com/hoangnb24/repository-harness/blob/485fd4062be1c71b27c1c9e5585ac4cd2faa7e06/docs/WORKFLOW.md), [encode-invariant skill](https://github.com/hoangnb24/repository-harness/blob/485fd4062be1c71b27c1c9e5585ac4cd2faa7e06/.agents/skills/encode-invariant/SKILL.md), [installed shim](https://github.com/hoangnb24/repository-harness/blob/485fd4062be1c71b27c1c9e5585ac4cd2faa7e06/scripts/agent-harness-block.md).
- Basis: structural absence including legitimate parent-mode review.
- Confidence: high.
- Caveats: a consumer's owning human authority may correctly occupy S5 within that *different* agent organization; this does not confer a Repository Harness S5 publication state.

### Absence scope

- Surfaces inspected: `AGENTS`/workflow authority, onboarding decision gates, invariant encoding, human-directed merge conflict policy, maintainer decisions and consumer-boundary docs.
- Plausible first-party paths checked: consumer policy escalation as S5=P; repository maintainer decisions as S5; proof/approval gates as S5; static instructions as organizational identity.
- Why no material first-party path remains: rules and escalations operate in an adjacent consumer/maintainer context, with no first-party autonomous S1 and no closed identity/ultimate-policy issue → legitimate owner → authoritative decision → return into first-party organizational operations.

## Distributed OSS parent arrangement

Repository maintainers legitimately govern releases and the generic guidance artifact. Their GitHub product decisions do not govern each installed consumer's agents or supply runtime identity/current-control/intelligence return loops at this selected boundary. Multiple user repositories independently own their product truth and tools.

## Self-hosted and non-human modes

`harness` runs locally and can operate offline on installed core state, but it is not a model-driven autonomous agent. Installing the supplied skills for a local/remote third-party coding agent creates an additional composed system; it does not change the current repository-relative first-party classification. The legacy protocol is explicitly unshipped.

## Recursion

The only internal operational hierarchy here is source/installation maintenance (CLI → core application → ports/merge/filesystem) and externally hosted agent guidance (user → consumer model agent → repository files). Neither forms first-party lower-recursion autonomous S1 operations coordinated by the assessed distribution.

## Variety and escalation

First-party maintenance absorbs filesystem/version/merge failure variety through checksums, validation, journaling, backups and staged human conflict resolution. Semantic task, cross-agent coordination, independent audit, prospective adaptation and ultimate product policy variety is left to external consumer agents and legitimate human owners. The division is explicitly intentional, not simply an implementation defect.

## Evidence gaps

- Observation is restricted to the frozen public current-tree source. Removed protocol-v1 releases and consumer-specific integrations are outside standard distribution; later revisions could change ownership.
- No live LLM/provider/Browser/agent or application-efficacy test was run. Source inspection and deterministic Index validation cannot prove an external agent actually followed the instructions.
- Evidence supports a bounded all-negative first-party conclusion for the current installed product, not an assertion that consumers could never build an autonomous organization from these components.

## Assessment summary

Repository Harness provides useful repository memory, evidence and permission guidance plus a carefully guarded installer/updater. Source-level review of the active Rust binary, installed payload and opt-in skills does not reveal first-party autonomous S1 operation. Independent consumer agents and humans own substantive engineering, coordination, audit and policy decisions. As a result, this is an **evidence-backed exclusion** from the Index's autonomous-harness cohort, not an assessment that the maintenance/protocol tool is low quality. Proposed canonical disposition: `excluded-no-agentic-vsm`.

**Vector:** — · — · — · — · — · —
