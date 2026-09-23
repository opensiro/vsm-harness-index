---
harness_id: onit
project_name: OnIt
repository: https://github.com/sibyl-oracles/onit
review_ref: 88f562d1c4e62a3a8599ac5d0bdfa6423a6e1fc0
reviewed_at: 2026-09-23
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-23
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# OnIt

## Review boundary

- System in focus: one OnIt agent run at pinned revision `88f562d1c4e62a3a8599ac5d0bdfa6423a6e1fc0`, including the first-party model/tool loop, prompt/runtime policy, session persistence, command approvals, scheduled-loop entry point, answer-verification path and trajectory-observation substrate.
- Purpose and identity: execute automation/research/coding tasks through one autonomous tool-using agent that can persist/resume sessions, run periodically, operate inside optional container isolation and fact-check completed answers.
- Relevant environment: user objectives, local files and repositories, shell/tool results, web/local-search evidence, model providers, container/host state and user approval for sensitive commands.
- Standard-distribution boundary: OnIt-owned `src/onit.py`, serving/chat/interpreter/runtime code, MCP tool registry/servers, session state, verification code, default configuration and trajectory-observation code. External model providers, websites, GitHub, host OS services and repository CI do not donate organizational functions.
- Credited operating / distribution surfaces: `README.md`; `docs/ARCHITECTURE.md`; `docs/CONFIGURATION.md`; `docs/SELF_IMPROVEMENT.md`; `src/onit.py`; `src/model/serving/chat.py`; `src/model/serving/verify.py`; `src/configs/default.yaml`; `src/sessions.py`; `src/learn/*`; first-party MCP tool/approval paths.
- Adjacent first-party surfaces excluded from ownership: `benchmarks/`, repository CI/release workflows, archived proposals, development tests and proposed self-improvement phases not wired into the assessed standard runtime.
- First-party operating / deployment modes considered: terminal/web agent execution, resumable session, scheduled `serve loop`, standard verification-enabled answer flow, optional background verification and the default learning mode `observe`.
- Recursion level: one OnIt agent run is the system-in-focus and its model/tool loop is the operational S1. The verifier is a complementary first-party checking path around that S1, but OnIt does not establish a multi-S1 metasystem at this boundary.
- Reviewed revision: `88f562d1c4e62a3a8599ac5d0bdfa6423a6e1fc0`.
- Observation date: 2026-09-23.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

OnIt is a single-agent harness around a persistent tool-using model loop. The runtime prepares the prompt, exposes MCP tools, executes model/tool turns, returns tool observations into later turns, persists sessions and can repeat the same task periodically. Command-policy and approval machinery constrain sensitive shell operations, while optional container isolation constrains execution environment rather than creating another organizational decision owner.

A distinct post-answer verifier is enabled by default. After the ordinary answer is written, `verify.py` checks factual claims against evidence gathered during the run; a background stage may perform read-only lookups and generate a corrected revision. This is a real complementary audit construction path because evidence checking happens outside the ordinary answer-generation sequence and can change the answer the user keeps. It remains `C`, not `A`, because the verifier calls the same serving `ask`/model path for audit judgment and revision, so a materially independent autonomous auditor is not supplied.

The repository also contains a trajectory-learning substrate, but its own frozen documentation states that OnIt is currently a static agent. `src/configs/default.yaml` sets learning autonomy to `observe`; `adapt`, `extend` and `evolve` are explicitly marked not yet built. `docs/SELF_IMPROVEMENT.md` likewise describes episodic recall, playbook, skill synthesis and scaffold evolution as later proposal/RFC phases. Those adjacent/prospective surfaces are not credited as S4.

## S1 — Operations

