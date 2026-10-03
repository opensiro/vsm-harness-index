---
harness_id: froe
project_name: Froe
repository: https://github.com/dcoldeira/froe
review_ref: f23a0e5c31fe6c05c8d284750802f344e4a702f1
reviewed_at: 2026-10-03
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-03
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# Froe

## Review boundary

- System in focus: the first-party dcoldeira/froe local coding-agent distribution at frozen revision f23a0e5c31fe6c05c8d284750802f344e4a702f1, including the Go model/tool loop, coding tools, provider adapters, permission gate, session and project-memory state, bounded locate workflow and its post-answer verification/recheck path, terminal commands, JSON-RPC server and Neovim client where they directly reach that same runtime.
- Purpose and identity: provide local-first, bounded software-engineering assistance, including one-shot autonomous coding through froe do, interactive chat, read-only code localization, project memory and editor-integrated operation.
- Relevant environment: the selected local project and filesystem, user task, shell and Git state, project instruction files, local or configured model runtime, provider responses, permission decisions, session history and durable project memories.
- Standard-distribution boundary: the shipped Go binary, internal agent/tools/provider/repo/session/perms packages, top-level command implementations, JSON-RPC path and Neovim client are inside. Model servers and hosted providers supply inference; the target repository, host shell/Git and user-authored project instructions are environment or parent inputs rather than Froe organizational decision owners.
- Credited operating / distribution surfaces: README.md; cmd/froe/do.go; cmd/froe/locate.go; cmd/froe/locate_run.go; cmd/froe/locate_evidence.go; internal/agent/agent.go and its completion-check helpers; internal/tools; internal/perms; internal/session; internal/repo/instructions.go; directly reached RPC/Neovim execution surfaces.
- Adjacent first-party surfaces excluded from ownership: eval/ benchmark fixtures and verify scripts, unit tests, contributor/development documentation and roadmap work. They corroborate runtime behavior but are not imported as operating VSM owners.
- First-party operating / deployment modes considered: froe do with normal approval, accept-edits and yolo modes; froe locate; interactive chat/resume; terminal use; Neovim through the same binary over JSON-RPC; durable project memory and project-instruction loading.
- Recursion level: one Froe-assisted coding organization around one project/task. The primary model-backed coding loop is the operating S1. Froe deliberately does not ship multi-agent/subagent spawning at this revision.
- Reviewed revision: f23a0e5c31fe6c05c8d284750802f344e4a702f1.
- Observation date: 2026-10-03.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

Froe is a single Go binary with its own provider-neutral model/tool loop and first-party coding tools. The froe do path resolves a model/provider, constructs project context and persisted history, loads durable project memories, registers the full coding tool set, installs a permission gate and starts agent.Agent with ApplyEdits enabled. The agent then repeatedly asks the model for a response, executes requested tools, returns observations and errors, detects repeated or fruitless calls, bounds context and turns, and continues until the model finishes or a runtime limit stops the run.

Permission policy is an enforcement layer around model-selected actions. The default asks for mutating calls, accept-edits can auto-approve file changes while retaining shell approval, and yolo approves actions except hard denials. These modes do not replace the model's open-ended choice of what coding operation to attempt next.

The agent loop also contains same-S1 reliability checks: after edits it can detect leftover target terms, incomplete numbered asks, unapplied code shown only in prose, or an explicitly requested check that has not been run, then nudge the same agent once. Those mechanisms improve task completion but use the same operating transcript/actor and are not the basis of complementary-audit credit.

The stronger audit-specific path is the shipped froe locate command. Locate gives the model read-only tools, independently pre-searches the project for issue terms, records model searches and opened ranges, then checks the produced answer directly against the project tree. Its deterministic checker corrects line citations, distinguishes missing paths, replays successful searches inside cited files and identifies matching lines the answer omitted. When such unjudged lines exist, Froe feeds them back to the model in a bounded recheck prompt and checks the replacement answer again. That is a first-party complementary-access and corrective-return constructor, although the final semantic judgment about whether each candidate line belongs in WHERE remains with the same model actor rather than an independent autonomous auditor.

Project session state is persisted in SQLite. The model can invoke the remember tool to propose durable project facts for later sessions, subject to the mutation gate; future runs inject those memories into current context. FROE.md, CLAUDE.md or AGENTS.md project guidance is also loaded into present context, with nearer files taking precedence. These are current-operation context mechanisms rather than prospective organizational adaptation or identity-policy closure.

