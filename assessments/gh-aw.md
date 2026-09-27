---
harness_id: gh-aw
project_name: GitHub Agentic Workflows
repository: https://github.com/github/gh-aw
review_ref: ff2eccd10a30d6a7bfaf0da449194e907a206555
reviewed_at: 2026-09-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-27
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: P
---

# GitHub Agentic Workflows

## Review boundary

- System in focus: one repository-level organization of agentic work compiled and operated through first-party GitHub Agentic Workflows (`gh-aw`) at pinned revision `ff2eccd10a30d6a7bfaf0da449194e907a206555`, including compiled agent jobs, tool/sandbox controls, concurrency and AI-credit regulation, threat detection, safe-output application and runtime-loaded workflow instructions.
- Purpose and identity: let repository owners define durable AI-powered work organizations in Markdown/frontmatter, execute model-driven repository work under constrained authority, regulate concurrent/resource use, independently challenge proposed writes, and preserve repository-owner authority over the workflow's load-bearing purpose and policy.
- Relevant environment: repository/issue/PR state; GitHub Actions runs; configured AI engines and model providers; tools/MCP servers; network resources; concurrent workflow runs; shared write surfaces; AI-credit availability; agent outputs and patches; threat signals; repository-owner instruction changes; external GitHub authorization and environment controls.
- Standard-distribution boundary: the public `gh-aw` CLI/compiler and the runtime jobs/configuration it generates for supported GitHub Actions execution, including built-in engine adapters, agent-job sandbox/tool wiring, concurrency controls, AI-credit guardrails, threat-detection jobs, safe-output jobs and runtime workflow-body loading. GitHub Actions itself, model/provider internals, external MCP/tool services and repository applications built on top remain dependencies/environment; their internal organizational functions are not imported.
- Credited operating / distribution surfaces: `README.md`; `docs/src/content/docs/reference/faq.md`; `docs/src/content/docs/guides/working-with-workflows.mdx`; `docs/src/content/docs/reference/concurrency.md`; `docs/src/content/docs/specs/ai-credits-specification.md`; `docs/src/content/docs/reference/threat-detection.md`; `docs/src/content/docs/reference/safe-outputs.md`; `docs/src/content/docs/specs/safe-outputs-specification.md`; generated agent/detection/safe-output job architecture reachable through supported compilation and execution.
- Adjacent first-party surfaces excluded from ownership: repository contributor/maintainer workflows and `.github/workflows/*` dogfood as autonomous owners of the product boundary; experimental benchmark/reporting results not wired into standard adaptation; scratchpad/design material without shipped closure; GitHub-host governance of the `github/gh-aw` project itself; AI-provider internals; ordinary GitHub Actions platform behavior not specifically composed by `gh-aw`.
- First-party operating / deployment modes considered: normal compiled agentic workflow execution with a built-in engine; concurrent workflow execution under generated concurrency groups; safe-output-enabled write workflows; default AI threat detection; workflow-author configured custom detection; daily/per-run AI-credit guardrails; repository-owner editing of runtime-loaded Markdown instructions; experimental steering only as current-run evidence, not S5 ownership.
- Recursion level: the repository-level `gh-aw` workflow organization is the system-in-focus. Individual model-driven agentic workflow runs and dispatched worker workflows can be S1 units when they own separate substantive repository outcomes. Compiler/runtime guardrails and complementary detection operate at the metasystem around those units. External AI engines supply model inference but do not donate their own S2-S5 functions.
- Reviewed revision: `ff2eccd10a30d6a7bfaf0da449194e907a206555`.
- Observation date: 2026-09-27.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

GitHub Agentic Workflows compiles a Markdown workflow definition into a standard GitHub Actions lock workflow. Frontmatter chooses triggers, permissions, tools, engine, network policy, concurrency and guarded output surfaces; the Markdown body supplies the operational instructions. At runtime a generated agent job invokes a configured AI engine inside the `gh-aw` sandbox/tool boundary. The agent interprets instructions, observes repository/tool state and produces task results or structured requests for later writes. Built-in engine implementations are swappable; their provider internals remain external to the assessed boundary.

