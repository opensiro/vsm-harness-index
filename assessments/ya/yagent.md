---
harness_id: yagent
project_name: Yagent
repository: https://github.com/Mechres/Yagent
review_ref: 14d2999bf2abb280645fcafe2f15552ad9e49922
reviewed_at: 2026-10-23
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-23
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: C
autonomy_s4: A(P)
autonomy_s5: —
---

# Yagent

## Review boundary

- System in focus: one installed local Yagent coding/research assistant at the pinned Go source revision, including its primary agent, optional first-party child investigations, shared scratch, project memory, review-role constructor, skill lifecycle and supported TUI/REPL/headless interface.
- Purpose and identity: assist a local operator with repository coding, audits, review, web research, structured goals and repeatable workflows through model/tool turns.
- Relevant environment: one local workspace, command/runtime toolchain, optional local/cloud OpenAI-compatible inference, web search, skill files and configurable independent MCP integrations.
- Standard-distribution boundary: the shipped single Go binary's runtime paths (REPL/TUI and headless local HTTP/SSE) with primary model/child-model inference but not the external providers, web engines or independent MCP server's governance.
- Credited operating / distribution surfaces: `cmd/yagent`, `internal/ui`, `internal/agent`, `internal/tools`, `internal/skills`, `internal/memory`, `internal/jobs`, `internal/playbook`, `internal/workspace`, `internal/config` and directly used first-party integrations.
- Adjacent first-party surfaces excluded from ownership: maintainer changes/roadmap/CI, development evaluation fixtures and live-model benchmark protocols, contributing/project `AGENTS.md`, and any standalone provider process or configured external advisor/MCP service not shown as a first-party governing role.
- First-party operating / deployment modes considered: interactive REPL/TUI, headless `serve`, goal/research/playbook, optionally read-only child agents with specialist roles, automatic skill write (`skills.write_approval=false`, default) and parent-reviewed staged skill write (`true`).
- Recursion level: one deployed local coding-agent cell: the parent task actor plus its bounded first-party child S1 investigative units; external independent installations are not a common runtime organization.
- Reviewed revision: `14d2999bf2abb280645fcafe2f15552ad9e49922`.
- Observation date: 2026-10-23.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Yagent's `internal/agent.Agent` owns a bounded model/tool feedback loop, context budgeting and persisted history. The model selects filesystem, shell, Git, web, index, memory, skills and optional MCP tools. A tool dispatcher validates inputs, applies tactical approval and write/verification gates, and returns results for another decision. `RunGoal`/`RunResearch` drive repeated turns with progress checks. The CLI/TUI and local HTTP/SSE server use the same agent core; the latter's authorization and single-running-turn rule are not an additional independent organization.

The production chat environment wires a `subagent` tool to a fresh model-driven `RunSubagent` with a separately scoped read-only registry; up to eight child investigations may run concurrently. Children may write only confined scratchpad notes. Built-in `auditor` and `test-engineer` roles give a distinct child context direct read access to source/Git evidence and request independent findings, but no always-on audit or mandatory repair step is implemented. The general scratch and concurrent fan-out are useful for collaboration, but there is no baked-in conflict-detection/attenuation rule tied to competing S1 activities.

Yagent also has a concrete prospective adaptation lifecycle: after sufficient tool-intensive work or successful goal execution, the model is offered a new opportunity to distill a reusable `SKILL.md` procedure or playbook. `skill_manage` validates/deduplicates candidate skills. With default `skills.write_approval=false` it applies a model-selected skill immediately; with the supported gate enabled it writes to `pending/skills`, exposes diff/verification, and waits for an operator's `/skills approve` or rejection before activation. Accepted procedures appear in future skill catalogs and are loaded on demand.

