---
harness_id: gagans-agent-os
project_name: agent-os
repository: https://github.com/gagans23/agent-os
review_ref: d318787db1fce4163e470ac1c94f5a74d667303f
reviewed_at: 2026-09-20
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: P
autonomy_s5: —
---

# agent-os

## Review boundary

- System in focus: the first-party `gagans23/agent-os` local personal-agent runtime at the frozen candidate revision, including its command router, provider-backed job execution, persistent memory/context/jobs, governed swarm, skills, MCP bridge, risk/approval path, trace/audit storage and first-party skill-proposal workflow.
- Purpose and identity: provide a local-first governed personal-agent runtime in which user work is routed through persistent context and skills, agent execution is traced and risk-gated, parallel sub-jobs can be organized into a swarm, and reusable capability changes are admitted through an explicit human gate.
- Relevant environment: user commands and learned user context, local files and configured MCP services, model-provider outputs, task results and failures, successful novel workflows, and external Ninja Harness evaluation results consumed by the runtime.
- Standard-distribution boundary: the shipped `agent_os` package, CLI/Web command surfaces and local stores at the pinned revision. Model providers, configured MCP servers, messaging/deployment services and Ninja Harness are external dependencies/systems and do not contribute organizational ownership merely because agent-os invokes them.
- Credited operating / distribution surfaces: `agent_os/command_router.py`, `runner.py`, `providers.py`, `orchestrator.py`, persistent memory/context/jobs, `skill_registry.py`, `skill_synth.py`, risk/approval machinery, `audit.py`, supervisor/health surfaces and the standard CLI/Web paths that invoke the same command router.
- Adjacent first-party surfaces excluded from ownership: tests, examples, repository CI/release workflows, documentation/roadmap material and deployment examples are corroborating evidence only; Ninja Harness is a separately versioned external evaluation/certification system and is explicitly outside the standalone ownership boundary.
- First-party operating / deployment modes considered: configured local-model or API-model `/run` execution; deterministic no-provider fallback; `/swarm` parallel sub-jobs; local CLI/Web operation; MCP calls through the governed router; human approval/rejection of privileged actions; and the gated successful-run-to-skill learning path.
- Recursion level: one running agent-os installation is the system-in-focus. Parallel swarm sub-jobs are distinct S1 operational units for the S2 witness, but they are not claimed to be recursively viable systems.
- Reviewed revision: `d318787db1fce4163e470ac1c94f5a74d667303f`.
- Observation date: 2026-09-20.
- Generated Profile version: `0.2.3`.
- Generated Methodology version: `0.3.5`.
- Current Profile version: `0.2.3`.
- Current Methodology version: `0.3.5`.

The frozen batch-#89 review ref is preserved. Current or future upstream behavior is not used to upgrade this assessment. In particular, Ninja Harness remains an external evaluation/certification layer even where its score is consumed by first-party agent-os logic.

## Repository architecture

`CommandRouter` is the common transport-independent control surface used by CLI/Web operation. With a provider configured, it wires the provider's `as_agent_fn()` into `/run`, while `run_job()` supplies persistent memory context and a matched reusable skill, records the trajectory, calls the agent function, persists the result and optionally invokes Ninja Harness for an external evaluation. The model provider is an external reasoning service, but the first-party runtime owns task admission, context/skill assembly, invocation, persistence, risk gating and the subsequent learning/control paths around that invocation.

The governed swarm is a first-party organization over several operational sub-jobs. A configured model can decompose one goal into independent sub-tasks; `Orchestrator.run()` then executes them concurrently through the same `run_job()` path and synthesizes completed outputs. A concrete coordination disturbance is documented in the implementation itself: parallel workers otherwise race while switching the shared SQLite stores into WAL mode and can fail with `database is locked`. Before fan-out, `_init_shared_db()` opens/closes the shared job and memory stores so WAL/schema initialization has completed before worker connections contend for them.

Trust/control machinery is extensive but mostly deterministic or parent-gated. Risk classification decides whether a command may auto-run; privileged commands are queued until a human invokes `/approve` or `/reject`. `Supervisor` restarts one child under a fixed backoff policy. `/status`, `/health`, trace views and the hash-chained audit log expose operational state and provenance, but no first-party whole-system current-control actor or sufficiently independent complementary auditor was established at this revision. Ninja Harness may independently grade a trace, but that judgment belongs to the separate Ninja system and cannot be imported as agent-os-owned S3*.

