---
harness_id: voly
project_name: VOLY
repository: https://github.com/voly-codes/voly
review_ref: d21dab640647ca5a0a096e12b01a9a3a4f7432af
reviewed_at: 2026-10-31
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: C
autonomy_s5: —
---

# VOLY

## Review boundary

- System in focus: self-hosted VOLY open-core SDK, local A2A execution/control pipeline and exposed capability-adaptation constructor surfaces.
- Purpose and identity: execute governed agent work with explicit evidence, executor/model routing, safety/cost control and measured capability options.
- Relevant environment: project/source/workspaces, provider endpoints, external coding executors and external capability-pack sources; human operator and local outcome evidence.
- Standard-distribution boundary: published voly Python package, supported Agent/Workflow SDK, local A2A pipeline and capability/evaluation CLI/API at the exact frozen revision.
- Credited operating / distribution surfaces: owned SDK tool loop, actual same-cwd lock integration, opt-in required-mode agentic judge and function-specific staged/evaluated capability interfaces.
- Adjacent first-party surfaces excluded from ownership: commercial voly-cloud, product demo/benchmark output, tests as autonomous actors, projects/ dogfood organizations, Headroom internals and remote Cloudflare publication as local activation. External CLI internal organization is not imported.
- First-party operating / deployment modes considered: SDK chat/tool mode, executor and hybrid local A2A, configured lead mode, shadow/required judge, capability pack/evaluated/learning/sensing modes and self-hosted operator approvals.
- Recursion level: one open-core installation coordinating local runs; tool/workflow agents are operational cells, external products remain dependencies.
- Reviewed revision: `voly-codes/voly@d21dab640647ca5a0a096e12b01a9a3a4f7432af`; immutable intake #2446 / serial controller #2447; historical #201 pin preserved.
- Observation date: 2026-10-31.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[README.md](https://github.com/voly-codes/voly/blob/d21dab640647ca5a0a096e12b01a9a3a4f7432af/README.md); [pyproject.toml](https://github.com/voly-codes/voly/blob/d21dab640647ca5a0a096e12b01a9a3a4f7432af/pyproject.toml) market a control plane, but the actual [voly/sdk/agent.py](https://github.com/voly-codes/voly/blob/d21dab640647ca5a0a096e12b01a9a3a4f7432af/voly/sdk/agent.py); [voly/sdk/tools.py](https://github.com/voly-codes/voly/blob/d21dab640647ca5a0a096e12b01a9a3a4f7432af/voly/sdk/tools.py) also implement a bounded first-party model-selected allowlisted tool loop with tool observations returned to subsequent model calls. This establishes S1 independently of wrapped coding CLI internals. Workflow/Plan state persists execution, dependencies, approval/cancellation and restart. [voly/a2a/lead.py](https://github.com/voly-codes/voly/blob/d21dab640647ca5a0a096e12b01a9a3a4f7432af/voly/a2a/lead.py); [voly/a2a/hybrid.py](https://github.com/voly-codes/voly/blob/d21dab640647ca5a0a096e12b01a9a3a4f7432af/voly/a2a/hybrid.py); [voly/a2a/cwd_lock.py](https://github.com/voly-codes/voly/blob/d21dab640647ca5a0a096e12b01a9a3a4f7432af/voly/a2a/cwd_lock.py) assign roles/tiers, call executors and serialize file-writing runs on a shared working tree.

[voly/pipeline/stages_a2a.py](https://github.com/voly-codes/voly/blob/d21dab640647ca5a0a096e12b01a9a3a4f7432af/voly/pipeline/stages_a2a.py); [voly/a2a/agentic_judge.py](https://github.com/voly-codes/voly/blob/d21dab640647ca5a0a096e12b01a9a3a4f7432af/voly/a2a/agentic_judge.py) wire a separate optional read-only judge after ordinary role execution. Required mode can downgrade the accepted pipeline result; shadow mode only records. [voly/capability/packs.py](https://github.com/voly-codes/voly/blob/d21dab640647ca5a0a096e12b01a9a3a4f7432af/voly/capability/packs.py); [voly/capability/evaluated_packs.py](https://github.com/voly-codes/voly/blob/d21dab640647ca5a0a096e12b01a9a3a4f7432af/voly/capability/evaluated_packs.py); [voly/cli/commands/capability_evaluated_cmd.py](https://github.com/voly-codes/voly/blob/d21dab640647ca5a0a096e12b01a9a3a4f7432af/voly/cli/commands/capability_evaluated_cmd.py) expose staged external guidance, outcome measurements, activation/retirement decisions and bounded checksum-verified variant rendering. Whole-tree call-site inspection finds EvaluatedPackRouter/render_variant_task used by the capability CLI/API/probe surfaces, not automatically consumed by the ordinary A2A/SDK task route. Generic capability_route uses the separate CapabilityRegistry/ExecutorMatcher. [voly/sensing/interpret.py](https://github.com/voly-codes/voly/blob/d21dab640647ca5a0a096e12b01a9a3a4f7432af/voly/sensing/interpret.py); [voly/decisions.py](https://github.com/voly-codes/voly/blob/d21dab640647ca5a0a096e12b01a9a3a4f7432af/voly/decisions.py) implement RSS signal/options and human-approved business actions; this is not assumed to be adaptation of the harness. Apache-2.0 applies to the open core.

## Operational model

The first-party operational agent loop is credited at its explicit SDK mode. Local code-writing executors are dependencies invoked by an owned workflow; their internal metasystem is not borrowed. Shared-cwd exclusion is real conflict-specific coordination support, but discretionary coordination still needs composition. The extra judge can challenge the whole solver episode beyond normal role reporting. Capability adoption provides an S4-specific constructor with an identified integration boundary, not an autonomously closed live learning loop.

## S1 — Operations

- State: A
- Function: Deliver task outcomes through the shipped SDK model/tool/observation loop.
- Disturbance / variety regulated: Ambiguous user task, tool choice, tool failures and returned observations.
- Decisive decision or feedback right: Model selects the next registered tool/arguments and completion response within a bounded task.
- Decision owner: The Agent SDK model actor in chat/tool mode.
- Supporting / enforcement mechanisms: AIGateway transport, named tool allowlist/registry, max_tool_steps, telemetry and typed result.
- Closure path: Agent._run_chat obtains tool_calls → invokes resolved allowed tool → appends result/error observations to messages → calls the model again.
- Boundary reachability: Public Agent(tools=[...]) resolves registered tools and runs _run_chat through the supported SDK; external model API is inference transport, and no external CLI metasystem is needed for this witness.
- Why this is / is not agent-owned: This source owns the loop rather than only forwarding an external coding CLI. Deterministic limits and tool execution do not own semantic action selection.
- Evidence: [voly/sdk/agent.py](https://github.com/voly-codes/voly/blob/d21dab640647ca5a0a096e12b01a9a3a4f7432af/voly/sdk/agent.py); [voly/sdk/tools.py](https://github.com/voly-codes/voly/blob/d21dab640647ca5a0a096e12b01a9a3a4f7432af/voly/sdk/tools.py); [voly/ai_gateway/providers.py](https://github.com/voly-codes/voly/blob/d21dab640647ca5a0a096e12b01a9a3a4f7432af/voly/ai_gateway/providers.py); [docs/backend/sdk.md](https://github.com/voly-codes/voly/blob/d21dab640647ca5a0a096e12b01a9a3a4f7432af/docs/backend/sdk.md)
- Basis: structural
- Confidence: high
- Caveats: Source-based boundary judgment; no live model or production effectiveness claim.

## S2 — Coordination

- State: C
- Function: Attenuate destructive interference between concurrent file-writing runs sharing one cwd.
- Disturbance / variety regulated: Independent run outcomes can mix file edits/git deltas on one project tree.
- Decisive decision or feedback right: A coordination policy must choose/revise lock scope/admission/conflict response; shipped code supplies the specific exclusion and release path.
- Decision owner: Developer/operator selects shared-cwd policy; no autonomous coordination actor is assembled.
- Supporting / enforcement mechanisms: cwd_executor_lock exclusive filesystem acquisition, stale-owner handling, timeout and finally release, integrated around hybrid executor calls.
- Closure path: A writing run acquires lock → contender waits or times out → release/stale recovery permits its later execution, separating file-change evidence.
- Boundary reachability: make executor-runner path in hybrid.py enters cwd_executor_lock around AgentRunner.run. It is shipped integration, not an unwired lock example.
- Why this is / is not agent-owned: The conflict-specific function is implemented, but deterministic waiting and lock enforcement are not autonomous decision ownership; autonomous regulatory response would still need composition.
- Evidence: [voly/a2a/cwd_lock.py](https://github.com/voly-codes/voly/blob/d21dab640647ca5a0a096e12b01a9a3a4f7432af/voly/a2a/cwd_lock.py); [voly/a2a/hybrid.py](https://github.com/voly-codes/voly/blob/d21dab640647ca5a0a096e12b01a9a3a4f7432af/voly/a2a/hybrid.py); [tests/test_cwd_lock.py](https://github.com/voly-codes/voly/blob/d21dab640647ca5a0a096e12b01a9a3a4f7432af/tests/test_cwd_lock.py)
- Basis: structural
- Confidence: medium
- Caveats: Lock-file mkdir/open OSError paths log and yield without locking. This is a conditional supported exclusion path, not a universal fail-closed isolation guarantee; a focused source-native two-thread exercise passed.
- Distinct S1 units: independently executing project-work run cells whose file-capable agents produce different requested outcomes.
- Inter-S1 disturbance: simultaneous writes and contaminated per-run git/file-change accounting on the same cwd.
- Attenuating coordination relation: cross-process exclusion specifically around the file-writing executor; chat-only waves remain outside the lock.
- Feedback into subsequent S1 behaviour: a contender cannot enter its writing stage until release, or receives a bounded timeout; later execution sees the serialized tree.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: implementation states and enforces the precise same-tree interference/evidence collision, beyond DAG order.

## S3 — Inside-and-now control

- State: —
- Function: No whole-current organization-level discretionary control loop established beyond task-level orchestration.
- Disturbance / variety regulated: Aggregate resources/commitments across current runs, distinct from choosing tiers for one decomposed request.
- Decisive decision or feedback right: A whole-current regulating actor choosing/revising priorities/resources from that view.
- Decision owner: Developer/operator fixed limits and per-task lead choices; no cross-run discretionary regulator established.
- Supporting / enforcement mechanisms: Cost/spend limits, RunTracker visibility, lead tier/skill assignment, Plan approvals/cancel and fallback health.
- Closure path: Lead choices affect one request’s role execution; limits/fallback enforce preselected constraints. No shipped whole-current priority/bargaining return was established.
- Why this is / is not agent-owned: A lead selecting premium/cheap tiers for subtasks is resource-aware decomposition; limits/dashboard/control primitives alone do not establish S3 or parent mode.
- Evidence: [voly/a2a/lead.py](https://github.com/voly-codes/voly/blob/d21dab640647ca5a0a096e12b01a9a3a4f7432af/voly/a2a/lead.py); [voly/runner/agent_runner.py](https://github.com/voly-codes/voly/blob/d21dab640647ca5a0a096e12b01a9a3a4f7432af/voly/runner/agent_runner.py); [voly/cost_policy.py](https://github.com/voly-codes/voly/blob/d21dab640647ca5a0a096e12b01a9a3a4f7432af/voly/cost_policy.py); [voly/sdk/workflow.py](https://github.com/voly-codes/voly/blob/d21dab640647ca5a0a096e12b01a9a3a4f7432af/voly/sdk/workflow.py); [voly/plan/approval.py](https://github.com/voly-codes/voly/blob/d21dab640647ca5a0a096e12b01a9a3a4f7432af/voly/plan/approval.py)
- Basis: structural
- Confidence: high
- Caveats: Source-based boundary judgment; no live model or production effectiveness claim.

### Absence scope

- Surfaces inspected: Lead selection, runner live tracker, cost policy and SDK/Plan approval/cancellation paths.
- Plausible first-party paths checked: Agent model-tier allocation, spend enforcement, workflow controls, human approval and live run visibility.
- Why no material first-party path remains: No function-specific whole-current commitments decision actor/return across ongoing operations is shipped; a per-task resource plan and ordinary approvals do not independently satisfy this boundary.

## S3* — Complementary audit

- State: A
- Function: Independently challenge a completed local multi-agent solver episode using direct read-only repository evidence.
- Disturbance / variety regulated: Solver/role summaries and success flags can disagree with actual retained code/diff.
- Decisive decision or feedback right: Judge chooses evidence inspection and a pass/fail/uncertain verdict; required mode returns its challenge into accepted pipeline result.
- Decision owner: Separate AgenticJudgeAgent model run; solver/ordinary reviewer role does not control the judge verdict.
- Supporting / enforcement mechanisms: ReadOnlyJudgeWorkspace allowed list/read/search/git_diff tools, episode lineage, strict JSON parsing and pipeline status gating.
- Closure path: After ordinary assignments, stages_a2a runs the judge on solver episode and cwd → independent tool observations inform verdict → non-pass/error in required mode sets failed episode and partial/failed pipeline result.
- Boundary reachability: Configured evaluation.llm_judge.mode=required with cwd directly constructs and runs AgenticJudgeAgent in the supported local A2A pipeline after normal roles, not only in a benchmark.
- Why this is / is not agent-owned: The extra judgment is model-owned. Read-only tools and result parsing enforce independence/return; default/off and shadow modes do not receive an asserted blocking verdict.
- Evidence: [voly/pipeline/stages_a2a.py](https://github.com/voly-codes/voly/blob/d21dab640647ca5a0a096e12b01a9a3a4f7432af/voly/pipeline/stages_a2a.py); [voly/a2a/agentic_judge.py](https://github.com/voly-codes/voly/blob/d21dab640647ca5a0a096e12b01a9a3a4f7432af/voly/a2a/agentic_judge.py); [voly/a2a/environments.py](https://github.com/voly-codes/voly/blob/d21dab640647ca5a0a096e12b01a9a3a4f7432af/voly/a2a/environments.py); [docs/backend/pipeline.md](https://github.com/voly-codes/voly/blob/d21dab640647ca5a0a096e12b01a9a3a4f7432af/docs/backend/pipeline.md)
- Basis: structural
- Confidence: medium
- Caveats: This witness is the extra episode-level direct-evidence judge, not normal reviewer role or record-only runner EvalEngine. It blocks/downgrades accepted result; automatic production repair is not claimed.
- Claim being audited: successful multi-agent implementation and role-reported operational result.
- Ordinary reporting path: Assignment outputs/status, role metrics and merged solver episode.
- Complementary access path: direct list/read/search of retained project files and git diff through bounded read-only tools.
- Independence boundary: separate judge message/tool loop, no file-writing grant, explicit configured provider/model and allow_provider_reroute=False; different-provider deployment is configurable, not asserted universal.
- Who acts on findings: pipeline required-mode final-result/episode gate; IterativeRepairEnv separately exposes feedback-to-solver composition.

## S4 — Outside-and-then intelligence

- State: C
- Function: Develop and evidence-test externally sourced future capability options before adoption.
- Disturbance / variety regulated: Untrusted external skill/agent guidance may change future quality, cost and operational risk.
- Decisive decision or feedback right: Choose candidate/experiment/activation based on external provenance and prospective paired/held-out outcome value, then integrate chosen guidance into current execution.
- Decision owner: Operator/developer composes the adaptation judgment and final capability-consumption loop; no autonomous adaptation owner demonstrated.
- Supporting / enforcement mechanisms: External pack discovery/scanning/quarantine/staging, checksum-bound variant renderer, measured evidence store, activate/retire/activation-plan and evaluated route API.
- Closure path: The first-party constructor develops a source-provenanced supplemental task variant and state/evidence/route decisions. Caller must still feed the rendered task/route back to an executing Agent/Plan; ordinary pipeline does not automatically consume evaluated-pack state.
- Boundary reachability: Published capability CLI exposes pack install/stage, measured records, activation-plan/activate/retire/route and render-variant. No test fixture or Cloud-only behavior is borrowed.
- Why this is / is not agent-owned: This is purpose-specific prospective capability experimentation, not generic memory. The exposed adaptation path supports C; neither manually approved shadow instincts nor inert remote sync establishes a closed P/A mode.
- Evidence: [voly/capability/packs.py](https://github.com/voly-codes/voly/blob/d21dab640647ca5a0a096e12b01a9a3a4f7432af/voly/capability/packs.py); [voly/capability/pack_store.py](https://github.com/voly-codes/voly/blob/d21dab640647ca5a0a096e12b01a9a3a4f7432af/voly/capability/pack_store.py); [voly/capability/evaluated_packs.py](https://github.com/voly-codes/voly/blob/d21dab640647ca5a0a096e12b01a9a3a4f7432af/voly/capability/evaluated_packs.py); [voly/capability/validation.py](https://github.com/voly-codes/voly/blob/d21dab640647ca5a0a096e12b01a9a3a4f7432af/voly/capability/validation.py); [voly/cli/commands/capability_evaluated_cmd.py](https://github.com/voly-codes/voly/blob/d21dab640647ca5a0a096e12b01a9a3a4f7432af/voly/cli/commands/capability_evaluated_cmd.py); [voly/capability/routing.py](https://github.com/voly-codes/voly/blob/d21dab640647ca5a0a096e12b01a9a3a4f7432af/voly/capability/routing.py)
- Basis: structural
- Confidence: medium
- Caveats: Activation alone requires measured evidence; stronger activate-ready gate is separate. Whole-tree call-site inspection found no normal pipeline consumer of EvaluatedPackRouter/render_variant_task. Do not infer live adaptation from active state or a CLI report.
- External distinction: identifiable external capability checkout/component provenance, security constraints and guidance alternatives.
- Future / prospective distinction: expected quality/cost/latency of future use compared through candidate baseline/variant and held-out evidence.
- Adaptation option generated: bounded checksum-verified capability variant, activation/retirement decision and evaluated route hint.
- Path back into current capability / S3: explicit renderer/route API for subsequent task construction; automatic integration and autonomous selection remain to be composed, which bounds C.

## S5 — Policy and identity

- State: —
- Function: No runtime legitimate ultimate-policy/identity adjudication loop established.
- Disturbance / variety regulated: Ultimate purpose/policy tension rather than execution permission or capability safety.
- Decisive decision or feedback right: Authoritative identity/policy decision returned to govern operation.
- Decision owner: Operator configuration and developer policy; no S5-specific closed actor/parent path.
- Supporting / enforcement mechanisms: Protected-file/write guards, spend/DLP rules, approvals, learning-content restrictions and capability quarantine.
- Closure path: Policies/approvals constrain ordinary execution and imported guidance. They do not adjudicate ultimate identity or S3–S4 tension.
- Why this is / is not agent-owned: Safety/adoption/approval power is not S5 merely because it is authoritative over a narrower action.
- Evidence: [voly/plan/approval.py](https://github.com/voly-codes/voly/blob/d21dab640647ca5a0a096e12b01a9a3a4f7432af/voly/plan/approval.py); [voly/learning/instincts.py](https://github.com/voly-codes/voly/blob/d21dab640647ca5a0a096e12b01a9a3a4f7432af/voly/learning/instincts.py); [voly/capability/pack_admission.py](https://github.com/voly-codes/voly/blob/d21dab640647ca5a0a096e12b01a9a3a4f7432af/voly/capability/pack_admission.py); [voly/decisions.py](https://github.com/voly-codes/voly/blob/d21dab640647ca5a0a096e12b01a9a3a4f7432af/voly/decisions.py); [README.md](https://github.com/voly-codes/voly/blob/d21dab640647ca5a0a096e12b01a9a3a4f7432af/README.md)
- Basis: structural
- Confidence: high
- Caveats: Source-based boundary judgment; no live model or production effectiveness claim.

### Absence scope

- Surfaces inspected: Plan/business approval, learning lifecycle, capability admission, safety/operator configuration and README open-core boundary.
- Plausible first-party paths checked: Manual instinct approval, capability activation, business-option approval and write/spend/security policy.
- Why no material first-party path remains: All evidenced decisions concern bounded actions/capability or technical safety; no first-party ultimate-policy/identity matter→legitimate authority→return closure is supplied.

## Distributed OSS parent arrangement

The self-hosted operator owns deployment configuration and scoped approval. Maintainer governance/commercial cloud are distinct; no organization-level parent state is inferred from OSS contribution activity.

## Self-hosted and non-human modes

SDK/A2A optional modes are assessed independently. Required judge is opt-in; defaults/shadow do not inherit its blocking semantics. Human-approved business options execute domain actions, not automatically harness adaptation. Evaluated pack construction remains distinct from generic capability routing.

## Recursion

Nested workflow nodes/A2A roles are not by themselves recursively viable units. Independent runs have task outcomes and local variety; no complete per-node metasystem is claimed.

## Variety and escalation

Allowlisted tools and budgets bound task variety; same-tree exclusion reduces interference; extra required judge can reject solver-level success. Capability evidence/provenance attenuates imported option risk, with final adaptation integration explicitly left at C.

## Evidence gaps

No paid provider, external coding execution, Cloudflare deployment or full upstream pytest suite claimed. pytest was unavailable; a direct source-native two-thread cwd-lock exercise passed. Model reliability, actual independent-provider use and production capability benefit are unobserved. Evaluated routing/injection integration is a demonstrated construction boundary, not assumed closed.
