---
harness_id: openags
project_name: OpenAGS
repository: https://github.com/openags/auto-researcher
review_ref: 9bb9dfc6d5e66ad92e3652c8a2ed250d62f8c11f
reviewed_at: 2026-09-20
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: A
autonomy_s5: —
---

# OpenAGS

## Review boundary

- System in focus: one OpenAGS autonomous research project using the first-party folder-as-agent organization, coordinator, builtin agent engine, specialist research modules, shared file workspaces, and review/iteration protocol.
- Purpose and identity: coordinate autonomous specialist agents across the scientific lifecycle from idea/literature through proposal, experiments, manuscript, peer review, and iterative revision.
- Relevant environment: user research brief/uploads, external scientific literature/web, executable experiment environment, project filesystem, model providers, and research artifacts produced by prior stages.
- Standard-distribution boundary: the first-party OpenAGS builtin agent engine and research-project templates/orchestration. Optional Claude Code/Codex/Cursor/Gemini CLI runtimes are alternate external worker runtimes and are not borrowed as VSM owners where builtin first-party closure is available.
- Credited operating / distribution surfaces: OpenAGS `agent/` engine and builtin `Agent.loop`, research project folder/agent model, coordinator `SOUL.md`, specialist SOUL/skills, file-based upstream/downstream protocol, workflow orchestrator, and default research template.
- Adjacent first-party surfaces excluded from ownership: desktop UI, provider adapters for third-party CLI agents, PTY terminal, CI/release surfaces, examples/tests, and presentation-only renderer code. Third-party CLI agents and model providers are dependencies/alternate runtimes rather than imported organizational functions.
- First-party operating / deployment modes considered: OpenAGS builtin-agent autonomous workflow (`Auto Mode`) using the default research project template.
- Recursion level: one research project as the viable system; literature, proposal, experiments, manuscript, and review agents are the main S1 operational units, with the root coordinator acting across them.
- Reviewed revision: `9bb9dfc6d5e66ad92e3652c8a2ed250d62f8c11f`.
- Observation date: 2026-09-20.
- Generated Profile version: 0.2.3.
- Generated Methodology version: 0.3.5.
- Current Profile version: 0.2.3.
- Current Methodology version: 0.3.5.

## Repository architecture

OpenAGS explicitly separates a self-contained first-party agent engine, a scientific project-management layer, and UI/provider integrations. In builtin mode, the Python orchestrator reads an agent folder's `SOUL.md`, creates the first-party Agent, loads skills/memory, calls the LLM through LiteLLM, executes tool calls, returns tool results to message history, and loops until completion. The project organization is represented directly in the filesystem: each specialist has its own folder, SOUL, skills, memory/status/task files, and declared upstream/downstream artifacts.

The root coordinator is a distinct agent. In Auto Mode it reads all specialist status files, assigns tasks, decides what happens next, and after the first full research pass reads peer-review findings and decides which stages to rerun. The review agent has a separate role and complementary access to the manuscript, experiment report, literature notes, and web search; it produces an actionable review report that the coordinator consumes. Literature output is an upstream input to proposal and later work, providing a separate outside-and-then research-intelligence path.