The strongest adaptation path is `skill_synth.py`. After a successful, novel, non-trivial task, agent-os reconstructs a reusable procedure from the actual trace and creates a `SKILL.md` draft for future reuse. It deliberately does not install the draft itself. The router places it behind the human approval queue; approval writes the skill into the local skill library, reloads the registry and makes it matchable for later runs. This closes an outside/future adaptation loop in a parent-governed mode rather than an autonomous one. The weak-run `ImprovementProposal` path is even more conservative: it produces suggestions only and explicitly requires a separate human apply step.

Primary evidence:

- [`README.md`](https://github.com/gagans23/agent-os/blob/d318787db1fce4163e470ac1c94f5a74d667303f/README.md)
- [`agent_os/command_router.py`](https://github.com/gagans23/agent-os/blob/d318787db1fce4163e470ac1c94f5a74d667303f/agent_os/command_router.py)
- [`agent_os/runner.py`](https://github.com/gagans23/agent-os/blob/d318787db1fce4163e470ac1c94f5a74d667303f/agent_os/runner.py)
- [`agent_os/providers.py`](https://github.com/gagans23/agent-os/blob/d318787db1fce4163e470ac1c94f5a74d667303f/agent_os/providers.py)
- [`agent_os/orchestrator.py`](https://github.com/gagans23/agent-os/blob/d318787db1fce4163e470ac1c94f5a74d667303f/agent_os/orchestrator.py)
- [`agent_os/skill_synth.py`](https://github.com/gagans23/agent-os/blob/d318787db1fce4163e470ac1c94f5a74d667303f/agent_os/skill_synth.py)
- [`agent_os/improvement.py`](https://github.com/gagans23/agent-os/blob/d318787db1fce4163e470ac1c94f5a74d667303f/agent_os/improvement.py)
- [`agent_os/approvals.py`](https://github.com/gagans23/agent-os/blob/d318787db1fce4163e470ac1c94f5a74d667303f/agent_os/approvals.py)
- [`agent_os/audit.py`](https://github.com/gagans23/agent-os/blob/d318787db1fce4163e470ac1c94f5a74d667303f/agent_os/audit.py)
- [`agent_os/supervisor.py`](https://github.com/gagans23/agent-os/blob/d318787db1fce4163e470ac1c94f5a74d667303f/agent_os/supervisor.py)
- [`agent_os/daily_eval.py`](https://github.com/gagans23/agent-os/blob/d318787db1fce4163e470ac1c94f5a74d667303f/agent_os/daily_eval.py)

## Operational model

A normal model-backed `/run` enters the first-party router, receives persistent memory and any matched skill, and is handed to the configured provider-backed agent function. The resulting work product and trajectory become durable job/session state and can feed subsequent recall or learning. Privileged actions are not silently executed: they wait for explicit human approval. In swarm mode, one coordinator creates several independent sub-jobs, the first-party runtime executes them concurrently under shared persistent infrastructure, and their completed outputs are synthesized into one result.

For VSM ownership, the model actor owns ordinary S1 task behavior in the supported model-backed mode. The swarm contains an S2-specific coordination path, but its decisive coordination policy is built into deterministic runtime code rather than autonomously chosen by a model actor. Current-control and audit surfaces do not satisfy the stronger S3/S3* function tests. Adaptation is genuinely closed only after the parent human accepts a proposed future reusable skill. No ultimate identity/policy closure was established.

## S1 — Operations

- State: A
- Function: transform user-submitted personal-agent tasks into model-generated operational results under persistent context and reusable skills.
- Disturbance / variety regulated: heterogeneous user objectives, changing remembered/contextual information, matched skill procedures, provider responses, task failures and task-specific observations captured in the job trajectory.
- Decisive decision or feedback right: generate the substantive task response/action content from the current command plus runtime-supplied memory/skill context.
- Decision owner: the configured autonomous model actor reached through the first-party provider-backed `agent_fn` mode.
- Supporting / enforcement mechanisms: `CommandRouter`, `run_job()`, provider adapters, persistent memory/jobs, hooks, skill matching, traces, risk classification and configured provider transport.
- Closure path: command → router/risk admission → memory and matched-skill context → provider-backed autonomous agent function → result/trace persistence → returned user result and later memory/learning availability.
- Boundary reachability: a configured provider is an explicitly supported standard operating mode; `CommandRouter` automatically converts it to `agent_fn` and `/run` calls the first-party `run_job()` path. No adjacent development/evaluation agent is needed to supply the operational loop.
- Why this is / is not agent-owned: first-party Python code transports context and invokes the model, but the substantive response for an admitted task is selected by the autonomous model actor rather than predetermined by the router. The model service itself remains an external dependency, as with other model-backed harnesses.
- Evidence: pinned `agent_os/providers.py`, `agent_os/command_router.py`, `agent_os/runner.py` and README provider/run documentation.
- Basis: `structural` and `explicit`.
- Confidence: high.
- Caveats: with no provider configured agent-os can remain in deterministic fallback mode; `A` records the supported first-party model-backed operating mode, not a claim that every configuration is agent-owned.

## S2 — Coordination

- State: C
- Function: suppress a concrete shared-state collision among simultaneously executing swarm sub-jobs so sibling operations can proceed without corrupting or blocking one another during shared-store initialization.
- Disturbance / variety regulated: concurrent workers opening the shared jobs/memory SQLite stores can race on the journal-mode/WAL transition and produce `database is locked` failures before useful parallel work begins.
- Decisive decision or feedback right: establish the shared database schema/WAL state once before fan-out rather than letting sibling workers race to establish it independently.
- Decision owner: the first-party deterministic `Orchestrator` implementation/developer-selected coordination policy; no autonomous agent is shown choosing or revising this conflict-response rule at runtime.
- Supporting / enforcement mechanisms: `_init_shared_db()`, SQLite WAL/busy-timeout behavior, `ThreadPoolExecutor`, per-worker `JobStore`/`AgentMemory` connections and the normal swarm execution path.
- Closure path: swarm admitted → `_init_shared_db()` initializes the shared stores → parallel worker connections open against already-prepared stores → sibling sub-jobs execute and return results instead of colliding on journal initialization.
- Boundary reachability: `_init_shared_db()` is wired directly and unconditionally into first-party `Orchestrator.run()` before `ThreadPoolExecutor` fan-out in the shipped `/swarm` path; no downstream composition is needed to expose the coordination primitive.
- Why this is / is not agent-owned: the S2 function and feedback path are concrete, but the decisive response to the inter-worker conflict is a fixed runtime policy. The model may choose sub-tasks, but it does not own this coordination discretion, so the autonomous `A` threshold is not met.
- Evidence: pinned `agent_os/orchestrator.py`, especially `_init_shared_db()` and the explicit implementation comment explaining the `database is locked` race it prevents.
- Basis: `structural` and `explicit`.
- Confidence: high.
- Caveats: this classification is not based on decomposition, parallelism or synthesis by themselves; it is based on the specific inter-S1 shared-store collision and the first-party attenuation path. `C` records a real S2-specific first-party path without autonomous ownership of the decisive coordination rule.
- Distinct S1 units: concurrently executing swarm sub-jobs, each performing a separate user-derived operational task through `run_job()` and producing its own result.
- Inter-S1 disturbance: sibling workers contend on common jobs/memory SQLite initialization and can race on journal-mode switching, yielding `database is locked`.
- Attenuating coordination relation: the orchestrator initializes/closes the common stores once before worker fan-out, leaving workers to open already-prepared WAL/schema state.
- Feedback into subsequent S1 behaviour: after pre-initialization the sibling workers can enter their normal job execution paths concurrently rather than fail at shared-store setup.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the source explicitly ties the pre-fan-out relation to a concrete concurrency collision among sibling workers; it is not credited merely because a queue, shared database or parallel executor exists.

## S3 — Inside-and-now control

- State: —
- Function: no material first-party whole-system current-control function was established at the declared recursion.
- Disturbance / variety regulated: current job health, pending approvals, process failures, recent scores and swarm execution are observable or locally regulated, but no whole-installation resource/commitment/prioritization disturbance is shown under a qualifying S3 owner.
- Decisive decision or feedback right: no actor with a whole-system current view and discretionary authority over shared current resources, commitments, priorities, constraints, accountability or synergy was established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: `/status`, `/health`, job statistics, risk gates, human approvals for individual privileged commands, fixed supervisor restart/backoff rules, swarm concurrency configuration and persistent job state.
- Closure path: no qualifying whole-system current-control decision→subsequent-operation loop was found.
- Why this is / is not agent-owned: the available machinery observes or enforces local/static decisions. A human can approve a particular privileged action, but that is not evidence of whole-system S3 parent governance.
- Evidence: pinned `agent_os/command_router.py`, `approvals.py`, `supervisor.py`, `orchestrator.py`, jobs/health surfaces and README governance documentation.
- Basis: `structural`.
- Confidence: high.
- Caveats: later versions or downstream operator organizations could add S3 without changing the meaning of this frozen assessment.

### Absence scope

- Surfaces inspected: command/status/health handlers, jobs, approvals/risk policy, swarm orchestration/concurrency, supervisor/restart behavior, Web/CLI command surface, memory and audit stores.
- Plausible first-party paths checked: human approval as possible parent control, `/status`/health as possible whole-system view, supervisor as possible controller, swarm coordinator as possible S3, and fixed risk/concurrency limits as possible shared-resource regulation.
- Why no material first-party path remains: each candidate path lacks either a whole-system current view or a discretionary current-control right on behalf of the whole; the observed mechanisms are local approvals, monitoring or deterministic enforcement rather than S3 ownership.

## S3* — Complementary audit

- State: —
- Function: no qualifying first-party complementary and sufficiently independent audit function was established inside agent-os.
- Disturbance / variety regulated: traces, commands, approval decisions, scores and daily reliability summaries are recorded/checked, but they do not establish a separate first-party challenge channel to operational reality.
- Decisive decision or feedback right: no first-party auditor with materially independent access and a findings→control return path was found.
- Decision owner: not established inside the assessed boundary.
- Supporting / enforcement mechanisms: trace recording, hash-chained audit log and `verify()`, `/audit`, daily evaluation summaries, Ninja Harness invocation and persisted external scores.
- Closure path: no qualifying first-party complementary audit finding is returned into current control as an independently owned S3* judgment.
- Why this is / is not agent-owned: the audit database verifies integrity of the same recorded command/decision path; it does not independently challenge operational claims. Ninja Harness can supply a distinct evaluation judgment, but that judgment is owned by a separately scoped external system and is not imported into agent-os ownership.
- Evidence: pinned `agent_os/audit.py`, `runner.py`, `daily_eval.py`, README's explicit runtime/evaluation separation and batch-#89 boundary note.
- Basis: `explicit` and `structural`.
- Confidence: high.
- Caveats: external evaluation may still be operationally valuable and may feed adaptation proposals; the standalone VSM ownership boundary is narrower than an integrated multi-system deployment.

### Absence scope

- Surfaces inspected: trace recorder, audit log/hash verification, `/trace` and `/audit` views, Ninja evaluation call sites, daily evaluation, swarm synthesis scoring and human approval paths.
- Plausible first-party paths checked: tamper-evident audit as possible S3*, trace replay/inspection, external Ninja scoring, daily evaluation and approval review.
- Why no material first-party path remains: first-party traces/audit are ordinary provenance/observability without materially independent access, while the genuinely separate evaluator is outside agent-os; no first-party independent challenge owner plus corrective return loop is supplied.

## S4 — Outside-and-then intelligence

- State: P
- Function: turn a demonstrated novel user workflow into a reusable future capability when a legitimate parent human accepts the proposed adaptation.
- Disturbance / variety regulated: successful external/user work can reveal recurring procedures not represented in the current skill library, creating future capability mismatch if the runtime cannot preserve and reuse the newly demonstrated workflow.
- Decisive decision or feedback right: decide whether the proposed reusable `SKILL.md` becomes an installed capability for future agent runs.
- Decision owner: the human/operator parent through the explicit `/approve` or `/reject` gate.
- Supporting / enforcement mechanisms: trace capture, success/novelty/complexity tests in `propose_skill()`, draft persistence, approval queue, skill-file write, `SkillRegistry.reload()` and later skill matching in `run_job()`.
- Closure path: novel successful user task → first-party trace-derived skill draft → human review/approval → skill written into the live library and registry reloaded → later matching task receives the reusable procedure in its execution context.
- Boundary reachability: the learning path is wired into ordinary first-party `/run`/approved-run completion through `_maybe_propose_skill()` and the same standard approval command surface; no custom extension or repository-development actor is required.
- Why this is / is not agent-owned: agent-os autonomously constructs the candidate adaptation, but maintainer code explicitly refuses to install it silently. The decisive capability-change right belongs to the parent human, so the published state is standalone `P`, not `A`.
- Evidence: pinned `agent_os/skill_synth.py`, `agent_os/command_router.py`, `agent_os/skill_registry.py`, `approvals.py`, `runner.py` and README learning-loop documentation.
- Basis: `explicit` and `structural`.
- Confidence: high.
- Caveats: the separate weak-run `ImprovementProposal` path is propose-only and requires an additional apply step; it is supporting evidence of conservative adaptation design, not an autonomous S4 closure. External Ninja scores may contribute a signal in some learning paths but do not own agent-os's parent adaptation decision.
- External distinction: a real user/environment task succeeds through a procedure not already covered by the installed skill set; the learned option is grounded in the task's recorded operational trace rather than generated from an internal roadmap alone.
- Future / prospective distinction: the draft is created specifically as a reusable skill so later matching work can exploit the demonstrated procedure instead of rediscovering it.
- Adaptation option generated: a concrete `SKILL.md` draft containing name, triggers, reconstructed procedure and verification instructions.
- Path back into current capability / S3: parent approval writes the draft to the active skills directory, reloads the registry, and subsequent `run_job()` calls can match/inject the new procedure into model context.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy closure was established at the declared installation recursion.
- Disturbance / variety regulated: provider choice, risk rules, profiles, packs, skills and per-action approvals constrain behavior, but no evidenced identity/ultimate-policy dispute is escalated to and closed by a legitimate S5 authority.
- Decisive decision or feedback right: no qualifying ultimate identity/policy decision path was established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: configured profiles/tool allowlists, pluggable risk classifier, human approval of privileged actions, provider configuration, role packs and static governance defaults.
- Closure path: no identity/ultimate-policy issue → authority → authoritative decision → returned governing operation loop was found.
- Why this is / is not agent-owned: prompts/configuration and human vetoes over ordinary actions constrain S1 work but do not constitute S5 under the Profile without an identity-level issue and ultimate-policy closure.
- Evidence: pinned `agent_os/profiles.py`, `risk.py`, `approvals.py`, provider/pack configuration, command router and README governance material.
- Basis: `structural`.
- Confidence: high.
- Caveats: an operator obviously retains ordinary ownership of a self-hosted installation; the Methodology does not infer `S5=P` from generic configuration authority or per-task approvals.

### Absence scope

- Surfaces inspected: profiles/tool permissions, risk classification/policy extension, approval/rejection, provider configuration, packs/skills, command-router governance, audit state and documented controlled-autonomy levels.
- Plausible first-party paths checked: human final say over privileged tasks, policy configuration, role/profile selection and learning approvals as possible S5 authority.
- Why no material first-party path remains: the inspected rights concern ordinary operational safety/capability selection or S4 adaptation acceptance; no first-party mechanism reconstructs a genuine identity/ultimate-policy question and authoritative return-to-operation closure.

## Recursion

The swarm introduces several parallel operational sub-jobs, but each remains a task-scoped worker under one agent-os installation. The assessment does not infer recursive viability from parallel execution, profiles, providers or the coordinator/sub-job hierarchy. No child unit was shown to own the complete metasystemic set required for its own viability.

## Variety and escalation

Agent-os attenuates operational variety through persistent memory/skills, risk classification, bounded swarm concurrency, SQLite coordination, tracing and human approval. It amplifies capability through configurable providers, MCP servers, skills and role packs. Privileged actions escalate explicitly to the human approval queue rather than being silently executed; rejected actions terminate without effect. Evaluation failures or successful novel workflows can become proposals, but only the skill-learning path reviewed above has a demonstrated parent-owned future capability closure. External Ninja evaluation remains a separate system even where its signals cross this boundary.

## Evidence gaps

The frozen revision supplies enough evidence for inclusion and the published vector. The main remaining ambiguity is organizational rather than documentary: S2's conflict attenuation is mechanically closed but not agent-owned, so Methodology publication uses `C` rather than upgrading deterministic enforcement to `A`. No attempt is made to assess Ninja Harness here; an integrated agent-os + Ninja organization would require a separate system-in-focus and its own evidence.