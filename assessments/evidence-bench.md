---
harness_id: evidence-bench
project_name: Evidence Bench
repository: https://github.com/kstawiski/evidence-gated-scientific-agent
review_ref: 85b396a824dfad6ec0880cbe07d86d3e24920ae8
reviewed_at: 2026-10-17
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: C
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Evidence Bench

## Review boundary

- System in focus: Shipped first-party Python evidence-gated scientific research organization: ADK-based dual-proposer planning and synthesis; first-party `run_scientific_task` controller; model researcher/reporter and optional evidence/computation tools; independent model plan/report/visual critics; deterministic scientific validation, bounded remediation attempts and final supported/inconclusive/needs-human disposition. The recursion is one complete multi-stage scientific study/run, not the laboratory/company owning it.
- Purpose and identity: Generate evidence-grounded scientific plans, analysis/computation and reports without admitting unsupported source claims, computed results or figures; correct challenged plans/reports or retain unresolved findings.
- Relevant environment: User's research problem, source articles, workspace files, scientific/visual evidence, experiment/computation artifacts, configured Qwen/Gemma inference, optional external MCP/browser/package tools, human adjudication for residual uncertainty.
- Standard-distribution boundary: Runnable first-party `scientific_agent/orchestrator.py` with CLI/web/A2A caller and installed ADK planning workflow. The essential model/tool feedback, budget/phase control and Gemma review-return are in source; don't credit model-serving internals, hosted third-party tools, external source repositories, publication claims or evaluation scorecards.
- Credited operating / distribution surfaces: [scientific_agent/orchestrator.py](https://github.com/kstawiski/evidence-gated-scientific-agent/blob/85b396a824dfad6ec0880cbe07d86d3e24920ae8/scientific_agent/orchestrator.py); [scientific_agent/workflow.py](https://github.com/kstawiski/evidence-gated-scientific-agent/blob/85b396a824dfad6ec0880cbe07d86d3e24920ae8/scientific_agent/workflow.py); [scientific_agent/runtime.py](https://github.com/kstawiski/evidence-gated-scientific-agent/blob/85b396a824dfad6ec0880cbe07d86d3e24920ae8/scientific_agent/runtime.py); [scientific_agent/config.py](https://github.com/kstawiski/evidence-gated-scientific-agent/blob/85b396a824dfad6ec0880cbe07d86d3e24920ae8/scientific_agent/config.py); [scientific_agent/prompts.py](https://github.com/kstawiski/evidence-gated-scientific-agent/blob/85b396a824dfad6ec0880cbe07d86d3e24920ae8/scientific_agent/prompts.py); [scientific_agent/policy.py](https://github.com/kstawiski/evidence-gated-scientific-agent/blob/85b396a824dfad6ec0880cbe07d86d3e24920ae8/scientific_agent/policy.py); [scientific_agent/execution.py](https://github.com/kstawiski/evidence-gated-scientific-agent/blob/85b396a824dfad6ec0880cbe07d86d3e24920ae8/scientific_agent/execution.py); [scientific_agent/linting.py](https://github.com/kstawiski/evidence-gated-scientific-agent/blob/85b396a824dfad6ec0880cbe07d86d3e24920ae8/scientific_agent/linting.py); [scientific_agent/literature.py](https://github.com/kstawiski/evidence-gated-scientific-agent/blob/85b396a824dfad6ec0880cbe07d86d3e24920ae8/scientific_agent/literature.py); [scientific_agent/provenance.py](https://github.com/kstawiski/evidence-gated-scientific-agent/blob/85b396a824dfad6ec0880cbe07d86d3e24920ae8/scientific_agent/provenance.py); [scientific_agent/cli.py](https://github.com/kstawiski/evidence-gated-scientific-agent/blob/85b396a824dfad6ec0880cbe07d86d3e24920ae8/scientific_agent/cli.py); [scientific_agent/web/service.py](https://github.com/kstawiski/evidence-gated-scientific-agent/blob/85b396a824dfad6ec0880cbe07d86d3e24920ae8/scientific_agent/web/service.py); [scientific_agent/schemas.py](https://github.com/kstawiski/evidence-gated-scientific-agent/blob/85b396a824dfad6ec0880cbe07d86d3e24920ae8/scientific_agent/schemas.py).
- Adjacent first-party surfaces excluded from ownership: Benchmark `evals/` outputs are evidence about testing rather than direct ownership; packaged container/MCP/analysis backends are tools, not borrowed S3/S5 operators; third-party Qwen/Gemma providers and research literature not imported as internal policy/research organizations.
- First-party operating / deployment modes considered: Default two-branch Qwen/Gemma plan mode; opt-in simple-mode single Qwen plan plus Gemma audit; model researcher/reporter, requested optional code sandbox and search/literature tools; plan/verification fail-closed or inconclusive and bounded repair; report and multimedia audit; optional revisions preserving parent provenance.
- Recursion level: One scientific research run containing multiple first-party model-producing/specialist operations: independent plan generation, report/research execution, separately scoped model criticism, and constructor controller regulation over these current commitments.
- Reviewed revision: `85b396a824dfad6ec0880cbe07d86d3e24920ae8`, frozen #186, batch #1648 row 6.
- Observation date: 2026-10-17.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The source-owned entry `run_scientific_task` instantiates a current-run `ResearchBudgetController`, event ledger, workspace/input manifest and task evidence snapshot. It asks the installed ADK workflow for planning: Qwen and Gemma generate independent plan proposals and a Qwen synthesizer produces a MasterPlan, which is bound to the original task and subject to source-level deterministic plan lint plus separately requested Gemma plan audit. The controller re-prompts a plan repairer with **blocking review and lint findings**, or halts before research if the protocol is unsupported. This is a real first-party division of current task work, not a brochure diagram. [scientific_agent/orchestrator.py](https://github.com/kstawiski/evidence-gated-scientific-agent/blob/85b396a824dfad6ec0880cbe07d86d3e24920ae8/scientific_agent/orchestrator.py); [scientific_agent/workflow.py](https://github.com/kstawiski/evidence-gated-scientific-agent/blob/85b396a824dfad6ec0880cbe07d86d3e24920ae8/scientific_agent/workflow.py).

When planning passes, `_produce_report` instantiates configurable ADK model/tool research from workspace, literature, knowledge and optional Python/R sandbox tools. First-party `ToolPolicy`, `ScientificToolOrderGate` and `ResearchBudgetController` enforce admissible operations, source/evidence ordering, model-turn and tool-call counts outside the model's own discretion. Model research/reporting and optional programmatic computation thus form source-wired S1 action/evidence-return loops, not only hard-coded fixed research steps. [scientific_agent/orchestrator.py](https://github.com/kstawiski/evidence-gated-scientific-agent/blob/85b396a824dfad6ec0880cbe07d86d3e24920ae8/scientific_agent/orchestrator.py); [scientific_agent/runtime.py](https://github.com/kstawiski/evidence-gated-scientific-agent/blob/85b396a824dfad6ec0880cbe07d86d3e24920ae8/scientific_agent/runtime.py); [scientific_agent/policy.py](https://github.com/kstawiski/evidence-gated-scientific-agent/blob/85b396a824dfad6ec0880cbe07d86d3e24920ae8/scientific_agent/policy.py); [scientific_agent/execution.py](https://github.com/kstawiski/evidence-gated-scientific-agent/blob/85b396a824dfad6ec0880cbe07d86d3e24920ae8/scientific_agent/execution.py).

After the first report, controller `validate_report` checks source artifacts/provenance, citations, scientific outputs and deterministic report rules, while the **separately instructed Gemma reviewer** receives the actual master plan, resulting scientific report, deterministic validation, retrieval/computation evidence and controller artifacts. For applicable figures and tables the auditor can independently inspect multimodal display inputs. `_needs_repair` turns a failing audit or blocking evidence validation into actual bounded production re-entry; subsequent `_produce_report` receives the critic's findings, previous report and gathered evidence. If the repair loop fails or its budget runs out, unresolved findings are retained and final status becomes `inconclusive`, `requires_more_evidence` or `requires_human_decision`; it does not silently certify a rejected report. This supplies a complementary S3* audit-return path under declared evidence limits. [scientific_agent/orchestrator.py](https://github.com/kstawiski/evidence-gated-scientific-agent/blob/85b396a824dfad6ec0880cbe07d86d3e24920ae8/scientific_agent/orchestrator.py); [scientific_agent/linting.py](https://github.com/kstawiski/evidence-gated-scientific-agent/blob/85b396a824dfad6ec0880cbe07d86d3e24920ae8/scientific_agent/linting.py); [scientific_agent/workflow.py](https://github.com/kstawiski/evidence-gated-scientific-agent/blob/85b396a824dfad6ec0880cbe07d86d3e24920ae8/scientific_agent/workflow.py).

The service supports optional tool-set choices and task revision without handing the Qwen researcher authority to remove the controller's validation, risk/profile locks, execution budget, source integrity checks or final disposition. These are constructor-controlled **inside-and-now** workload commitments across planning, research, independent audit and repair. `simple_mode` changes how a plan is proposed, not the structural requirement to check its evidence. External literature gathering is research for a current scientific objective, not itself a future-oriented adaptation of the organization's ongoing capacities. Neither operational ethics/policy governance nor an ultimate S5 institution-level settlement loop appears in reviewed first-party controller code.

## S1 — Operations

- State: A
- Function: Perform research, produce a plan/report and generate grounded scientific evidence through actual model-directed source/tool interaction.
- Disturbance / variety regulated: Uncertain scientific question, varying source data and code results, inconsistent literature, missing provenance and model hallucinations.
- Decisive decision or feedback right: Qwen/Gemma planning models develop concrete alternative scientific plans, synthesizer selects a MasterPlan; first-party model researcher and reporter take bounded retrieval/computation/tool steps to produce a scientific report. Repair models use new observed findings to generate next revised outputs.
- Decision owner: First-party ADK/model role logic invoked by `run_scientific_task`; external inference is a configured backend, not an outside authored research operator.
- Supporting / enforcement mechanisms: Plan proposal/research/report prompts, ADK workflow, scientific ToolPolicy, retrieval evidence ledger, typed computation tools and deterministic lints.
- Closure path: objective/inputs → independent model plan candidates and auditable master → model/tool research and computation observations → model report with cited outputs → critique feedback → model repair/new report.
- Boundary reachability: The shipped orchestrator's `run_scientific_task` calls `build_planning_workflow` / `run_typed`, then `_produce_report`, which creates configured first-party ADK research/report toolsets. The same entry is reached through exported `run` and services.
- Why this is / is not agent-owned: Model planners/researchers select substantive plan/evidence and responsive report/repair content from observed sources and tool results; static control and policy guardrails are separate.
- Evidence: [scientific_agent/workflow.py](https://github.com/kstawiski/evidence-gated-scientific-agent/blob/85b396a824dfad6ec0880cbe07d86d3e24920ae8/scientific_agent/workflow.py); [scientific_agent/orchestrator.py](https://github.com/kstawiski/evidence-gated-scientific-agent/blob/85b396a824dfad6ec0880cbe07d86d3e24920ae8/scientific_agent/orchestrator.py); [scientific_agent/runtime.py](https://github.com/kstawiski/evidence-gated-scientific-agent/blob/85b396a824dfad6ec0880cbe07d86d3e24920ae8/scientific_agent/runtime.py); [scientific_agent/execution.py](https://github.com/kstawiski/evidence-gated-scientific-agent/blob/85b396a824dfad6ec0880cbe07d86d3e24920ae8/scientific_agent/execution.py).
- Basis: Reachable source-level model/tool/evidence-feedback implementation.
- Confidence: High on installed loops, not measured scientific correctness or model inference.
- Caveats: Actual Qwen/Gemma backend and any enabled optional code or MCP tools must be configured; benchmarking claims not imported.


## S2 — Coordination

- State: —
- Function: No demonstrated control attenuating a material inter-S1 operational collision rather than merely collecting parallel proposals and sequencing task stages.
- Disturbance / variety regulated: Two planners may provide different suggestions, but they have no shared mutable working target or independently competing active operational commitment requiring stabilization.
- Decisive decision or feedback right: Qwen synthesizes proposals into one plan; deterministic serial stage/gates select what comes next. Neither path detects and resolves interference among independent ongoing S1 operations.
- Decision owner: Planning join/synthesizer and single-run controller.
- Supporting / enforcement mechanisms: ADK max_concurrency=2 parallel planner generation, JoinNode, typed candidate collection, and final deterministic lint.
- Closure path: Two plan alternatives → synthesis → master plan, which is task content formation. There is no distinct operating-unit clash → anti-interference choice → changed sibling activity feedback documented.
- Why this is / is not agent-owned: A comparison of concurrently generated plans, their disagreement and synthesis is not by itself a Beer S2 loop, nor do research budgets alone prove inter-S1 mutual correction.
- Evidence: [scientific_agent/workflow.py](https://github.com/kstawiski/evidence-gated-scientific-agent/blob/85b396a824dfad6ec0880cbe07d86d3e24920ae8/scientific_agent/workflow.py); [scientific_agent/orchestrator.py](https://github.com/kstawiski/evidence-gated-scientific-agent/blob/85b396a824dfad6ec0880cbe07d86d3e24920ae8/scientific_agent/orchestrator.py); [scientific_agent/policy.py](https://github.com/kstawiski/evidence-gated-scientific-agent/blob/85b396a824dfad6ec0880cbe07d86d3e24920ae8/scientific_agent/policy.py).
- Basis: Bounded negative assessment of candidate planning/phase-control mechanisms.
- Confidence: Medium: deliberate independent planning and synthesis is source-real, but no specific inter-S1 disturbance/attenuation contract was found.
- Caveats: A deployment with multiple simultaneous runs may add coordination in a separate server layer; not credited without source proof for the assessed run.

### Absence scope

- Surfaces inspected: ADK branch-a/branch-b plan generation, JoinNode/synthesizer, phase controller, tool budget and sandbox output rules.
- Plausible first-party paths checked: Parallel planner debate, plan lint, task phase sequencing, centralized resource limits, per-attempt output workspaces.
- Why no material first-party path remains: Candidate mechanisms make the current scientific plan admissible or limit one task, but do not demonstrate self-other operational interference and a correction return between active S1 work streams.


## S3 — Inside-and-now control

- State: C
- Function: Whole-current scientific run control: when plans are accepted, which research/evidence/critique phase may proceed, how scarce model/tool/repair attempts are budgeted and when final outputs are supported or withheld.
- Disturbance / variety regulated: Unreliable plans, unsupported evidence, unbounded tool/model calls, failing audit findings, code/tool nonprogress and bounded available repair resources.
- Decisive decision or feedback right: `run_scientific_task` orchestrates planning/admissibility, reassigns rejected plans to repair, conditionally admits research, enforces research budgets, orders deterministic validation and independent reviewer, initiates limited repair, and sets final status rather than promoting rejected reports.
- Decision owner: First-party deterministic Python controller and configured `ResearchBudgetController`, not autonomous scientific principal or another model owning organization-wide allocation.
- Supporting / enforcement mechanisms: Planning.status, MaxRepairRounds, ToolPolicy, sandbox restrictions, deterministic lints, evidence/provenance ledger, `_needs_repair` and `_final_run_status`.
- Closure path: Current plan/evidence/critic state and resource use → controller selects stop, execute next unit or bounded repair → new operations/results → updated audit+status → repeat or present final result/needs-human with recorded reasons.
- Whole-system current view: Active master plan, model research state, evidence/retrieval and computation, deterministic validity, separate audit report, cumulative tool counts and attempts across one full scientific run.
- Current-control decision scope: The constructor controls operational commitments of specialized planning, research/reporting, critique and revision operations, their admissibility and their shared run budget.
- Boundary reachability: `run_scientific_task` allocates ResearchBudgetController, executes `prepare_and_audit_plan`, checks `planning.status` before `_produce_report`, validates outputs, invokes independent report review and loops repairs while `_needs_repair` and the configured round cap hold; `_final_run_status` controls final admission.
- Why this is / is not agent-owned: Decisive phase/budget/stop choices are expressed by static controller rules rather than a free model explicitly managing whole-current resource allocation; S3=C, not S3=A.
- Evidence: [scientific_agent/orchestrator.py](https://github.com/kstawiski/evidence-gated-scientific-agent/blob/85b396a824dfad6ec0880cbe07d86d3e24920ae8/scientific_agent/orchestrator.py); [scientific_agent/workflow.py](https://github.com/kstawiski/evidence-gated-scientific-agent/blob/85b396a824dfad6ec0880cbe07d86d3e24920ae8/scientific_agent/workflow.py); [scientific_agent/policy.py](https://github.com/kstawiski/evidence-gated-scientific-agent/blob/85b396a824dfad6ec0880cbe07d86d3e24920ae8/scientific_agent/policy.py); [scientific_agent/config.py](https://github.com/kstawiski/evidence-gated-scientific-agent/blob/85b396a824dfad6ec0880cbe07d86d3e24920ae8/scientific_agent/config.py).
- Basis: Source-attested current-commitment controller with feedback from multiple first-party operating roles.
- Confidence: High for constructor current-run regulation; no external scientific-team budget governance claimed.
- Caveats: Single-run scope is not project portfolio governance, and some phases use the same model provider for different prompts.


## S3* — Complementary audit

- State: A
- Function: Independently challenge active research plan and report claims from an alternative model/evidence path, with critic findings feeding real repair or an unresolved stop.
- Disturbance / variety regulated: Unsound scientific plans, citations without source support, fabricated computation values, contradictory data/display, incorrect visual readings and unsupported final conclusions.
- Decisive decision or feedback right: A separately instructed Gemma `PLAN_AUDITOR` audits the Qwen-generated MasterPlan; independent `REPORT_AUDITOR` evaluates claimed results against retrieved/computed artifact evidence and deterministic validation, while visual review can inspect actual figure/table pixel inputs. Critic verdict/blocking findings can force a repair or prevent supported terminal status.
- Decision owner: First-party distinct model-based Gemma critic invocation and structured VerificationReport judgment; constructor separately validates/reconciles the critic's outputs and commits control transitions.
- Supporting / enforcement mechanisms: Plan audit packet with independently generated checklist, retrieval/computation evidence, detached visual bytes, deterministic validators, unique audit artifacts and bounded repair envelopes.
- Closure path: Qwen plan/report claim → independent Gemma plan/report/artifact review → structured blocking/nonblocking findings → controller's `planning_status` or `_needs_repair` chooses repair/withholding → revised plan/report and re-audit → supported/needs-human termination.
- Claim being audited: Whether the plan's scientific method is admissible and whether report conclusions/displays are justified by gathered evidence.
- Ordinary reporting path: Qwen research/reporter structured scientific report, planned steps and source/output claims.
- Complementary access path: Gemma uses separately instructed audit prompts and controller-provided source/compute/citation/validation evidence plus actual rasterized displays, rather than merely accepting report narrative or self-score.
- Independence boundary: Distinct model-critic role and alternative evidence/report read path; not a different OS trust domain, protected human team or globally independent provider. Strictly bounded to enabled first-party run configuration.
- Who acts on findings: Constructor `prepare_and_audit_plan` and report repair loop consume Gemma's verdict and findings; `_repair_plan`/ `_produce_report` receive them, final `_final_run_status` refuses `supported` unless independent review is passing.
- Boundary reachability: `build_planning_workflow` invokes `audit_master_plan` on the actual master, and `run_scientific_task` invokes `_audit_report_resilient` on the actual report/retrieval/computation. `planning_status`, `_needs_repair` and final status consume those outcomes to change installed execution, not merely save benchmark scores.
- Why this is / is not agent-owned: The alternative critical reading and structured falsification findings are selected by a model with separate audit instructions and evidence packet; deterministic controller owns repair scheduling/format admission but not the semantic critic judgment. S3*=A, not just C.
- Evidence: [scientific_agent/workflow.py](https://github.com/kstawiski/evidence-gated-scientific-agent/blob/85b396a824dfad6ec0880cbe07d86d3e24920ae8/scientific_agent/workflow.py); [scientific_agent/orchestrator.py](https://github.com/kstawiski/evidence-gated-scientific-agent/blob/85b396a824dfad6ec0880cbe07d86d3e24920ae8/scientific_agent/orchestrator.py); [scientific_agent/prompts.py](https://github.com/kstawiski/evidence-gated-scientific-agent/blob/85b396a824dfad6ec0880cbe07d86d3e24920ae8/scientific_agent/prompts.py); [scientific_agent/linting.py](https://github.com/kstawiski/evidence-gated-scientific-agent/blob/85b396a824dfad6ec0880cbe07d86d3e24920ae8/scientific_agent/linting.py).
- Basis: Source-reachable independent critic alternate evidence with actual correction-return and bounded blocking.
- Confidence: High for model-based audit and repair wiring, medium for effectiveness of critic independence and coverage.
- Caveats: On model outage or exhaustion the controller can return inconclusive/needs-human rather than supported. Model critic has its own error modes and deterministic checks sometimes reject contradictory critic instructions.


## S4 — Outside-and-then intelligence

- State: —
- Function: No established prospective external strategic adaptation of the scientific *organization's own future capability* returned into whole-current S3.
- Disturbance / variety regulated: Scientific literature discoveries, new input datasets and computational results are changing task environment, but are handled as evidence for the *present user research question*.
- Decisive decision or feedback right: The agents retrieve literature and propose revised scientific methods, yet no first-party function evaluates externally changing opportunities or future organizational capabilities and installs a choice back into ongoing scientific-agent governance.
- Decision owner: Model research/plan production and constructor task validation, not a separate future-capability adaptation function.
- Supporting / enforcement mechanisms: Literature acquisition, knowledge library, revision tasks, plan synthesis/repair, model and tool configuration.
- Closure path: External paper/data → current study evidence/plan → accepted report or within-task repair. No organizational environment foresight → comparative capability options → enduring adaptation choice → current S3 return.
- Why this is / is not agent-owned: Scientific research may explore future hypotheses, but that is S1 work for a requested scientific study, not automatic evidence of this harness changing its own future operational repertoire.
- Evidence: [scientific_agent/literature.py](https://github.com/kstawiski/evidence-gated-scientific-agent/blob/85b396a824dfad6ec0880cbe07d86d3e24920ae8/scientific_agent/literature.py); [scientific_agent/workflow.py](https://github.com/kstawiski/evidence-gated-scientific-agent/blob/85b396a824dfad6ec0880cbe07d86d3e24920ae8/scientific_agent/workflow.py); [scientific_agent/orchestrator.py](https://github.com/kstawiski/evidence-gated-scientific-agent/blob/85b396a824dfad6ec0880cbe07d86d3e24920ae8/scientific_agent/orchestrator.py); [scientific_agent/knowledge.py](https://github.com/kstawiski/evidence-gated-scientific-agent/blob/85b396a824dfad6ec0880cbe07d86d3e24920ae8/scientific_agent/knowledge.py).
- Basis: Bounded negative review of strongest apparent prospective literature and revision flows.
- Confidence: Medium-high within one-run recursion.
- Caveats: External researchers/operators can improve prompts/tools in later repository revisions; those human activities are outside the reviewed deployed agent organization.

### Absence scope

- Surfaces inspected: Literature/knowledge acquisition, planning alternatives, repair/revision logic, environment provisioning and model choice settings.
- Plausible first-party paths checked: Parallel hypothesis planning, scientific paper search, future relevance of sources, report revision and package/tool support.
- Why no material first-party path remains: All candidate paths serve the current user's scientific problem and locked method; no demonstrated strategic capability-development option and two-way S3 return for the harness itself.


## S5 — Policy and identity

- State: —
- Function: No owned ultimate policy/identity/ethos settlement path distinguished from fixed scientific integrity and tool safety rules.
- Disturbance / variety regulated: Scientific risk labels, provenance obligations, tool permissions, domain/language constraints, evaluation failure and human reconsideration.
- Decisive decision or feedback right: Task requester and first-party configured controller impose a risk-sensitive scientific protocol and locked task constraints; on exhausted attempts the controller reports `requires_human_decision`, but it does not adjudicate ultimate organization identity/policy conflicts.
- Decision owner: Human scientific owner outside runtime for ultimate risk and approval; fixed first-party admission rules for current-run integrity.
- Supporting / enforcement mechanisms: MasterPlan/task protocol binding, ToolPolicy, static scientific safety rules, sandbox defaults, provenance manifest and risk classifications.
- Closure path: Inputs/risk constraints → fixed scientific gate and possible human escalation. No first-party policy dispute → ultimate legitimate purpose/ethos decision → binding return to organizational governance.
- Why this is / is not agent-owned: Fail-closed status, provenance hashes, immutable task locks and user escalation are robust current-run controls, not a system deciding its ultimate goals.
- Evidence: [scientific_agent/workflow.py](https://github.com/kstawiski/evidence-gated-scientific-agent/blob/85b396a824dfad6ec0880cbe07d86d3e24920ae8/scientific_agent/workflow.py); [scientific_agent/orchestrator.py](https://github.com/kstawiski/evidence-gated-scientific-agent/blob/85b396a824dfad6ec0880cbe07d86d3e24920ae8/scientific_agent/orchestrator.py); [scientific_agent/policy.py](https://github.com/kstawiski/evidence-gated-scientific-agent/blob/85b396a824dfad6ec0880cbe07d86d3e24920ae8/scientific_agent/policy.py); [docs/MVP_SCOPE.md](https://github.com/kstawiski/evidence-gated-scientific-agent/blob/85b396a824dfad6ec0880cbe07d86d3e24920ae8/docs/MVP_SCOPE.md).
- Basis: Bounded negative review of policy/risk/identity surfaces.
- Confidence: Medium-high.
- Caveats: A human scientific review board may have ultimate policy authority outside this product; no inherited S5 parent relation is scored without a first-party exposed closing loop.

### Absence scope

- Surfaces inspected: Input risk classifier, bind_controller_task, plan validation, ToolPolicy budgets/sandbox gates, status requires_human_decision and repository ethics statements.
- Plausible first-party paths checked: Scientific safety/admissibility contracts, forbidden tool calls, irreversible code execution, repair-budget exhaustion and human escalation.
- Why no material first-party path remains: The controller enforces prechosen task/risk rules and defers unresolved science; it does not possess a distinct recurring ultimate identity/values arbitration and authority-return path.


## Distributed OSS parent arrangement

The source can be used by a human researcher/lab, Qwen/Gemma model providers and optional external search/MCP/computational infrastructure. These are different decision owners. Configured agents and controller regulate one scientific workflow; no first-party authority to change the institution's ultimate research agenda is demonstrated. The provenance ledger records source/evidence identity but does not become S5.

## Self-hosted and non-human modes

The user may run configured Qwen/Gemma endpoints, offline sandboxed Python/R tools (explicitly enabled), separate package-worker, optional MCP and web/A2A interfaces. Run budgeting, evidence admission and critic reruns are first-party even when inference is remote. The model critic is a distinct prompt/model path, not guaranteed independent cloud trust hardware. Unsupported plans/reports can be returned unresolved rather than falsely admitted.

## Recursion

At one scientific-study recursion, specialized plan/research/report roles are operational producers; a deterministic whole-run controller regulates current phase and budgets; a distinct Gemma critic obtains evidence separate from first-party self-reporting and returns blocking findings. The independent parallel planners produce alternative proposals without evidenced inter-S1 anti-interference closure. No strategic organizational S4 or ultimate identity S5 is inherited from research domain goals.

## Variety and escalation

Variety is amplified through model literature retrieval, alternative planning and guarded execution; attenuated through independent criticism, deterministic source/provenance gates, bounded budgets and repair convergence checks. Nonconforming claims trigger repair or unresolved status; the controller does not force a scientific conclusion merely to finish.

## Evidence gaps

- This is a first-party source review at a pinned frozen SHA; no real Qwen/Gemma inference, code sandbox, scientific experiment or scientific efficacy benchmark was run.
- S3=C means constructor controls **this run's current specialized operations**; it does not prove an autonomous lab-wide supervisory manager or research portfolio control.
- S3*=A includes model-authored verification judgment fed by genuine separate evidence, but does not claim a different secure compute tenancy, human reviewer signoff or exact empirical critic performance.
- Parallel independent planners and plan synthesis are not by themselves a concrete S2 inter-operational interference regulator. Future first-party collision evidence could change this negative state.
- External scientific literature/knowledge search serves S1 current study; future model/skill development or institutional ethics authority are outside this run's S4/S5.