The write architecture deliberately separates operational reasoning from privileged mutation. Agent jobs are read-only by default. When `safe-outputs` are configured, the agent emits structured requested operations while separate jobs with scoped write permissions validate and apply those operations. This separation is supporting authority machinery rather than a VSM function by itself, but it is central to the current-control and audit topology.

`gh-aw` also ships concrete anti-interference rules. Per-workflow concurrency groups separate issue/PR/ref contexts, serialize conflicting runs when required and preserve queued work with `queue: max`; per-engine groups prevent simultaneous resource exhaustion; safe-output groups can serialize write application where duplicate operations would be undesirable; conclusion jobs receive generated groups specifically to avoid collision; and fan-out `job-discriminator` prevents independent dispatched runs from cancelling one another through a shared static slot. These are S2-specific constructor rules where they attenuate named run/run or write/write disturbances, not merely generic orchestration.

Current-control machinery is likewise constructor-owned. Per-run and rolling 24-hour AI-credit guardrails bound resource consumption and can prevent an agent from starting or continuing once the configured budget is exhausted. Concurrency/resource rules operate from workflow/run identity and aggregate budget state. Workflow authors and organization variables determine thresholds, but the standard distribution does not establish a separate first-party parent actor with a whole-system current view and returned discretionary S3 decision; this is therefore plain `C`, not `C(P)`.

Complementary audit is stronger. With safe outputs, a distinct threat-detection job runs after the producing agent and before privileged writes. It receives the workflow context, structured agent output and patch artifacts, asks a separate detection-agent invocation to judge prompt injection, secret leakage and malicious patches, emits a structured verdict/reasons object and can block the safe-output path. The decisive audit judgment is agentic; deterministic parsing and write gating enforce the verdict but do not own it. The standard path can also select a different built-in engine or add independent scanners without changing the functional separation.

The experimental A/B subsystem does not establish S4. It can assign variants, persist observations, analyze metrics and produce deterministic `PROMOTE` / `REJECT` / `EXTEND` / `INCONCLUSIVE` decisions, but its specification explicitly forbids the decision layer from changing traffic, mutating experiment state or promoting workflow sources. More importantly, it optimizes internal workflow behavior rather than closing the Profile's required external-and-prospective intelligence loop into changed current organizational capability.

Ultimate workflow purpose remains parent-governed. The Markdown body contains the instructions telling the agent what to accomplish and is deliberately loaded at runtime rather than frozen into the compiled lock file. A legitimate repository owner can change purpose/instructions in the authoritative workflow source, and the next run consumes that changed body without recompilation. That gives the parent a concrete policy/identity change → authoritative source → subsequent-operation return path. Frontmatter configuration and generic approvals are not used as S5 evidence by themselves.

## Operational model

A normal S1 begins when a supported trigger starts the compiled workflow. `gh-aw` constructs the agent job with the selected engine, permitted tools, sandbox/network boundary and current Markdown instructions. The model-driven actor reasons over repository/tool observations and chooses context-sensitive actions within those constraints. Where a write is required, the agent produces a structured safe-output request rather than receiving the write token directly.

Multiple such work cells can coexist. The generated concurrency layer determines which cells may run together and which must queue, cancel or use distinct fan-out slots, preventing specific collisions and resource contention. Current resource regulation applies per-run and rolling-workflow AI-credit budgets. Before a proposed privileged mutation is applied, a separate detection actor audits the proposed output/patch and may return a blocking threat finding.

Across runs, the repository-owned Markdown source acts as the authoritative purpose surface. Because its body is loaded at execution time, a legitimate owner amendment returns directly into later operation. This parent loop is distinct from an ordinary agent deciding how to execute the currently assigned work.

## S1 — Operations

