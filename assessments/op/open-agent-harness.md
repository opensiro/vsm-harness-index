---
harness_id: open-agent-harness
project_name: open-agent-harness
repository: https://github.com/KenSuh/open-agent-harness
review_ref: a74fae79eee54fe5b095224d7c451e762e3b6554
reviewed_at: 2026-10-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-24
status: excluded-no-agentic-vsm
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# open-agent-harness

## Review boundary

- System in focus: the public Python `oah` CLI and library at frozen `a74fae79eee54fe5b095224d7c451e762e3b6554`, including task/intent packets, stage/model routing, Claude Code/Codex subprocess adapters, leased worktrees, static gates, skill ranking, logs/receipts, optional TypeSafe Jev ranking and delivered CLI workflows.
- Purpose and identity: supply a reproducible, constrained work process around installed Claude Code and Codex CLI agents, with separate implementation and review stages, task-scoped concurrency restrictions and auditable evidence. The repository explicitly labels the product **developer preview** at this revision.
- Relevant environment: developer/operator, Git repository/worktrees, task scope and intent, external Claude Code and Codex installations with their own agent tool loops, provider accounts, optional TypeSafe Jev service, CI gates and local task state.
- Standard-distribution boundary: first-party `src/oah` CLI, fixed stage/risk/model/skill rules, packet/lease/brief construction, external-process management, state/evidence gates and optional rerank service adapter. The general autonomous planning/coding/tool cycles inside `claude` and `codex` are external runtimes, not imported into first-party `oah` S1 ownership.
- Credited operating / distribution surfaces: `src/oah/{call,cli,routing,skillsel,lease,preflight,briefs,runs,rules,gates,models}.py`, `src/oah/engines/{claude,codex,proc}.py`, `src/oah/rerank/{base,typesafe}.py`, supported CLI entrypoint, shipped default templates and task/intent storage.
- Adjacent first-party surfaces excluded from ownership: tests/fakes, developer plan documents, CI/release automation, toolkit distribution, optional companion applications, future features marked *planned* in README, and external Claude/Codex/Jev cognition. A feature roadmap or diagram is not execution evidence.
- First-party operating / deployment modes considered: interactive developer workflow; `oah call claude --stage initial`; `oah call codex --stage review|correction`; task leases, packets/intent and scope conflicts; fixed-model/effort routing; background/wait; optional Jev advisory difficulty and fixed-candidate skill reranking; gates/wiki/finish; the documented P6 review/land flow checked against shipped status and source.
- Recursion level: the repository-local OAH process and its first-party workflow boundary. Externally invoked coding-agent CLIs can be autonomous lower-level systems in a wider composed deployment; this assessment does not reassign their autonomy to the first-party coordinator.
- Reviewed revision: `a74fae79eee54fe5b095224d7c451e762e3b6554`.
- Observation date: 2026-10-24.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.7`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.7`.

## Repository architecture

`oah call` prepares a task run deterministically: it checks a live lease and packet/intent binding, enforces `initial → claude`, `review/correction → codex`, scores known stage/scope/risk axes to a tier, selects a configured model/effort and skills, assembles an instruction brief and constructs a subprocess command. The `claude` adapter builds `claude -p ...`; the `codex` adapter builds `codex exec ...`. The `proc` and `call` layers run or detach the external command, enforce timeouts, store logs and report observed output, model and process exit state. These are substantial first-party reliability and governance mechanisms, but they do not decide the next coding edit in response to tool output.

The lease/scope store atomically blocks overlapping task writers, records holder, worktree, expiry and intent revisions, while preflight, gates and hook commands prevent unsafe or stale completion. These controls can regulate external-agent collisions without becoming separate first-party agentic operational units. Optional TypeSafe Jev calls ask an external model for a bounded choice among already generated skills or advisory difficulty tiers. The shipped `routing.recommend` stays rule-owned; the difficulty advisory cannot override the task tier. This limited classification does not instantiate a first-party open-ended goal → tool/action → observation → next-action loop.

Crucially, README marks the iterative Codex review/correction/re-review and `oah land` converged-review enforcement as **planned P6** at the frozen revision, even while depicting the intended future architecture. We credit available `oah call`, gate, packet, lease, routing and Jev primitives, not planned independent review/land loops. No external model or CLI was launched during this assessment.

Primary pinned source:

- [`README.md`](https://github.com/KenSuh/open-agent-harness/blob/a74fae79eee54fe5b095224d7c451e762e3b6554/README.md) — developer-preview status, available/planned feature matrix and external Claude/Codex/Jev role boundary.
- [`src/oah/call.py`](https://github.com/KenSuh/open-agent-harness/blob/a74fae79eee54fe5b095224d7c451e762e3b6554/src/oah/call.py) — preparation, external command execution, log/result capture, background continuation and task/intent guard.
- [`src/oah/engines/claude.py`](https://github.com/KenSuh/open-agent-harness/blob/a74fae79eee54fe5b095224d7c451e762e3b6554/src/oah/engines/claude.py) and [`codex.py`](https://github.com/KenSuh/open-agent-harness/blob/a74fae79eee54fe5b095224d7c451e762e3b6554/src/oah/engines/codex.py) — CLI adapters, not first-party coding model/tool loops.
- [`src/oah/engines/proc.py`](https://github.com/KenSuh/open-agent-harness/blob/a74fae79eee54fe5b095224d7c451e762e3b6554/src/oah/engines/proc.py) — subprocess lifecycle and timeouts.
- [`src/oah/lease.py`](https://github.com/KenSuh/open-agent-harness/blob/a74fae79eee54fe5b095224d7c451e762e3b6554/src/oah/lease.py) — scope lease/atomic conflict enforcement.
- [`src/oah/routing.py`](https://github.com/KenSuh/open-agent-harness/blob/a74fae79eee54fe5b095224d7c451e762e3b6554/src/oah/routing.py) — deterministic stage/effort/risk score routing.
- [`src/oah/rerank/typesafe.py`](https://github.com/KenSuh/open-agent-harness/blob/a74fae79eee54fe5b095224d7c451e762e3b6554/src/oah/rerank/typesafe.py) — external bounded classification adapter.
- [`src/oah/gates/check.py`](https://github.com/KenSuh/open-agent-harness/blob/a74fae79eee54fe5b095224d7c451e762e3b6554/src/oah/gates/check.py) — deterministic validation gates, not independent LLM audit.

## Operational model

Operator/task packet → OAH checks lease/intent/stage/scope → rules choose tier and configured external engine → OAH starts `claude` or `codex` subprocess with a structured brief → external agent owns the coding/review tool loop → OAH records process/outputs and applies deterministic task-scope/validation controls. The first-party controller can gate and preserve work, but the decisive semantic response to arbitrary task and workspace observations is implemented outside its source/distribution boundary. Removing the installed external CLIs leaves useful task-control infrastructure and optional bounded reranking, but no owned coding actor.

## S1 — Operations

- State: —
- Function: first-party autonomous execution of open-ended user coding tasks is not established at the frozen OAH boundary.
- Disturbance / variety regulated: arbitrary repository state, coding alternatives, command/tool feedback and task ambiguity are handled by external Claude Code or Codex agent loops; OAH regulates preparation, stage, scope, cost tiers, allowed tools and process health.
- Decisive decision or feedback right: inspect an operation's actual source/tool result, choose a substantive coding/review action and revise the next action from feedback.
- Decision owner: installed `claude` and `codex` agent CLIs, not `src/oah/call.py`. Optional Jev owns a bounded rerank/advice question rather than coding action selection.
- Supporting / enforcement mechanisms: rule-scored difficulty tiers, model/effort selection, brief/skill construction, process launcher/timeout, run log, leases, packet/intent checks, gates and hooks.
- Closure path: OAH produces stage-specific command/brief → external CLI performs its private model/tool recurrence → result and exit code are recorded by OAH. The substantive operation loop does not return as a first-party OAH next-action decision.
- Why this is / is not agent-owned: the adapter code constructs `claude -p` or `codex exec` calls, while `routing.recommend` is fixed scoring and Jev advice is bounded and cannot rewrite tier/plan. First-party code does not supply a substitutable coding loop when external engines are removed.
- Evidence: [`call.py`](https://github.com/KenSuh/open-agent-harness/blob/a74fae79eee54fe5b095224d7c451e762e3b6554/src/oah/call.py); [`engines/claude.py`](https://github.com/KenSuh/open-agent-harness/blob/a74fae79eee54fe5b095224d7c451e762e3b6554/src/oah/engines/claude.py); [`engines/codex.py`](https://github.com/KenSuh/open-agent-harness/blob/a74fae79eee54fe5b095224d7c451e762e3b6554/src/oah/engines/codex.py); [`routing.py`](https://github.com/KenSuh/open-agent-harness/blob/a74fae79eee54fe5b095224d7c451e762e3b6554/src/oah/routing.py).
- Basis: explicit + structural absence.
- Confidence: high in the pinned first-party executable boundary.
- Caveats: an assembled OAH + external Claude/Codex deployment can perform autonomous coding, but this does not satisfy repository-relative first-party S1 admission.

### Absence scope

- Surfaces inspected: `oah` CLI, call preparation and process execution, both external-engine adapters, model/effort rules, first-party skills/briefs, lease/packet routing and provider reranking.
- Plausible first-party paths checked: Python caller as a coding agent, subprocess output as OAH decision feedback, Jev task difficulty/skill rerank as S1, task packet instructions as first-party cognition, and planned review loop as a shipped actor.
- Why no material first-party path remains: OAH only selects/launches outside agent engines and enforces fixed protocol; it lacks its own open-ended coding action/feedback owner in supported modes.

## S2 — Coordination

- State: —
- Function: task scopes and leases protect multiple externally operated agent worktrees, but no plurality of first-party autonomous OAH S1 units is established at this recursion.
- Disturbance / variety regulated: two external coding agents may race over overlapping source paths or stale intent, which first-party scope conflict and generation guard attenuate.
- Decisive decision or feedback right: fixed scope overlap check refuses another work lease; no first-party S1-to-S1 coordination policy owner exists.
- Decision owner: deterministic lease/scope code and initiating human/operator; substantive worker decisions remain in external CLIs.
- Supporting / enforcement mechanisms: `LeaseStore`/journal, `StateLock`, `scope.overlaps`, worktree binding, intent revisions, generation checks and gate records.
- Closure path: operator proposes lease → OAH checks scope/holder and grants or refuses → external CLI operates within lease → return/finish releases it. This is useful cross-engine isolation but does not constitute first-party S2 over OAH-owned S1s.
- Why this is / is not agent-owned: the actual agents coordinated are installed Claude/Codex systems. Locking their resources does not transfer their autonomous S1 ownership to OAH.
- Evidence: [`lease.py`](https://github.com/KenSuh/open-agent-harness/blob/a74fae79eee54fe5b095224d7c451e762e3b6554/src/oah/lease.py); [`scope.py`](https://github.com/KenSuh/open-agent-harness/blob/a74fae79eee54fe5b095224d7c451e762e3b6554/src/oah/scope.py); [`call.py`](https://github.com/KenSuh/open-agent-harness/blob/a74fae79eee54fe5b095224d7c451e762e3b6554/src/oah/call.py).
- Basis: explicit + structural absence at the first-party autonomous recursion.
- Confidence: high.
- Caveats: at a larger composed system including those independently installed CLIs, the same lease contract could support an S2 analysis; that is not the declared first-party boundary.

### Absence scope

- Surfaces inspected: scope/lease conflict logic, worktrees, actor names, task packets, intent binding, stages and separate agent subprocesses.
- Plausible first-party paths checked: leases as inter-S1 attenuation, stage routing as coordination, overlapping-worktree refusal as autonomous S2 and planned review workflow as an actor team.
- Why no material first-party path remains: no qualifying OAH-owned S1 plurality exists; the coordination relation serves adjacent external coding runtimes.

## S3 — Inside-and-now control

- State: —
- Function: no first-party autonomous or complete parent-governed whole-current portfolio control loop over OAH-owned S1 operations is established.
- Disturbance / variety regulated: task stage, scope, timeouts, model risk floors, stalled subprocesses and intent mismatches are enforced as fixed run/lease conditions.
- Decisive decision or feedback right: inspect the ongoing whole organization's commitments and revise execution priorities/resources on that evidence.
- Decision owner: human author controls packets and commands; OAH's stage and lease checks are fixed logic, and model-level coding planning is delegated to external agents.
- Supporting / enforcement mechanisms: configured stages, packets, intent revision, run records, lease listing, effort tiers and dispatch guards.
- Closure path: supplied task plan/packet → OAH fixed checks and external stage launch; no closed portfolio observation → discretionary first-party current restructuring → changed S1 allocation path is shipped.
- Why this is / is not agent-owned: a fixed stage route and task stop/renew commands do not implement current whole-system management. A user manually calling different stages is not an operationally closed first-party S3 parent mode.
- Evidence: [`call.py`](https://github.com/KenSuh/open-agent-harness/blob/a74fae79eee54fe5b095224d7c451e762e3b6554/src/oah/call.py); [`routing.py`](https://github.com/KenSuh/open-agent-harness/blob/a74fae79eee54fe5b095224d7c451e762e3b6554/src/oah/routing.py); [`cli.py`](https://github.com/KenSuh/open-agent-harness/blob/a74fae79eee54fe5b095224d7c451e762e3b6554/src/oah/cli.py).
- Basis: structural absence.
- Confidence: medium-high.
- Caveats: future planned P6 review convergence might change the control topology; frozen source cannot be scored for that future code.

### Absence scope

- Surfaces inspected: stage dispatch, task/intent records, risk-based effort scoring, lease commands, background wait and planned reviewer workflow.
- Plausible first-party paths checked: `call.prepare` as S3, human lease changes as S3=P, stage enforcement as whole-current control, and future reviewer convergence as autonomous S3.
- Why no material first-party path remains: available code prepares and tracks each task/stage under fixed rules without a first-party portfolio-level discretionary control/return owner.

## S3* — Complementary audit

- State: —
- Function: claimed Claude→Codex independent review loop is planned in the frozen distribution, while existing validation and optional bounded Jev reranking do not audit an OAH-owned S1 report.
- Disturbance / variety regulated: false completion claims, stale task scope, broken gates and risky changed files are anticipated by static proof/validation infrastructure; general code-review judgment belongs to a future external Codex reviewer loop.
- Decisive decision or feedback right: independently inspect a first-party production actor's actual claim/evidence and return corrective challenge into its autonomous operation.
- Decision owner: deterministic `gates` and future external Codex reviewer; optional TypeSafe Jev ranks predefined skill/effort candidates rather than validating actual code diff or a production claim.
- Supporting / enforcement mechanisms: test/gate ledger, hash/scope/intent checks, run/effort receipts, `rerank/typesafe`, README P6 design.
- Closure path: current gates evaluate configured condition and CLI records result; intended P6 Codex review→fix→re-review loop is not available. No shipped independent complementary-audit closure over first-party S1 exists.
- Why this is / is not agent-owned: code-level review cognition would run inside external Codex; fixed checks and Jev routing advice cannot be counted as a separate first-party S3* auditor.
- Evidence: [`README.md`](https://github.com/KenSuh/open-agent-harness/blob/a74fae79eee54fe5b095224d7c451e762e3b6554/README.md); [`gates/check.py`](https://github.com/KenSuh/open-agent-harness/blob/a74fae79eee54fe5b095224d7c451e762e3b6554/src/oah/gates/check.py); [`rerank/typesafe.py`](https://github.com/KenSuh/open-agent-harness/blob/a74fae79eee54fe5b095224d7c451e762e3b6554/src/oah/rerank/typesafe.py).
- Basis: explicit planned/runtime contrast + structural absence.
- Confidence: high.
- Caveats: this is not a claim that Claude/Codex cannot review well; only the current source-first first-party loop is being classified.

### Absence scope

- Surfaces inspected: README feature matrix, available `oah call`, reviewer stage routing, static gates, Jev rerank, run receipts, test/CI code and planned P6 documents.
- Plausible first-party paths checked: Codex review stage as shipped independent audit, Jev skill rerank as S3*, deterministic gates as S3*, and external CLI review as first-party audit ownership.
- Why no material first-party path remains: iterative independent review/return is still planned and its discretionary judge is outside OAH; no OAH-owned agent production report/audit pair is instantiated.

## S4 — Outside-and-then intelligence

- State: —
- Function: no shipped first-party prospective external learning and capability-adoption closure was established.
- Disturbance / variety regulated: provider model catalogs, risk categories, task revisions, skill metadata and tool-version drift are tracked/refreshed under prewritten rules.
- Decisive decision or feedback right: generate and adopt a new future organizational capability/strategy from prospective environment intelligence.
- Decision owner: human/config author for tool/skill updates; fixed catalog and toolkit update logic select known options.
- Supporting / enforcement mechanisms: model cache freshness, `routing.score_axes`, toolkit updater, optional external Jev difficulty advice, packet revision and local wiki.
- Closure path: configured catalogs can refresh and advice can return without changing the rule-owned tier; no external forecast → alternative strategy → adoption → revised future first-party operating capability loop.
- Why this is / is not agent-owned: catalog freshness and task-scoped skill selection are present-tool routing, not autonomous evolution of the harness capability repertoire.
- Evidence: [`models.py`](https://github.com/KenSuh/open-agent-harness/blob/a74fae79eee54fe5b095224d7c451e762e3b6554/src/oah/models.py); [`routing.py`](https://github.com/KenSuh/open-agent-harness/blob/a74fae79eee54fe5b095224d7c451e762e3b6554/src/oah/routing.py); [`rerank/typesafe.py`](https://github.com/KenSuh/open-agent-harness/blob/a74fae79eee54fe5b095224d7c451e762e3b6554/src/oah/rerank/typesafe.py).
- Basis: structural absence.
- Confidence: medium-high.
- Caveats: users can update installed external skills and agent models manually; that does not constitute a first-party S4 organizational adaptation function.

### Absence scope

- Surfaces inspected: model catalogs and drift checks, risk scoring, optional Jev advice, skills/toolkit selection, task intent revisions and wiki maintenance.
- Plausible first-party paths checked: model refresh as S4, skills recommendation as future adaptation, Jev as prospective planner, user-updated toolkit as autonomy and packet revision as strategy change.
- Why no material first-party path remains: mechanisms choose or validate already configured current-operation options; no separately owned future-oriented capability adoption returns into OAH organization.

## S5 — Policy and identity

- State: —
- Function: first-party protocol constraints and human instructions exist, but no runtime ultimate-policy/identity adjudication loop for an autonomous OAH organization is established.
- Disturbance / variety regulated: goal revision, task scope, actor permissions, stage ownership, force release, push restrictions and provider permissions are handled through fixed configured rules and explicit human commands.
- Decisive decision or feedback right: decide identity/ultimate purpose or resolve competing legitimate top-level policies and return a durable ruling into ongoing first-party operations.
- Decision owner: human developer/operator sets task intents, rules and approvals; CLI validates those settings mechanically; external agent has its separate provider-native permissions.
- Supporting / enforcement mechanisms: intent revision, packet constraints, `AGENTS.md` policy templates, lease authority checks, shell hooks, gate ledger and config.
- Closure path: operator authors constraints → OAH enforces them around external CLI launch; no organizational identity conflict → legitimate ultimate authority judgment → authoritative ongoing first-party policy return is implemented.
- Why this is / is not agent-owned: strong rule enforcement is valuable but does not equal S5 ownership; the assessed standard distribution lacks the underlying autonomous OAH S1 organization to govern.
- Evidence: [`rules.py`](https://github.com/KenSuh/open-agent-harness/blob/a74fae79eee54fe5b095224d7c451e762e3b6554/src/oah/rules.py); [`intent.py`](https://github.com/KenSuh/open-agent-harness/blob/a74fae79eee54fe5b095224d7c451e762e3b6554/src/oah/intent.py); [`lease.py`](https://github.com/KenSuh/open-agent-harness/blob/a74fae79eee54fe5b095224d7c451e762e3b6554/src/oah/lease.py).
- Basis: structural absence.
- Confidence: high.
- Caveats: do not mistake this for a judgment on maintainer governance, user safety practices or the effectiveness of external agent permission controls.

### Absence scope

- Surfaces inspected: task intent, rules/templates, stage configuration, lease privileges, force release, pre-commit/pre-push hooks and documented user approvals.
- Plausible first-party paths checked: packet intent as constitution, `rules sync` as S5, immutable intent binding as policy feedback, human `oah finish` as S5=P, and external provider approval as OAH S5.
- Why no material first-party path remains: source defines task-level execution constraints and workflow hygiene, not a closed ultimate-identity decision/return function.

## Recursion

At the declared repository-local recursion OAH is a task-control and process/evidence substrate for already-autonomous external coding CLIs. Larger compositions may treat Claude/Codex as explicit viable S1s with OAH leases and gates as common coordination mechanisms; that cannot justify local Index autonomous S1 ownership without changing the system-in-focus and attribution boundary.

## Variety and escalation

OAH attenuates execution variety through stage-specific engine selection, risk/effort scoring, bounded candidate selection, leases, intent revisions, worktree isolation, process timeouts, gate receipts and operator overrides. Failures and refusals are recorded with error codes. The system can demand explicit operator decisions in the wider workflow; on this frozen revision no first-party open-ended coding loop or completed model-independent review convergence loop exists.

## Evidence gaps

- Source-first only: public pinned revision inspected, no live `claude`, `codex`, Jev or model-provider call; no practical task-quality measurement.
- README labels P6 review convergence and landing as planned. Future commits could change eligibility, but this row never re-pins the source to score later work.
- Leases and deterministic execution controls are materially implemented; the negative assessment is about **agentic VSM ownership at the first-party recursion**, not absence of functional control-plane engineering.
- Proposed canonical disposition after independent review: `excluded-no-agentic-vsm`, vector `S1=— / S2=— / S3=— / S3*=— / S4=— / S5=—`.

## Assessment summary

The frozen `open-agent-harness` first-party distribution provides practical protocol/routing/lease/evidence support around external Claude Code and Codex CLIs, but does not itself own a continuing general operational agent decision/tool/observation loop. Its intended reviewer convergence is not yet shipped. Exclusion as `excluded-no-agentic-vsm` is a bounded first-party eligibility decision, not a judgment that the composed product has no autonomous agents.
