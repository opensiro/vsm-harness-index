---
harness_id: cloi
project_name: Cloi
repository: https://github.com/gabrielchasukjin/cloi
review_ref: 1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9
reviewed_at: 2026-11-07
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# Cloi

## Review boundary

- System in focus: the installed local-first `@cloi-ai/cloi` Node/Ollama terminal coding agent at the frozen revision, including CLI/one-shot and resumed sessions, its model/tool loop, first-party file/shell/Python tools, failure escalation, claim verification, approvals and persistent state.
- Purpose and identity: execute a user's local coding or repository-investigation request by choosing actions against real workspace/tool observations and reporting an evidence-bounded result.
- Relevant environment: local repository and command results, changing source and tests, local Ollama models, hardware resource limits, tool errors, operator approvals, context-window pressure and sessions interrupted across turns.
- Standard-distribution boundary: published CLI entry `bin/cloi.js` into `src/cli/repl.js`/`src/agent/loop.js`; Ollama is a required inference dependency, not an external agent harness donating organizational functions. The model-backend module is first-party, the inference service is not.
- Credited operating / distribution surfaces: `bin/cloi.js`, `src/cli/repl.js`, `src/agent/{loop,prompt,verify,judge,permission,compact}.js`, `src/tools/{index,registry,fs-tools,shell,workspace,python,recall,todo}.js`, `src/session/store.js`, `src/config.js`, documented installed setup and optional escalation/review configurations.
- Adjacent first-party surfaces excluded from ownership: `bench/compare.js`, `bench/python-tool.js`, `integrations/terminal-bench/`, `test/`, contributor documentation and npm packaging scripts; benchmark/evaluation and installation checks do not themselves become live runtime management or S3* auditors. External Ollama infrastructure, the human operating the terminal, and hypothetical third-party workflows are outside first-party agent ownership.
- First-party operating / deployment modes considered: interactive `cloi`, one-shot `cloi "task"`, `--continue` sessions, default raw-file claim checking, optional escalation to a larger local model, optional model-based answer judgment, and human-approved or explicit `--yes` side-effect permission modes.
- Recursion level: one local user-goal/workspace coding-agent session. Model calls, serial tool executions and a replacement model on failure remain one operational S1 unit; Cloi expressly does not ship subagents or a separate multi-unit operating organization.
- Reviewed revision: `1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9`; observation date 2026-11-07; active Profile `0.2.4`, Methodology `0.3.7`.

## Repository architecture

`startRepl` assembles a first-party tool registry, persisted SQLite `Session`, permission manager and the `runTurn` model/tool loop. On each step, `runTurn` rebuilds context from SQLite, requests one Ollama model response, dispatches the chosen local source/shell/Python tool subject to human or preconfigured effect approval, records output and failures, and returns observations into the next model choice. A source/result named store is durable across sessions; compaction changes model-visible context but preserves the full transcript. A stronger configured inference model can replace the initial model after bounded explicit failure signals while continuing the same goal and evidence history; this is one S1's recovery path, not a separate management recursion.

The default `verifyAnswers: true` adds a narrow, first-party verification path when the model stops using tools: runtime checks final claims against freshly inspected filesystem reality (path existence, line limits, absence statements, source quotes and read coverage) plus the ordered post-edit shell result. A contradictory outcome becomes a feedback message requiring a correction or new evidence; the bounded retry can trigger inference-model escalation. An additional model-based `judgeAnswer` is normally off until escalation, and its evidence comes from clipped model-tool-step logs rather than direct independent file inspection. This review credits the raw-file check, **not** the judge's self-contained evidence-summary critique, as the narrowly complementary path.

Frozen primary sources:

- [README: product/modes/no subagents](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/README.md)
- [Architecture/verification/escalation](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/internals.md)
- [Shipped agent loop and verification return](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/src/agent/loop.js)
- [Direct workspace claim verification](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/src/agent/verify.js)
- [Model reviewer scope/limits](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/src/agent/judge.js)
- [Enabled default and optional configurations](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/src/config.js)
- [CLI composition](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/src/cli/repl.js)
- [Approval owner](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/src/agent/permission.js)
- [Local hardware/model setup](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/src/cli/setup.js)
- [Persisted transcript/results](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/src/session/store.js)

## Operational model

The user sets an objective and decides whether dangerous local effects are authorized. The configured model chooses investigation, coding operations and their arguments, observes first-party tool outcomes, and can revise its course. Persistence, model-handoff limits, source checks and permission rules are supplied by the deterministic program. The ordinary S1 reporting path is the model's completion answer informed by earlier observations. At completion, a distinct source-derived runtime checker can challenge that answer from direct local workspace evidence and return contradictions into another model step; it is a narrow audit constructor, not an independent autonomous S3* organization.

## S1 — Operations

- State: A
- Function: perform the user's local source investigation and coding request through model-selected workspace tools and feedback.
- Disturbance / variety regulated: unknown code, failing tests/shell commands, changing file content, malformed model tool calls, incomplete fixes and long/interrupted task sessions.
- Decisive decision or feedback right: the configured Ollama-backed model chooses tool calls, substantive code edits/investigations, follow-up actions and when to submit a final answer; on bounded failure a configured stronger model can inherit the same task.
- Decision owner: model-guided Cloi agent loop; deterministic JS enforces tool schemas, hard limits, approvals, session persistence and failure-sensitive model switching.
- Supporting / enforcement mechanisms: `runTurn`, `ToolRegistry`, file/shell/Python/recall tools, SQLite `Session`, context compactor, abort/retry/strike rules, permission manager and Ollama transport.
- Closure path: user goal → model tool/argument choice → permitted local effect → tool output stored in SQLite → next model choice or corrected final answer.
- Boundary reachability: the default `cloi` and one-shot CLI both route into `startRepl` and `runTurn`; the first-party tool registry is explicitly assembled and executable through the installed code path.
- Why this is / is not agent-owned: without the model, hardcoded guards and the tool registry cannot choose goal-specific source edits, decide which error to investigate or form the substantive response.
- Evidence: [runtime](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/src/agent/loop.js), [REPL](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/src/cli/repl.js), [registry](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/src/tools/index.js), [README](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: no real Ollama-backed provider invocation was executed; traced runnable code and first-party scripted tests establish the loop, not actual task success on any benchmark.

## S2 — Coordination

- State: —
- Function: no in-boundary attenuation loop between distinct concurrently operating S1 organizational units is shipped.
- Disturbance / variety regulated: tool errors, permission denials and repeated calls can disrupt a single agent's work, but there are no distinct supported child coding units competing over shared execution commitments.
- Distinct S1 units: one model/tool loop; replacing the primary model after failure is a sequential continuation of the same task, not a second simultaneously operating S1.
- Inter-S1 disturbance: none materially established inside the supported single-agent coding session.
- Attenuating coordination relation: not applicable; serial dispatch, session storage and the Python interpreter's tool multiplexing are within one S1 execution path.
- Feedback into subsequent S1 behaviour: error/permission feedback alters one operating unit's next tool choice; no distinct inter-unit interference feedback is established.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: provider escalation, per-tool gating, task plan and durable result handles do not create distinct conflicting operations to coordinate.
- Decisive decision or feedback right: no separate inter-S1 coordination right.
- Decision owner: none identified within the assessed boundary.
- Supporting / enforcement mechanisms: serial loop, single conversation store, Python tool bindings, local permission guard and optional model escalation.
- Closure path: S1 errors return to that S1; no S2-specific inter-unit anti-interference relation.
- Why this is / is not agent-owned: changing inference model or scheduling serial tools does not produce a second operational organization or an agent-owned conflict-resolution right.
- Evidence: [README known gaps](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/README.md), [loop](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/src/agent/loop.js), [tool registry](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/src/tools/index.js).
- Basis: structural absence review.
- Confidence: high.
- Caveats: externally launching multiple independent Cloi sessions would require external coordination, which is not a first-party S2 mode.

### Absence scope

- Surfaces inspected: CLI/REPL entry, model/tool loop, failure escalation, tool registry and Python tool bindings, SQLite session/result store and product's explicit no-subagent declaration.
- Plausible first-party paths checked: concurrent S1 child loops, shared operation arbitration, interference/collision feedback and an effectful S2 conflict return.
- Why no material first-party path remains: no shipped child/sibling operational recursion or competing work units are evidenced; the installed operating task is serial, and errors/approvals return to the same model/tool loop.

## S3 — Inside-and-now control

- State: —
- Function: no distinct whole-system current resource/commitment manager is established beyond per-turn task execution and fixed safeguards.
- Disturbance / variety regulated: local model stalls, unusable tool calls, shell errors, user cancellation, context limits and incomplete tasks are current S1 failures, not a governed portfolio of separate operational units.
- Decisive decision or feedback right: no first-party whole-system operational allocation, reprioritization, commitments or exception intervention right was found.
- Decision owner: model owns its one coding task; deterministic runtime owns failure thresholds and model-handoff enforcement, with user owning external task and permission choice.
- Supporting / enforcement mechanisms: iteration/strike caps, escalation on observed errors, session resume, compaction, `update_plan`, user prompt and model configuration.
- Closure path: an error may cause the same goal to continue on a stronger configured model; no separately owned current-control decision for a whole operational organization is returned.
- Why this is / is not agent-owned: error-driven provider switching is deterministic per-task recovery, not an agent manager deciding across resources, operating units or system-wide commitments.
- Evidence: [failure recovery](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/src/agent/loop.js), [internal design](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/internals.md), [configuration](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/src/config.js).
- Basis: structural absence review.
- Confidence: medium-high.
- Caveats: a human may manually reconfigure models or stop a session, but ordinary S1 supervision does not establish an independently closed S3 parent mode.

### Absence scope

- Surfaces inspected: complete `runTurn` lifecycle, escalation counters, context and persistent session state, CLI commands, setup/model selection and user approvals.
- Plausible first-party paths checked: global current operational view, shared resource allocation, separate current-control owner, exception intervention across S1 commitments and returned control.
- Why no material first-party path remains: the supported system has one model-selected coding goal, and all reviewed limits/handoffs regulate that goal without a distinct whole-current S3 decision.

## S3* — Complementary audit

- State: C
- Function: challenge narrow factual assertions made in the coding agent's final report using evidence read directly from the workspace, beyond trusting the model's own answer or normal tool transcript.
- Disturbance / variety regulated: invented file names, out-of-range source lines, false symbol-absence claims, unsupported code quotations, insufficient source coverage and an apparently completed edit followed by a still-failing command.
- Decisive decision or feedback right: a separate first-party deterministic verifier can declare a claim contradictory to independently read filesystem reality, disallow immediate acceptance of the answer and return the exact contradiction to the operational model for new action.
- Decision owner: constructor-defined runtime check (`verifyAnswer`/`checkCoverage`/`checkEditOutcome`), not an autonomous model auditor; agent chooses the subsequent repair within a deterministic retry/escalation guard. Thus narrow complementary-audit constructor `C`, not `A`.
- Supporting / enforcement mechanisms: source-path resolution, fresh `fs.readFileSync`/file enumeration, source-line and negative-symbol checking, saved tool-output comparison, ordering of actual edit/command events and the `maxVerificationRetries` cap.
- Claim being audited: whether the agent's *final* statements about files, source, absence and post-edit testing are supported by actual workspace content and observed effects.
- Ordinary reporting path: the producing model sees the earlier tool results, compaction summary and own final answer, which may omit or misstate reality.
- Complementary access path: after the model stops, the runtime directly resolves and re-reads workspace file data and inspects ordered effect logs; this path need not accept the producer's narrative as source truth.
- Independence boundary: deterministic checker is not the model's own semantic self-review and directly accesses host files beyond its final narrative. Independence is limited to those mechanically falsifiable claims: it is **not** a separate end-to-end implementation reviewer, independent provider or source-aware S3 manager. The optional `judgeAnswer` only receives clipped ordinary tool evidence and is not independently credited as raw-source audit.
- Who acts on findings: `runTurn` turns a contradiction into a user-role corrective message, allows a bounded new model/tool step, and may escalate to the configured model; after retry exhaustion it can still finish, so no unconditional assurance of a correct final claim is asserted.
- Closure path: model final claim → fresh runtime source/effect contradiction → specific feedback in persisted conversation → operational model's next investigation/correction opportunity → new answer and another check.
- Boundary reachability: `verifyAnswers` is `true` in shipped `DEFAULTS`; `runTurn` calls all three verification functions in its no-tool-call completion branch before announcing completion. No external reviewer product or installation of a separate audit service is needed.
- Why this is / is not agent-owned: the source-derived contradiction would be made by JS code with the model removed; the model is an audited producer and subsequent repairer, not owner of the independent audit judgment. `C` records this first-party evidence/feedback construction, not an autonomous audit function or generalized QA certification.
- Evidence: [raw-source checks](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/src/agent/verify.js), [default enablement](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/src/config.js), [corrective return](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/src/agent/loop.js), [review-model limitations](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/src/agent/judge.js), [verify regression tests](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/test/verify.test.js).
- Basis: explicit + structural.
- Confidence: medium.
- Caveats: a cautious boundary: this is a limited final-answer claim audit, not a second fully independent code-quality or acceptance audit. `verifyAnswers` is operator-disableable and heuristic; the judge model fails open on exceptions/unparseable verdicts. Review cannot guarantee accuracy after bounded retries, and no provider-backed live acceptance test was executed.

## S4 — Outside-and-then intelligence

- State: —
- Function: no prospectively future-oriented external-environment sensing and capability adaptation choice/return is established.
- Disturbance / variety regulated: hardware fit, Ollama model availability, current request difficulty and compaction pressure influence present execution but not a managed future environmental option portfolio.
- Decisive decision or feedback right: none for a separated future-facing adaptation strategy; setup ranks existing models against present machine constraints and runtime switches on observed task failure.
- Decision owner: deterministic setup recommendation and current-run escalation code, with the operator confirming model downloads/configuration.
- Supporting / enforcement mechanisms: RAM/VRAM detection, model catalog/tier measurements, placement check, fallback configuration, per-turn escalation and session compaction.
- Closure path: setup detects present hardware → deterministic candidate selection → configured local inference; run-time failure may switch models. No external-and-future option formation and organizational return beyond present task execution.
- Why this is / is not agent-owned: adaptive provider selection on a failed turn and context summary are current task resilience, not S4's outside-and-then capability deliberation.
- Evidence: [hardware/setup](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/src/cli/setup.js), [model recommendation](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/src/util/recommend.js), [escalation/compaction](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/src/agent/loop.js).
- Basis: structural absence review.
- Confidence: medium-high.
- Caveats: maintaining the model benchmark/catalog is developer work, not an automated prospective capability governance loop at runtime.

### Absence scope

- Surfaces inspected: first-run setup, hardware/model catalog, persisted config, in-turn escalation, agent prompt, named memory and session summarization.
- Plausible first-party paths checked: sensing emerging external options, forecasting future constraints, generating competing future capability changes, returning an authorized choice to present operations.
- Why no material first-party path remains: shipped adaptations are present hardware fit/current failure/finite-context recovery; prospective organizational S4 choice and controlled downstream capability revision are not evidenced.

## S5 — Policy and identity

- State: —
- Function: no first-party organizational mission/identity and ultimate-policy decision/ratification loop is established.
- Disturbance / variety regulated: dangerous writes, commands, leaked secrets and out-of-workspace paths are local effect risks subject to existing user/config rights rather than ultimate identity questions.
- Decisive decision or feedback right: no S5-specific identity-policy issue and legitimate deciding authority/returned binding resolution; the user can grant or deny individual tool effects.
- Decision owner: human for per-action approval and developer/configuration for fixed safety rules, not a distinct parent S5 policy owner in the harness's supported recursion.
- Supporting / enforcement mechanisms: per-tool ask/allow/always/deny, `autoApprove`/`--yes`, path containment, sanitized process environment, model prompts and user configuration.
- Closure path: side-effect request → permission manager/user approval → effect allowed or denied; no organizational identity disagreement → legitimate charter decision → durable returned policy governing future operations.
- Why this is / is not agent-owned: safety checks and session-local permission grants do not amount to institutional ultimate-policy authority. A permissive headless `--yes` mode does not create autonomous S5 rights.
- Evidence: [approval controls](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/src/agent/permission.js), [CLI operator modes](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/bin/cloi.js), [config](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/src/config.js).
- Basis: structural absence review.
- Confidence: medium-high.
- Caveats: user-owned external operating rules can exist outside the reviewed product; they are not borrowed as a standard-distribution S5 parent mode.

### Absence scope

- Surfaces inspected: CLI permission mode, per-action approval, path containment/secrets, system prompt, durable configuration and session database, published contributor guidance.
- Plausible first-party paths checked: deliberation over purpose/identity, legitimacy and ratification of ultimate policy, authoritative policy revision and returned control across subsequent operations.
- Why no material first-party path remains: the reviewed controls regulate permissible tool effects and local setup; no identity-level organizational decision-and-return process is provided.

## Recursion

The local task runner is one first-party S1 unit. Different Ollama models serving the same session are successive inference owners of that S1 task, not independent concurrent S1s requiring S2. The deterministic file-claim checker checks that unit's reporting path without becoming a second S1. Multiple user-launched processes would require externally composed governance not present in the assessed standard distribution.

## Variety and escalation

Model/tool feedback amplifies source-editing options; workspace fences, approval prompts, bounded retries and protected environment constrain hazardous effects. Failed tool runs, disproved file claims and repeated surrender can return a corrective message or hand the same task to a stronger model. Default direct-file claim checking is deliberately narrow complementary verification. These current-run mechanisms do not establish inter-unit S2, a whole-current S3, future-facing S4 or ultimate-policy S5. Generic permission prompts are not identity-policy ratification and model fallback is not inter-recursive escalation.

## Evidence gaps

Frozen repository identity `976309424` matched public metadata and the checked-out frozen commit. First-party JS source and the explicit CLI/loop/config path were read. `npm test` with uninstalled dependencies ran **222 tests: 220 PASS, 2 failed to import `chalk`** (`test/diff.test.js`, `test/ui.test.js`); `npm ci --offline --ignore-scripts` could not fill the missing package tarball (`ENOTCACHED`), so a full upstream suite pass is not claimed. No live Ollama task was executed. The S3* conclusion is limited to demonstrably independent direct source checks, not the advice-only evidence-summary model judge, human audit, or broad correctness of implemented patches. No external model performance results are imported from benchmarks.

## Assessment summary

Cloi owns the ordinary model-guided local coding/tool operation (**S1=A**). It also ships a default, mechanically independent direct-filesystem challenge of narrow final-answer claims with corrective feedback, classified as a constructor-owned complementary audit path (**S3*=C**, not an autonomous separate auditor). The default runtime is one serial coding agent, and its fixed error recovery, hardware/model selection and tool permissions do not close S2/S3/S4/S5 (**—**). This is a pinned-source organizational classification, not a performance or safety guarantee.

Proposed vector: **`A · — · — · C · — · —`**.