Primary evidence: [architecture and builtin Agent execution](https://github.com/openags/auto-researcher/blob/9bb9dfc6d5e66ad92e3652c8a2ed250d62f8c11f/docs/architecture.md), [coordinator SOUL](https://github.com/openags/auto-researcher/blob/9bb9dfc6d5e66ad92e3652c8a2ed250d62f8c11f/templates/default/SOUL.md), [reviewer SOUL](https://github.com/openags/auto-researcher/blob/9bb9dfc6d5e66ad92e3652c8a2ed250d62f8c11f/templates/default/review/SOUL.md).

## Operational model

Specialist agents autonomously produce research artifacts through first-party Agent loops. The coordinator does not perform the specialist research itself; it owns the cross-project scheduling/current-control decisions. Shared files provide the ordinary work/reporting path. The reviewer separately interrogates manuscript claims against experiments/literature and external citation checks, then writes findings that the coordinator uses to determine subsequent work. The literature agent performs environment-facing scientific sensing whose output changes the proposal/experiment program.

## S1 — Operations

- State: A
- Function: specialist research agents perform the operational scientific work: literature review, proposal development, experiments, manuscript production, and peer review/revision artifacts.
- Disturbance / variety regulated: open-ended scientific questions, external literature, experiment implementation/execution, result interpretation, and manuscript construction.
- Decisive decision or feedback right: choose the next specialist reasoning/tool/file action needed to produce each role's research outcome within its SOUL/skill contract.
- Decision owner: each first-party builtin OpenAGS Agent executing the corresponding specialist folder/role.
- Supporting / enforcement mechanisms: SOUL and skill loading, tool engine, memory/session/history, filesystem workspaces, upstream/downstream paths, LiteLLM transport, timeouts, and orchestrator lifecycle.
- Closure path: observations/tool results return to the specialist Agent loop; the agent updates role artifacts/status and those outputs become available to downstream agents/coordinator.
- Boundary reachability: the repository documents a complete first-party builtin Agent path (`Agent.loop`) used by the research layer; S1 therefore does not depend on Claude Code/Codex/Cursor/Gemini owning the operational loop.
- Why this is / is not agent-owned: the first-party agent engine closes model decision → tool execution → observation → next decision inside the supported builtin mode.
- Evidence: [builtin-agent execution path](https://github.com/openags/auto-researcher/blob/9bb9dfc6d5e66ad92e3652c8a2ed250d62f8c11f/docs/architecture.md#%E8%B7%AF%E5%BE%84-1-openags-builtin-agentpython-%E5%90%8E%E7%AB%AF), [folder-as-agent model](https://github.com/openags/auto-researcher/blob/9bb9dfc6d5e66ad92e3652c8a2ed250d62f8c11f/docs/architecture.md#%E6%A0%B8%E5%BF%83%E6%A6%82%E5%BF%B5folder--agent), [default specialist workflow](https://github.com/openags/auto-researcher/blob/9bb9dfc6d5e66ad92e3652c8a2ed250d62f8c11f/templates/default/SOUL.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: alternate CLI-agent backends are not used to justify S1 ownership; the credited mode is the self-contained builtin OpenAGS agent engine.

## S2 — Coordination

- State: —
- Function: no material S2-specific regulation of a demonstrated inter-S1 conflict/oscillation is established at the declared project recursion.
- Disturbance / variety regulated: not established.
- Decisive decision or feedback right: not established as S2.
- Decision owner: not applicable.
- Supporting / enforcement mechanisms: upstream/downstream file contracts, fixed first-pass sequence, TASKS/STATUS files, agent dispatch, and shared project artifacts organize work but do not by themselves establish an inter-S1 interference witness.
- Closure path: workflow outputs feed downstream specialists, but that sequencing/dependency path is not sufficient for S2.
- Why this is / is not agent-owned: named multi-agent roles and communication through files are generic organization/hand-off primitives unless tied to a concrete conflict or oscillation between S1 units and an attenuation loop.
- Evidence: [file-based agent communication](https://github.com/openags/auto-researcher/blob/9bb9dfc6d5e66ad92e3652c8a2ed250d62f8c11f/docs/architecture.md#agent-%E9%97%B4%E9%80%9A%E4%BF%A1%E6%96%87%E4%BB%B6%E5%B0%B1%E6%98%AF%E9%80%9A%E4%BF%A1%E6%9C%BA%E5%88%B6), [coordinator first-pass sequence](https://github.com/openags/auto-researcher/blob/9bb9dfc6d5e66ad92e3652c8a2ed250d62f8c11f/templates/default/SOUL.md).
- Basis: structural negative finding.
- Confidence: high.
- Caveats: workflow dependency management may prevent some practical clashes, but the required S2-specific disturbance/attenuation witness is not established in the reviewed evidence.

### Absence scope

- Surfaces inspected: folder-as-agent architecture, upstream/downstream file contracts, coordinator dispatch/status logic, workflow orchestrator, specialist templates, agent engine, and review iteration.
- Plausible first-party paths checked: shared files, fixed first-pass ordering, TASKS/STATUS protocol, start/wait decisions, specialist dependencies, and agent dispatch.
- Why no material first-party path remains: these surfaces establish sequencing/delegation/reporting but not a concrete inter-S1 interference/conflict/oscillation plus a specific coordination relation that changes subsequent S1 behavior to attenuate it.

## S3 — Inside-and-now control

- State: A
- Function: maintain a whole-project current view and decide which specialist work starts, waits, reruns, or is complete.
- Disturbance / variety regulated: incomplete or failed stages, changing project status, downstream dependency readiness, review-identified weaknesses, and need to redirect current research effort.
- Decisive decision or feedback right: choose the next active specialist/task and, after the first pass, choose which research stages must rerun in response to current project evidence.
- Decision owner: the root coordinator Agent in Auto Mode.
- Supporting / enforcement mechanisms: specialist `STATUS.md` and `TASKS.md`, workflow/orchestrator process management, timeout/failure handling, fixed initial stage order, project files, and start/wait/all-complete action protocol.
- Closure path: coordinator reads current statuses/review findings, emits `start_agent`/`wait`/`all_complete`/`needs_human` decisions and writes/assigns specialist tasks; the orchestrator launches or withholds subsequent work accordingly.
- Boundary reachability: Auto Mode and the root coordinator are part of the default first-party project template and builtin workflow, not an external operator or development-only controller.
- Why this is / is not agent-owned: deterministic orchestration executes start/stop/status mechanics, while the coordinator Agent is explicitly instructed to make pipeline decisions and decide what happens next from the whole project state.
- Whole-system current view: all specialist status files, project-level memory/key decisions, current stage completion, and review outputs across the research project.
- Current-control decision scope: assignment and ordering of current specialist work, whether to wait, whether the project is complete, and which stages to rerun after review.
- Evidence: [coordinator Auto Mode and role](https://github.com/openags/auto-researcher/blob/9bb9dfc6d5e66ad92e3652c8a2ed250d62f8c11f/templates/default/SOUL.md), [workflow protocol](https://github.com/openags/auto-researcher/blob/9bb9dfc6d5e66ad92e3652c8a2ed250d62f8c11f/docs/workflow-protocol.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: fixed first-pass sequencing is enforcement/support; S3 credit comes from the coordinator's evidenced discretionary current-control decisions, especially status-based dispatch and post-review rerun choice.

## S3* — Complementary audit

- State: A
- Function: independently review the manuscript/research claims using complementary access to manuscript, experiment results, literature notes, and external citation verification, then return actionable findings into project control.
- Disturbance / variety regulated: unsupported claims, weak methodology/experiments, citation hallucination or misrepresentation, missing baselines/limitations, and paper-level weaknesses not caught by ordinary production.
- Decisive decision or feedback right: make peer-review judgments, classify major/minor concerns, score review criteria, issue a verdict, and prescribe a revision roadmap.
- Decision owner: the distinct review Agent.
- Supporting / enforcement mechanisms: dedicated review SOUL/folder, read access to manuscript/experiment/literature artifacts, web search for citation spot-checking, structured review format, and persisted `review-report.md`.
- Closure path: review findings are written under `review/reviews/`; after the first pass the coordinator reads those weaknesses and decides which stages need to rerun, returning audit findings into changed subsequent operation.
- Boundary reachability: the reviewer is a default specialist in the standard project template and a standard first-pass stage; its report is explicitly part of the coordinator's iteration mode.
- Why this is / is not agent-owned: the reviewer makes substantive adversarial/audit judgments rather than merely applying a deterministic syntax gate; the coordinator, not the reviewer, owns corrective project-control decisions.
- Claim being audited: the manuscript's scientific claims, citations, experimental support, logic, completeness, and reproducibility.
- Ordinary reporting path: manuscript output and specialist status/results flow normally into the project filesystem and coordinator.
- Complementary access path: the reviewer reads the full manuscript plus experiment report plus literature review and independently web-searches sampled citations; it is instructed to adversarially probe alternative explanations/failure conditions/missing experiments.
- Independence boundary: a separate review role/folder with its own SOUL and artifact is outside the manuscript-producing agent's ordinary production loop, while retaining direct access to underlying experiment/literature evidence.
- Who acts on findings: the root coordinator reads review weaknesses and selects which stages to rerun; affected specialists then perform the corrective work.
- Evidence: [reviewer SOUL](https://github.com/openags/auto-researcher/blob/9bb9dfc6d5e66ad92e3652c8a2ed250d62f8c11f/templates/default/review/SOUL.md), [coordinator iteration mode](https://github.com/openags/auto-researcher/blob/9bb9dfc6d5e66ad92e3652c8a2ed250d62f8c11f/templates/default/SOUL.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: model/provider independence is not claimed; organizational independence comes from the distinct review role, separate artifact, complementary evidence surfaces, and explicit findings-to-control return path.

## S4 — Outside-and-then intelligence

- State: A
- Function: sense the external scientific landscape through the literature specialist and turn those distinctions into future-facing research proposals/experiment direction consumed by later S1 work.
- Disturbance / variety regulated: risk of pursuing already-solved, poorly grounded, or scientifically irrelevant directions and missing externally established methods/results that should shape the project.
- Decisive decision or feedback right: select and synthesize externally retrieved papers/field distinctions that should inform the project proposal and later research program.
- Decision owner: the literature Agent, with downstream proposal/experiment agents autonomously using the returned research intelligence.
- Supporting / enforcement mechanisms: paper-search skills/web access, literature notes/memory, fixed upstream paths, shared project filesystem, and coordinator sequencing.
- Closure path: literature agent searches/reads external work and writes literature notes; the proposal agent explicitly reads `../literature/notes/` and `memory.md`; experiment/manuscript stages consume the proposal/literature outputs, changing subsequent project work.
- Boundary reachability: literature is a default first-party specialist stage in the project template, and its artifacts are wired as upstream inputs to subsequent specialists in every supported runtime.
- Why this is / is not agent-owned: the first-party literature Agent decides what external evidence is relevant and synthesizes it; file plumbing only returns that intelligence to current capability.
- External distinction: current prior papers, methods, results, and gaps retrieved from outside the project.
- Future / prospective distinction: which field gaps/constraints should shape the proposal and experiments the project has not yet executed.
- Adaptation option generated: literature-grounded research/proposal directions and constraints for experiment design.
- Path back into current capability / S3: persisted literature notes become explicit upstream inputs to proposal and later experiment/manuscript work under coordinator sequencing.
- Evidence: [folder/agent upstream-downstream architecture](https://github.com/openags/auto-researcher/blob/9bb9dfc6d5e66ad92e3652c8a2ed250d62f8c11f/docs/architecture.md), [research workflow skill](https://github.com/openags/auto-researcher/blob/9bb9dfc6d5e66ad92e3652c8a2ed250d62f8c11f/skills/research-workflow/SKILL.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: project memory and peer review alone are not used to justify S4; the credit rests on external scientific sensing and a closed return path into future project work.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy closure is established at the research-project recursion.
- Disturbance / variety regulated: not established at S5 scope.
- Decisive decision or feedback right: not established.
- Decision owner: not applicable.
- Supporting / enforcement mechanisms: SOUL role definitions, user project brief, templates, skills, provider configuration, and `needs_human` escalation constrain operation but do not themselves establish ultimate-policy governance.
- Closure path: no evidenced identity/policy issue → legitimate ultimate authority → authoritative decision → returned operation loop is established.
- Why this is / is not agent-owned: the coordinator manages current work but is not shown redefining the project's ultimate identity/policy; generic human input/escalation is not automatically parent-governed S5.
- Evidence: [coordinator SOUL](https://github.com/openags/auto-researcher/blob/9bb9dfc6d5e66ad92e3652c8a2ed250d62f8c11f/templates/default/SOUL.md), [architecture](https://github.com/openags/auto-researcher/blob/9bb9dfc6d5e66ad92e3652c8a2ed250d62f8c11f/docs/architecture.md).
- Basis: structural negative finding.
- Confidence: high.
- Caveats: a user can direct a project and the coordinator can request human input, but neither fact alone establishes S5 without a genuine ultimate-policy issue and authoritative return path.

### Absence scope

- Surfaces inspected: project/root SOUL, specialist role definitions, workflow protocol, human-input action, skills, provider configuration, project memory, and template lifecycle.
- Plausible first-party paths checked: project brief, root coordinator authority, `needs_human`, editable SOUL/skills, memory, and workflow configuration.
- Why no material first-party path remains: reviewed paths define or manage operations but do not establish a runtime identity/ultimate-policy dispute/proposal reaching a legitimate authority and returning as binding policy to subsequent operation.

## Recursion

One OpenAGS research project is the declared viable system. Specialist folders are S1 units at that recursion; the coordinator acts across them. Each specialist uses the first-party Agent engine internally, so a specialist can also be analyzed as a lower recursion, but this assessment does not import lower-level feature names as higher-level VSM functions. Alternate CLI agents are runtime substitutions rather than additional organizational units by default.

## Variety and escalation

OpenAGS absorbs research variety by specialization, persistent file workspaces, memories/status, tool-capable builtin agents, coordinator dispatch, review-driven iteration, and explicit failure/timeout handling. Specialists can surface failed/blocked states through status files; the coordinator can wait, assign/reassign work, declare completion, or request human input. `needs_human` is recorded as an escalation mechanism but not promoted to S5 without identity-level content.

## Evidence gaps

- Reassess S2 if OpenAGS adds an explicit first-party conflict/oscillation detector and coordination relation among specialist S1 units rather than only dependency sequencing.
- Reassess S5 if a supported project mode introduces a genuine ultimate-policy/identity proposal or dispute with explicit parent/agent authority and a returned binding decision.
- If builtin Agent execution is removed in favor of third-party CLI-only operation, reassess S1 ownership instead of silently borrowing the external harness's operational loop.