Primary evidence:

- [README.md](https://github.com/dcoldeira/froe/blob/f23a0e5c31fe6c05c8d284750802f344e4a702f1/README.md)
- [cmd/froe/do.go](https://github.com/dcoldeira/froe/blob/f23a0e5c31fe6c05c8d284750802f344e4a702f1/cmd/froe/do.go)
- [cmd/froe/locate.go](https://github.com/dcoldeira/froe/blob/f23a0e5c31fe6c05c8d284750802f344e4a702f1/cmd/froe/locate.go)
- [cmd/froe/locate_run.go](https://github.com/dcoldeira/froe/blob/f23a0e5c31fe6c05c8d284750802f344e4a702f1/cmd/froe/locate_run.go)
- [cmd/froe/locate_evidence.go](https://github.com/dcoldeira/froe/blob/f23a0e5c31fe6c05c8d284750802f344e4a702f1/cmd/froe/locate_evidence.go)
- [internal/agent/agent.go](https://github.com/dcoldeira/froe/blob/f23a0e5c31fe6c05c8d284750802f344e4a702f1/internal/agent/agent.go)
- [internal/perms/perms.go](https://github.com/dcoldeira/froe/blob/f23a0e5c31fe6c05c8d284750802f344e4a702f1/internal/perms/perms.go)
- [internal/session/store.go](https://github.com/dcoldeira/froe/blob/f23a0e5c31fe6c05c8d284750802f344e4a702f1/internal/session/store.go)
- [internal/repo/instructions.go](https://github.com/dcoldeira/froe/blob/f23a0e5c31fe6c05c8d284750802f344e4a702f1/internal/repo/instructions.go)

## Operational model

For a normal coding task, the user chooses the objective and operating mode. Froe assembles project context, history, memories and tools; the model chooses a tool call or final answer; Froe executes or permission-gates that call; and the resulting file, search, command or error evidence is returned to the model for the next decision. The yolo mode demonstrates a first-party path in which execution does not depend on per-action human approval, while the default mode keeps a human safety gate around side effects.

For locate, the operating answer is additionally challenged after the model stops. Froe reads underlying project evidence through a deterministic path separate from the model's prose, identifies omissions or invalid citations, and can force one bounded recheck before returning the checked result to the user.

## S1 — Operations

- State: A
- Function: perform software-engineering work against the selected local project by interpreting a task, inspecting repository evidence, choosing file/search/shell actions, applying changes when authorized and adapting later actions to returned observations.
- Disturbance / variety regulated: heterogeneous repository structure and code, incomplete or incorrect task descriptions, tool failures, command/test outcomes, context limits, local-model errors and evolving workspace state during a coding task.
- Decisive decision or feedback right: choose which available coding tool/action to invoke next, what project evidence to inspect or modify, and when the task is complete enough to stop.
- Decision owner: the model-backed Froe agent operating through the first-party Agent loop.
- Supporting / enforcement mechanisms: tool registry; provider adapters and tool-call strategies; project map/instructions; session history and memories; permission gate; hard denials; turn/context budgets; repeated-call and fruitless-search detectors; completion nudges; CLI/RPC rendering.
- Closure path: user task and project context → model-selected tool call → first-party permission/enforcement and tool execution → concrete result/error from the local environment → returned observation in the next model turn → revised operation or completion.
- Boundary reachability: froe do directly instantiates this loop with the shipped coding tools. The supported yolo mode removes per-action approval except non-overridable hard denials, so autonomous operation does not require an application author to compose a separate agent runtime.
- Why this is / is not agent-owned: removing the model-backed actor while retaining the tools, gates, persistence and deterministic nudges removes the open-ended judgment that selects and sequences repository-facing coding actions.
- Evidence: [cmd/froe/do.go](https://github.com/dcoldeira/froe/blob/f23a0e5c31fe6c05c8d284750802f344e4a702f1/cmd/froe/do.go); [internal/agent/agent.go](https://github.com/dcoldeira/froe/blob/f23a0e5c31fe6c05c8d284750802f344e4a702f1/internal/agent/agent.go); [internal/perms/perms.go](https://github.com/dcoldeira/froe/blob/f23a0e5c31fe6c05c8d284750802f344e4a702f1/internal/perms/perms.go); [README.md](https://github.com/dcoldeira/froe/blob/f23a0e5c31fe6c05c8d284750802f344e4a702f1/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the default permission mode can require a human to approve side effects, but that gate approves or denies the model's proposed action rather than choosing the coding operation. The standard distribution also exposes an unattended yolo mode.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 coordination function is established at the reviewed recursion.
- Disturbance / variety regulated: no concrete mutual interference, collision or oscillation among distinct operational S1 units is established because the shipped organization exposes one primary coding-agent loop rather than a peer/subagent population.
- Decisive decision or feedback right: not established at S2 scope.
- Decision owner: not established.
- Supporting / enforcement mechanisms: sequential model/tool execution, SQLite WAL/busy-timeout behavior, session persistence, permission serialization and ordinary command sequencing.
- Closure path: not applicable; no distinct-S1 interference → attenuation → returned coordination feedback relation was found.
- Why this is / is not agent-owned: the frozen architecture explicitly defers multi-agent/subagent spawning. Database concurrency support permits multiple processes to use persisted state but does not make them coordinated operational units.
- Evidence: [docs/ARCHITECTURE.md](https://github.com/dcoldeira/froe/blob/f23a0e5c31fe6c05c8d284750802f344e4a702f1/docs/ARCHITECTURE.md); [internal/agent/agent.go](https://github.com/dcoldeira/froe/blob/f23a0e5c31fe6c05c8d284750802f344e4a702f1/internal/agent/agent.go); [internal/session/store.go](https://github.com/dcoldeira/froe/blob/f23a0e5c31fe6c05c8d284750802f344e4a702f1/internal/session/store.go).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: terminal and Neovim are two front ends to the same binary, not two S1 units.

### Absence scope

- Surfaces inspected: complete frozen source tree; agent loop; command entry points; session store; RPC/Neovim path; architecture and roadmap; tools and permission machinery.
- Plausible first-party paths checked: subagent or peer spawning, concurrent worker coordination, shared task queues, session/process concurrency, terminal/editor dual-client operation and provider/runtime parallelism.
- Why no material first-party path remains: multi-agent execution is explicitly deferred, and the remaining concurrency/sequencing mechanisms protect one runtime or persistence store rather than attenuating an evidenced interference relation between distinct S1 units.

## S3 — Inside-and-now control

- State: —
- Function: no material whole-system current-control function over multiple operational commitments, shared resources or priorities is established.
- Disturbance / variety regulated: turn exhaustion, repeated calls, fruitless searches, permission violations, unchecked edits and context pressure are regulated locally inside one operating loop, not as organization-wide current-control variety.
- Decisive decision or feedback right: not established at S3 scope.
- Decision owner: not established.
- Supporting / enforcement mechanisms: max-turn limits; repeated-call and fruitless-search aborts; permission gate; hard denylist; context budgeting; completion/checklist/leftover nudges; operator cancellation and model selection.
- Closure path: these mechanisms stop, constrain or push the same S1 to finish its current task. They do not receive a whole-organization current view and revise shared commitments, resource allocations or priorities across operational units.
- Why this is / is not agent-owned: deterministic runtime safeguards enforce local execution rules; they do not acquire S3 ownership merely because they supervise the loop.
- Evidence: [internal/agent/agent.go](https://github.com/dcoldeira/froe/blob/f23a0e5c31fe6c05c8d284750802f344e4a702f1/internal/agent/agent.go); [internal/perms/perms.go](https://github.com/dcoldeira/froe/blob/f23a0e5c31fe6c05c8d284750802f344e4a702f1/internal/perms/perms.go); [cmd/froe/do.go](https://github.com/dcoldeira/froe/blob/f23a0e5c31fe6c05c8d284750802f344e4a702f1/cmd/froe/do.go).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: human approval/cancellation is local action governance rather than a qualifying first-party parent S3 loop.

### Absence scope

- Surfaces inspected: agent progress/abort/completion logic; permissions; session state; model routing; terminal/RPC controls; context budgeting; tools; architecture/roadmap.
- Plausible first-party paths checked: current-run supervision, operator approval/cancel, model routing, safety budgets, session metrics, concurrent sessions and any whole-deployment manager/scheduler.
- Why no material first-party path remains: every located control surface either supports one S1 or enforces preset/user decisions; no whole-current regulator with substantive authority over a set of operational commitments/resources is present.

## S3* — Complementary audit

- State: C
- Function: challenge the completeness and evidential validity of the supported locate operation after the model has produced an answer, using direct project evidence outside the model's prose and returning discrepancies for corrective re-judgment.
- Disturbance / variety regulated: omitted matching sites, stale or nonexistent cited paths, incorrect line numbers and uncorroborated code-location claims that can survive an ordinary model/tool search run.
- Decisive decision or feedback right: the first-party deterministic locate checker independently reads the project tree, corrects/rejects citation facts and identifies matching lines absent from the answer; when omissions are found, it forces a bounded recheck before accepting a replacement result.
- Decision owner: constructor-level deterministic Froe runtime for the audit-specific evidence comparison and return path. The same model actor supplies the semantic judgment about whether each surfaced candidate belongs in the final WHERE/WATCH OUT classification, so no distinct autonomous auditor owns the full judgment.
- Supporting / enforcement mechanisms: pre-run gatherEvidence; capture of successful searches and opened ranges; relines; splitByExistence; sweepSites/withoutMentioned; surroundings; missing-path resolution; bounded recheckTurns.
- Closure path: locate model answer → first-party direct filesystem/tree checks and replay of successful searches → omitted/invalid evidence detected → missed lines returned in recheckPrompt → model re-judges them in a bounded follow-up → replacement answer is checked again → checked result is rendered to the user.
- Boundary reachability: froe locate is a top-level shipped command and the same locate sequence is intentionally reusable from the first-party editor/RPC path. No external benchmark, reviewer product or application-authored glue is needed to invoke the complementary check/recheck loop.
- Why this is / is not agent-owned: removing the deterministic post-answer checker removes the independent evidence challenge and recheck trigger. Removing the model does not leave a complete semantic auditor, however; the runtime can identify unjudged candidate evidence but relies on the model to decide its meaning. That makes the first-party path a constructor S3* rather than autonomous S3*.
- Evidence: [cmd/froe/locate_run.go](https://github.com/dcoldeira/froe/blob/f23a0e5c31fe6c05c8d284750802f344e4a702f1/cmd/froe/locate_run.go); [cmd/froe/locate_evidence.go](https://github.com/dcoldeira/froe/blob/f23a0e5c31fe6c05c8d284750802f344e4a702f1/cmd/froe/locate_evidence.go); [cmd/froe/locate.go](https://github.com/dcoldeira/froe/blob/f23a0e5c31fe6c05c8d284750802f344e4a702f1/cmd/froe/locate.go); [README.md](https://github.com/dcoldeira/froe/blob/f23a0e5c31fe6c05c8d284750802f344e4a702f1/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the positive claim is deliberately narrow to the audit-specific locate workflow. The same-S1 verify/checklist/leftover nudges in froe do and the offline eval/ suite are not independently promoted to S3*. Constructor credit reflects the supplied complementary evidence/feedback path, not an independently model-owned reviewer.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material external-and-prospective organizational adaptation loop is established.
- Disturbance / variety regulated: durable memories, current project instructions, task-dependent model choice and resumed sessions change present execution context, but they do not sense future environmental change and select a capability/strategy adaptation for subsequent operation.
- Decisive decision or feedback right: not established at S4 scope.
- Decision owner: not established.
- Supporting / enforcement mechanisms: SQLite project memories; model-callable remember tool; session history/resume; project map/instructions; context budgeting; current task/model routing in the editor.
- Closure path: memories and instructions are injected into later current-task prompts, but no prospective scan → adaptation option → selected persistent capability/strategy change → return-to-operation loop was found.
- Why this is / is not agent-owned: remember preserves reusable project facts learned during operations, and routing chooses a model for the current task. Those are memory/current execution adaptations, not the Profile's outside-and-then intelligence function.
- Evidence: [internal/tools/remember.go](https://github.com/dcoldeira/froe/blob/f23a0e5c31fe6c05c8d284750802f344e4a702f1/internal/tools/remember.go); [internal/session/store.go](https://github.com/dcoldeira/froe/blob/f23a0e5c31fe6c05c8d284750802f344e4a702f1/internal/session/store.go); [docs/ROADMAP.md](https://github.com/dcoldeira/froe/blob/f23a0e5c31fe6c05c8d284750802f344e4a702f1/docs/ROADMAP.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: project memory can be agent-authored and durable, but learning/persistence alone is insufficient for S4 without a prospective environmental adaptation loop.

### Absence scope

- Surfaces inspected: memory tool/store and future injection; session resume; project context/instruction loading; model routing; roadmap; eval/; provider registry; agent loop.
- Plausible first-party paths checked: durable learned facts, dynamic model selection, benchmark-driven model changes, roadmap/evaluation feedback, self-update/evolution and capability installation.
- Why no material first-party path remains: inspected mechanisms preserve or select current operating context/capability; no supported path converts external future-oriented intelligence into an enacted organizational adaptation.

## S5 — Policy and identity

- State: —
- Function: no material runtime identity or ultimate-policy closure is established at the assessed recursion.
- Disturbance / variety regulated: system prompts, project instructions, permission modes, hard denials and user configuration constrain operation, but no first-party process adjudicates an identity/ultimate-policy issue and returns that resolution as authoritative organizational policy.
- Decisive decision or feedback right: not established at S5 scope.
- Decision owner: not established inside the reviewed organization.
- Supporting / enforcement mechanisms: default system prompt; FROE.md/CLAUDE.md/AGENTS.md project guidance; permission modes; hard denylist; provider/model configuration; user task and host privileges.
- Closure path: static or user-authored instructions/configuration are loaded directly into current operation. No identity/policy issue is escalated to a legitimate S5 authority, decided there, and returned as a governing policy change for later operation.
- Why this is / is not agent-owned: the model acts under supplied project guidance and safety constraints but has no authority to redefine Froe's identity or ultimate policy. Generic user approval and editable instruction files do not by themselves establish S5.
- Evidence: [cmd/froe/do.go](https://github.com/dcoldeira/froe/blob/f23a0e5c31fe6c05c8d284750802f344e4a702f1/cmd/froe/do.go); [internal/repo/instructions.go](https://github.com/dcoldeira/froe/blob/f23a0e5c31fe6c05c8d284750802f344e4a702f1/internal/repo/instructions.go); [internal/perms/perms.go](https://github.com/dcoldeira/froe/blob/f23a0e5c31fe6c05c8d284750802f344e4a702f1/internal/perms/perms.go).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: project owners can author durable instructions and users can choose permission modes, but those configuration paths do not demonstrate first-party identity/ultimate-policy adjudication and returned closure.

### Absence scope

- Surfaces inspected: system prompt; project instruction discovery/precedence; permission modes and denials; model/provider registry; memory/session state; CLI/RPC configuration; architecture and roadmap.
- Plausible first-party paths checked: agent-authored policy change, project-owner policy escalation, runtime constitutional/mission updates, governance commands, approval decisions and durable instruction reload.
- Why no material first-party path remains: authority remains externally supplied as task/configuration/instructions and no runtime identity/ultimate-policy decision loop is implemented.

## Recursion

The reviewed distribution has one primary model-backed coding S1 per run/session. Terminal and Neovim are front ends to the same runtime. Separate sessions and process-safe persistence do not create a coordinated higher-recursion organization, and the architecture explicitly defers multi-agent/subagent spawning.

## Variety and escalation

Froe amplifies operational variety through model discretion, repository search/read/edit/write/bash/Git tools, project context, memory and multiple provider strategies. It attenuates failure variety through permissions, hard denials, turn/context budgets, repeated-call detection, result caching, completion nudges and the locate-specific complementary sweep.

Exceptional local failures can stop a run, return tool errors to the model, request human permission, or surface checked locate discrepancies. These are bounded operational/audit escalation paths; they do not establish separate S3, S4 or S5 ownership.

## Evidence gaps

The assessment is revision-relative to f23a0e5c31fe6c05c8d284750802f344e4a702f1. External model/runtime internals were not imported. Offline eval fixtures were inspected as corroborating development infrastructure but excluded from operating ownership. The complete frozen tree and the plausible S2-S5 paths identified above were inspected, so no unresolved evidence gap requires a question-mark state.

## Assessment summary

Froe closes autonomous coding S1 through its shipped model/tool feedback loop. It deliberately remains single-agent at this revision, so no material S2 or whole-system S3 path is present. Its locate command does ship a materially complementary direct-project evidence sweep that can contradict an answer and return missed evidence for a bounded recheck; because that audit-specific judgment/closure is supplied as a deterministic constructor around the same model rather than an independent autonomous auditor, S3* is C. Durable memory, project instructions, routing and safety policy remain current-operation/context mechanisms rather than S4 or S5 closure.

Proposed vector: **A · — · — · C · — · —**
