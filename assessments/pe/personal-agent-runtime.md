---
harness_id: personal-agent-runtime
project_name: Personal Agent Runtime
repository: https://github.com/Sweetienite/personal-agent-runtime
review_ref: 41940107f285b6be0679962abe37be0e8d6441fe
reviewed_at: 2026-11-11
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C(P)
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# Personal Agent Runtime

## Review boundary

- System in focus: a local PAR installation with SQLite Kernel, task contracts, private-workspace worker adapter, coordinator MCP bridge, approval modes, per-project locks, check runner, candidate integration and supported manual hand-off.
- Purpose and identity: allow one or more vendor AI coding tools to perform scoped work under persistent task state, explicitly delegated permissions and independently measured acceptance evidence, without silently applying patches to a real project.
- Relevant environment: code projects, Codex CLI and other external agents, tasks, failures/quota, changing workspaces and dependent patches, human operator, external MCP coordinator app.
- Credited operating / distribution surfaces: `src/par/core/kernel.py`, `attempt.py`, `submission.py`, `review.py`, `candidate.py`, `store.py`, `approvals.py`, `src/par/execution/`, `providers/codex.py`, `src/par/mcp/catalog.py`, `cli_task.py` and the supported MCP/CLI integration modes.
- Adjacent first-party surfaces excluded from ownership: outside Codex model internals, unverifiable GUI agent automation, read-only evaluation/fake providers, optional experimental Antigravity/Copilot adapters, third-party MCP host itself, downstream human application of patches and the upstream maintainer's own governance.
- First-party operating/deployment modes: verified automatic Codex CLI worker on supported macOS; external Codex/Claude MCP coordinator using 21 Kernel tools; local human CLI parent; verified manual WorkBuddy hand-off where the human does the external work.
- Recursion level: one PAR-managed project/collection of task attempts under one installed Kernel ledger. Individual agent work attempts are S1; coordinator(s) act over a task portfolio.
- Reviewed revision: `41940107f285b6be0679962abe37be0e8d6441fe`, source-static on 2026-11-11. No live Codex/Claude Desktop, provider quota or real project mutation was exercised in this assessment.
- Generated Profile/Methodology: 0.2.4 / 0.3.8; active Profile/Methodology: 0.2.4 / 0.3.8.

## Repository architecture

The Kernel accepts strict task contracts via CLI or 21-tool MCP coordinator bridge; permissions, lease and project locks are checked within SQLite transactions. For an allowed write task, it builds a private clone and launches a configured native Codex CLI worker. The external model controls that worker's edits and its internal tool loop, while the Kernel captures its outputs as untrusted data, independently compares the workspace, reruns acceptance checks and persists evidence. A coordinator or human can inspect task state/diff, approve or reject, assemble verified candidate patches and choose subsequent tasks; no patch is applied to the real repository without a separate human action. See [architecture](https://github.com/Sweetienite/personal-agent-runtime/blob/41940107f285b6be0679962abe37be0e8d6441fe/docs/en/ARCHITECTURE.md), [readme and compatibility limits](https://github.com/Sweetienite/personal-agent-runtime/blob/41940107f285b6be0679962abe37be0e8d6441fe/README.md) and [MCP catalog](https://github.com/Sweetienite/personal-agent-runtime/blob/41940107f285b6be0679962abe37be0e8d6441fe/src/par/mcp/catalog.py).

## Operational model

- A configured native worker (only Codex currently verified) owns model-driven coding choices in a private workspace, but cannot bypass Kernel path/approval/evidence gates.
- A separately connected MCP coordinator may make task/approval/review/portfolio decisions within a lease and the configured approval mode. The Kernel supplies C-level function-specific construction paths; it does not itself launch or own the model coordinator.
- A human can alternatively exercise current-control rights through the CLI and choose `human_only`; a manual GUI hand-off does not count as automated S1 for that external tool.

## S1 — Operations