- State: A
- Function: perform substantive repository work requiring model interpretation/reasoning, including tasks such as triage, review, failure investigation, documentation maintenance, dependency analysis and repository reporting.
- Disturbance / variety regulated: ambiguous natural-language instructions; changing issue/PR/repository state; tool observations; model uncertainty; external data available through permitted tools; task-specific errors and incomplete evidence.
- Decisive decision or feedback right: choose the next context-sensitive reasoning/tool action needed to satisfy the workflow instructions and revise later actions in response to returned observations.
- Decision owner: the model-driven agent actor executed by the first-party generated agent job.
- Supporting / enforcement mechanisms: compiler-generated job; selected built-in engine adapter; sandbox; network allowlist/firewall; GitHub/MCP tool allowlists; context assembly; read-only token posture; run/turn/resource bounds; structured safe-output interface.
- Closure path: trigger + runtime-loaded workflow instructions -> generated agent job invokes the selected model-driven actor -> actor interprets current context and calls permitted tools -> observations return to the agent execution -> later actions/output change accordingly -> a substantive task result or structured requested mutation is produced.
- Boundary reachability: the README defines agentic workflows specifically as Markdown/frontmatter compiled into GitHub Actions that run AI agents, and the supported standard path wires built-in engines into the generated agent job; no adjacent dogfood agent is required for this operational loop.
- Why this is / is not agent-owned: removing the model-driven actor while retaining the compiler, sandbox, permissions and safe-output machinery leaves enforcement and transport but not the contextual decision about what repository action/reasoning step to attempt next.
- Evidence: [`README.md`](https://github.com/github/gh-aw/blob/ff2eccd10a30d6a7bfaf0da449194e907a206555/README.md); [`docs/src/content/docs/reference/faq.md`](https://github.com/github/gh-aw/blob/ff2eccd10a30d6a7bfaf0da449194e907a206555/docs/src/content/docs/reference/faq.md); [`docs/src/content/docs/guides/working-with-workflows.mdx`](https://github.com/github/gh-aw/blob/ff2eccd10a30d6a7bfaf0da449194e907a206555/docs/src/content/docs/guides/working-with-workflows.mdx).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: Copilot/Claude/Codex/Gemini/Pi provider internals remain external systems. `A` credits the agent actor in the first-party `gh-aw` execution path, not higher-order functions internal to any provider.

## S2 — Coordination

- State: C
- Function: attenuate concrete interference among concurrently active S1 workflow cells by serializing contexts that would collide while allowing independent work to proceed without sharing a cancellation/resource slot.
- Disturbance / variety regulated: concurrent runs for the same issue/PR/ref displacing one another; multiple agent jobs exhausting one engine slot; safe-output jobs applying duplicate/conflicting mutations; conclusion jobs colliding; fan-out children cancelling one another because they inherit the same static job-level concurrency group.
- Decisive decision or feedback right: determine whether a run/job must queue, may execute concurrently, should cancel an outdated peer, or requires a unique job discriminator to avoid unintended contention.
- Decision owner: constructor-defined `gh-aw` concurrency policy generated from workflow/event identity and configured concurrency fields; no model actor owns the collision semantics.
- Supporting / enforcement mechanisms: per-workflow concurrency groups; per-engine groups; `queue: max`; `cancel-in-progress`; `safe-outputs.concurrency-group`; conclusion-job group; `concurrency.job-discriminator`; GitHub Actions concurrency enforcement.
- Closure path: concurrent S1/job intents reach generated concurrency grouping -> `gh-aw` assigns the relevant common or disjoint group and queue/cancel policy -> a conflicting run waits/cancels while independent/discriminated work proceeds -> the admitted/queued outcome changes which S1 executes next and prevents the named collision from reaching operation.
- Boundary reachability: concurrency groups and queue/discriminator behavior are compiler-generated first-party runtime configuration in the supported standard distribution; they do not require an adopter to invent a separate coordination protocol.
- Why this is / is not agent-owned: the same queue/cancel/discriminator decision occurs if the worker model is removed and the compiler/runtime policy remains. The function-specific path therefore exists as `C`, not `A`.
- Distinct S1 units: independently triggered model-driven workflow runs and fan-out worker workflow runs that own separate repository-work outcomes under the same `gh-aw` organization.
- Inter-S1 disturbance: siblings can compete for the same issue/PR/ref execution slot, engine capacity, output-application lane or static fan-out slot, causing cancellation, duplicate mutation, resource exhaustion or conclusion collision.
- Attenuating coordination relation: event-specific concurrency groups serialize genuinely shared contexts; per-engine groups cap shared model capacity; safe-output/conclusion groups serialize collision-prone post-processing; `job-discriminator` separates independent fan-out children that should not compete.
- Feedback into subsequent S1 behaviour: queued runs execute only after the current holder completes, outdated PR runs can be cancelled, and discriminated fan-out children receive distinct slots so their operational jobs continue instead of being displaced.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the mapping is tied to explicit documented collision/resource-contention classes and generated attenuation rules that alter later S1 admission/execution; orchestrator fan-out or delegation alone is not used as the S2 witness.
- Evidence: [`docs/src/content/docs/reference/concurrency.md`](https://github.com/github/gh-aw/blob/ff2eccd10a30d6a7bfaf0da449194e907a206555/docs/src/content/docs/reference/concurrency.md); [`docs/src/content/docs/patterns/orchestrator-ops.md`](https://github.com/github/gh-aw/blob/ff2eccd10a30d6a7bfaf0da449194e907a206555/docs/src/content/docs/patterns/orchestrator-ops.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: dispatch/call-workflow topology is corroborating evidence for distinct operational cells, not S2 by itself. The positive S2 mapping rests on explicit interference and attenuation.

## S3 — Inside-and-now control

- State: C
- Function: regulate current workflow resource consumption and execution admission from aggregate/current run state using first-party budget and concurrency policy.
- Disturbance / variety regulated: a single run consuming excessive AI credits; one workflow consuming excessive credits across a rolling 24-hour window; agent jobs over-consuming shared engine capacity; unbounded concurrent execution disrupting current service/resource availability.
- Decisive decision or feedback right: determine whether a current run may start/continue under its per-run and rolling daily resource envelope and whether current jobs may enter a shared engine/concurrency slot.
- Decision owner: constructor/workflow-configuration policy resolved and enforced by first-party `gh-aw` compiler/runtime paths. Workflow authors or organization variables can set thresholds, but no separately closed parent S3 mode with the required whole-system current view and discretionary returned decision is established at the reviewed boundary.
- Supporting / enforcement mechanisms: `max-ai-credits`; `max-daily-ai-credits`; AWF firewall budget enforcement; rolling 24-hour usage accounting; generated environment/config resolution; per-engine concurrency; warning/failure reporting; disable/bypass rules for explicitly user-initiated invocations.
- Closure path: current run/rolling usage and concurrent-slot state are evaluated -> configured first-party budget/concurrency rule admits, queues, throttles or blocks execution -> agent start/continuation changes accordingly -> subsequent current operation remains inside the resolved resource envelope.
- Boundary reachability: AI-credit guardrails and generated concurrency controls are normative shipped `gh-aw` runtime/compiler behavior and are active through ordinary compiled workflow execution.
- Why this is / is not agent-owned: model actors do not decide whether the organization should exceed the configured budget/concurrency envelope. The decisive regulatory policy is constructor/configuration-owned; runtime enforcement executes it.
- Whole-system current view: for the declared workflow organization, rolling 24-hour AI-credit accounting aggregates consumption across runs, while generated concurrency/resource state tracks admission to shared workflow/engine slots rather than only one model turn's local state.
- Current-control decision scope: current resource/credit budget, current run admission/continuation and shared execution capacity. Tool choice, prompt interpretation and safe-output content remain operational or audit matters rather than S3 ownership.
- Evidence: [`docs/src/content/docs/specs/ai-credits-specification.md`](https://github.com/github/gh-aw/blob/ff2eccd10a30d6a7bfaf0da449194e907a206555/docs/src/content/docs/specs/ai-credits-specification.md); [`docs/src/content/docs/reference/concurrency.md`](https://github.com/github/gh-aw/blob/ff2eccd10a30d6a7bfaf0da449194e907a206555/docs/src/content/docs/reference/concurrency.md); [`actions/setup/md/ai_credits_rate_limit_error.md`](https://github.com/github/gh-aw/blob/ff2eccd10a30d6a7bfaf0da449194e907a206555/actions/setup/md/ai_credits_rate_limit_error.md); [`actions/setup/md/daily_workflow_aic_exceeded.md`](https://github.com/github/gh-aw/blob/ff2eccd10a30d6a7bfaf0da449194e907a206555/actions/setup/md/daily_workflow_aic_exceeded.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: `safe-outputs.steer`, GitHub Environment review and organization-level variables provide useful human/operator controls, but they are not promoted to S3 parent mode here because the frozen standard path does not establish the complete parent whole-system-current-view -> discretionary S3 decision -> returned whole-system operation closure required for `(P)`.

## S3* — Complementary audit

- State: A
- Function: independently challenge the producing agent's proposed output/code changes for security-relevant failures before privileged mutation is applied.
- Disturbance / variety regulated: prompt-injected behavior; leaked credentials/secrets; malicious or suspicious code patches; producing-agent claims that are unsafe when checked against the actual structured output, patch and workflow context.
- Decisive decision or feedback right: judge whether the produced artifact contains one or more configured threat classes and return a structured approve/block finding with reasons before safe outputs are applied.
- Decision owner: the separate threat-detection agent invocation that analyzes the producer's artifacts/context and emits the security judgment. Deterministic result parsing and safe-output gating enforce that judgment but do not own it.
- Supporting / enforcement mechanisms: dedicated `detection` job; staged workflow prompt/context; `agent_output.json`; `aw.patch`; configurable detection engine; structured JSON verdict; optional pre/post scanners; blocking/failure path into `safe_outputs`; scoped write separation.
- Closure path: producing agent finishes -> artifacts are staged into the separate threat-detection job -> detection actor inspects workflow context/output/patch -> verdict/reasons are emitted -> a detected threat blocks or conditions the safe-output lane -> privileged repository mutation therefore changes according to complementary findings.
- Boundary reachability: threat detection is automatically enabled with safe outputs by default, runs as a distinct generated job before supported safe-output writes, and can use a separate built-in engine; no adjacent repository dogfood reviewer is required.
- Why this is / is not agent-owned: removing the detection model actor while retaining the parser/gate leaves no equivalent semantic judgment over prompt injection, secret leakage or malicious patches. Conversely, removing the gate leaves a judgment but not enforcement. The audit judgment is therefore agent-owned while enforcement remains supporting machinery.
- Claim being audited: that the producing agent's proposed structured output and code patch are safe enough to enter the privileged safe-output application path.
- Ordinary reporting path: the main agent job produces normal task output / structured safe-output items and patch artifacts from its operational context.
- Complementary access path: the separate detection job receives the raw structured output, patch, prompt/import context and workflow intent rather than relying only on the producing agent's self-report.
- Independence boundary: detection executes after the main agent in a distinct job/context, can use a separately configured built-in engine and owns no production step; the producer cannot select the trusted detection-job identity from its own output.
- Who acts on findings: generated safe-output/control logic blocks or withholds privileged writes when the audit finding is unsafe; tracking/reporting surfaces may additionally expose the finding to maintainers.
- Evidence: [`docs/src/content/docs/reference/threat-detection.md`](https://github.com/github/gh-aw/blob/ff2eccd10a30d6a7bfaf0da449194e907a206555/docs/src/content/docs/reference/threat-detection.md); [`docs/src/content/docs/reference/safe-outputs.md`](https://github.com/github/gh-aw/blob/ff2eccd10a30d6a7bfaf0da449194e907a206555/docs/src/content/docs/reference/safe-outputs.md); [`docs/src/content/docs/specs/safe-outputs-specification.md`](https://github.com/github/gh-aw/blob/ff2eccd10a30d6a7bfaf0da449194e907a206555/docs/src/content/docs/specs/safe-outputs-specification.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: using the same provider/model family for producer and detector does not make their contexts/roles identical, but it can correlate failure modes. The positive mapping relies on job/context separation and complementary raw-artifact access, not on a claim of statistical independence between model weights.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party external-and-prospective adaptation loop is established in the supported `gh-aw` distribution at the pinned boundary.
- Disturbance / variety regulated: not applicable for a positive S4 mapping.
- Decisive decision or feedback right: not established.
- Decision owner: none established at this boundary.
- Supporting / enforcement mechanisms: experiment assignment/analysis, audit/forecast/reporting, dependency/model catalog updates, external tools/search and repository-maintenance workflows were inspected but do not by themselves close S4.
- Closure path: no qualifying external-distinction -> prospective adaptation option -> adopted change to present organizational capability loop is established.
- Why this is / is not agent-owned: the repository contains learning/analysis/experimentation machinery, but no standard autonomous actor is shown owning a future-capability adaptation decision that closes back into the assessed organization.
- Evidence: [`docs/src/content/docs/experimental/experiments-specification.md`](https://github.com/github/gh-aw/blob/ff2eccd10a30d6a7bfaf0da449194e907a206555/docs/src/content/docs/experimental/experiments-specification.md); [`docs/src/content/docs/reference/audit.md`](https://github.com/github/gh-aw/blob/ff2eccd10a30d6a7bfaf0da449194e907a206555/docs/src/content/docs/reference/audit.md); [`docs/src/content/docs/specs/forecast-specification.md`](https://github.com/github/gh-aw/blob/ff2eccd10a30d6a7bfaf0da449194e907a206555/docs/src/content/docs/specs/forecast-specification.md).
- Basis: explicit + structural negative review.
- Confidence: high.
- Caveats: repository-local dogfood agents may propose improvements to `gh-aw` itself, but contributor/R&D loops are adjacent to the assessed product distribution and cannot be imported as runtime S4 ownership.

### Absence scope

- Surfaces inspected: A/B experiment schema/assignment/persistence/statistical decision path; audit/forecast tooling; workflow imports/dependencies; model-catalog synchronization; runtime-loaded instructions; safe-output writes; repository dogfood improvement workflows and related documentation discovered in the frozen tree.
- Plausible first-party paths checked: experiment `PROMOTE/REJECT` decisions; automated reporting; model/dependency refresh; agent-authored pull requests; external research/search tasks; instruction-maintenance workflows; persistent experiment state.
- Why no material first-party path remains: the experiment decision layer explicitly must not change traffic or promote workflow sources, and the other reviewed paths either maintain the product, report current/historical state, or permit arbitrary application-level external research without supplying a standard `gh-aw` organizational intelligence loop. None closes external/future sensing into an adopted change of present `gh-aw` capability at the declared distribution boundary.

## S5 — Policy and identity

- State: P
- Function: preserve legitimate repository-owner authority over the workflow organization's load-bearing purpose/instructions across runs and return an authoritative policy/purpose amendment into later operation.
- Disturbance / variety regulated: drift between the repository owner's intended workflow purpose and the instructions actually governing future agent runs; need to replace or refine top-level task/policy instructions without allowing an ordinary operational agent to silently become ultimate authority.
- Decisive decision or feedback right: accept and commit an authoritative change to the Markdown workflow body that defines what the agent is to accomplish and the policy/instruction context governing later runs.
- Decision owner: the legitimate repository owner/maintainer acting at the parent recursion through repository write/governance authority. No first-party autonomous `gh-aw` actor is established as ultimate authority over its own workflow identity.
- Supporting / enforcement mechanisms: authoritative `.md` workflow source; repository write/merge controls; runtime body loading; compiler separation between runtime-loaded body and compiled frontmatter; GitHub revision history.
- Closure path: identity/purpose/instruction issue is resolved by the legitimate repository parent -> parent changes/accepts the authoritative Markdown workflow body -> the body remains the source consumed at runtime -> the next workflow run loads the amended instructions -> subsequent S1 operation is governed by the returned parent decision.
- Boundary reachability: runtime loading of the Markdown body is a documented standard `gh-aw` behavior: changes to instructions, output templates, context, conditions and examples take effect on the next run without recompilation. The return path is therefore part of ordinary supported execution rather than a project-specific dogfood loop.
- Why this is / is not agent-owned: an operational agent may propose repository changes through safe outputs, but repository authority still determines whether the load-bearing workflow source changes. The agent does not acquire legitimate ultimate-policy authority merely by being able to draft a patch.
- Identity / ultimate-policy issue: what durable purpose/instructions define this agentic workflow across executions, including a parent decision to replace or refine those load-bearing instructions.
- Ultimate authority in each claimed mode: parent mode only — legitimate repository owner/maintainer authority over the authoritative workflow source. No supported autonomous S5 mode is established.
- Return-to-operation path: committed Markdown-body amendment -> runtime body load on the next trigger -> model-driven S1 receives changed authoritative instructions -> later work follows the amended purpose/policy.
- Evidence: [`README.md`](https://github.com/github/gh-aw/blob/ff2eccd10a30d6a7bfaf0da449194e907a206555/README.md); [`docs/src/content/docs/guides/working-with-workflows.mdx`](https://github.com/github/gh-aw/blob/ff2eccd10a30d6a7bfaf0da449194e907a206555/docs/src/content/docs/guides/working-with-workflows.mdx); [`docs/src/content/docs/reference/faq.md`](https://github.com/github/gh-aw/blob/ff2eccd10a30d6a7bfaf0da449194e907a206555/docs/src/content/docs/reference/faq.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: a prompt or static config alone would not establish S5. The positive mapping rests on the parent-owned authoritative amendment plus the documented runtime reload that returns the changed purpose/policy into subsequent operation. Run-scoped steering and generic write approvals are current-control/authorization mechanisms and are not used as the S5 witness.

## Recursion

A repository can contain several compiled agentic workflows, and an orchestrator workflow can dispatch/call worker workflows. Such nesting is not automatically VSM recursion. This assessment credits a repository-level `gh-aw` work organization where individual model-driven runs/worker workflows own separable operational outcomes and the surrounding first-party compiler/runtime supplies coordination, current regulation, complementary audit and parent-governed purpose return. A downstream adopter that composes a different organization around `gh-aw` is a separate system-in-focus requiring its own evidence.

## Variety and escalation

`gh-aw` attenuates operational variety through tool/permission/network restriction, bounded AI-credit use, concurrency groups, sandboxing and structured safe-output envelopes. S2-specific contention is handled before or around S1 execution rather than delegated to the worker model. Threat findings escalate from the ordinary producer path into a complementary detection job before privileged mutation. Identity-level change remains with repository parent authority and returns through the runtime-loaded workflow body. These mechanisms do not imply that every constraint is S3 or every human approval is S5; each positive mapping above uses its own function-specific closure.

## Evidence gaps

- No reviewed public upstream result at the frozen revision directly measures `gh-aw`'s native S2 disturbance-to-attenuation capability under a comparable cross-harness benchmark cell; the concurrency evidence is mechanism evidence for the standalone assessment, not a capability-depth observation.
- No complete first-party parent S3 loop was credited. Human steering, environment approvals and organization variables were inspected but did not establish the required whole-system current-view/discretionary-return chain at this boundary.
- Threat-detection independence is structural/job-context independence, not a claim that producer and detector model failures are statistically independent when they use the same engine family.
- The repository contains extensive experimental and dogfood improvement machinery, but no standard-distribution S4 closure was established without importing adjacent project-maintenance activity.
- S5 parent ownership is established from authoritative source amendment and runtime return; no autonomous or constructor-owned ultimate-policy mode is credited.