- State: A
- Function: perform user-directed automation, research and coding work through an iterative autonomous model/tool loop.
- Disturbance / variety regulated: uncertain user objectives, local/web/repository state, tool results, command failures, model output and iterative evidence discovered during execution.
- Decisive decision or feedback right: choose task-local reasoning, which available tool to invoke, how to use returned observations and when the task is sufficiently complete to answer.
- Decision owner: the autonomous model actor reached by OnIt's first-party chat/runtime path.
- Supporting / enforcement mechanisms: prompt generation, MCP tool registry, interpreter, session persistence, command policy/approvals, retries/failover, optional container isolation and loop limits.
- Closure path: user or scheduler admits a task → OnIt invokes the model with tools/context → model chooses tool/action → tool result returns into the next model turn → the model adapts its task-local behavior and eventually produces an answer.
- Boundary reachability: terminal/web execution and `serve loop` route through the shipped `process_task`/chat serving path and use the standard MCP tool registry; no development-only actor is needed.
- Why this is / is not agent-owned: OnIt runtime enforces policy, persistence and transport, while substantive task-local action selection and reasoning belong to the model actor.
- Evidence: [`README.md`](https://github.com/sibyl-oracles/onit/blob/88f562d1c4e62a3a8599ac5d0bdfa6423a6e1fc0/README.md); [`docs/ARCHITECTURE.md`](https://github.com/sibyl-oracles/onit/blob/88f562d1c4e62a3a8599ac5d0bdfa6423a6e1fc0/docs/ARCHITECTURE.md); [`src/onit.py`](https://github.com/sibyl-oracles/onit/blob/88f562d1c4e62a3a8599ac5d0bdfa6423a6e1fc0/src/onit.py); [`src/model/serving/chat.py`](https://github.com/sibyl-oracles/onit/blob/88f562d1c4e62a3a8599ac5d0bdfa6423a6e1fc0/src/model/serving/chat.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: scheduled repetition changes when S1 runs; it does not create a separate metasystemic function.

## S2 — Coordination

- State: —
- Function: no inter-S1 coordination function is established at the declared run boundary.
- Disturbance / variety regulated: the standard runtime operates one primary model/tool loop; no distinct sibling S1 units and interaction-generated conflict/oscillation are established for S2 mapping.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: tool ordering, retry/failover, command approvals, sessions, scheduler and server/tool subprocesses sequence or constrain one operational loop rather than coordinate sibling S1s.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: there is no established S2 function to classify.
- Evidence: [`docs/ARCHITECTURE.md`](https://github.com/sibyl-oracles/onit/blob/88f562d1c4e62a3a8599ac5d0bdfa6423a6e1fc0/docs/ARCHITECTURE.md); [`src/onit.py`](https://github.com/sibyl-oracles/onit/blob/88f562d1c4e62a3a8599ac5d0bdfa6423a6e1fc0/src/onit.py); [`src/model/serving/chat.py`](https://github.com/sibyl-oracles/onit/blob/88f562d1c4e62a3a8599ac5d0bdfa6423a6e1fc0/src/model/serving/chat.py).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: MCP subprocess plurality is implementation topology, not evidence of distinct operational S1 units.

### Absence scope

- Surfaces inspected: core chat/tool loop, MCP server topology, scheduler, sessions, failover/retries, command-policy/approval machinery and verifier path.
- Plausible first-party paths checked: multiple MCP servers, scheduled repetitions, serving failover and concurrent web/terminal surfaces.
- Why no material first-party path remains: these mechanisms service or repeat one autonomous operational loop; no reviewed path establishes sibling S1 units, a concrete interaction-generated disturbance and S2-specific mutual adjustment fed back into their later behavior.

## S3 — Inside-and-now control

- State: —
- Function: no distinct whole-system current-control function is established above the single OnIt operational agent at this recursion.
- Disturbance / variety regulated: command approvals, loop limits, session stop/cancel, failover and scheduling constrain local task execution but do not regulate shared current resources, commitments, priorities or accountability across multiple S1 operations on behalf of a whole.
- Decisive decision or feedback right: not established at a metasystemic current-control level.
- Decision owner: not established.
- Supporting / enforcement mechanisms: approval queue, command policy, task cancellation, retry/failover, scheduled period and session state are execution-control mechanisms around one S1.
- Closure path: not applicable for the negative finding.
- Boundary reachability: no qualifying first-party S3 mode was found.
- Why this is / is not agent-owned: human approval of a sensitive command and deterministic enforcement of loop/safety policy remain local S1 constraints rather than S3 ownership.
- Evidence: [`src/onit.py`](https://github.com/sibyl-oracles/onit/blob/88f562d1c4e62a3a8599ac5d0bdfa6423a6e1fc0/src/onit.py); [`src/mcp/servers/tasks/os/bash/approvals.py`](https://github.com/sibyl-oracles/onit/blob/88f562d1c4e62a3a8599ac5d0bdfa6423a6e1fc0/src/mcp/servers/tasks/os/bash/approvals.py); [`src/mcp/servers/tasks/os/bash/command_policy.py`](https://github.com/sibyl-oracles/onit/blob/88f562d1c4e62a3a8599ac5d0bdfa6423a6e1fc0/src/mcp/servers/tasks/os/bash/command_policy.py).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: approval authority is not promoted to S3 merely because a human can block an operational command.

### Absence scope

- Surfaces inspected: task/run lifecycle, scheduler, sessions, safety/approval queue, command policy, model failover and web/terminal controls.
- Plausible first-party paths checked: scheduled loop management, user stop/cancel, command approvals, model failover and session persistence/resume.
- Why no material first-party path remains: all inspected rights regulate one operational agent/task path; no whole-system view plus discretionary current regulation of multiple S1 operations is established.

## S3* — Complementary audit

- State: C
- Function: challenge a finished answer against independently reconstructed run evidence and optionally external read-only evidence, then return concrete corrections into the delivered answer.
- Disturbance / variety regulated: an ordinary answer may contain unsupported, stale or factually incorrect claims despite appearing complete.
- Decisive decision or feedback right: determine which claims are unsupported/incorrect and whether they should be flagged or rewritten before/after delivery.
- Decision owner: constructor path. The first-party verifier supplies the specialized audit/evidence/revision path, but audit judgment and revision use the same serving `ask` model path rather than a materially independent autonomous auditor.
- Supporting / enforcement mechanisms: `verify_answers` default, trusted-source/evidence matching, bounded fast check, read-only background lookup tools, issue extraction, revision prompt, timeout/fail-open guards and late-correction presentation.
- Closure path: ordinary agent writes answer → verifier separately inspects claims against transcript/evidence and optional read-only lookups → findings are converted to a correction note or revision request → corrected/flagged answer is returned to the user → the delivered operational result changes under audit feedback.
- Boundary reachability: `src/configs/default.yaml` documents `verify_answers: true` as the code default and `verify_background: true`; `src/model/serving/chat.py` wires the standard answer path into `verify_answer`, so no development-only evaluator is required.
- Why this is / is not agent-owned: the audit path is function-specific and materially separate from ordinary answer generation, but the same model-serving actor is asked to make verifier/revision judgments. This establishes an S3* constructor path rather than autonomous independent audit ownership.
- Evidence: [`src/configs/default.yaml`](https://github.com/sibyl-oracles/onit/blob/88f562d1c4e62a3a8599ac5d0bdfa6423a6e1fc0/src/configs/default.yaml); [`src/model/serving/chat.py`](https://github.com/sibyl-oracles/onit/blob/88f562d1c4e62a3a8599ac5d0bdfa6423a6e1fc0/src/model/serving/chat.py); [`src/model/serving/verify.py`](https://github.com/sibyl-oracles/onit/blob/88f562d1c4e62a3a8599ac5d0bdfa6423a6e1fc0/src/model/serving/verify.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: a distinct provider call or second generation is not by itself organizational independence; the frozen implementation deliberately reuses the serving `ask` path.
- Claim being audited: factual/support claims in the ordinary completed answer produced by the operational chat loop.
- Ordinary reporting path: normal model/tool loop generates and streams the answer using task transcript and gathered evidence.
- Complementary access path: verifier re-reads evidence separately from the ordinary generation path, clears directly supported claims and may use bounded read-only lookup tools for uncovered claims before constructing findings.
- Independence boundary: complementary evidence selection/checking and revision protocol are first-party separate code paths, but autonomous judgment is incomplete because the same serving `ask`/model path performs verdict/revision calls.
- Who acts on findings: the verifier path itself appends a correction note or requests a revised answer; web/terminal late-correction handling returns that corrected result to the user.

## S4 — Outside-and-then adaptation

- State: —
- Function: no live outside-and-future adaptation loop is established in the frozen standard distribution.
- Disturbance / variety regulated: OnIt records trajectories and verifier signals, but current runtime behavior remains static; external outcomes are observed without generating/publishing a changed prompt, memory policy, skill/tool set or scaffold into subsequent operation.
- Decisive decision or feedback right: not established in the shipped runtime.
- Decision owner: not established.
- Supporting / enforcement mechanisms: `src/learn` trajectory/event/report substrate and default `learn.autonomy: observe` preserve evidence for later analysis but do not adapt capability.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: the frozen repository explicitly says OnIt is currently a static agent and labels `adapt`, `extend` and `evolve` as not yet built.
- Evidence: [`src/configs/default.yaml`](https://github.com/sibyl-oracles/onit/blob/88f562d1c4e62a3a8599ac5d0bdfa6423a6e1fc0/src/configs/default.yaml); [`docs/SELF_IMPROVEMENT.md`](https://github.com/sibyl-oracles/onit/blob/88f562d1c4e62a3a8599ac5d0bdfa6423a6e1fc0/docs/SELF_IMPROVEMENT.md); [`src/learn/lifecycle.py`](https://github.com/sibyl-oracles/onit/blob/88f562d1c4e62a3a8599ac5d0bdfa6423a6e1fc0/src/learn/lifecycle.py).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: collecting rich trajectories and verifier outcome signals can support a future S4 implementation; capability existence is not inferred from the roadmap.

### Absence scope

- Surfaces inspected: default learn configuration, trajectory/events/lifecycle/report code, `SELF_IMPROVEMENT.md`, verifier metrics and proposed recall/playbook/skill/scaffold loops.
- Plausible first-party paths checked: episodic recall, playbook/procedural memory, skill synthesis, scaffold evolution and verifier-derived learning signals.
- Why no material first-party path remains: the active mode is observation-only; the repository explicitly marks the capability-changing `adapt`, `extend` and `evolve` modes as not yet built and later improvement loops as proposal/RFC rather than operating distribution.

## S5 — Identity / ultimate policy

- State: —
- Function: no runtime identity/ultimate-policy closure is established.
- Disturbance / variety regulated: configuration, prompt templates, command policy, user approvals and learning-autonomy settings constrain operation but are not evidenced as an identity-level dispute/decision loop for the OnIt organization.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: static configuration, prompt templates, safety approvals and command policies enforce operational rules without becoming S5.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: no qualifying S5 function is established.
- Evidence: [`src/configs/default.yaml`](https://github.com/sibyl-oracles/onit/blob/88f562d1c4e62a3a8599ac5d0bdfa6423a6e1fc0/src/configs/default.yaml); [`src/mcp/servers/tasks/os/bash/command_policy.py`](https://github.com/sibyl-oracles/onit/blob/88f562d1c4e62a3a8599ac5d0bdfa6423a6e1fc0/src/mcp/servers/tasks/os/bash/command_policy.py); [`src/model/serving/harness.py`](https://github.com/sibyl-oracles/onit/blob/88f562d1c4e62a3a8599ac5d0bdfa6423a6e1fc0/src/model/serving/harness.py).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: a human approving a shell command is an operational safety right, not identity/ultimate-policy governance.

### Absence scope

- Surfaces inspected: runtime/default config, prompt templates, command policies/approvals, learning-autonomy configuration, session lifecycle and scheduled operation.
- Plausible first-party paths checked: approval authority, static prompt/config ownership, learning autonomy ladder and scheduler policy.
- Why no material first-party path remains: inspected decisions are task-local safety/configuration or unrealized future-development choices; no runtime identity/ultimate-policy matter reaches an authoritative owner and returns to govern subsequent operation as S5.
