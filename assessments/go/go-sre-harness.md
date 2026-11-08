---
harness_id: go-sre-harness
project_name: go-sre-harness
repository: https://github.com/rainyZhou2/SreAgentHarness
review_ref: 218c2ce880cbbda33df6464b78aef96d201be913
reviewed_at: 2026-11-08
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C
autonomy_s3_star: C
autonomy_s4: P
autonomy_s5: P
---

# go-sre-harness

## Review boundary

- System in focus: first-party self-hosted Go SRE diagnosis/incident harness, including rule-based and configured external-LLM cognitive strategies, database-backed run/step/attempt workers, orchestration DSL, gateway, policy/approval controls, independent conclusion verifier and profile evaluation/canary service.
- Purpose and identity: a multi-tenant SRE agent that can investigate incidents, form evidence-cited hypotheses, invoke incident tools under a risk floor, recover interrupted runs and improve versioned behavior with operator approval.
- Relevant environment: tenant/user SRE incidents, cloud/Kubernetes/system probes, Git/configured MCP and HTTP tools, credentials for external LLM providers, SQL stores, broker/notification surfaces and human responders/approvers.
- Standard distribution: `cmd/harness` server/worker and `cmd/harness-local`/Wails desktop local mode; default scripted/rule-based strategy exercises transport without provider keys, while substantive adaptive model choice requires an external model configured. A profile can compile a multi-agent flow with child Runs. First-party `internal/app` and `internal/localapp` install the services.
- Credited operating / distribution surfaces: `internal/cognitive`, `internal/kernel`, `internal/flow`, `internal/planner`, `internal/verify`, `internal/policy`, `internal/scheduler`, `internal/gateway`, `internal/store/pg`, `internal/localstore`, `internal/eval`, `internal/profile`, `internal/api`, `internal/app`, `internal/localapp`, `plugins/sretools` and shipped entrypoints.
- Adjacent first-party surfaces excluded from ownership: aspirational design documents, demo/screenshots, external provider reasoning, operator-written incident facts, third-party Kubernetes/cloud platforms and owner/maintainer GitHub governance. No VSM function is inferred solely from an API route name.
- Licensing boundary: the frozen repository has no top-level `LICENSE`, `COPYING` or other license grant; only vendored frontend assets have license files. GitHub reports no recognized repository SPDX license. This is **publicly readable source, not verified OSI-open-source licensing**. The Index's current canonical exclusion predicate is `excluded-no-agentic-vsm`, which is not met by this functioning agent harness; its licensing uncertainty is retained and not silently represented as permissively reusable OSS.
- Modes: default Go worker with rule verifier; external model-backed S1; optional configured cross-run target-rate rules (S2 C); deterministic instance-wide reconciler (S3 C); optionally separate model judge (S3* C); parent-governed profile evaluation/canary and durable policy changes (S4/S5 P). No mode implies that all knobs are active in a fresh deployment.
- Recursion level: one tenant-facing harness instance with multiple incident runs/child workflows; a child Run or provider is not a self-governing viable organization.
- Reviewed revision: `rainyZhou2/SreAgentHarness@218c2ce880cbbda33df6464b78aef96d201be913`; observation `2026-11-08`; Profile `0.2.4` / Methodology `0.3.7`.

## Repository architecture

