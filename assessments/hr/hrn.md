---
harness_id: hrn
project_name: hrn
repository: https://github.com/cristiangirlea/harness
review_ref: 16d27aea0d7276d411fa1e93d2208b66f4fa39e0
reviewed_at: 2026-10-26
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: C
autonomy_s4: P
autonomy_s5: —
---

# hrn

## Review boundary

- System in focus: the installed local hrn coding harness, including supported API, batch, MCP, inspection and evaluation commands.
- Purpose and identity: execute coding tasks, preserve their evidence and let the operator compare and select execution arrangements.
- Relevant environment: user repositories, tools, model providers, optional installed agent CLIs and the local operator.
- Standard-distribution boundary: root Go module and documented local commands at the frozen revision; no private AdaNext deployment is assumed.
- Credited operating / distribution surfaces: `cmd/hrn`, `internal/agent`, `internal/tools`, `internal/batch`, `internal/ws`, `internal/hrnmcp`, `internal/eval`, `internal/route`, reporting and local watch surfaces. Evaluation is credited only where it is an explicitly shipped operator command with returned selection into this same local harness.
- Adjacent first-party surfaces excluded from ownership: contributor instructions and CI, external `hrn-evals` suites, the separately built `server` deployment module, planned AdaNext tools and unbuilt experience/practice slices. Unit tests corroborate construction but do not supply runtime decision owners.
- First-party operating / deployment modes considered: native API tool loop, optional CLI adapters, parallel batches, MCP integration, operator-invoked evaluation/judging and evidence-based purpose routing.
- Recursion level: one local harness installation and its repository task cells; not the maintainer's development organization.
- Reviewed revision: `16d27aea0d7276d411fa1e93d2208b66f4fa39e0`.
- Observation date: 2026-10-26.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The [API backend](https://github.com/cristiangirlea/harness/blob/16d27aea0d7276d411fa1e93d2208b66f4fa39e0/internal/agent/api.go) assembles instructions, sends model requests, dispatches returned tool choices, appends observations and continues until completion or a configured limit. Optional Claude/Codex/Gemini/OpenCode/agy adapters are external execution arrangements; inclusion does not depend on borrowing their internal decisions. Local tools constrain filesystem effects and command execution. Run records preserve messages, results, usage and resumable conversations.

[Batches](https://github.com/cristiangirlea/harness/blob/16d27aea0d7276d411fa1e93d2208b66f4fa39e0/internal/batch/batch.go) run distinct task cells in isolated branches and leased worktrees, check configured gates and carry failure evidence to configured retries. [Issue leases](https://github.com/cristiangirlea/harness/blob/16d27aea0d7276d411fa1e93d2208b66f4fa39e0/internal/ws/issue.go) protect work identity across local checkouts. The [MCP surface](https://github.com/cristiangirlea/harness/blob/16d27aea0d7276d411fa1e93d2208b66f4fa39e0/internal/hrnmcp/server.go) exposes delegation, recorded results, diffs and integration to a separately supplied host. It does not package that host's supervisory cognition.

The shipped evaluator can compare backend/model configurations, optionally judge gate-passing diffs in neutral read-only checkouts, and record a comparison. The operator can adopt purpose-specific backend/model/effort choices from those results through `route from-eval`. [Experience documentation](https://github.com/cristiangirlea/harness/blob/16d27aea0d7276d411fa1e93d2208b66f4fa39e0/docs/experience.md) separates built record-keeping from future practice/learning designs; planned features are not credited.

## Operational model

A repository coding task has a durable result, local environmental variety and an autonomous model-driven choice/action loop in the native API backend. Multiple batch tasks are distinct S1 units. The model owns investigative and repair decisions; deterministic tools, limits, gates and leases support or constrain them. Operators select execution modes, gates and comparison/adoption commands. An external MCP caller can compose further control but its organization is not included by assumption.

## S1 — Operations

- State: A
- Function: produce code changes or investigation results in a repository.
- Disturbance / variety regulated: unknown code, tool errors, denied actions and failing implementation attempts.
- Decisive decision or feedback right: choose the next investigation, edit, command or completion response based on accumulated observations.
- Decision owner: the agent instantiated inside `APIBackend.Run`.
- Supporting / enforcement mechanisms: Anthropic transport, tool schemas, workspace confinement, permission selection, budgets, run records and batch gates.
- Closure path: model tool choice → local execution or denial → `tool_result` appended to conversation → subsequent model choice, ending in a recorded result.
- Boundary reachability: the native `api` backend is shipped in the installed binary, with its own loop and local tools; optional external CLI engines are unnecessary for this witness.
- Why this is / is not agent-owned: without the model's choices the transport and tools cannot determine which repository work to perform. Configuration bounds action without supplying the investigative decision.
- Evidence: [APIBackend.Run and runTools](https://github.com/cristiangirlea/harness/blob/16d27aea0d7276d411fa1e93d2208b66f4fa39e0/internal/agent/api.go), [permissions](https://github.com/cristiangirlea/harness/blob/16d27aea0d7276d411fa1e93d2208b66f4fa39e0/docs/permissions.md).
- Basis: structural.
- Confidence: high.
- Caveats: source establishes construction and ownership, not coding performance; provider credentials are deployment prerequisites.

## S2 — Coordination

- State: C
- Function: prevent distinct coding task cells from claiming the same issue or concurrently corrupting a shared worktree/branch.
- Disturbance / variety regulated: duplicate issue ownership and competing access to reusable repository workspaces.
- Distinct S1 units: separate API-backed batch tasks or concurrent local runs acting on one repository.
- Inter-S1 disturbance: two tasks naming one issue, or two runs trying to reuse the same worktree slot, would duplicate work or overwrite another cell's checkout.
- Attenuating coordination relation: issue acquisition before execution, exclusive slot leases, skip/wait/refusal for occupied slots and release after task completion.
- Feedback into subsequent S1 behaviour: a conflicting task does not start; an available isolated slot is selected, and released resources become eligible for later tasks.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the code explicitly detects duplicate issue claims and occupied workspaces and changes admission of concurrent work because of those collisions.
- Decisive decision or feedback right: select task/issue boundaries and resolve contention or takeover beyond the fixed lease rule.
- Decision owner: caller/developer/operator; the shipped lease controller does not supply an autonomous coordination actor.
- Supporting / enforcement mechanisms: atomic lease files, process-identity checks, Git worktree locking, duplicate-key checks and issue-release records.
- Closure path: task issue/slot request → collision decision/refusal or isolated allocation → admission of the corresponding task → release; autonomous exception judgment must be composed around the exposed result.
- Boundary reachability: `batch.Run` invokes `takeIssues` and workspace allocation in the normal installed batch path; CLI/MCP callers receive the resulting refusal or record.
- Why this is / is not agent-owned: removing a candidate coordinating agent leaves the same fixed exclusion rule; C credits the specific conflict/feedback constructor rather than the existence of parallel execution.
- Evidence: [batch.Run/takeIssues](https://github.com/cristiangirlea/harness/blob/16d27aea0d7276d411fa1e93d2208b66f4fa39e0/internal/batch/batch.go), [workspace Take](https://github.com/cristiangirlea/harness/blob/16d27aea0d7276d411fa1e93d2208b66f4fa39e0/internal/ws/ws.go), [issue leases](https://github.com/cristiangirlea/harness/blob/16d27aea0d7276d411fa1e93d2208b66f4fa39e0/docs/workspaces.md).
- Basis: structural.
- Confidence: high.
- Caveats: leases do not establish negotiated agent coordination or a general conflict-resolution policy.

## S3 — Inside-and-now control

- State: —
- Function: no material whole-current regulatory decision loop established in the assessed local distribution.
- Disturbance / variety regulated: candidate paths concern resource consumption, failing tasks and selection of passing branches.
- Decisive decision or feedback right: whole-system reprioritization or resource/commitment intervention is not assigned to a first-party regulator.
- Decision owner: task/spec author selects fixed limits; an external MCP host or operator may make further judgments outside the supplied loop.
- Supporting / enforcement mechanisms: parallel worker bound, per-run ceilings, configured retry order, gate execution, result inspection and branch merge.
- Closure path: fixed task failure feedback can retry that task; it does not reconstruct whole-system current regulation.
- Why this is / is not agent-owned: the native worker decides local work, not the allocation or revision of the wider installation's commitments.
- Evidence: [batch execution and retry](https://github.com/cristiangirlea/harness/blob/16d27aea0d7276d411fa1e93d2208b66f4fa39e0/internal/batch/batch.go), [MCP batch/show/merge](https://github.com/cristiangirlea/harness/blob/16d27aea0d7276d411fa1e93d2208b66f4fa39e0/internal/hrnmcp/batch.go), [MCP host instructions](https://github.com/cristiangirlea/harness/blob/16d27aea0d7276d411fa1e93d2208b66f4fa39e0/internal/hrnmcp/server.go).
- Basis: structural, bounded negative.
- Confidence: medium.
- Caveats: an independently composed supervisory organization may have S3, but generic batch control and MCP extensibility alone do not establish its first-party constructor.

### Absence scope

- Surfaces inspected: API limit/permission paths, batch spec/run/retry, local records/watch/report, MCP delegation/inspection/merge and backend preferences.
- Plausible first-party paths checked: shared parallel bounds, failed-task retry, passing-branch selection, operator backend changes and outside MCP supervision.
- Why no material first-party path remains: these implement preselected constraints, local repair, integration or generic outside supervision; no supplied whole-current feedback process revises shared commitments/resources as an organizational regulator. This conclusion is local-mode-relative, not a verdict on the separate remote-server organization.

## S3* — Complementary audit

- State: C
- Function: challenge a gate-passing coding cell's success claim through separate direct inspection of its change.
- Claim being audited: the cell's final explanation and passing gates adequately represent completion of the requested work.
- Ordinary reporting path: worker final answer and deterministic gate status in batch/evaluation records.
- Complementary access path: a separately instantiated judge receives the real diff, untracked-file warning, task/rubric and neutral read-only candidate checkout, not just the worker's summary.
- Independence boundary: new judge run, no inherited project instructions, anonymized Git metadata/variant paths and read-only mode. Producer text remains one explicit, challengeable evidence input.
- Who acts on findings: operator/consumer of recorded judge scores; automatic corrective disposition beyond evaluation is not supplied.
- Disturbance / variety regulated: plausible success claims or passing tests that conceal an inadequate implementation.
- Decisive decision or feedback right: judge raw change against a rubric and return its findings to control of later work.
- Decision owner: the configured judge owns the evidence judgment; operator/developer must compose authoritative corrective return.
- Supporting / enforcement mechanisms: checkout blinding, read-only tool restriction, verdict parsing and persisted score/reason.
- Closure path: passing cell → direct-evidence judge → recorded finding/comparison → caller inspection; a governing response into production is left to the consumer.
- Boundary reachability: optional `Judge` is wired into the shipped `hrn eval` path. This is an operator-facing product capability, not CI testing of hrn; no external `hrn-evals` suite or developer-only verifier supplies the owner.
- Why this is / is not agent-owned: a separate model can make audit judgments, but no complete first-party autonomous audit-to-correction loop is established; C preserves the missing control composition.
- Evidence: [judgeAll/evidenceOf/judgeCell](https://github.com/cristiangirlea/harness/blob/16d27aea0d7276d411fa1e93d2208b66f4fa39e0/internal/eval/judge.go), [blind checkout](https://github.com/cristiangirlea/harness/blob/16d27aea0d7276d411fa1e93d2208b66f4fa39e0/internal/eval/blind.go), [evaluator wiring](https://github.com/cristiangirlea/harness/blob/16d27aea0d7276d411fa1e93d2208b66f4fa39e0/internal/eval/eval.go).
- Basis: structural.
- Confidence: medium-high.
- Caveats: independence is claim-relative; shared model families and attacker-controlled diffs are not strong security isolation. The assessment ran no judge/model experiment.

## S4 — Outside-and-then intelligence

- State: P
- Function: operator-governed adaptation of the installation's future execution repertoire using comparative evidence about external model/backend choices.
- External distinction: backend/model/effort alternatives differ in measured completion and estimated cost.
- Future / prospective distinction: which alternatives should serve later tasks of each purpose, rather than only explaining one past run.
- Adaptation option generated: qualifying purpose-specific routing rows derived from measured alternatives, retaining evidence ID/date.
- Path back into current capability / S3: `route from-eval` saves selected rows; subsequent native runs, batch tasks and MCP runs consult them when choices are unspecified. This changes present execution capability; it does not separately establish an autonomous S3 regulator.
- Disturbance / variety regulated: the operator's execution arrangement may be an inferior cost/capability fit for future work.
- Decisive decision or feedback right: commission comparison, accept its pass/cost criterion and adopt or override the resulting routing policy.
- Decision owner: legitimate local installation operator, not an autonomous strategic agent.
- Supporting / enforcement mechanisms: evaluation records, `route.FromEval`, persisted routing table, validation and application to new runs.
- Closure path: operator compares alternatives → inspects options and selects `route from-eval`/`route set` → saved routing decision → later tasks use returned backend/model/effort choices.
- Boundary reachability: these are shipped local commands with a documented direct connection to production `run`/batch/MCP selection. No future Ada learning slice or adjacent external research actor is required.
- Why this is / is not agent-owned: deterministic cost/pass selection cannot replace the operator's decision to assess and adopt an execution strategy. No first-party agent owns this prospective adoption loop.
- Evidence: [evidence routing and return](https://github.com/cristiangirlea/harness/blob/16d27aea0d7276d411fa1e93d2208b66f4fa39e0/docs/evaluations.md), [route adoption command](https://github.com/cristiangirlea/harness/blob/16d27aea0d7276d411fa1e93d2208b66f4fa39e0/cmd/hrn/route.go), [option selection](https://github.com/cristiangirlea/harness/blob/16d27aea0d7276d411fa1e93d2208b66f4fa39e0/internal/route/route.go), [runtime application](https://github.com/cristiangirlea/harness/blob/16d27aea0d7276d411fa1e93d2208b66f4fa39e0/internal/route/table/table.go).
- Basis: structural and explicit documented operator mode.
- Confidence: medium.
- Caveats: narrow model/backend adaptation, not autonomous environmental research; no general strategic forecasting or empirical improvement claim. Evaluation alone would not establish S4 without this adoption/return wiring.

## S5 — Policy and identity

- State: —
- Function: no material runtime identity/ultimate-policy resolution loop supplied at this boundary.
- Disturbance / variety regulated: candidate constraints concern permission modes, command safety, backend access and task acceptance.
- Decisive decision or feedback right: no identity-level proposal and authoritative returned resolution are exposed as a first-party process.
- Decision owner: operator selects fixed configuration; contributor governance owns the separate software project.
- Supporting / enforcement mechanisms: system instructions, permission checks, guarded commands and operator-only dangerous-mode opt-in.
- Closure path: ordinary action approval returns to a tool call; this is not identity-policy closure.
- Why this is / is not agent-owned: no agent or parent runtime path settles identity/ultimate-policy matters for the local harness.
- Evidence: [API instructions/approval](https://github.com/cristiangirlea/harness/blob/16d27aea0d7276d411fa1e93d2208b66f4fa39e0/internal/agent/api.go), [permissions](https://github.com/cristiangirlea/harness/blob/16d27aea0d7276d411fa1e93d2208b66f4fa39e0/docs/permissions.md), [MCP guard boundary](https://github.com/cristiangirlea/harness/blob/16d27aea0d7276d411fa1e93d2208b66f4fa39e0/internal/hrnmcp/server.go).
- Basis: structural, bounded negative.
- Confidence: high.
- Caveats: an operator can govern a real installation without that governance being packaged as the assessed function.

### Absence scope

- Surfaces inspected: runtime instructions, approval modes, command guards, backend preference/access configuration, MCP startup and contributor documents.
- Plausible first-party paths checked: operator dangerous-mode decision, permission elicitation, backend enablement and project contribution rules.
- Why no material first-party path remains: all shipped returns govern ordinary operations or static access; none routes an identity/ultimate-policy issue to legitimate authority and returns its resolution into this harness. Development governance is an adjacent recursion.

## Distributed OSS parent arrangement

The local operator owns the evidenced S4 mode. Maintainer/contributor decisions about hrn releases are separate and are not organization-wide parent-function evidence for every installation.

## Self-hosted and non-human modes

The binary can run a native API loop or expose local tooling to an external MCP host. Host autonomy is not borrowed. Remote-server deployment is a separate explicitly unassessed boundary.

## Recursion

Parallel work cells establish distinct operations, not complete recursive viable systems. No full S1–S5 closure is inferred from batches or delegation.

## Variety and escalation

Tool observations amplify local investigation; permissions and budgets attenuate actions. Leases prevent concrete concurrent-work collisions. Fixed retry feedback preserves failed-attempt context; unknown durable effects require recovery rather than blind replay. These channels do not alone create whole-system autonomy.

## Evidence gaps

No live model, provider, external CLI or quality run was performed. A Go toolchain was unavailable locally, so no native Go test result is claimed. Source-backed ownership is distinct from observed effectiveness. Remote tenancy/server control and private AdaNext arrangements need their own declared-boundary assessment; the local findings do not speak for them.
