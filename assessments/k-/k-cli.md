---
harness_id: k-cli
project_name: K-CLI
repository: https://github.com/krishivjoshi219-collab/K-Cli
review_ref: 2f375d94ba445cdf51d3fb2bbfcc49f12f36ff89
reviewed_at: 2026-10-23
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-23
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# K-CLI

## Review boundary

- System in focus: the installed first-party K-CLI local developer/coding workstation, including its optional agent, multi-persona, subagent, GitHub-review and SDK modes.
- Purpose and identity: undertake repository-aware coding and developer operations with model-directed implementation, patching, compiler/test feedback, and optional specialized worker roles.
- Relevant environment: selected local Git repository, source and tests, shell/compiler output, configured model providers, PR diffs and CI/review comments, operator permissions, dependency failures and provider responses.
- Standard-distribution boundary: Python package executable via k-cli and first-party SDK, local SessionManager and Orchestrator, SubagentDispatcher, Verifier/Patcher/GitGuard, CLI PR review/fix operations and the separately exposed SDK PR watcher.
- Credited operating / distribution surfaces: k_cli/cli.py, k_cli/core/session.py, k_cli/core/sdk.py, k_cli/core/llm_driver.py, k_cli/agents/orchestrator.py, k_cli/agents/subagents.py, k_cli/github/github_client.py, k_cli/github/pr_watcher.py, k_cli/git/verifier.py, k_cli/git/patcher.py, k_cli/git/conflict_resolver.py and local tool/permission routes.
- Adjacent first-party surfaces excluded from ownership: developer-maintained documentation and benchmark claims, tests/mocks, hackathon/evaluation material, project contributor/CI governance and unshipped or broken background-daemon import. AWS Strands/Bedrock, LLM endpoints, GitHub and external PR reviewers are dependencies or environmental actors, not donated first-party organizational owners.
- First-party operating / deployment modes considered: interactive terminal SessionManager; model-directed standalone run; sequential persona pipeline; separate model-driven threaded subagents; optional PR review/fix CLI and SDK PR-watch calls; local sandbox, checkpoints and memory. A duplicated CLI watch registration exposes the background healer command whose module is absent at this ref, so that command is not credited as a functioning audit mode.
- Recursion level: one locally operated developer/coding workstation, including its own distributed coding tasks, not the maintainer organization that releases K-CLI or an entire GitHub project.
- Reviewed revision: 2f375d94ba445cdf51d3fb2bbfcc49f12f36ff89 (batch #996 frozen row 8).
- License screen: root LICENSE grants MIT; pyproject.toml declares the OSI-approved MIT classifier. No repin.
- Observation date: 2026-10-23.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

K-CLI ships a Python model/provider driver, tool/shell and local Git operations, a SessionManager that builds context and loops over code generation and verification, and an Orchestrator that passes outputs through Researcher, Architect, Coder, Critic and a deterministic Verifier with bounded debugger retries. Those named phases use one shared driver sequentially, not five simultaneously governing organizational systems. An optional SubagentDispatcher decomposes a prompt into threaded role tasks, evaluates dependencies and gathers output with PatchAggregator. Its workers issue distinct model calls, while thread limits and status transitions are deterministic. A separate GitHub PR review/fix path can inspect actual PR diff/review/CI artifacts, publish model-authored review feedback and later use comments for a corrective patch operation, but these steps require composition; no automatic auditor-to-primary-coding-control path is wired.

Persistent sessions, project learning notes, adaptive request/model routing, conflict resolution, static security rules, sandboxing, Git rollback and build/test validation are real local facilities. None should be renamed a VSM function solely because of its feature name. The root README contains performance, safety and benchmark claims that this assessment does not adopt as executed evidence. Native mock/script tests exercised operating code only, with no live model inference.

Frozen primary source: [session.py](https://github.com/krishivjoshi219-collab/K-Cli/blob/2f375d94ba445cdf51d3fb2bbfcc49f12f36ff89/k_cli/core/session.py), [orchestrator.py](https://github.com/krishivjoshi219-collab/K-Cli/blob/2f375d94ba445cdf51d3fb2bbfcc49f12f36ff89/k_cli/agents/orchestrator.py), [subagents.py](https://github.com/krishivjoshi219-collab/K-Cli/blob/2f375d94ba445cdf51d3fb2bbfcc49f12f36ff89/k_cli/agents/subagents.py), [PRLifecycleManager](https://github.com/krishivjoshi219-collab/K-Cli/blob/2f375d94ba445cdf51d3fb2bbfcc49f12f36ff89/k_cli/github/github_client.py), [PR watcher](https://github.com/krishivjoshi219-collab/K-Cli/blob/2f375d94ba445cdf51d3fb2bbfcc49f12f36ff89/k_cli/github/pr_watcher.py), [CLI](https://github.com/krishivjoshi219-collab/K-Cli/blob/2f375d94ba445cdf51d3fb2bbfcc49f12f36ff89/k_cli/cli.py), [SDK](https://github.com/krishivjoshi219-collab/K-Cli/blob/2f375d94ba445cdf51d3fb2bbfcc49f12f36ff89/k_cli/core/sdk.py).

## Operational model

K-CLI's model chooses coding output or corrections from task and tool/compiler feedback (S1=A). In optional parallel-subagent mode, independently invoked model roles work against one workspace and their outputs are aggregated. Task dependencies, worker status and patch aggregation do not demonstrate a specific inter-worker interference response (S2=—). The sequential persona controller and threaded scheduler do not give a distinct actor whole-current resource/commitment regulatory discretion (S3=—). Separate first-party PR review plus a PR-fix consumer is an intentionally exposed but not automatically integrated complementary audit/correction constructor (S3*=C). No shipped outside-and-then capability adaptation or identity-level ultimate-policy closure is established (S4/S5=—).

## S1 — Operations

- State: A
- Function: decide and carry out local software development, code generation, verification-driven repair, repository inspection and optional delegated coding work.
- Disturbance / variety regulated: task ambiguity, codebase state, model results, compiler/test errors, patch failures and changing worker outputs.
- Decisive decision or feedback right: configured model chooses generated implementation, response to diagnostics and subsequent debugger or delegated actions.
- Decision owner: model-backed K-CLI coding loop and separately prompted model workers; operator selects initial goal and provider.
- Supporting / enforcement mechanisms: LLMDriver transports inference; SessionManager manages context; Orchestrator prompts phases; Verifier, Patcher, GitGuard, shell tools, budgets and sandbox execute or constrain actions.
- Closure path: task/context → model code or role decision → deterministic validation and tool/patch outcome → later model correction or returned result.
- Boundary reachability: shipped CLI run/session commands, first-party Orchestrator, and explicit subagents/SDK routes instantiate the model driver and relevant tools.
- Why this is / is not agent-owned: removing the model leaves static prompts, checks and retry scheduling but no substantive choice of code or repair.
- Evidence: [Orchestrator](https://github.com/krishivjoshi219-collab/K-Cli/blob/2f375d94ba445cdf51d3fb2bbfcc49f12f36ff89/k_cli/agents/orchestrator.py), [SessionManager](https://github.com/krishivjoshi219-collab/K-Cli/blob/2f375d94ba445cdf51d3fb2bbfcc49f12f36ff89/k_cli/core/session.py), [SubagentWorker](https://github.com/krishivjoshi219-collab/K-Cli/blob/2f375d94ba445cdf51d3fb2bbfcc49f12f36ff89/k_cli/agents/subagents.py).
- Basis: explicit source and native mock-test wiring.
- Confidence: high for construction and feedback path; no efficacy claim.
- Caveats: simulated driver tests do not verify real provider quality, convergence or claims of flawless code.

## S2 — Coordination

- State: —
- Function: no complete regulation of specific interference among two independently coding S1 workers is established in the supported multi-agent mode.
- Disturbance / variety regulated: possible overlapping file edits, incompatible worker patches, conflicting dependencies or inconsistent test/implementation outcomes.
- Decisive decision or feedback right: no demonstrated model-owned collision judgment that selects and returns an inter-worker attenuation response.
- Decision owner: fixed dependency scheduler and aggregation code determine dispatch/collection; separate Git conflict tool resolves repository-level conflicts on explicit invocation.
- Supporting / enforcement mechanisms: SubagentTask dependencies, thread pool cap, shared message queue, worker statuses, PatchAggregator and separate ConflictResolver.
- Closure path: dependencies gate task launches and outputs are concatenated/verified, but incompatible simultaneous worker modifications are not detected, arbitrated and fed back as S2-specific corrected S1 commitments.
- Why this is / is not agent-owned: model-selected initial decomposition is task routing; deterministic DAG sequencing is not a demonstrated disturbance-specific coordination decision.
- Evidence: [SubagentDispatcher and PatchAggregator](https://github.com/krishivjoshi219-collab/K-Cli/blob/2f375d94ba445cdf51d3fb2bbfcc49f12f36ff89/k_cli/agents/subagents.py), [ConflictResolver](https://github.com/krishivjoshi219-collab/K-Cli/blob/2f375d94ba445cdf51d3fb2bbfcc49f12f36ff89/k_cli/git/conflict_resolver.py).
- Basis: structural source with 24/24 subagent and 62/62 conflict/patch tests.
- Confidence: medium-high, bounded to the shipped execution path.
- Caveats: the separate git conflict resolver may repair branch conflicts as a coding task; that alone does not prove coordination among K-CLI's own operational units.

### Absence scope

- Surfaces inspected: decomposer, SubagentDispatcher, worker message queue, PatchAggregator, conflict repair, CLI subagent invocation and their focused tests.
- Plausible first-party paths checked: DAG dependencies as mutual adjustment; patch aggregation as collision arbitration; explicit 3-way Git conflict solver as intra-team regulation; message statuses as corrective feedback.
- Why no material first-party path remains: none connects an evidenced pair of mutually interfering internal S1 work cells to a detected conflict, a coordination decision and altered subsequent worker behaviour in the installed mode.

## S3 — Inside-and-now control

- State: —
- Function: no distinct whole-current control owner is evidenced across K-CLI operational workers.
- Disturbance / variety regulated: competing task commitments, active worker capacity, priority changes and whole-session resource constraints.
- Decisive decision or feedback right: no model/parent first-party holder of continuing cross-worker commitment or priority intervention is present after the initial decomposition.
- Decision owner: the user selects goal and runtime caps; deterministic scheduler enforces max_workers and RAM checks; model makes local coding choices.
- Supporting / enforcement mechanisms: Orchestrator's fixed phase ordering, SubagentDispatcher's task/status/active-thread maps, thread cap and memory budget.
- Closure path: task dependencies and status completion are observed, but no whole-current discretionary resource bargaining, reassignment or intervention is returned into live worker operations.
- Why this is / is not agent-owned: replacing any proposed manager actor with static scheduler logic leaves the same launch/cap behaviour; names and status dashboards are not authority.
- Evidence: [Orchestrator](https://github.com/krishivjoshi219-collab/K-Cli/blob/2f375d94ba445cdf51d3fb2bbfcc49f12f36ff89/k_cli/agents/orchestrator.py), [SubagentDispatcher](https://github.com/krishivjoshi219-collab/K-Cli/blob/2f375d94ba445cdf51d3fb2bbfcc49f12f36ff89/k_cli/agents/subagents.py).
- Basis: structural source and mock-native orchestration tests.
- Confidence: medium-high.
- Caveats: local user commands and static limits are not separately demonstrated parent S3 modes.

### Absence scope

- Surfaces inspected: persona state machine, task decomposer, active-thread status maps, budget checks, runtime/session CLI, SDK and dashboard.
- Plausible first-party paths checked: initial model task decomposition as S3 allocation; status dashboard as whole-current view; RAM cap and max_workers as current-control decisions; manual operator model/persona choice as parent S3.
- Why no material first-party path remains: no shipped actor receives a whole-current view and actually revises shared operational commitments, priorities or cross-worker constraints with a returned decision; enforcement and task routing remain local/fixed.

## S3* — Complementary audit

- State: C
- Function: optional independent examination of already-produced repository PR artifacts beyond the coding loop's own routine compiler/test reports.
- Disturbance / variety regulated: defects or security/performance problems surviving coding and routine validation, visible in proposed PR changes and CI/review context.
- Decisive decision or feedback right: a separate model review evaluates live PR diff and changed-file evidence and can issue an APPROVE, REQUEST_CHANGES or COMMENT judgment; a separately invoked fix operation can consume review comments and CI to generate and verify a corrective patch.
- Decision owner: review model for audit judgment when configured with a real provider; operator/developer still composes when to run it, whether to publish findings, and whether to invoke remediation.
- Supporting / enforcement mechanisms: GitHubClient fetches direct PR artifacts, PRLifecycleManager structures verdicts and comments, Verifier/Patcher/GitGuard check repairs; GitHub review API transports the finding.
- Closure path: optional CLI pr review → direct diff + file list → independent model verdict → optionally posted GitHub review → separately invoked pr fix reads comments and CI → model-directed verified patch. There is no automatic required auditor-to-coding-loop return.
- Boundary reachability: shipped CLI pr review and pr fix subcommands and SDK watch_prs reach the first-party PRLifecycleManager or PRWatcherDaemon in normal non-mock configuration. The duplicate watch CLI command and absent background healer module are not used to establish this constructor.
- Why this is / is not agent-owned: model can own the separate audit judgment, but this is C rather than A because the first-party product does not close the whole independent corrective audit cycle without external composition.
- Evidence: [PRLifecycleManager review/fix](https://github.com/krishivjoshi219-collab/K-Cli/blob/2f375d94ba445cdf51d3fb2bbfcc49f12f36ff89/k_cli/github/github_client.py), [CLI pr commands](https://github.com/krishivjoshi219-collab/K-Cli/blob/2f375d94ba445cdf51d3fb2bbfcc49f12f36ff89/k_cli/cli.py), [SDK PR watcher](https://github.com/krishivjoshi219-collab/K-Cli/blob/2f375d94ba445cdf51d3fb2bbfcc49f12f36ff89/k_cli/core/sdk.py).
- Basis: explicit supported opt-in constructor and 65/65 focused GitHub mock tests; no real PR or live LLM audit executed.
- Confidence: medium for the constructor, not for autonomous audit quality or enforcement.
- Caveats: the watcher instantiated directly uses a mock driver by default; the SDK injects its configured driver. A CLI audit need not post comments, and a review is not a mandatory merge block.
- Claim being audited: correctness/safety/performance of already-proposed code changes.
- Ordinary reporting path: same coding loop's compiler/test outcome, patch success and worker summaries.
- Complementary access path: fresh review prompt built from GitHub PR diff, file list, PR metadata and later CI/comments, separately from generator session context.
- Independence boundary: distinct invocation and review decision context from the code-generating phase; composable, not a permanently independent organizational reviewer or guaranteed different model/provider.
- Who acts on findings: GitHub review recipients, operator and an optionally separately invoked PR-fix model; no automatic correction guarantee.

## S4 — Outside-and-then intelligence

- State: —
- Function: no completed externally and prospectively oriented capability-adaptation loop is established for this local workstation.
- Disturbance / variety regulated: changing dependencies, model/tool offerings, developer needs and future failure classes might matter, but no operational S4 loop is shown.
- Decisive decision or feedback right: none evidenced for evaluation and adoption of future capability options at the declared recursion.
- Decision owner: user chooses models and writes project memories/rules; adaptive current-request routing and repository intelligence remain operational mechanisms.
- Supporting / enforcement mechanisms: project memory notes, DevDocs retrieval, smart model router, model hub, trending/research commands and runtime session storage.
- Closure path: present-task context/model selection can change immediate execution; there is no external future model → adaptation alternative → decision → changed ongoing capability loop.
- Why this is / is not agent-owned: storing notes or choosing a model for this request does not own outside-and-then adaptation.
- Evidence: [model driver](https://github.com/krishivjoshi219-collab/K-Cli/blob/2f375d94ba445cdf51d3fb2bbfcc49f12f36ff89/k_cli/core/llm_driver.py), [CLI memory/model routes](https://github.com/krishivjoshi219-collab/K-Cli/blob/2f375d94ba445cdf51d3fb2bbfcc49f12f36ff89/k_cli/cli.py), [SessionManager](https://github.com/krishivjoshi219-collab/K-Cli/blob/2f375d94ba445cdf51d3fb2bbfcc49f12f36ff89/k_cli/core/session.py).
- Basis: first-party feature wiring and absence adjudication.
- Confidence: medium-high.
- Caveats: future extensions or a separate human product roadmap could add S4 but are outside this frozen shipped mode.

### Absence scope

- Surfaces inspected: persistent/project memory, smart routing, model management, DevDocs, trend commands, optional swarms and project development/roadmap notes.
- Plausible first-party paths checked: dynamic model selection, memory learning, externally sourced docs/repositories, repeated repair and benchmark evaluations as capability adaptation.
- Why no material first-party path remains: all return to immediate task support, manual note retention or adjacent development/evaluation; no supported first-party future-environment options loop changes the workstation's capability in dialogue with current control.

## S5 — Policy and identity

- State: —
- Function: no ultimate purpose/identity-policy decision and return path is established at the local workstation recursion.
- Disturbance / variety regulated: questions about ultimate identity, mission or permissible organizational trade-offs are not operationally adjudicated by the shipped agent.
- Decisive decision or feedback right: none at S5 level; the operator configures action permissions, providers and workflow modes.
- Decision owner: human local operator for tactical policy/configuration; project maintainer governance is an adjacent recursion.
- Supporting / enforcement mechanisms: permission/rule configuration, sandbox, credentials, GitHub merge gate and prompt/system persona selection.
- Closure path: tactical decisions influence next actions but no identified ultimate-policy issue → legitimate authority judgment → returned governing policy operation is wired.
- Why this is / is not agent-owned: control of action limits, security checks or commit permissions is enforcement rather than identity determination.
- Evidence: [CLI](https://github.com/krishivjoshi219-collab/K-Cli/blob/2f375d94ba445cdf51d3fb2bbfcc49f12f36ff89/k_cli/cli.py), [GitGuard](https://github.com/krishivjoshi219-collab/K-Cli/blob/2f375d94ba445cdf51d3fb2bbfcc49f12f36ff89/k_cli/git/git_guard.py), [sandbox](https://github.com/krishivjoshi219-collab/K-Cli/blob/2f375d94ba445cdf51d3fb2bbfcc49f12f36ff89/k_cli/core/sandbox.py).
- Basis: inspected standard configuration, permission, CLI and governance boundary.
- Confidence: medium-high.
- Caveats: no inference from external repository maintainer policy to the local product harness.

### Absence scope

- Surfaces inspected: runtime rules, credentials, sandbox controls, persona selection, permission/approval paths, Git/PR operations and maintainer project documents.
- Plausible first-party paths checked: human permission prompt as parent S5, custom rules as evolving mission policy, PR merge authorization as ultimate authority and project README/roadmap as runtime identity control.
- Why no material first-party path remains: each is an action-level constraint, operator configuration or adjacent maintainer process without a shipped identity-policy issue, authoritative judgment and returned system-level policy closure.

## Distributed OSS parent arrangement

The public repository and contributors develop and release K-CLI, but their project coordination is not part of the locally installed coding session. No distributed parent S3/S4/S5 mode is inferred from GitHub contribution or release activity.

## Self-hosted and non-human modes

Local model/provider configuration and optional human review/PR commands are supported, but no additional parent-governed whole-current, prospective or identity closure is credited. A separate automatic model-driven reviewer can be composed from shipped PR APIs, hence the bounded S3*=C constructor; the reviewer is not mandated or autonomously integrated into coding operation.

## Recursion

The primary coding session is the local operational unit. Optional threaded model workers may form lower-recursion task cells; their mere creation does not establish a complete metasystem. GitHub project governance and external LLM providers are not promoted into this recursion.

## Variety and escalation

Model generations and child tasks absorb operational coding variety; verifier failures prompt bounded debugger retries, GitGuard supports rollback and the operator can choose further work. PR review findings can be published and separately taken up by the PR-fix route. Neither retry/status nor ordinary human intervention is treated as an algedonic channel or S5 decision without additional evidence.

## Evidence gaps

- Deterministic mock/native checks: Orchestrator 6/6, Persona 17/17, Subagents 24/24, Session 16/16, Verifier 28/28, Conflict/Patcher 62/62, GitGuard/SmartGit 37/37, Driver 23/23, GitHub/CLI 65/65, SDK/features 17/17: **295/295 PASS**. No model-provider inference or live PR action was performed.
- The initially sandboxed run had false environment failures from inaccessible /proc PID lookup and the default read-only home cache; the same selected tests passed with normal /proc and a dedicated temporary K_CLI_CACHE_DIR.
- No live-model evaluation of role decisions, substantive code quality, adverse case resolution, audit independence in deployment or GitHub ruleset enforcement was performed. The S3* conclusion is a source-supported constructor, not an observed successful independent audit.
- CLI watch is registered twice, with the later registration referring to a missing background_daemon module; this path was not treated as a functioning standard audit loop. Independently callable PR review/fix routes remain present.
