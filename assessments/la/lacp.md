---
harness_id: lacp
project_name: LACP
repository: https://github.com/0xNyk/lacp
review_ref: e31f134b689afd6a71d94b0420682d1f528d6fa1
reviewed_at: 2026-11-02
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# LACP

## Review boundary

- System in focus: LACP v0.10.1 local policy, execution, evidence and recovery wrapper around installed Claude, Codex, Hermes and other CLI coding agents, including its optional Claude plugin hooks and swarm adapters.
- Purpose and identity: route agent tasks through explicit risk, budget, context and provider controls; keep execution evidence; provide multi-session worktree/swarm facilities and session stop-quality checks.
- Relevant environment: operator-defined tasks, trust flags, workspace git state, local or remote execution targets, provider CLIs, process capacity, output/artifact files, task overlaps, transcript claims and test failures.
- Standard-distribution boundary: public bin/ CLI wrappers, scripts/lacp-lib.sh, config policies, plugin/hooks/hooks.json and bundled hook scripts installed alongside existing external model agents. External CLI and models own coding/tool session decisions; operator supplies risk policy and approvals.
- Credited operating / distribution surfaces: lacp run/route/sandbox-run, orchestrate/up/swarm, worktree adapter, plugin Claude Stop/PreTool/PostTool hooks and shipped policy schema.
- Adjacent first-party surfaces excluded from ownership: repository maintainer governance, docs roadmap, CI tests and release scripts, standalone user dashboards, and unrelated optional Obsidian/knowledge integrations without a mission control closure.
- Modes considered: direct gated invocation and adopted-local wrappers; dmux/tmux/Claude worktree sessions; swarm manifest planning and launch; optional plugin Stop quality gate with Ollama. Optional remote sandbox requires installed adapter and explicit opt-in.
- Recursion: one local operator-owned execution control plane hosting one or multiple model S1 sessions; a manifest is not itself a model supervisor.
- Frozen source: e31f134b689afd6a71d94b0420682d1f528d6fa1; observation 2026-11-02; Profile 0.2.4, Methodology 0.3.7.

## Repository architecture

LACP explicitly delegates model, tool and session ownership to existing agent hosts. Its run/sandbox-run pipeline classifies command risk and route from provided context, enforces selected budgets and context contracts, then executes the host command with trace/artifact capture. The multi-session orchestration adapter launches external agents in tmux/dmux/Claude worktrees. Swarm planning normalizes per-job file reservations, detects exact/prefix-overlap across distinct sessions and emits collision warnings. Launch forwards jobs to the deterministic orchestrate adapter even if planning has warnings; separately defined per-swarm file-lock helpers are not called by the launch path. The Claude plugin installs a Stop hook that scans the agent's final message and transcript, optionally runs allowed tests, optionally asks a local Ollama model to score incomplete-work rationalization, and can block the agent's attempted stop. This is a supported construction surface, but the Ollama path is health-dependent, often bypassed by heuristic fast path and fail-open.

