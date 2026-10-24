---
harness_id: zerostack
project_name: zerostack
repository: https://github.com/gi-dellav/zerostack
review_ref: 16fadb3b8f29238a5716eaf937ecf9d41a42f946
reviewed_at: 2026-10-06
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-06
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# zerostack

## Review boundary

- System in focus: the first-party zerostack coding runtime at frozen revision 16fadb3b8f29238a5716eaf937ecf9d41a42f946, including its model/tool agent loop, built-in prompts, task subagents, orchestrator-mode headless workers, worktree/supervision protocol, reviewer workers, permissions/session/loop state, advisor, memory and supported interactive/headless/ACP execution.
- Purpose and identity: perform software-engineering work through a coding agent that can directly edit/test, dispatch read-only investigations, or in the shipped orchestrator mode decompose complex work into fresh autonomous coding workers, supervise them and integrate their results.
- Relevant environment: user goals/approvals, repository files and tests, worker worktrees, process exit/timeout state, worker result flags/logs, provider/model responses, permissions, session history, memory and external MCP/tool services.
- Standard-distribution boundary: the shipped zerostack binary plus repository-owned prompts and runtime modules. Pi/OpenCode are inspirations only. External providers, MCP servers, shell programs and the optional separately installed multistack product are dependencies and cannot donate ownership.
- Credited operating / distribution surfaces: src/agent, src/extras/subagents, src/extras/advisor, src/extras/loop, src/extras/git_worktree, permission/session/runtime paths, data/prompts including orchestrator/review/review-security, built-in tools and supported headless/interactive/ACP modes.
- Adjacent first-party surfaces excluded from ownership: repository CI/tests/docs as development evidence, and external multistack. A generic named prompt is credited only where its instructions are actually a shipped runtime operating mode with reachable first-party tools/subprocess paths.
- First-party operating / deployment modes considered: normal coding mode; read-only task subagents; orchestrator prompt mode with fresh headless write workers; read-only review/review-security worker mode; optional advisor model or human handoff; loop/worktree modes; supported provider/permission variants.
- Recursion level: one complex zerostack coding run in orchestrator mode is the viable-unit candidate for multi-agent functions. The conductor and spawned full coding workers are operational S1 units when each owns a focused coding outcome.
- Reviewed revision: 16fadb3b8f29238a5716eaf937ecf9d41a42f946.
- Observation date: 2026-10-06.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

The core Rust Agent streams model turns, dispatches coding tools and feeds results back into one conversation. The default subagent feature adds a task tool whose children are fresh-context read-only investigation agents; multiple prompts run in parallel and return ordered summaries.

The shipped orchestrator prompt adds a materially different mode: the conductor may launch full fresh zerostack -p workers through bash with explicit tool/permission/model bounds. It is told to partition independent workstreams, keep at most three concurrent workers, isolate output, use per-worker PID/timeout and DONE/FAILED result contracts, re-dispatch failed work after shrinking scope, and use separate git worktrees where overlapping file edits would otherwise collide. The conductor, not a deterministic static queue, decides the substantive partition, isolation strategy, fail policy and later integration order.

The same shipped prompt catalog supports fresh read-only review/review-security workers. Such a worker can directly inspect repository files with read/grep/find_files under its own context and return findings to the conductor before integration. This is distinct from the optional Advisor, which sees a transcript and provides strategic guidance but lacks an independent repository evidence channel.

## Operational model

Ordinary coding remains model-owned S1. In orchestrator mode the conductor turns one complex user objective into several operational worker commitments and regulates their interaction. Worker process/log/flag state returns to the conductor, which decides whether work is accepted, retried with smaller scope, abandoned or integrated.

Isolation and supervision are not inferred merely from concurrency. The positive S2/S3 claims use the explicit first-party orchestration protocol for conflicting file scopes/worktrees, process status, structured result contracts and merge sequencing. S3* uses a separate fresh model context with direct read-only repository evidence.

## S1 — Operations