Sources: [`internal/agent/agent.go`](https://github.com/Mechres/Yagent/blob/14d2999bf2abb280645fcafe2f15552ad9e49922/internal/agent/agent.go), [`internal/ui/repl.go`](https://github.com/Mechres/Yagent/blob/14d2999bf2abb280645fcafe2f15552ad9e49922/internal/ui/repl.go), [`internal/tools/subagent.go`](https://github.com/Mechres/Yagent/blob/14d2999bf2abb280645fcafe2f15552ad9e49922/internal/tools/subagent.go), [`internal/skills/write.go`](https://github.com/Mechres/Yagent/blob/14d2999bf2abb280645fcafe2f15552ad9e49922/internal/skills/write.go).

## Operational model

The main coding/research model and optional independently prompted child investigators are S1 actors. The children are read-only regarding project code and report into the parent, which chooses the next task operations. Lifecycle rules, verification gates, token/resource limits and user approvals supply guardrails, but must not be mistaken for owners of separate S3 or ultimate S5 judgments. The independent `auditor` role exposes a specific complementary review *constructor*; skill distillation is separately future-facing S4 capability adaptation. Its human review option is a distinct mode, not a statement that every default skill write needs approval.

## S1 — Operations

- State: A
- Function: execute coding/research requests through iterative model-chosen tool actions, including goal rounds and delegated investigations.
- Disturbance / variety regulated: uncertain repository structure, tool/compilation failures, complex goals, changing context size, provider errors and missing evidence.
- Decisive decision or feedback right: choose tools, arguments, subsequent edits and investigation/goal steps in response to observed outputs and failure feedback.
- Decision owner: configured primary model, and independent child models within their constrained delegated tasks.
- Supporting / enforcement mechanisms: Go loop, tool dispatch and permissions, semantic/code indexes, tests/smoke gates, history condensation, SQLite memory, goal retries and model-inference client.
- Closure path: operator goal → model selects action → allowed tool executes → result/diagnostic enters model history → model revises task or finishes; child investigations similarly return model-selected findings to the parent.
- Boundary reachability: standard `chat`/TUI and `serve` wire the first-party `Agent` and tool registry; `RunSubagent` can be invoked through the production registered `subagent` tool.
- Why this is / is not agent-owned: scripts constrain but do not select model-driven coding choices; removal of the model leaves no comparable autonomous task-step judgment.
- Evidence: [`internal/agent/agent.go`](https://github.com/Mechres/Yagent/blob/14d2999bf2abb280645fcafe2f15552ad9e49922/internal/agent/agent.go); [`internal/tools/tools.go`](https://github.com/Mechres/Yagent/blob/14d2999bf2abb280645fcafe2f15552ad9e49922/internal/tools/tools.go); [`internal/ui/repl.go`](https://github.com/Mechres/Yagent/blob/14d2999bf2abb280645fcafe2f15552ad9e49922/internal/ui/repl.go).
- Basis: direct source tracing, README and offline unit tests for agent/child/tool behavior.
- Confidence: high for the shipped route.
- Caveats: no live model coding-quality experiment was attempted; deterministic tests validate mechanisms, not real-provider task success.

## S2 — Coordination

- State: —
- Function: no complete disturbance-specific coordination function between the separately running primary/child S1 actors is established.
- Disturbance / variety regulated: competing edits, conflicting findings or context handoffs could arise, but shipped child agents are read-only for the code workspace and their investigations are independent.
- Decisive decision or feedback right: no first-party actor is delegated an inter-child conflict judgment; the parent chooses and consumes the tasks, and runtime only bounds simultaneous execution.
- Decision owner: parent model makes task-level delegation choices; semaphore/parallel dispatch and scratch filesystem enforce already-selected mechanics.
- Supporting / enforcement mechanisms: up-to-eight read-only child fan-out, toolset/role restrictions, common `.yagent/scratch` note tools and shared-provider slot semaphore.
- Closure path: children complete and return summaries; optional scratch reads can share information, but there is no shipped conflict/oscillation observation → specific coordination decision → altered competing child behaviors circuit.
- Why this is / is not agent-owned: a shared blackboard, limited concurrency and task decomposition are not S2-specific conflict regulation without an evidenced attenuation judgment/feedback path.
- Evidence: [`internal/tools/subagent.go`](https://github.com/Mechres/Yagent/blob/14d2999bf2abb280645fcafe2f15552ad9e49922/internal/tools/subagent.go); [`internal/tools/scratch.go`](https://github.com/Mechres/Yagent/blob/14d2999bf2abb280645fcafe2f15552ad9e49922/internal/tools/scratch.go); [`internal/llm/slot.go`](https://github.com/Mechres/Yagent/blob/14d2999bf2abb280645fcafe2f15552ad9e49922/internal/llm/slot.go).
- Basis: production wiring, child limitations and related tests.
- Confidence: medium-high for the bounded first-party organization.
- Caveats: an operator could deliberately program coordinated child tasks through scratch notes; this is not evidence of an already-completed S2-specific runtime route.

### Absence scope

- Surfaces inspected: child spawning and parallel task combination, role/tool subsets, shared scratch, model slots, goals, playbooks, background jobs, headless session isolation and project memory.
- Plausible first-party paths checked: parent assignment as S2; scratchpad as conflict attenuator; provider semaphore as coordination; playbook phases and task queues as cross-S1 regulation.
- Why no material first-party path remains: they share/sequence data or bound access, without a material independently owned and returned interference-control decision between distinct S1 operational units.

## S3 — Inside-and-now control

- State: —
- Function: no separate whole-current management actor allocates resources, priorities or commitments across the deployed S1 organization.
- Disturbance / variety regulated: running-task delays, failed tests, hung jobs and model budgets are handled as operational retries, caps and tool controls.
- Decisive decision or feedback right: no actor with a whole-system current status owns a cross-S1 intervention or commitment reallocation.
- Decision owner: primary S1 model chooses its own task/subtask operations; deterministic goal/verification gates, child cap and UI controls enforce local constraints.
- Supporting / enforcement mechanisms: `RunGoal`, test/smoke/diagnostic gates, playbook stages, background-job status/kill, process slots, TUI workspace view and session cancellation.
- Closure path: failures may reopen the current goal and timeout/cancel may stop the turn; no separate portfolio view → S3 judgment → changed cross-S1 resource/commitment path is shown.
- Why this is / is not agent-owned: task retry, dynamic schema gating and status rendering do not independently select organizational current-control tradeoffs.
- Evidence: [`internal/agent/agent.go`](https://github.com/Mechres/Yagent/blob/14d2999bf2abb280645fcafe2f15552ad9e49922/internal/agent/agent.go); [`internal/tools/bg.go`](https://github.com/Mechres/Yagent/blob/14d2999bf2abb280645fcafe2f15552ad9e49922/internal/tools/bg.go); [`internal/ui/tui.go`](https://github.com/Mechres/Yagent/blob/14d2999bf2abb280645fcafe2f15552ad9e49922/internal/ui/tui.go).
- Basis: bounded analysis of current-state/priority/stop/control surfaces.
- Confidence: medium-high.
- Caveats: a separate human project manager could control multiple installations, but that is outside the local first-party runtime boundary.

### Absence scope

- Surfaces inspected: goals, plan/research mode, playbooks, agent loop, independent child fan-out, provider budget, jobs, UI and headless sessions.
- Plausible first-party paths checked: parent model as manager of subordinate children; background job tools as S3 interventions; TUI workspace overview as an operator S3 view; deterministic success predicates as management.
- Why no material first-party path remains: no separate comprehensive live activity/commitment view with an actor choosing resource and priority redirection across the operating units; tactical subtask control remains S1.

## S3* — Complementary audit

- State: C
- Function: supply a distinct fresh-context adversarial inspection of current code/changes, with evidence-backed findings returned to the producing parent.
- Disturbance / variety regulated: unnoticed security/correctness defects, regressions and misreported code quality from the primary coding loop.
- Decisive decision or feedback right: decide which source/Git-backed findings to report independently; a mandatory finding-to-repair obligation remains uncomposed.
- Decision owner: separately initialized child model using the first-party `auditor`/`test-engineer` role preset; parent model chooses whether to invoke it and what to do with the result.
- Supporting / enforcement mechanisms: role-specific adversarial prompt, restricted read-only registry including direct file/index/Git review, isolated child context, bounded iterations and returned child summary.
- Closure path: parent delegates audit → role-specific fresh child inspects actual workspace/diff → child reports verified findings into parent's tool-result path → parent can choose corrections; no first-party required correction/retest closure follows every adverse finding.
- Boundary reachability: production `newChatEnv` registers `SetSubagent` and implements fresh `RunSubagent`; `subagent(role:"auditor")` and role default tool restrictions are exposed in the shipped tool schema and UI path.
- Claim being audited: correctness, security, test gaps and architectural concerns in repository work proposed/performed by S1.
- Ordinary reporting path: primary coding model's own tool results, compilation/test output and implementation summary.
- Complementary access path: fresh child context and read-only direct `fs_read`, Git diff/status/log, grep, index/call references and optionally web results.
- Independence boundary: independent inference context/role and tool restrictions but possibly same provider/model and same organizational parent; it is not institutionally independent, mandatory, or guaranteed to notice a defect.
- Who acts on findings: parent main model/operator may repair, but no automatic first-party completed return is required.
- Why this is / is not agent-owned: the audit-specific child model makes the substantive verification judgments; the constructor is present, while compulsory corrective feedback is not.
- Evidence: [`internal/tools/subagent.go`](https://github.com/Mechres/Yagent/blob/14d2999bf2abb280645fcafe2f15552ad9e49922/internal/tools/subagent.go); [`internal/agent/agent.go`](https://github.com/Mechres/Yagent/blob/14d2999bf2abb280645fcafe2f15552ad9e49922/internal/agent/agent.go); [`internal/ui/repl.go`](https://github.com/Mechres/Yagent/blob/14d2999bf2abb280645fcafe2f15552ad9e49922/internal/ui/repl.go).
- Basis: wired role/subagent code and offline tests of role prompt and delegated reporting.
- Confidence: medium-high for audit constructor, not efficacy.
- Caveats: optional on-demand audit; `C` does not assert independent model provider, systematic coverage or an automatic finding-to-fix return. Deterministic diagnostics alone were not counted as independent audit.

## S4 — Outside-and-then intelligence

- State: A(P)
- Function: turn observed task/workflow mistakes and successes into new reusable procedures that change how future Yagent operations are performed.
- Disturbance / variety regulated: repetitive task rediscovery, lost procedural know-how, repeated tool failures and changes in effective repository workflows.
- Decisive decision or feedback right: in autonomous mode the model selects, synthesizes, deduplicates and requests application of a reusable `SKILL.md` procedure; in optional parent mode the human examines and accepts/rejects a staged future capability change.
- Decision owner: model actor in default ungated `skill_manage` mode; the operator for final adoption in the separate configured `skills.write_approval=true` mode.
- Supporting / enforcement mechanisms: 5+ tool-call/success-or-error triggers, `skillCreationPrompt`, direct skill catalog/retrieval, `skill_manage`, procedural content validator, duplicate detection, scanner, project/global stores, pending diff/verification review and `/skills approve|reject` commands.
- Closure path: complex work/failure/user correction → bounded model distillation invitation → model observes work context and selects procedural adaptation → direct accepted `SKILL.md` write or pending proposal with parent approval → future skill catalog/`skill_view` makes the adopted guidance available to later operations.
- Boundary reachability: production `Agent` calls `maybeOfferSkillCreation` after sufficiently complex turns; `newChatEnv` supplies the actual skills store and `skill_manage` registry. REPL/TUI expose approval toggle, pending diff, verification and approval/rejection in the same installed runtime.
- External distinction: tool failures and successes in the actual user workspace, prior operator corrections, commands, repository practices and reusable task patterns outside the agent's static implementation.
- Future / prospective distinction: the generated procedure explicitly targets later related tasks, persisted separately from one present answer and surfaced in next skill catalogs.
- Adaptation option generated: model-authored new or patched `SKILL.md`, potentially a later reusable playbook distilled after a completed autonomous goal.
- Path back into current capability / S3: accepted skills live in persistent global/project store, appear in available-skills context and are loaded through `skill_view` when triggered; the parent-reviewed mode returns the adoption decision via `ApprovePending` before the skill becomes usable.
- Why this is / is not agent-owned: in default mode only the model makes the substantive procedure/selection judgment and write applies without a parent choice; in opt-in gate mode the human has a legitimate final alternative-adoption right and closes it through approve/reject. The two modes are distinct, not concurrent ultimate authorities.
- Evidence: [`internal/agent/agent.go`](https://github.com/Mechres/Yagent/blob/14d2999bf2abb280645fcafe2f15552ad9e49922/internal/agent/agent.go); [`internal/tools/skills.go`](https://github.com/Mechres/Yagent/blob/14d2999bf2abb280645fcafe2f15552ad9e49922/internal/tools/skills.go); [`internal/skills/write.go`](https://github.com/Mechres/Yagent/blob/14d2999bf2abb280645fcafe2f15552ad9e49922/internal/skills/write.go); [`internal/ui/repl.go`](https://github.com/Mechres/Yagent/blob/14d2999bf2abb280645fcafe2f15552ad9e49922/internal/ui/repl.go); [`internal/config/config.go`](https://github.com/Mechres/Yagent/blob/14d2999bf2abb280645fcafe2f15552ad9e49922/internal/config/config.go).
- Basis: source/prod wiring and native offline tests for automatic offers, staged/applied writes, review approval and persistence.
- Confidence: medium-high for the available alternative closure modes.
- Caveats: only conditional opportunities, not continuous horizon scanning; a model may decline to write any skill, and future quality benefit was not measured. Parent mode requires opting in to write approval; default is `false`. A playbook write by itself does not add a new ownership mode.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Model operating `skill_manage` with default `write_approval=false` | Successful complex turn/errors/correction and model's one-shot skill offer | Validated model-selected SKILL.md applies directly and enters persistent future catalog | `internal/agent/agent.go`; `internal/tools/skills.go`; `internal/config/config.go` |
| Parent (`P`) | Operator reviewing staged candidate | Supported `skills.write_approval=true` config; model offers a new/changed skill | Model stages proposal, human views diff/optionally verifies and `/skills approve` applies it or rejects | `internal/tools/skills.go`; `internal/skills/write.go`; `internal/ui/repl.go` |

## S5 — Policy and identity

- State: —
- Function: no first-party ultimate identity, mission or constitutional-policy arbitration loop governs the local coding-agent organization.
- Disturbance / variety regulated: per-tool risk, prompt trust, LLM credentials, research deliverables and permissions are controlled locally without a higher legitimate identity policy process.
- Decisive decision or feedback right: no claimed S5 owner can decide ultimate organizational purpose and return binding changes to continuing operations.
- Decision owner: operator configures models, access and session rules; model owns coding and skill creation decisions within those tactical constraints.
- Supporting / enforcement mechanisms: tool approval, `/yolo`, sandbox, untrusted content wrapping, memory redaction, skill approval, headless optional bearer token and config overlays.
- Closure path: authorized/unauthorized tactical effects are enforced; no ultimate mission-policy issue → S5 deliberation → authoritative identity decision → governing return appears.
- Why this is / is not agent-owned: authorization and safety controls, even when an operator chooses them, do not by themselves demonstrate identity-level governing functions.
- Evidence: [`internal/config/config.go`](https://github.com/Mechres/Yagent/blob/14d2999bf2abb280645fcafe2f15552ad9e49922/internal/config/config.go); [`internal/ui/serve.go`](https://github.com/Mechres/Yagent/blob/14d2999bf2abb280645fcafe2f15552ad9e49922/internal/ui/serve.go); [`internal/tools/tools.go`](https://github.com/Mechres/Yagent/blob/14d2999bf2abb280645fcafe2f15552ad9e49922/internal/tools/tools.go).
- Basis: reviewed policy/auth/config and escalation surfaces.
- Confidence: medium-high.
- Caveats: maintainer project governance is outside this runtime; approval of a reusable skill is S4 adaptation adoption, not identity-policy settlement.

### Absence scope

- Surfaces inspected: CLI REPL/TUI/headless config/auth, policy modes, tool sandbox/approval, skills manager, goal and research objectives, repository governance files.
- Plausible first-party paths checked: operator skill acceptance as S5, `/yolo` as policy authority, headless token as S5 identity, maintainers/AGENTS.md as a distributed parent constitution.
- Why no material first-party path remains: these regulate one workflow/capability or access permission; they do not constitute a runtime-wide ultimate-policy decision/return at the declared recursion.

## Distributed OSS parent arrangement

Upstream contributors can change and release the Go binary, but their GitHub collaboration is adjacent to independently installed Yagent runtime cells. The optional `(P)` in S4 refers to a **local operator's verified skill-adoption path**, not collective project governance over multiple installations.

## Self-hosted and non-human modes

The default local session can run the S1 task loop and model-author procedural knowledge without parent skill approval. A deliberately enabled first-party `skills.write_approval` mode changes the S4 adoption owner to a reviewing human, with explicit approve/reject return. Ordinary headless session creation, termination and per-tool risk approval do not separately close S3 or S5.

## Recursion

The primary coding agent and its isolated read-only child investigations are distinct S1 actors under a single local installation. The output of child auditor reports to the parent; there is no independently established full child S1–S5 metasystem, nor a first-party governing collective across installed copies.

## Variety and escalation

Model failures and runtime tests feed operational correction. Child investigation notes help share context but do not automatically adjudicate inter-child conflict. A specialist child auditor can supply complementary independent findings without mandated repair. Learned procedures can be promoted autonomously or by optional operator approval, reducing prospective rediscovery in later work.

## Evidence gaps

- Frozen source was inspected and its Go 1.25.0 toolchain was downloaded into a temporary isolated path. No live LLM/Ollama/provider tests ran. The selected native offline `Test.*(Subagent|Scratch|Skill|Goal|WriteApproval|Pending)` suite across agent/tools/skills/config passed; full `go test ./... -short` did **not** pass cleanly in this container.
- The full run included failures in Go runtime-smoke/goal-gate fixture tests (`no smoke runner`), a write-protection test running with elevated filesystem privileges, and bubblewrap tests unable to create Linux namespaces. Those failures are preserved as observed environment-sensitive test results; they are not counted as a green full suite or a source defect without a controlled compatible host repeat.
- No real provider was used to show successful independent audit findings, actual sibling contention reduction, beneficial future skill use or quality of model-authored procedures. S3* is a first-party audit constructor `C`, not a proven mandatory corrective loop; S4 modes rest on demonstrable adoption wiring, not measured adaptation efficacy.
- Unobserved external MCP advisors or a hand-coded scratch coordination protocol may extend the system but were not credited as native S2/S3/S5 ownership.