- State: A
- Function: perform bounded AI coding tasks with model-selected edits and feedback from a workspace/command environment.
- Disturbance / variety regulated: requested code change, runtime/test failures, tool results, path restrictions and provider conditions.
- Decisive decision or feedback right: within an approved task, Codex CLI model selects code edits/tool steps and may revise its plan from observed workspace behavior.
- Decision owner: first-party-launched native Codex worker operating via the vendor CLI; PAR's Kernel owns scope/verification enforcement rather than the coding decision.
- Supporting / enforcement mechanisms: Codex adapter, private attempt clone, process group, task contract, scoped paths, timeouts, structured events, retry/relay and independent acceptance runner.
- Closure path: approved task contract → Kernel starts native Codex CLI in private workspace → model edits/tools and returns result → Kernel compares patch/checks → coordinator/human reviews, accepts or requests another attempt.
- Boundary reachability: default distribution exposes a native Codex adapter with documented and dated `VERIFIED_AUTO` path; the operator must configure a supported macOS Codex installation/login.
- Why this is / is not agent-owned: the external model is the executor with discretionary editing choices, but PAR wraps it in a first-party standard execution/feedback path rather than merely documenting an arbitrary manual copy-paste action.
- Evidence: [Codex adapter](https://github.com/Sweetienite/personal-agent-runtime/blob/41940107f285b6be0679962abe37be0e8d6441fe/src/par/providers/codex.py), [Kernel run logic](https://github.com/Sweetienite/personal-agent-runtime/blob/41940107f285b6be0679962abe37be0e8d6441fe/src/par/core/kernel.py), [verified compatibility](https://github.com/Sweetienite/personal-agent-runtime/blob/41940107f285b6be0679962abe37be0e8d6441fe/docs/en/COMPATIBILITY.md).
- Basis: implemented adapter and dated documented real-provider evidence; this assessment remains source-static.
- Confidence: high for the single verified Codex mode, lower for cross-provider generality.
- Caveats: experimental/terms-restricted adapter paths and manual-only WorkBuddy are excluded from autonomous S1 evidence.

## S2 — Coordination

- State: C
- Function: attenuate competing write attempts into the same project and dependency-invalidated execution across distinct S1 tasks.
- Disturbance / variety regulated: simultaneous write workers clobbering one project's current files, and a downstream task using an unaccepted or stale predecessor baseline.
- Decisive decision or feedback right: the Kernel supplies project-specific lock refusal, dependency readiness and candidate-baseline gates, returning a blocked/wait outcome; an external coordinator must compose discretionary replanning or alternative assignment.
- Decision owner: first-party function-specific Kernel gate is deterministic, not an autonomous mediator; a configured external MCP coordinator may choose retry/reassign/pause, but is not a shipped internally launched agent at this boundary.
- Supporting / enforcement mechanisms: per-project transaction lock, bounded worker capacity, dependency graph, `run_next`, candidate composition, `not_before` and coordinator lease.
- Distinct S1 units: separate native coding attempts for independently submitted task contracts, potentially targeting the same project or using dependent accepted patches.
- Inter-S1 disturbance: concurrent attempts can write incompatible changes from one base, while an unaccepted predecessor can invalidate the next worker's premises.
- Attenuating coordination relation: project lock denies a second concurrent worker for that project; readiness checks gate dependent tasks until predecessors are accepted/closed and use a verified candidate for file-changing ancestors.
- Feedback into subsequent S1 behaviour: `run_next` skips locked projects, blocked dependent tasks remain queued, and the coordinator can later use `create_candidate`/`rebase_task`/retry before a worker starts.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the lock and candidate rules target a named inter-worker write conflict and dependency causality, with a concrete prevention/feedback return; no claim that a queue by itself is S2.
- Closure path: competing same-project task or unmet predecessor → kernel lock/dependency refusal → changed eligible execution set → external coordinator/CLI may select another task or verified baseline → next worker starts safely.
- Boundary reachability: project lock, dependency and candidate paths exist in shipped Kernel/CLI/MCP, but composition of autonomous arbitration beyond hard gates is required for `C` rather than `A`.
- Why this is / is not agent-owned: deterministic conflict prevention is not autonomous mediation; the first-party S2-specific constructor permits an external decision owner, not a complete first-party AI coordinator.
- Evidence: [Kernel capacity/lock/dependency logic](https://github.com/Sweetienite/personal-agent-runtime/blob/41940107f285b6be0679962abe37be0e8d6441fe/src/par/core/kernel.py), [candidate/dependency baseline](https://github.com/Sweetienite/personal-agent-runtime/blob/41940107f285b6be0679962abe37be0e8d6441fe/src/par/core/candidate.py), [MCP task coordination tools](https://github.com/Sweetienite/personal-agent-runtime/blob/41940107f285b6be0679962abe37be0e8d6441fe/src/par/mcp/catalog.py).
- Basis: concrete conflict-specific first-party regulation primitive with open autonomous ownership.
- Confidence: medium; the lock is coarser than path-level parallel-conflict arbitration.
- Caveats: ordinary `max_parallel_workers=1` deployments do not exercise inter-worker concurrency; positive `C` rests on the explicitly shipped same-project gate and its response path, not a measured multi-agent optimization.

## S3 — Inside-and-now control

- State: C(P)
- Function: supervise a project's task portfolio, execution commitments, approvals, recovery and candidate integration from current state.
- Disturbance / variety regulated: pending approvals, blocked/rate-limited tasks, failed checks, worker capacity, stale coordinator lease and integration dependencies.
- Decisive decision or feedback right: decide which current tasks to submit/run/retry/pause/recover, which approved patches to assemble, and which evidence to accept or reject.
- Decision owner: in base `C`, an external Codex/Claude MCP host model must supply ongoing supervisory judgment over shipped tools; in distinct parent `P`, the local human operator uses PAR CLI and controls lease/approvals.
- Supporting / enforcement mechanisms: SQLite ledger, task/result status, `list_tasks`, `review_task`, `run_task`, candidate management, approval modes, lease enforcement and terminal CLI.
- Whole-system current view: `list_tasks` and per-task result/approval/dependency data cover the active portfolio, while `coordinator status` and Kernel events show ownership and recoverability.
- Current-control decision scope: choose current worker commitments, recovery versus retry, permission and acceptance decisions, and verified candidate assembly across dependent tasks.
- Closure path: ledger task/project status → MCP model or operator judgment → first-party state-changing tool/CLI call → Kernel transaction/worker action → updated result and task portfolio.
- Boundary reachability: shipped 21-tool MCP construction path for Codex/Claude coordinators and separately operational CLI for the human; PAR does not automatically launch a coordinator model or claim one is always connected.
- Why this is / is not agent-owned: the model-driven supervisor is externally composed, hence `C` rather than `A`; parent CLI mode is genuinely whole-portfolio operating governance, not merely a permission prompt.
- Evidence: [MCP catalog](https://github.com/Sweetienite/personal-agent-runtime/blob/41940107f285b6be0679962abe37be0e8d6441fe/src/par/mcp/catalog.py), [coordinator mode and lease](https://github.com/Sweetienite/personal-agent-runtime/blob/41940107f285b6be0679962abe37be0e8d6441fe/docs/COORDINATORS.md), [architecture and CLI](https://github.com/Sweetienite/personal-agent-runtime/blob/41940107f285b6be0679962abe37be0e8d6441fe/docs/en/ARCHITECTURE.md).
- Basis: first-party autonomous constructor plus separate closed parent-mode control path.
- Confidence: medium-high for control tools, medium for any particular external coordinator behavior.
- Caveats: two modes are alternatives, not two simultaneous ultimate owners; coordinator lease prevents stale bridges from exercising state-changing rights.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | Externally configured MCP model coordinator; actor must be composed | Current task/approval/result observation | `list_tasks`/`review_task` → discretionary MCP decision → `run_task`/`retry_task`/`accept_task` → ledger/worker update | [MCP tools](https://github.com/Sweetienite/personal-agent-runtime/blob/41940107f285b6be0679962abe37be0e8d6441fe/src/par/mcp/catalog.py) |
| Parent (`P`) | Local project operator through CLI | Whole-portfolio status, approval or failure | Human `par task`/`par coordinator` decision → Kernel transaction → changed task state or runner | [architecture](https://github.com/Sweetienite/personal-agent-runtime/blob/41940107f285b6be0679962abe37be0e8d6441fe/docs/en/ARCHITECTURE.md) |

## S3* — Complementary audit

- State: C
- Function: challenge a coding worker's completion claim using independent scope/diff/check evidence before accepting a result.
- Disturbance / variety regulated: false self-reported success, unauthorized file changes, failures that the worker concealed or missed, and invalid dependent patch composition.
- Decisive decision or feedback right: Kernel independently runs test commands/inspects changed paths and marks review blockers; an external model coordinator may separately inspect the diff and decide accept/reject with a recorded reason.
- Decision owner: Kernel owns deterministic evidence collection and blocking, but a discretionary autonomous audit judge is not launched by PAR itself; composing a sufficiently independent MCP reviewer is left to the developer/operator.
- Supporting / enforcement mechanisms: private verification clone, `acceptance.checks`, result envelope, file/path comparison, `get_task_diff`, `review_task`, `reject_task`, `accept_task` and verified candidate reruns.
- Claim being audited: worker's delivered code change conforms to its strict task contract and passes the specified tests, regardless of the worker's self-report.
- Ordinary reporting path: worker-generated text summary and structured events captured as untrusted data.
- Complementary access path: Kernel reads workspace diff/paths and independently runs configured checks; coordinator accesses those observations through `get_task_diff` and review blockers, not merely worker narration.
- Independence boundary: verifier/check runner is separate from worker execution and the worker cannot mark its own results accepted. No default second independent LLM reviewer is shipped, so audit-agent ownership remains a `C` construction path, not `A`.
- Who acts on findings: Kernel refuses unsupported acceptance, while coordinator/human may reject or retry the task, correct contracts, or rebuild a candidate for dependent work.
- Closure path: worker result → Kernel independent diff/checks → `REVIEW_REQUIRED` with evidence/blockers → configured coordinator or parent review choice → `ACCEPTED`, rejected or retried work.
- Boundary reachability: acceptance checks, result/diff and MCP review actions are shipped and enabled; to claim autonomous complementary reviewer the integrator must assign an external model with independent audit judgment.
- Why this is / is not agent-owned: deterministic checking is first-party audit-specific feedback, not itself an autonomous reviewer, and an external MCP actor needs composition/independence guarantees.
- Evidence: [architecture verification sequence](https://github.com/Sweetienite/personal-agent-runtime/blob/41940107f285b6be0679962abe37be0e8d6441fe/docs/en/ARCHITECTURE.md), [review/acceptance code](https://github.com/Sweetienite/personal-agent-runtime/blob/41940107f285b6be0679962abe37be0e8d6441fe/src/par/core/review.py), [MCP audit tool surface](https://github.com/Sweetienite/personal-agent-runtime/blob/41940107f285b6be0679962abe37be0e8d6441fe/src/par/mcp/catalog.py).
- Basis: complementary first-party verifier plus audit-specific model construction path.
- Confidence: medium; real audit independence is not established by default.
- Caveats: passing caller-specified tests cannot prove general correctness; `C` must never be promoted to `A` merely because the Kernel independently executes commands.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party long-horizon environment-to-future-capability adaptation program demonstrated within the installed local runtime.
- Disturbance / variety regulated: changing provider quotas and project context affect current work routing; no strategic outside-and-then options process is supplied.
- Decisive decision or feedback right: no model/parent actor evaluates prospective external environment options and returns a long-horizon capability change through a first-party S4 circuit.
- Decision owner: human may choose new provider/adapter configuration outside the runtime; this is not a closed S4 governance mode.
- Supporting / enforcement mechanisms: worker routing health, active profiles, documented adapter extension points, task contracts, candidates and manual hand-off.
- Closure path: provider fallback/worker change alters a current attempt, and accepted patches modify task deliverables; neither constitutes evidence of a forward-looking strategic adaptation loop.
- Why this is / is not agent-owned: quota-driven current worker choice and support for new adapters are operational/extension mechanics, not future environment analysis with selected adaptation authority.
- Evidence: [architecture extension points](https://github.com/Sweetienite/personal-agent-runtime/blob/41940107f285b6be0679962abe37be0e8d6441fe/docs/en/ARCHITECTURE.md), [coordinator modes](https://github.com/Sweetienite/personal-agent-runtime/blob/41940107f285b6be0679962abe37be0e8d6441fe/docs/COORDINATORS.md), [README limits](https://github.com/Sweetienite/personal-agent-runtime/blob/41940107f285b6be0679962abe37be0e8d6441fe/README.md).
- Basis: bounded source-static no-path.
- Confidence: medium-high for standard distribution.
- Caveats: an external coordinator can strategize separately; its unshipped strategic process is not credited to PAR.

### Absence scope

- Surfaces inspected: adapters/routing, profiles, health/failure handling, task/candidate integration, coordinator prompt, docs roadmap and extension points.
- Plausible first-party paths checked: quota fallback, project context reading, worker role routing, adapter configuration and candidate integration.
- Why no material first-party path remains: these do not acquire prospective external distinctions, generate/evaluate a future adaptation option, and return a changed capability through a first-party long-horizon circuit.

## S5 — Policy and identity

- State: —
- Function: no first-party ultimate mission/identity decision/return loop established at the PAR installation boundary.
- Disturbance / variety regulated: task risk, permissions and coordinator control are strongly bounded, but do not decide what the organization is ultimately for.
- Decisive decision or feedback right: an operator selects `approval_mode` and grants, but those delegate execution authority rather than resolve durable identity-level purpose.
- Decision owner: legitimate human owner controls the system outside PAR; no installed first-party S5 actor or parent mission decision process is shown.
- Supporting / enforcement mechanisms: approval profiles, `human_only`/`coordinator_scoped`/`coordinator_autonomous`, lease, path-policy and no-auto-apply rule.
- Closure path: operator mode selection changes who may approve/retry/accept, an S3/current operational authority setting, not itself a mission identity circuit.
- Why this is / is not agent-owned: a decision grant or human approval does not establish VSM S5 ultimate-policy function by name alone.
- Evidence: [approval modes and control](https://github.com/Sweetienite/personal-agent-runtime/blob/41940107f285b6be0679962abe37be0e8d6441fe/docs/COORDINATORS.md), [architecture authorization](https://github.com/Sweetienite/personal-agent-runtime/blob/41940107f285b6be0679962abe37be0e8d6441fe/docs/en/ARCHITECTURE.md), [Kernel approvals](https://github.com/Sweetienite/personal-agent-runtime/blob/41940107f285b6be0679962abe37be0e8d6441fe/src/par/core/approvals.py).
- Basis: bounded no-path after checking legitimate permission and policy candidates.
- Confidence: medium.
- Caveats: strong operational security is recognized without inferring ultimate organizational identity governance.

### Absence scope

- Surfaces inspected: profiles, Kernel approval/lease, task contracts, coordinator prompts, CLI and human apply-patch boundary.
- Plausible first-party paths checked: approval modes and grants, user coordinator takeover, project write policy and no-auto-apply invariant.
- Why no material first-party path remains: all regulate who can run or accept tasks; no substantive mission dispute, identity owner and return into subsequent purpose-level operation is wired.

## Distributed OSS parent arrangement

No inference from the upstream repository's maintainer/contributor activity to distributed S3–S5 ownership is made. `C(P)` concerns the installed task portfolio with an explicitly selectable local human mode, not maintainer governance.

## Self-hosted and non-human modes

PAR is local and offline by default. A connected Codex or Claude MCP coordinator may decide inside the lease and approval mode, but that model is not launched by PAR and its autonomy cannot be assumed in every installation. Manual hand-off and human patch application remain intentional boundaries.

## Recursion

Each native worker attempt is S1 only when performing a real coding task; dependency/locking rules coordinate those efforts. Kernel verification is audit feedback, not a second coding operation, and the model coordinator is a higher-level task supervisor.

## Variety and escalation

Contracts, path restrictions, project locks, finite worker concurrency, independent acceptance checks, append-only events, coordinator lease, no automatic patch application, recovery and candidate recheck attenuate unsafe variety. Security and permission mechanisms are not treated as automatic S5 identity claims.

## Evidence gaps

- Source-static; no new real-provider, multi-worker collision, independent MCP audit reviewer or human-led S3 run was executed here. Repository's own dated compatibility records are evidence of a narrower supported mode, not universal verification.
- `C` for S2 and S3* means function-specific primitives with missing autonomous owner/independence composition; it does not certify safe concurrent integration or independent LLM review.
- The S3 parent mode is an alternative local CLI authority arrangement; neither a global distributed parent nor an automated strategic S4/S5 is inferred.
