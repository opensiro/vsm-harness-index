---
harness_id: puny
project_name: Puny
repository: https://github.com/christianhelle/puny
review_ref: dcdecb253b81415152aac4d3590d2186adfa0c81
reviewed_at: 2026-10-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-04
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Puny

## Review boundary

- System in focus: Puny's first-party native terminal coding-agent distribution at frozen revision `dcdecb253b81415152aac4d3590d2186adfa0c81`, including the model/tool chat loop, built-in coding tools, session persistence, planning/build/review modes, branch-review machinery, and the shipped implement → review → fix orchestrate loop.
- Purpose and identity: turn a coding request into repository changes through a lightweight native model/tool loop, while optionally subjecting committed branch changes to a fresh-context independent review and bounded repair/re-review cycle.
- Relevant environment: user objective, current repository/filesystem and Git state, configured model/provider, tool results, tests/lint/build commands, origin/main, durable session artifacts, saved PRDs, review reports and iteration limits.
- Standard-distribution boundary: first-party Zig runtime under `src/`, its built-in tool registries, prompts, session/review/orchestrate machinery and shipped CLI modes are inside. External model providers, provider-hosted inference, Git remote hosting and host OS/toolchain processes are dependencies/environment. Repository-development CI and the separate `scripts/council*` utilities are adjacent development/review tooling and do not donate ownership to the assessed Puny runtime.
- Credited operating / distribution surfaces: normal interactive/oneshot build mode; built-in read/write/edit/list/shell/search/Git/web/skill tools; durable session save/resume; planning mode; `--review` and `/review`; `--orchestrate` and `/orchestrate`; fresh per-phase contexts; read-only review tool allowlist; saved `review-results.md`; bounded fix/re-review iterations.
- Adjacent first-party surfaces excluded from ownership: `scripts/council.sh`, `scripts/council.ps1` and council prompts; repository CI/release/test organization; mock provider fixtures; documentation claims that are not instantiated by the frozen runtime; multiple independently launched Puny processes that the product does not coordinate.
- First-party operating / deployment modes considered: interactive terminal sessions; one-shot prompts; supported local/hosted providers; saved/restored sessions; build/planning/review modes; autonomous orchestrate mode on a feature branch.
- Recursion level: one Puny goal-to-repository-change execution is the focal operation. A fresh review phase is a complementary audit actor over committed work at the same harness recursion, not a peer production S1.
- Reviewed revision: `dcdecb253b81415152aac4d3590d2186adfa0c81`.
- Observation date: 2026-10-04.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Puny ships its own Zig model/tool runtime. The CLI selects a provider/model, maintains the conversation and presents a mode-specific tool schema. In build mode the model can read, write and edit files, run shell commands, search the codebase, inspect Git state, fetch web pages and load skills. Tool calls are executed by Puny and their concrete outputs return into later model turns.

Sessions persist messages and planning state to UUID-scoped session directories and can be resumed. This makes current work durable, but the persisted state is conversation/task context rather than an autonomous mechanism for changing Puny's future capabilities or policy.

The shipped orchestrate mode creates a stronger organizational structure around the same coding operation. It runs `implement → (review → fix)*` with every phase starting from a fresh conversation. Implement/fix phases use build mode and can change source. Before review, Puny sweeps remaining work into committed state so the reviewer sees the complete committed branch diff.

Each review phase switches to a separate fresh conversation, enters review mode, blocks source writes, removes write/edit tools, limits shell execution to review-safe commands and pins an immutable `merge-base..HEAD` branch range against freshly fetched `origin/main`. The review model is given a dedicated evidence-driven system prompt and direct read/check tools. It must call `save_review_results` with its own analysis, evidence-completeness judgment and merge-worthiness verdict. Puny validates the report shape and converts `merge_worthy && evidence_complete` into the trusted outcome.

A rejected verdict is not merely displayed. The saved report path is inserted into a fresh fix-phase instruction, the build-mode model is told to open that report, resolve every finding and confirm tests, then the branch is committed and re-reviewed. The loop stops only when the independent reviewer returns merge-worthy, the configured iteration budget is exhausted, or an operational failure/abort occurs.

Primary evidence:

- [README.md](https://github.com/christianhelle/puny/blob/dcdecb253b81415152aac4d3590d2186adfa0c81/README.md)
- [CLI/model initialization](https://github.com/christianhelle/puny/blob/dcdecb253b81415152aac4d3590d2186adfa0c81/src/main.zig)
- [chat loop](https://github.com/christianhelle/puny/blob/dcdecb253b81415152aac4d3590d2186adfa0c81/src/chat/chat.zig)
- [chat/session runtime](https://github.com/christianhelle/puny/blob/dcdecb253b81415152aac4d3590d2186adfa0c81/src/chat/session.zig)
- [tool registry](https://github.com/christianhelle/puny/blob/dcdecb253b81415152aac4d3590d2186adfa0c81/src/tools/root.zig)
- [session persistence](https://github.com/christianhelle/puny/blob/dcdecb253b81415152aac4d3590d2186adfa0c81/src/chat/persistence.zig)
- [orchestrate loop](https://github.com/christianhelle/puny/blob/dcdecb253b81415152aac4d3590d2186adfa0c81/src/chat/orchestrate.zig)
- [branch review](https://github.com/christianhelle/puny/blob/dcdecb253b81415152aac4d3590d2186adfa0c81/src/review/review.zig)
- [review report tool](https://github.com/christianhelle/puny/blob/dcdecb253b81415152aac4d3590d2186adfa0c81/src/tools/review.zig)
- [review/orchestrate prompts](https://github.com/christianhelle/puny/blob/dcdecb253b81415152aac4d3590d2186adfa0c81/src/prompts/prompts.zig)

## Operational model

A normal Puny build session sends the objective/current context to the selected model together with first-party coding-tool schemas. The model chooses tool calls or a final response. Puny executes each allowed tool against the local environment and returns the result to the model, which can revise the repository or gather more evidence until it decides the requested work is complete.

In orchestrate mode, that production loop is wrapped in a bounded audit closure. A fresh implement model changes and commits the branch. A fresh read-only reviewer independently inspects the immutable committed range and relevant surrounding code/checks, then decides merge-worthiness. If rejected, Puny writes the review report and starts another fresh build context whose explicit task is to fix every finding. The repaired commits become the next review subject.

## S1 — Operations

- State: A
- Function: perform coding work against the local project by interpreting a user task, selecting built-in repository/tool actions, changing source and observing results until the requested outcome is reached.
- Disturbance / variety regulated: heterogeneous codebases and tasks, incomplete local context, tool/provider failures, command/test results, Git state, file contents, context-window pressure and reviewer findings during orchestrated repair.
- Decisive decision or feedback right: choose which project evidence/tool to use next, what source changes to make, how to react to tool/check results and when the coding task is complete.
- Decision owner: the configured model-backed Puny coding actor operating through the first-party native chat/tool loop.
- Supporting / enforcement mechanisms: mode-specific tool registry; filesystem/shell/search/Git/web/skill tools; provider transports; session persistence; context compaction; retry handling; Git backstop commits; prompts and CLI/session lifecycle.
- Closure path: task + repository/session state → model chooses tool/action → Puny executes against the environment → concrete result/error returns into the conversation → model revises the work or completes.
- Boundary reachability: the normal supported CLI directly instantiates this model/tool loop with local or hosted provider choices; no external agent framework must supply the operational loop.
- Why this is / is not agent-owned: if the model actor is removed while deterministic tools/session storage remain, open-ended coding judgment about what to inspect, change and do next disappears.
- Evidence: `src/main.zig`; `src/chat/chat.zig`; `src/chat/session.zig`; `src/tools/root.zig`; README.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: model inference is provider-supplied, but provider transport is a dependency; Puny concretely instantiates and governs the actor/tool feedback loop.

## S2 — Coordination

- State: —
- Function: no material first-party coordination function among multiple same-recursion production S1 units was established.
- Disturbance / variety regulated: Puny intentionally ships without subagents or first-party parallel worker organization; README directs users who want parallel work to run another independent instance.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: single-session mode state; Git branch scope; one orchestrate phase at a time; provider/session identifiers.
- Closure path: no distinct production-S1 interference → coordination response → changed peer behavior path exists in the shipped organization.
- Why this is / is not agent-owned: fresh implement/review/fix contexts are sequential roles around one operation, while the reviewer is an audit role rather than a peer production S1. Independently launched Puny processes are not coordinated by Puny.
- Evidence: README; `src/chat/orchestrate.zig`; `src/tools/root.zig`.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: plurality of phases/models is not sufficient for S2 without multiple operational S1s and a concrete interference relation.

### Absence scope

- Surfaces inspected: normal chat loop; tool registry; orchestrate phases; review mode; session persistence; Git/repository state; README's parallel-work guidance.
- Plausible first-party paths checked: multiple model contexts as workers; implement/fix concurrency; reviewer as production peer; multiple sessions; independently launched processes.
- Why no material first-party path remains: phases execute sequentially, sessions are independent conversations, reviewer is read-only complementary audit, and no shipped relation coordinates interference among autonomous coding peers.

## S3 — Inside-and-now control

- State: —
- Function: no distinct whole-system current-control function over a portfolio of operational S1 commitments/resources was established.
- Disturbance / variety regulated: orchestrate iteration bounds, phase transitions, session state, context budgets and review outcomes regulate one focal coding operation rather than several operational units.
- Decisive decision or feedback right: not established at S3 level.
- Decision owner: not established.
- Supporting / enforcement mechanisms: orchestrate state progression; max iterations; write blocking by mode; session/context budgets; Git preflight/backstop commits; retry/error handling.
- Closure path: these mechanisms bound or sequence the current task; no whole-system current view plus substantive resource/priority/commitment intervention across multiple S1s exists.
- Why this is / is not agent-owned: the orchestrate controller is deterministic phase machinery. It enforces the implement/review/fix protocol but does not exercise discretionary current management over an operational portfolio.
- Evidence: `src/chat/orchestrate.zig`; `src/core/session.zig`; `src/chat/session.zig`; `src/review/review.zig`.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: a strong autonomous workflow controller is not automatically VSM S3.

### Absence scope

- Surfaces inspected: orchestrate controller, phase/iteration state, session manager, context budgets, provider/model selection, review outcome, Git commit/review lifecycle.
- Plausible first-party paths checked: orchestrator as manager; iteration budget as resource allocation; model/provider switching; session fleet control; review veto as whole-current management.
- Why no material first-party path remains: all inspected control acts on one goal/branch lifecycle; there is no distinct whole-current authority over multiple production operations.

## S3* — Complementary audit

- State: A
- Function: independently audit the committed branch produced by the coding actor, determine whether it is safe/complete enough to merge, and return blocking findings into a corrective implementation/re-review loop.
- Disturbance / variety regulated: implementation defects, regressions, compatibility/security/performance/error-handling problems, missing tests/docs, failed checks and false confidence by the implementing model.
- Decisive decision or feedback right: a fresh model-backed reviewer independently decides whether evidence is complete and whether the immutable committed branch range is merge-worthy, while identifying concrete findings and recommended fixes.
- Decision owner: the separate fresh-context Puny review actor. Deterministic report validation, write blocking and outcome conversion enforce the review contract but do not supply the substantive audit judgment.
- Supporting / enforcement mechanisms: `beginPhase(.review)` context reset; dedicated review system prompt; freshly fetched `origin/main`; immutable merge-base..HEAD scope; review-only read/check tool registry; global source-write block; `save_review_results`; host validation of required sections/evidence flags; bounded orchestrate iterations.
- Closure path: build actor commits implementation → Puny resets context and starts read-only reviewer over immutable committed range → reviewer directly inspects changed/surrounding files and can run relevant checks → reviewer saves evidence + merge-worthiness verdict → rejection writes `review-results.md` → fresh fix actor is explicitly instructed to open the report and resolve every finding → fixes are committed → another fresh review runs; approval terminates the loop as merge-worthy.
- Boundary reachability: both `/review`/`--review` and `/orchestrate`/`--orchestrate` are shipped first-party CLI modes. Orchestrate directly wires the reviewer verdict into repair/re-review without user intervention.
- Why this is / is not agent-owned: removing the review model while retaining report-format validation, immutable Git scope and read-only enforcement removes the open-ended judgment about what is wrong, what evidence to gather and whether the branch is merge-worthy. The deterministic host can only validate/store an already chosen verdict.
- Evidence: `src/chat/orchestrate.zig`; `src/review/review.zig`; `src/tools/root.zig`; `src/tools/review.zig`; `src/prompts/prompts.zig`; README.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: implement, review and fix may use the same configured provider/model family, but the audit has a fresh conversation, distinct review-only prompt/tool authority, immutable committed evidence scope and source-write prohibition; independence is role/context/evidence separation rather than provider diversity.
- Claim being audited: that the current committed feature branch is merge-worthy relative to the freshly resolved origin/main baseline.
- Ordinary reporting path: the build actor edits/commits source and could otherwise finish after its own checks and final response.
- Complementary access path: the fresh review actor receives the immutable branch/base scope, directly reads project evidence and surrounding code, and can run read-only build/test/lint/check commands rather than trusting the implementer's self-report.
- Independence boundary: review starts after a context reset, excludes the implement/orchestrate build prompt, blocks source mutation, exposes a distinct tool allowlist and scopes its verdict to committed Git evidence. It can reject work the implementer considered complete.
- Who acts on findings: a subsequent fresh build-mode model context receives the generated report path and explicit instruction to resolve every listed finding; the repaired branch is then re-submitted to another fresh review.

## S4 — Intelligence / adaptation

- State: —
- Function: no material autonomous outside-and-future intelligence/adaptation loop was established.
- Disturbance / variety regulated: durable sessions, saved PRDs, skills, web fetch, context compaction and provider/model selection improve or preserve current work, but they do not autonomously redesign persistent Puny capability/strategy for future operations.
- Decisive decision or feedback right: not established at S4 level.
- Decision owner: not established.
- Supporting / enforcement mechanisms: session message persistence/resume; planning artifacts; skills loading; web fetch; context compaction; provider/model picker; review-derived current-task repair.
- Closure path: no environmental/future sensing → selected persistent adaptation → later-operation behavior change loop was found.
- Why this is / is not agent-owned: retained conversation/project instructions and reusable user-authored skills are context/capability inputs, not an autonomous prospective self-adaptation process.
- Evidence: README; `src/chat/persistence.zig`; `src/chat/session.zig`; `src/skills/`; provider/model selection surfaces.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: Puny can fetch current web evidence during a task, but current-task research is not by itself S4.

### Absence scope

- Surfaces inspected: durable session persistence/resume; planning/PRD artifacts; skills; web access; model/provider switching; context compaction; orchestrate review/fix learning.
- Plausible first-party paths checked: session memory as long-term learning; skills as self-modification; reviewer feedback as capability adaptation; provider/model selection as prospective strategy change.
- Why no material first-party path remains: identified mechanisms persist context or accept externally selected configuration/content; they do not autonomously choose and install a durable future-facing organizational adaptation.

## S5 — Policy and identity

- State: —
- Function: no material identity/ultimate-policy decision loop was established at the assessed runtime recursion.
- Disturbance / variety regulated: mode restrictions, system prompts, tool allowlists, source-write blocks, provider configuration and commit discipline constrain execution but remain operating/safety/process policy.
- Decisive decision or feedback right: no qualifying identity-level conflict/proposal is decided by a legitimate ultimate authority and returned as binding organizational governance.
- Decision owner: not established at S5 level.
- Supporting / enforcement mechanisms: build/planning/review modes; static prompts; tool registries; write-block flag; CLI/config choices; Git branch preconditions; commit rules.
- Closure path: no identity/ultimate-policy issue → legitimate authority decision → returned governance → changed subsequent operation loop was found.
- Why this is / is not agent-owned: the coding/review actors operate within preconfigured host rules; they do not own or resolve the system's identity/ultimate policy.
- Evidence: `src/prompts/prompts.zig`; `src/tools/root.zig`; `src/core/session.zig`; CLI/configuration surfaces.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: review veto and write blocking are strong governance mechanisms, but they govern artifact progression rather than a genuine S5 policy/identity question.

### Absence scope

- Surfaces inspected: system/review/orchestrate prompts; tool/mode restrictions; session/config persistence; provider/model configuration; Git/review preconditions; user-selected skills.
- Plausible first-party paths checked: review verdict as policy; commit discipline as identity; user config as parent authority; persistent prompts/skills as standing policy.
- Why no material first-party path remains: these mechanisms define or enforce operating rules and task constraints without a closed identity/ultimate-policy decision relation.

## Recursion

The focal recursion is one coding objective on one project/branch. Build/fix contexts are operational S1 enactments of that objective. The review phase is a separate complementary audit role with independent context and restricted authority, not a second production operation.

## Variety and escalation

Puny attenuates operational variety through curated tools, context budgets/compaction, durable sessions, mode-specific authority, Git branch scoping, review-safe shell restrictions and bounded orchestrate iterations. Audit findings escalate through `review-results.md` into a new fix context; unresolved findings trigger another review until approval or the iteration limit.

## Evidence gaps

No `?` state is required. The pinned implementation directly establishes the model/tool S1 and the independent fresh-context review/rework S3* closure. It also gives sufficient negative evidence to bound sessions, planning, orchestration and runtime restrictions without promoting them to S2/S3/S4/S5.

## Assessment summary

Puny closes autonomous S1 through its native model/tool coding loop and autonomous S3* through a separate fresh-context, read-only branch reviewer whose merge-worthiness findings are fed into fresh fix contexts and re-reviewed. It intentionally lacks first-party parallel operational workers, so no S2 or whole-current S3 is established; durable sessions/skills do not close prospective S4, and mode/tool/commit policies do not establish identity-level S5.

**Vector:** A · — · — · A · — · —