This is a substantial first-party Go runtime, not merely an SDK or a protocol description: the worker leases and executes stored steps, cognitive strategies emit reasoning and tool intents, the policy gate binds risk class/approval to actions, tool observations return into subsequent reasoning, and the planner compiles user/LLM flows with child runs and re-plan attempts. The run DB owns recovery and event provenance. The kernel also has a conclusion verifier separate from the generating strategy, while profile candidates are independently evaluated on frozen runs and can be rolled out behind human approval. The source contains **zero checked-in Go `_test.go` files** at the frozen ref, and this assessment environment lacks the `go` executable; no actual Go test run or integrated live-server reliability claim is made ([worker](https://github.com/rainyZhou2/SreAgentHarness/blob/218c2ce880cbbda33df6464b78aef96d201be913/internal/kernel/worker.go), [agent loop](https://github.com/rainyZhou2/SreAgentHarness/blob/218c2ce880cbbda33df6464b78aef96d201be913/internal/kernel/agentloop.go), [flow](https://github.com/rainyZhou2/SreAgentHarness/blob/218c2ce880cbbda33df6464b78aef96d201be913/internal/kernel/flow.go), [application wiring](https://github.com/rainyZhou2/SreAgentHarness/blob/218c2ce880cbbda33df6464b78aef96d201be913/internal/app/app.go#L484-L532)).

## S1 — Operations

- State: A
- Function: model-directed incident investigation through plans, hypotheses and tool calls, with observed system state and errors feeding the next reasoning step.
- Disturbance / variety regulated: novel user incidents, unknown root cause, heterogeneous SRE tools, contradictory evidence, tool failure and interrupted/retried attempts.
- Decisive decision or feedback right: configured cognitive/LLM strategy selects hypothesis, tool call and next reasoning step; a model planner may choose a runnable flow and revise it after failure.
- Decision owner: active model-backed strategy/planner inside the worker, constrained by tenant policy; scripted strategy is a deterministic smoke mode and is not counted as model autonomy.
- Supporting / enforcement mechanisms: Run/Step/Attempt transactional ledger and leases, strategies, prompt manifest, model gateway, policy gate, `ToolCall`, flow compiler, retries, memory retrieval, evidence refs and tool observations.
- Closure path: incident goal is persisted; worker obtains a fenced step lease and assembles context; model selects a real tool or conclusion; tool executes after safety/approval evaluation, writes output, and the next leased reasoning step can adjust hypotheses, plan or finish.
- Boundary reachability: normal server/local entrypoints initialize the worker with cognitive strategies, tool registry, gateway and planner; a configured model and granted external tools reach the real execution path, while local scripted strategy can demonstrate plumbing only.
- Why this is / is not agent-owned: action/hypothesis choice is model-cognitive rather than authored runbook; policy and transactional persistence constrain/record, but do not choose the agent's investigative next action.
- Evidence: [agent loop](https://github.com/rainyZhou2/SreAgentHarness/blob/218c2ce880cbbda33df6464b78aef96d201be913/internal/kernel/agentloop.go), [loop safeguards and tool result](https://github.com/rainyZhou2/SreAgentHarness/blob/218c2ce880cbbda33df6464b78aef96d201be913/internal/kernel/loop.go#L200-L441), [model/planner strategy](https://github.com/rainyZhou2/SreAgentHarness/blob/218c2ce880cbbda33df6464b78aef96d201be913/internal/cognitive/llm.go), [flow child execution](https://github.com/rainyZhou2/SreAgentHarness/blob/218c2ce880cbbda33df6464b78aef96d201be913/internal/kernel/flow.go#L23-L240).
- Basis: pinned first-party Go source and declared entrypoints; no compiled/runtime or credentialed model E2E.
- Confidence: medium-high for reachable source-level execution; operational correctness unverified.
- Caveats: a rule-based run without an LLM does not prove an autonomous S1 choice; the source has no Go unit tests, and the available environment has no `go` compiler.

## S2 — Coordination

- State: C
- Function: prevent several independently operating incident agents from exceeding an operator-defined shared-tool/target action budget, and return typed denial feedback for subsequent reasoning.
- Disturbance / variety regulated: separate run/child agents attempting repeated restarts/side effects against the same target within a tenant or exhausting concurrent worker capacity.
- Decisive decision or feedback right: an optional `rate` policy consults **shared tenant action-intent history** for a tool/target/window and applies configured `deny` or approval; pool/lease mechanics additionally prevent over-admission of active execution.
- Decision owner: operator-authored `RuleEngine` and deterministic policy/work scheduler; an executing model can react to the refusal but has no right to relax the floor.
- Supporting / enforcement mechanisms: per-target/per-tool `Rate` match and PostgreSQL/local `CountActions`, fail-closed history errors, action-intent ledger, policy gate, resource pool, serialized branch writer, typed refusal observations.
- Closure path: first incident Run commits a relevant action intent; a concurrent second Run asks for the same tool/target; the shared counter reports the activity, rule matches threshold and gates action; denial/approval requirement returns to the second agent's next step. Activity ages out of the rule window, so later executions can become eligible.
- Boundary reachability: `RuleEngine.EvaluateRequest` is a runnable gate and store implementations count persisted tenant intents; tenant policy configuration may enable `rate.per="target"`. This is not a claim that a default fresh install has a protective rate rule for every SRE tool.
- Why this is / is not agent-owned: C credits an implemented but **configured** cross-S1 interference/feedback mechanism; it is not A because the system does not evidence autonomous model negotiation of contention policies.
- Distinct S1 units: separately executing incident Runs and flow-child model agents within the same tenant, sharing SRE action targets.
- Inter-S1 disturbance: risk of repeated real side effects on the same service/target within one time window, caused by *multiple* agents (the mechanism also works with one agent).
- Attenuating coordination relation: shared target-scoped action count conditions the second action gate on the first agent's recorded intent, reducing repeated/colliding tool effects.
- Feedback into subsequent S1 behaviour: denial/approval status and reason are returned as a refused action in the model's observation stream; operator approval or elapsed time changes future eligibility.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: `rate.per="target"` explicitly inspects real overlapping **tool/target history** across all tenant runs rather than merely passing messages, serializing one child or applying unrelated safety checks.
- Evidence: [target-aware rate contract/counter](https://github.com/rainyZhou2/SreAgentHarness/blob/218c2ce880cbbda33df6464b78aef96d201be913/internal/policy/rules.go#L89-L110), [rate-rule evaluation](https://github.com/rainyZhou2/SreAgentHarness/blob/218c2ce880cbbda33df6464b78aef96d201be913/internal/policy/rules.go#L320-L457), [shared SQL count](https://github.com/rainyZhou2/SreAgentHarness/blob/218c2ce880cbbda33df6464b78aef96d201be913/internal/store/pg/triggers.go#L64-L82), [refusal feedback](https://github.com/rainyZhou2/SreAgentHarness/blob/218c2ce880cbbda33df6464b78aef96d201be913/internal/kernel/loop.go#L200-L243).
- Basis: first-party code-level cross-run rule and durable ledger; no collision experiment executed.
- Confidence: medium: explicit source-specific path but behavior depends on configured policy and functioning persistent store.
- Caveats: rate windows are not atomic reservations against two concurrent first intents; both may pass before either records intent. Tenant-level policy protects only matching configured tool/targets and does not prove universal S2 negotiation.

## S3 — Inside-and-now control

- State: C
- Function: retain an instance-wide current view of lease/run/approval queue liveness and automatically recover stalled operations while preserving the worker and policy contract.
- Disturbance / variety regulated: lost messages, worker crashes/expired leases, stuck conversation branches, stale queues and expired approval requests across simultaneously active incident runs.
- Decisive decision or feedback right: first-party `Reconciler.Tick` reads global persistent state and decides which expired leases/approvals/stalled branches to reactivate or expire; an instance pool caps active work independently of model suggestions.
- Decision owner: deterministic owner-instance reconciler and configuration, not a demonstrated LLM portfolio executive; user/operator owns the parameters.
- Supporting / enforcement mechanisms: database Run/Step state, expired lease recovery, approval expiration, stalled-branch activation, stale run rewake, pool semaphores and notifications/outbox.
- Closure path: durable state and timeouts make blocked/stale runs visible to the periodic reconciler; it returns leases to recoverable state, expires approval, wakes a run/branch and reconnects the next worker step to the same run ledger.
- Boundary reachability: server app initializes the scheduler/reconciler in the normal service mode; the implementation operates on all relevant store runs for an instance, not a test-only runbook.
- Why this is / is not agent-owned: first-party live control is deterministic and bounded; C is a composable organizational current-control facility, **not** S3=A model choice over enterprise priorities.
- Whole-system current view: store-wide run leases, approval expirations, queued and stalled branch state inside the configured tenant/server boundary; excludes external production estate health, personnel or business portfolio.
- Current-control decision scope: recovery/expiration/re-dispatch and per-process capacity, not redefinition of incident strategy, global budget allocation or policies.
- Evidence: [reconciler sweep](https://github.com/rainyZhou2/SreAgentHarness/blob/218c2ce880cbbda33df6464b78aef96d201be913/internal/scheduler/scheduler.go#L96-L158), [concurrency backpressure](https://github.com/rainyZhou2/SreAgentHarness/blob/218c2ce880cbbda33df6464b78aef96d201be913/internal/kernel/pool.go#L9-L41), [durable state recovery](https://github.com/rainyZhou2/SreAgentHarness/blob/218c2ce880cbbda33df6464b78aef96d201be913/internal/localstore/kernel.go#L125-L168).
- Basis: first-party service code and durable semantics; no service-level restart fault-injection performed.
- Confidence: medium-high for bounded S3-like runtime control, low for model-managed all-incident resource decisions.
- Caveats: distinction from S2: S3 here reconciles the **whole current execution state**, not conflicts between two specific operational cells. A service monitor does not establish human-equivalent governance autonomy.

## S3* — Complementary audit

- State: C
- Function: check an agent's final incident claims against actual cited observations using a kernel-owned rule layer, with an optional separate model judge and bounded corrective backtracking.
- Disturbance / variety regulated: unsupported self-declared incident resolution, fabricated citations, references to failed tool calls, inconsistent verification and conclusion/evidence mismatch.
- Decisive decision or feedback right: verifier decides SUPPORTED/INSUFFICIENT/CONTRADICTED from a canonical evidence map; configured distinct judge may perform semantic support checks without being given the original agent's prompt/history; kernel can return a challenge step to the producing model.
- Decision owner: non-agent rule verifier by default and optional independent model judge; kernel for backtrack/action decision, not the producing strategy.
- Supporting / enforcement mechanisms: `verify.Verifier`, `ModelJudge` with a separate alias/prompt, canonical citation resolver, internal `conclusion_review` follow-up, bounded `MaxBacktracks`, durable independent_verification report and reasoning score gating.
- Closure path: final task decision exposes structured claims; kernel reconstructs cited evidence from real observation refs, verifier evaluates it; on insufficient/contradicted status and remaining budget, a kernel-owned challenge returns issues to S1 reasoning and revised claims can be checked again. Otherwise report persists with an unsupported outcome.
- Boundary reachability: normal server `internal/app` defaults `HARNESS_REASONING_VERIFY=true`, and local runtime installs the rule verifier; setting `HARNESS_VERIFIER_MODEL_ALIAS` adds a separate model judge. Hence C covers both genuine compulsory mechanical check and explicitly configured complementary model path, not a claim of always-on independent semantic LLM audit.
- Why this is / is not agent-owned: generator cannot grant its own claim status; a configured separate model may apply actual semantic judgment. Default rule-only citation check is deterministic and could not alone warrant S3*=A.
- Claim being audited: the final agent-reported VERIFIED/REFUTED incident hypotheses and cited evidence supporting diagnosis/conclusion.
- Ordinary reporting path: producing strategy's structured decision/hypotheses and summary, including its own claimed verification and cited refs.
- Complementary access path: kernel independently resolves canonical refs to recorded tool observations, evidence and memory available in the run ledger; optional judge reads those observations under a distinct prompt and model identity.
- Independence boundary: separate verifier code and optional judge model call from the producer; uses the **same source-observation corpus** (not direct independent re-probing of external environment), and is configurable/disableable by the operator.
- Who acts on findings: kernel inserts hidden `conclusion_review` challenge to producer within backtrack budget; saved report/metrics also inform operator and profile quality gate.
- Evidence: [verifier contract/rules](https://github.com/rainyZhou2/SreAgentHarness/blob/218c2ce880cbbda33df6464b78aef96d201be913/internal/verify/verify.go#L1-L187), [separate judge](https://github.com/rainyZhou2/SreAgentHarness/blob/218c2ce880cbbda33df6464b78aef96d201be913/internal/verify/judge.go#L20-L127), [kernel corrective loop](https://github.com/rainyZhou2/SreAgentHarness/blob/218c2ce880cbbda33df6464b78aef96d201be913/internal/kernel/review.go#L120-L212), [default and optional app wiring](https://github.com/rainyZhou2/SreAgentHarness/blob/218c2ce880cbbda33df6464b78aef96d201be913/internal/app/app.go#L503-L524).
- Basis: implemented return-to-producer code and separate-model mode; no live independent review result witnessed.
- Confidence: medium-high for code-level closure; stronger claims of verifier *truthfulness* are unsupported by testing here.
- Caveats: canonical citation existence is not external truth, and a separately prompted judge sharing the same evidence corpus is only bounded independence. The repository contains no Go tests to independently corroborate runtime execution.

## S4 — Outside-and-then intelligence

- State: P
- Function: operator-led prospective improvement of future incident-handling capability through frozen real-run datasets, candidate profile variants, offline evaluation, holdout gates, measured canary and return to active profile.
- Disturbance / variety regulated: changing external incident mix/service reliability and observed mismatch between current agent behavior and future target quality, failure rate, tool safety or cost.
- Decisive decision or feedback right: owner/proposer chooses a candidate future profile version; non-inferiority gate compares candidate vs historical baseline and forbids failed promotion; a *distinct approving human* authorizes canary, the monitor auto-rolls back detected regressions, and owner chooses promotion.
- Decision owner: legitimate local operator/approver for strategic option proposal/adoption; deterministic replay gate and canary monitor control test and rollback. No autonomous S4=A external trend strategist is claimed.
- Supporting / enforcement mechanisms: dataset recording from actual runs, frozen holdout evaluation, profile candidate versioning, `Gate` thresholds, `Approve` anti-self-approval, percentage-bucketed canary rollout, control/canary stats and continuous rollback monitor.
- Closure path: real incident-run outcomes/feedback become dataset cases; owner proposes candidate to improve future SRE responses; baseline/candidate replay produces gate evidence; different authorized approver accepts; routed future Runs exercise canary, with rollback on breach; successful owner promotion sets the new active profile version used by subsequent Runs.
- Boundary reachability: `internal/eval.Service` implements all transitions, `ResolveProfile` routes real new Runs to canary/active versions, and API offers candidate/evaluation/approval/rollout operations; this is a supported **human-parent** improvement mode, not merely a README suggestion.
- Why this is / is not agent-owned: an operator supplies the future option and authority to promote; automatic evaluation/rollback are supporting tests. P avoids assigning a strategic choice to the diagnostic LLM.
- External distinction: incident outcomes and operator feedback originate from real monitored SRE services outside the harness's own model loop; frozen evaluation cases preserve these past external disturbances rather than generating synthetic internal tests alone.
- Future / prospective distinction: a proposed candidate is assessed against a frozen holdout **before** it handles future incidents, and canary groups measure whether a prospective new configuration should become the next active operating default.
- Adaptation option generated: a human operator/proposer supplies a new version of evolvable model, reasoning, memory or planner configuration, judged against holdout baseline and released only after a distinct human gate; there is no autonomous option inventor credited.
- Path back into current capability / S3: `StartCanary`/`ResolveProfile` makes new Runs use the candidate profile percentage; `Promote` changes active profile for subsequent S1 Runs, while `MonitorTick` protects current S3 control by quarantining and rolling back regressions.
- Evidence: [real-run dataset recording](https://github.com/rainyZhou2/SreAgentHarness/blob/218c2ce880cbbda33df6464b78aef96d201be913/internal/eval/service.go#L187-L266), [candidate replay/gate](https://github.com/rainyZhou2/SreAgentHarness/blob/218c2ce880cbbda33df6464b78aef96d201be913/internal/eval/service.go#L325-L396), [separate human approval and canary](https://github.com/rainyZhou2/SreAgentHarness/blob/218c2ce880cbbda33df6464b78aef96d201be913/internal/eval/service.go#L397-L455), [promotion and active routing](https://github.com/rainyZhou2/SreAgentHarness/blob/218c2ce880cbbda33df6464b78aef96d201be913/internal/eval/service.go#L456-L505), [rollback monitor](https://github.com/rainyZhou2/SreAgentHarness/blob/218c2ce880cbbda33df6464b78aef96d201be913/internal/eval/service.go#L506-L580).
- Basis: first-party persisted candidate/evaluation/canary implementation and return-to-operation controls.
- Confidence: medium for supported human-guided future adaptation; no empirical dataset/canary deployment witnessed.
- Caveats: dataset replay and regression monitoring do not independently sense geopolitical or strategic future. No model-origin selection of an outside future option is established. The README's phrase "evolution loop is complete" is read only as bounded product-level parent-guided capability improvement.

## S5 — Policy and identity

- State: P
- Function: operator-governed versioned policy/authority of the SRE agent profile, maintaining a non-relaxable risk floor and controlling when identity-critical tools/policies change across future Runs.
- Disturbance / variety regulated: proposed efficiency/evolution changes that would weaken safety policy, permit destructive R3 actions or change an agent's enduring tool/authorization identity without legitimate authority.
- Decisive decision or feedback right: human operator creates/edits immutable versioned profiles and must authorize frozen identity fields; evolution candidates cannot modify tools, approval policy, risk overrides, allowed aliases, strategy or flow; framework policy floor forbids R3 and requires approval for R2.
- Decision owner: tenant administrator/legitimate human owner and enforced framework floor, not individual incident-solving agent or arbitrary extension plugin.
- Supporting / enforcement mechanisms: `profile.Spec` frozen/evolvable distinction and `ApplyPatch` reject rules, `policy.Guarded` safety floor, identity-bound plan/action approvals, profile version pinning, tenant permissions and audit ledger.
- Closure path: owner changes constitutive profile in permitted profile-creation/update pathway; a new immutable version persists, a Run pins the authorized version, and the worker's effective tool/policy scope is rebuilt under it. A candidate aiming to change a frozen field fails rather than silently changing the ultimate rules.
- Boundary reachability: profile APIs and app are real entrypoints; `profile.Spec` is passed to worker tool/policy resolution, and the guard is composed around custom policy. The claimed P mode is a human-parent governing boundary, not autonomous S5=A.
- Why this is / is not agent-owned: ultimate identity/prohibition belongs to the operator/framework. The agent may optimize cognitive parameters but cannot authorize itself to relax safety-critical frozen fields.
- Identity / ultimate-policy issue: enduring agent's allowed tools, safety risk classes, approval requirements, strategy and immutable flow are constitution-level profile boundaries, distinct from approving an individual action intent.
- Ultimate authority in each claimed mode: authorized human/operator plus non-bypassable safety floor; no independent agent's power to rewrite its own policy.
- Return-to-operation path: new authorized profile version is persisted and pinned into subsequent Run creation; policy floor applies to every later tool intent.
- Evidence: [operator-owned profile and frozen fields](https://github.com/rainyZhou2/SreAgentHarness/blob/218c2ce880cbbda33df6464b78aef96d201be913/internal/profile/profile.go#L1-L113), [non-bypassable policy floor](https://github.com/rainyZhou2/SreAgentHarness/blob/218c2ce880cbbda33df6464b78aef96d201be913/internal/policy/gate.go#L53-L90), [human separate approval](https://github.com/rainyZhou2/SreAgentHarness/blob/218c2ce880cbbda33df6464b78aef96d201be913/internal/eval/service.go#L397-L415), [profile API](https://github.com/rainyZhou2/SreAgentHarness/blob/218c2ce880cbbda33df6464b78aef96d201be913/internal/api/profiles.go).
- Basis: versioned schema, executable policy floor and owner-facing API code.
- Confidence: medium-high for structural human authority and return, not for live compliance reliability.
- Caveats: approving one risk-R2 command is S1 safety governance, not by itself S5. Only durable changes to the governing profile/identity plus non-relaxable floor support S5=P here.

## Modes and ownership

| Supported mode / owner | S1 | S2 | S3 | S3* | S4 | S5 |
| --- | --- | --- | --- | --- | --- | --- |
| Model-backed incident Run | A | — | — | C (rule check) | — | — |
| Multi-Run server, configured target-rate rule | A | C | C (reconciler) | C | — | — |
| Optional separate `HARNESS_VERIFIER_MODEL_ALIAS` | A | C | C | C (model judgment) | — | — |
| Human-gated profile evaluation/canary | A | — | C | C | P | P |
| Local scripted smoke/no provider key | — | — | C | C (rules if claims) | — | P |

Aggregate vector represents union of implemented supported modes, not simultaneous out-of-box agent ownership of six functions.

## Recursion

An incident `Run` may contain child Runs in flow branches with independent cognitive decisions, but those subruns inherit tenant policy and execution orchestration; they are not individually autonomous S3/S4/S5 organizations. Multi-tenant operation gives an instance-wide deterministic reconciler, not a demonstrated separate metasystem for every subagent. Evaluation and policy approval are parent-owned functions of the managed harness instance.

## Variety and escalation

Typed tools, model/provider choice, flow DSL, hypotheses and memory expand diagnostic variety; risk floors, per-target rate rules, tool approvals, leases and serialized branch control attenuate errors and interference. Current failed leases are recovered by a periodic reconciler. Unsupported conclusions return through a bounded kernel review step; failed or inconclusive checks terminate visibly when the budget is spent. Parent-controlled profile evaluation proposes changes against earlier real incidents, with holdout non-inferiority and rollout rollback before wider adoption. Unknown external side-effect outcomes escalate to a human without automatic retry.

## Evidence gaps

- The exact frozen tree contains **no project Go `_test.go` files** and the assessment runner has no `go` binary; the source could not be built or exercised here. No verified cluster, model-provider or canary outcome is claimed. Code-level confidence is not deployment reliability.
- The repository does **not** contain a first-party license grant at this ref. Its public GitHub visibility is not equivalent to established open-source licensing; treat external redistribution as unlicensed until the author clarifies it.
- Configured per-target action-rate rules are a credible S2 collision attenuator but not a transactional distributed mutex. Model judgment under S3* is optional; the default rule reviewer checks provenance, not factual truth outside observed tool data.
- S3 and S4 are limited to deterministic instance recovery and human-parent prospective profile evolution; neither establishes autonomous model-led enterprise portfolio management or environmental strategy research.