- State: A
- Function: autonomously inspect, modify and verify software in response to a user goal, directly or through focused fresh coding workers.
- Disturbance / variety regulated: unfamiliar code, implementation choices, test failures, tool/process failures, ambiguous local evidence, provider/model variation and bounded delegated work.
- Decisive decision or feedback right: select substantive coding/tool actions, interpret results, choose implementation changes and decide when the assigned operational objective is complete.
- Decision owner: the active model-backed zerostack Agent; spawned headless coding workers own their bounded workstreams.
- Supporting / enforcement mechanisms: tool dispatch, permission modes, sandboxing, session/context handling, prompt modes, worktrees, retry/turn bounds and provider adapters.
- Closure path: user/parent goal → model chooses code/tool actions → first-party runtime executes → evidence returns → model revises or completes; delegated write workers close the same loop inside their explicit workstream.
- Boundary reachability: both ordinary and headless -p modes use the first-party coding runtime; orchestrator mode invokes those workers through a shipped prompt/tool path.
- Why this is / is not agent-owned: deterministic runtime mechanisms constrain execution but do not choose the implementation or interpret the engineering evidence.
- Evidence: [README.md](https://github.com/gi-dellav/zerostack/blob/16fadb3b8f29238a5716eaf937ecf9d41a42f946/README.md); [src/agent/runner.rs](https://github.com/gi-dellav/zerostack/blob/16fadb3b8f29238a5716eaf937ecf9d41a42f946/src/agent/runner.rs); [data/prompts/orchestrator.md](https://github.com/gi-dellav/zerostack/blob/16fadb3b8f29238a5716eaf937ecf9d41a42f946/data/prompts/orchestrator.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: read-only task subagents are supporting investigation S1s only when their focused result is treated as an operational outcome; the stronger multi-agent claims below use full headless coding workers.

## S2 — Coordination

- State: A
- Function: attenuate interference among concurrently active coding workers by choosing independent scopes or isolated worktrees and integrating their changes in a controlled order.
- Disturbance / variety regulated: parallel workers overwriting the same files, interleaved outputs, cross-talk through shared sessions, conflicting branches/worktrees and integration conflicts.
- Decisive decision or feedback right: decide task/file partition, whether work can share the checkout or requires separate worktrees, and the sequential integration order after isolated verification.
- Decision owner: the model-backed conductor operating under the shipped orchestrator prompt.
- Supporting / enforcement mechanisms: fresh --no-session workers, per-worker temp logs/result files, git worktrees/branches, wait/merge protocol and deterministic shell/git behavior.
- Closure path: conductor identifies parallelizable work and possible overlap → assigns separate worker scopes and, for overlap, isolated worktrees → workers execute independently → conductor inspects their results/diffs → merges accepted work sequentially or reworks conflicting/failed streams.
- Boundary reachability: orchestrator is a shipped prompt mode and explicitly describes executable zerostack -p commands, worktree isolation and merge behavior using the first-party binary/runtime.
- Why this is / is not agent-owned: worktrees and git enforce separation, but the conductor chooses which operational commitments may run together, which scopes must be isolated and how accepted streams are integrated.
- Distinct S1 units: full fresh zerostack -p coding workers, each owning a bounded independent write workstream.
- Inter-S1 disturbance: two concurrent workers editing overlapping files can overwrite/conflict; the prompt explicitly identifies this risk and changes the topology when it exists.
- Attenuating coordination relation: the conductor assigns separate file scopes where possible and otherwise places workers in distinct worktrees before sequential merge.
- Feedback into subsequent S1 behaviour: worker DONE/FAILED state plus isolated diff/test evidence determines whether a stream is integrated, re-run with narrower scope, or not merged; conflicts are resolved before subsequent integration.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the mechanism is selected specifically to reduce interference between distinct operational workstreams and feeds their interaction outcome back into how those workstreams proceed/integrate.
- Evidence: [data/prompts/orchestrator.md](https://github.com/gi-dellav/zerostack/blob/16fadb3b8f29238a5716eaf937ecf9d41a42f946/data/prompts/orchestrator.md); [README.md](https://github.com/gi-dellav/zerostack/blob/16fadb3b8f29238a5716eaf937ecf9d41a42f946/README.md); [src/extras/git_worktree/mod.rs](https://github.com/gi-dellav/zerostack/blob/16fadb3b8f29238a5716eaf937ecf9d41a42f946/src/extras/git_worktree/mod.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the ordinary read-only task subagents do not establish S2 by themselves; the positive claim is for the full coding-worker orchestration mode.

## S3 — Inside-and-now control

- State: A
- Function: regulate current multi-worker commitments by monitoring active worker status/results and deciding continue, retry, shrink scope, fail-fast, or integrate.
- Disturbance / variety regulated: hung workers, timeouts, failed verification, incomplete/missing result contracts, worker disagreement and current integration readiness.
- Decisive decision or feedback right: choose current worker concurrency/fail policy, kill peers under fail-fast when appropriate, retry only failed work, shrink timed-out scope, and decide which completed streams are ready to merge.
- Decision owner: the model-backed conductor.
- Supporting / enforcement mechanisms: PIDs, timeout exit codes, per-worker logs, DONE/FAILED files, wait-all/fail-fast shell controls, worktree status/diff/tests and sequential merge commands.
- Closure path: conductor launches current worker set → observes exit/status/result contracts and verification evidence → makes bounded current-control decision per stream → retries/stops/integrates accordingly → remaining current work proceeds under the returned decision.
- Boundary reachability: these supervision and recovery rules are part of the shipped orchestrator operating prompt and use reachable first-party headless workers plus standard runtime tools.
- Why this is / is not agent-owned: timeout/shell primitives only expose/enforce status; the conductor interprets the whole worker set and decides the substantive response.
- Whole-system current view: the conductor retains the parent task decomposition plus each current worker PID/exit code, log/result flag, touched-file report, verification result and worktree/diff state.
- Current-control decision scope: active commitment count, wait-all versus fail-fast, cancellation after peer failure, retry versus scope reduction, acceptance for integration and integration order.
- Evidence: [data/prompts/orchestrator.md](https://github.com/gi-dellav/zerostack/blob/16fadb3b8f29238a5716eaf937ecf9d41a42f946/data/prompts/orchestrator.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the long-horizon Ralph loop's deterministic iteration budget is not the owner of this claim; S3 is credited to the conductor's multi-worker current-control decisions.

## S3* — Complementary audit

- State: A
- Function: independently inspect a coding workstream with a fresh read-only reviewer context and return findings before the conductor accepts/integrates the work.
- Disturbance / variety regulated: implementation defects, security weaknesses, missing tests or incorrect worker self-reports that can survive ordinary author execution.
- Decisive decision or feedback right: independently inspect repository evidence and produce an Approve / Needs Changes / Reject style review judgment or security findings.
- Decision owner: the separate model-backed review or review-security zerostack worker.
- Supporting / enforcement mechanisms: --no-session fresh context, --read-only/tool allowlist, review/review-security system prompt, dedicated worker log/result path and parent integration gate.
- Closure path: coding worker produces changes → conductor dispatches a fresh read-only review worker over the relevant files/change → reviewer reads/searches repository evidence and returns findings → conductor uses findings to accept, repair/re-run or withhold integration.
- Boundary reachability: review and review-security are shipped prompt modes; orchestrator documents least-privilege fresh workers and includes a concrete read-only audit-worker invocation pattern.
- Why this is / is not agent-owned: the reviewer model makes the audit judgment from its own fresh repository-reading path; deterministic prompt/tool restrictions merely enforce independence/least privilege.
- Claim being audited: a worker's implementation/change or its claim that a bounded workstream is correct and ready for integration.
- Ordinary reporting path: the author worker's DONE/FAILED flag, summary, touched-file list and verification report.
- Complementary access path: a separate --no-session read-only reviewer can directly read/grep/find the repository rather than trusting the author worker's report.
- Independence boundary: fresh context, no resumed parent/sibling history, read-only specialist prompt and separate process/model call.
- Who acts on findings: the conductor receives the reviewer result and owns the subsequent repair/re-run/integration decision.
- Evidence: [data/prompts/orchestrator.md](https://github.com/gi-dellav/zerostack/blob/16fadb3b8f29238a5716eaf937ecf9d41a42f946/data/prompts/orchestrator.md); [data/prompts/review.md](https://github.com/gi-dellav/zerostack/blob/16fadb3b8f29238a5716eaf937ecf9d41a42f946/data/prompts/review.md); [data/prompts/review-security.md](https://github.com/gi-dellav/zerostack/blob/16fadb3b8f29238a5716eaf937ecf9d41a42f946/data/prompts/review-security.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the optional Advisor is not needed for this claim and is not treated as independent audit merely because it uses another model; S3* rests on the fresh direct repository-evidence worker path.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party external-and-prospective adaptation loop is established.
- Disturbance / variety regulated: no qualifying external/future condition is placed under a loop that develops future organizational options and returns them into current capability.
- Decisive decision or feedback right: none established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: persistent Markdown memory, web/search tools, provider switching, advisor strategy, prompt/model mapping and context compaction support current/future sessions but do not by themselves close S4.
- Closure path: not applicable.
- Boundary reachability: no positive S4 path claimed.
- Why this is / is not agent-owned: memory can retain facts and an advisor can recommend a current course correction, but neither path establishes an outside-and-then option-development loop with a return into S3/current capability.
- Evidence: [src/extras/memory/mod.rs](https://github.com/gi-dellav/zerostack/blob/16fadb3b8f29238a5716eaf937ecf9d41a42f946/src/extras/memory/mod.rs); [src/extras/advisor/mod.rs](https://github.com/gi-dellav/zerostack/blob/16fadb3b8f29238a5716eaf937ecf9d41a42f946/src/extras/advisor/mod.rs); [docs/CONFIG.md](https://github.com/gi-dellav/zerostack/blob/16fadb3b8f29238a5716eaf937ecf9d41a42f946/docs/CONFIG.md).
- Basis: structural absence review.
- Confidence: high.
- Caveats: cross-session notes and model/config choices may affect later runs, but persistence/configuration/reaction is not sufficient S4 under the active Methodology.

### Absence scope

- Surfaces inspected: memory, advisor, provider/model routing, web search, prompt chaining, loop validation, worktree orchestration and session persistence.
- Plausible first-party paths checked: learned future strategy, autonomous model/tool reconfiguration, durable experience feedback, environment scanning and retained plan adaptation.
- Why no material first-party path remains: inspected paths either support current execution, store context, or react to current failures; no closed external-and-prospective option loop was found.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy governance loop is established.
- Disturbance / variety regulated: no identity-level policy conflict is routed to an authoritative S5 owner.
- Decisive decision or feedback right: none established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: permission modes, sandbox/security policy, system prompts, prompt-mode directives, config and human approvals constrain operation but do not establish ultimate identity authority.
- Closure path: not applicable.
- Boundary reachability: no positive S5 path claimed.
- Why this is / is not agent-owned: coding/orchestrator/reviewer agents operate inside developer/user-authored rules and cannot authoritatively redefine zerostack's identity or ultimate operating principles.
- Evidence: [README.md](https://github.com/gi-dellav/zerostack/blob/16fadb3b8f29238a5716eaf937ecf9d41a42f946/README.md); [src/permission/mod.rs](https://github.com/gi-dellav/zerostack/blob/16fadb3b8f29238a5716eaf937ecf9d41a42f946/src/permission/mod.rs); [docs/CONFIG.md](https://github.com/gi-dellav/zerostack/blob/16fadb3b8f29238a5716eaf937ecf9d41a42f946/docs/CONFIG.md).
- Basis: structural absence review.
- Confidence: high.
- Caveats: human advisor handoff provides current guidance and permissions provide local control, but neither is an identity/ultimate-policy loop.

### Absence scope

- Surfaces inspected: permission modes, prompts, advisor handoff, config, sandbox, hooks, model/provider selection and orchestration protocol.
- Plausible first-party paths checked: autonomous constitution/policy revision, parent identity governance, durable authority changes and agent-written security policy.
- Why no material first-party path remains: all identified policy surfaces are operating constraints or current guidance rather than identity-level authoritative closure.

## Distributed OSS parent arrangement

The assessed organization is a running zerostack coding organization, not the GitHub maintainer project. Maintainers/contributors are not imported as runtime parent S3/S4/S5 owners.

## Self-hosted and non-human modes

zerostack supports local and hosted providers plus headless/ACP operation. The positive S2/S3/S3* claims use non-human first-party model/runtime paths and do not depend on the optional human Advisor handoff.

## Recursion

In orchestrator mode the conductor plus full coding workers form the assessed viable unit. Coding workers are S1; the conductor owns S2 and S3 over them; fresh read-only specialist reviewer workers provide S3*. Read-only task subagents, provider clients and shell/git primitives are supporting components unless instantiated in those functions.

## Variety and escalation

Ordinary engineering variety remains in S1. Cross-worker overlap/conflict is attenuated by model-selected partition/worktree isolation under S2. Current worker failures/timeouts/verification state are regulated by the conductor under S3. A fresh reviewer can challenge worker output under S3*. Memory, advisor and policy enforcement do not create S4/S5.

## Evidence gaps

No ? state is required. The frozen source includes an explicit executable orchestration protocol with concrete worker commands, isolation/supervision/result contracts and reviewer-worker examples, plus sufficient memory/policy surfaces to support the negative S4/S5 conclusions.