Primary sources: [README](https://github.com/0xNyk/lacp/blob/e31f134b689afd6a71d94b0420682d1f528d6fa1/README.md), [framework scope](https://github.com/0xNyk/lacp/blob/e31f134b689afd6a71d94b0420682d1f528d6fa1/docs/framework-scope.md), [sandbox run](https://github.com/0xNyk/lacp/blob/e31f134b689afd6a71d94b0420682d1f528d6fa1/bin/lacp-sandbox-run), [swarm](https://github.com/0xNyk/lacp/blob/e31f134b689afd6a71d94b0420682d1f528d6fa1/bin/lacp-swarm), [Stop hook](https://github.com/0xNyk/lacp/blob/e31f134b689afd6a71d94b0420682d1f528d6fa1/plugin/hooks/scripts/stop_quality_gate.py).

## Operational model

The coding-agent host makes substantive file/tool decisions in its own model loop; LACP enforces the operator's selected execution envelope around that loop. In multi-session mode, a human or external model/launcher supplies a manifest with tasks, commands and reservations. LACP computes and reports conflicts without independently negotiating a new peer work allocation. The optional stop-quality model is a distinct scoring actor from the underlying coding host but consumes mostly its textual completion claims rather than a separately privileged full product audit.

## S1 — Operations

- State: A
- Function: undertake a coding task through an external Claude/Codex/Hermes model-and-tool session under LACP's first-party invocation contract.
- Disturbance / variety regulated: source/code uncertainty and implementation/test feedback within the working session.
- Decisive decision or feedback right: hosted coding model chooses tool calls and edits and adapts to results, while LACP checks their execution conditions.
- Decision owner: configured external agent model reached through the standard LACP run/adopted-local or multi-session path.
- Supporting / enforcement mechanisms: lacp run/route/sandbox-run, CLI host command execution, provider adapter and local policy/artifact capture.
- Closure path: task → launched model host → model tool/results → successive model decisions → host final result under LACP controls.
- Boundary reachability: documented quick-start and adopted-local wrappers execute real Claude/Codex commands; not a repository demo-only flow.
- Why this is / is not agent-owned: without the hosted model, the deterministic wrapper can route shell commands but cannot perform discretionary coding actions.
- Evidence: [README](https://github.com/0xNyk/lacp/blob/e31f134b689afd6a71d94b0420682d1f528d6fa1/README.md), [orchestrate](https://github.com/0xNyk/lacp/blob/e31f134b689afd6a71d94b0420682d1f528d6fa1/bin/lacp-orchestrate), [up](https://github.com/0xNyk/lacp/blob/e31f134b689afd6a71d94b0420682d1f528d6fa1/bin/lacp-up).
- Basis: explicit + structural.
- Confidence: high on installed host integration, not provider task quality.
- Caveats: external host supplies the model/tool loop; LACP alone can route an arbitrary non-agent shell command, which is not the credited S1 mode.

## S2 — Coordination

- State: C
- Function: expose specific interference information between planned parallel coding sessions through reservation overlap detection.
- Disturbance / variety regulated: separate agents claiming exact or nested workspace paths, risking conflicting writes during a swarm.
- Decisive decision or feedback right: collision list and warnings identify overlapping peer reservations, but a developer/host must compose an autonomous actor to reassign or block affected jobs and close the peer correction loop.
- Decision owner: no first-party autonomous conflict mediator; current caller/operator decides whether to amend the manifest. C credits the purpose-built first-party construction path, not autonomous closure.
- Supporting / enforcement mechanisms: per-job reservations, normalize_reservation, reservations_overlap, collision report in swarm plan JSON and user-visible warnings.
- Closure path: distinct session reservations → exact/prefix overlap report → caller can revise job reservations and re-plan; no automatic post-report job correction is installed.
- Boundary reachability: lacp swarm plan and launch are standard CLI operations and expose machine-readable collision diagnostics.
- Why this is / is not agent-owned: the tool knows which S1 peers conflict but neither an agent nor the deterministic launcher chooses a corrected division of work; warnings alone do not imply A.
- Distinct S1 units: separate Claude/Codex sessions within one swarm job manifest, commonly operating on a shared repository/worktrees.
- Inter-S1 disturbance: conflicting claimed files/directories between two different session IDs, detected as exact or prefix-overlap reservations.
- Attenuating coordination relation: purpose-built path reservations and overlap warnings allow a composed controller to separate ownership before launch.
- Feedback into subsequent S1 behaviour: a host controller can consume collisions JSON, revise manifest ownership and rerun plan; this return requires composition and is not implemented automatically.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: algorithm compares actual work claims of distinct sessions for file-level mutual interference rather than merely scheduling generic tasks.
- Evidence: [swarm planning](https://github.com/0xNyk/lacp/blob/e31f134b689afd6a71d94b0420682d1f528d6fa1/bin/lacp-swarm), [swarm CI fixtures](https://github.com/0xNyk/lacp/blob/e31f134b689afd6a71d94b0420682d1f528d6fa1/scripts/ci/test-swarm.sh).
- Basis: explicit + structural constructor.
- Confidence: high for detector, moderate for C functional threshold.
- Caveats: collisions are warnings, not hard admission errors; unused lock helper definitions and a scored episode winner are not evidence of an automatically negotiated peer-resolution loop.

## S3 — Inside-and-now control

- State: —
- Function: no first-party discretionary whole-system supervisory control loop is established by routing and deterministic policy checks alone.
- Disturbance / variety regulated: load pressure, risk tier, budgets and session contexts are handled by preselected deterministic rules, not a mission-level current supervisor.
- Decisive decision or feedback right: none established for whole operational portfolio intervention.
- Decision owner: operator configures risk and budgets; LACP then enforces thresholds per invocation, without returning a whole-system discretionary decision from a qualified parent mode.
- Supporting / enforcement mechanisms: risk tier mapping, context/fingerprint checks, runtime-pressure load backoff, swarm status and manual launch policies.
- Closure path: no whole-system view → owner-selected current portfolio change → feedback-adjusted operating plan loop.
- Boundary reachability: no positive S3 mode claimed.
- Why this is / is not agent-owned: command routing and preconfigured limits are enforcement; a launcher naming multiple sessions is not automatically a current-control agent.
- Evidence: [route](https://github.com/0xNyk/lacp/blob/e31f134b689afd6a71d94b0420682d1f528d6fa1/bin/lacp-route), [sandbox-run](https://github.com/0xNyk/lacp/blob/e31f134b689afd6a71d94b0420682d1f528d6fa1/bin/lacp-sandbox-run), [runtime capacity](https://github.com/0xNyk/lacp/blob/e31f134b689afd6a71d94b0420682d1f528d6fa1/scripts/lacp-lib.sh).
- Basis: bounded structural absence.
- Confidence: medium-high.
- Caveats: humans may manually administer many agent sessions, but a first-party closed parent current-control mode was not established from configuration/status APIs.

### Absence scope

- Surfaces inspected: run/route policy, swarm/orchestrate manifests and status, runtime capacity and risk approvals.
- Plausible first-party paths checked: whole-operation view, discretionary reallocation across active agents, parent/human supervisory decision route and returned changed commitments.
- Why no material first-party path remains: the source runs selected commands and threshold gates, but it does not join a live whole-system supervisor decision with reallocation and subsequent feedback.

## S3* — Complementary audit

- State: C
- Function: expose a separate stop-time completion challenge and evidence checks against a coding agent's attempted termination.
- Disturbance / variety regulated: premature stop, unverified success claims, test deferral and rationalized incomplete tasks.
- Decisive decision or feedback right: the bundled Stop hook can inspect transcript/optional tests and invoke a separate local Ollama model for criteria-based completion scoring, returning block/allow to the original Claude session.
- Decision owner: optional local scorer and deterministic tests rather than the coding agent; fully independent truth/contract access and evaluator availability still require caller composition.
- Supporting / enforcement mechanisms: Claude plugin hooks.json, transcript scan, test verification allowlist, Ollama JSON scoring, bounded stop-block counter and feedback in Stop protocol.
- Closure path: coding-agent stop request → hook scans claims/test evidence → optional separate score or failed test → block and reason returned to coding agent; fail-open and fast-path gaps limit completeness.
- Boundary reachability: the first-party Claude plugin installs the Stop hook; enabling Ollama/test evidence is environment dependent and not guaranteed for every run.
- Why this is / is not agent-owned: a separate model may challenge claims, but text-only default scoring, heuristics and fail-open missing scorer leave the full complementary evidence authority/closure to be composed, so C rather than A.
- Claim being audited: coding agent's final response that current work is complete or that deferrals are legitimate.
- Ordinary reporting path: coding agent's last assistant message and session transcript.
- Complementary access path: distinct Stop process, optional test invocation and independent local Ollama score with sprint criteria.
- Independence boundary: separate hook process/model from coding agent, but most scoring input is agent-authored narrative; product-level read-only independent oracle not generally installed.
- Who acts on findings: Claude Stop protocol can block the finish and inject reason for another agent turn, subject to max-block circuit breaker.
- Evidence: [hooks registration](https://github.com/0xNyk/lacp/blob/e31f134b689afd6a71d94b0420682d1f528d6fa1/plugin/hooks/hooks.json), [Stop hook](https://github.com/0xNyk/lacp/blob/e31f134b689afd6a71d94b0420682d1f528d6fa1/plugin/hooks/scripts/stop_quality_gate.py).
- Basis: explicit + structural constructor.
- Confidence: high for hook path; moderate for adequacy of independent audit evidence.
- Caveats: heuristic fast-path skips scoring often, Ollama failure allows stop and three-block cap prevents indefinite audit enforcement.

## S4 — Outside-and-then intelligence

- State: —
- Function: no externally anchored future adaptation decision loop established.
- Disturbance / variety regulated: future provider/capability changes may be tracked by commands or updated manually, but not selected and returned by a first-party agent intelligence cycle.
- Decisive decision or feedback right: none established for prospectively adapting the operating system.
- Decision owner: none established.
- Supporting / enforcement mechanisms: memory/learning commands, vendor watch, optimization and historical episode data.
- Closure path: no evidenced external signal → model future option → adopted operating capability return.
- Boundary reachability: no positive S4 mode claimed.
- Why this is / is not agent-owned: recording run lessons or evaluating current candidates does not itself close S4 future adaptation.
- Evidence: [README](https://github.com/0xNyk/lacp/blob/e31f134b689afd6a71d94b0420682d1f528d6fa1/README.md), [vendor watch](https://github.com/0xNyk/lacp/blob/e31f134b689afd6a71d94b0420682d1f528d6fa1/bin/lacp-vendor-watch).
- Basis: bounded structural absence.
- Confidence: medium.
- Caveats: optional monitoring scripts are potential inputs, not by themselves a closed adaptation organization.

### Absence scope

- Surfaces inspected: memory and learning tools, vendor watch, optimization, swarm episode handling and runbook.
- Plausible first-party paths checked: external trend sensing, future option development, agent/parent adoption judgment and changed present capability.
- Why no material first-party path remains: individual tools lack a source-evidenced, closed prospective decision-and-return relation at the assessed run boundary.

## S5 — Policy and identity

- State: —
- Function: no identity or ultimate organizational policy adjudication loop established.
- Disturbance / variety regulated: risk-tier and trust decisions constrain commands, not identity-level policy disputes.
- Decisive decision or feedback right: no S5 authority/return, despite strong task security gates.
- Decision owner: none established for S5; operator policy file/approvals set execution constraints.
- Supporting / enforcement mechanisms: sandbox policy, critical risk approvals, trust flags, agent-id registry and pre-tool guards.
- Closure path: no ultimate-policy issue → legitimate parent identity decision → changed policy returned to future operation.
- Boundary reachability: no positive S5 mode claimed.
- Why this is / is not agent-owned: fixed security rules and per-command approval are not mission identity governance.
- Evidence: [route](https://github.com/0xNyk/lacp/blob/e31f134b689afd6a71d94b0420682d1f528d6fa1/bin/lacp-route), [sandbox-run](https://github.com/0xNyk/lacp/blob/e31f134b689afd6a71d94b0420682d1f528d6fa1/bin/lacp-sandbox-run).
- Basis: bounded structural absence.
- Confidence: high.
- Caveats: external operator or maintainer may own policy for an actual organization, not the built-in run loop.

### Absence scope

- Surfaces inspected: policy JSON, risk approvals, agent identity registry, stop/pre-tool hooks and maintainer boundaries.
- Plausible first-party paths checked: substantive identity policy conflict, legitimate adjudication, return of changed identity commitments into agent execution.
- Why no material first-party path remains: installed controls enforce already-chosen command risk constraints and record identities without governing ultimate identity.

## Distributed OSS parent arrangement

Maintainers and local users can modify LACP policy/release behavior, but the repository's public development flow is adjacent to each local agent execution. No distinct distributed-OSS parent S3/S4/S5 closed mode inferred.

## Self-hosted and non-human modes

Local first-party plugins support externally model-owned coding work; human budget/critical approvals and opt-in remote execution are per-command constraints. No parent modifier is assigned without a whole-function decision return.

## Recursion

One operator deployment wraps one or more external agent S1 sessions. Swarm jobs are distinct operational cells whose path reservations feed an S2 construction surface; static policy rules and hook processes are not automatically higher viable levels.

## Variety and escalation

Risk, budget, context, fingerprint, load and Stop-hook checks generate allow/block/log results. A collision report can inform composition of corrected peer ownership. Separate Ollama quality scoring can return a stop block. Fail-open paths and uncalled lock helpers limit credited closure.

## Evidence gaps

Frozen source inspection and static code/CI evidence, not a paid provider or Claude/plugin runtime E2E execution. The S2 and S3* C states deliberately distinguish shipped construction paths from guaranteed autonomous coordination/audit closure.
