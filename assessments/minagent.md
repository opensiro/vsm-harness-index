---
harness_id: minagent
project_name: MinAgent
repository: https://github.com/Nichonauta/MinAgent
review_ref: 02880e3c981ba57cd95d2266d6c0ea07b1abe44c
reviewed_at: 2026-10-02
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-02
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: A
autonomy_s5: —
---

# MinAgent

## Review boundary

- System in focus: one first-party MinAgent terminal coding-agent composition at frozen revision `02880e3c981ba57cd95d2266d6c0ea07b1abe44c`, including the model/tool conversation loop, workspace file tools, optional terminal/MCP/skills surfaces, context compaction, workspace inventory and `AGENTS.md` project-guidance lifecycle, including the documented `/init` adaptation path.
- Purpose and identity: perform coding work against the launch workspace through a model-driven tool loop while maintaining enough project context and persistent guidance for later work.
- Relevant environment: the user's coding requests and approvals; workspace/repository structure, source files and `AGENTS.md`; file/process/tool results; model-provider responses; configured MCP servers and local skills.
- Standard-distribution boundary: shipped Node.js runtime and built-in commands/tools reached from the documented `minagent` launch path are inside. External model servers, MCP servers, user-authored skill resources, operating-system shell behaviour and user-edited project files are adjacent inputs/dependencies unless first-party MinAgent wiring explicitly closes a credited path through them.
- Credited operating / distribution surfaces: `README.md`; `src/minagent.mjs`; `src/init-project.mjs`; `src/workspace.mjs`; `src/context.mjs`; `src/openai.mjs`; `src/config.mjs`; `src/skills.mjs`; `src/mcp.mjs`; `src/terminal-command.mjs`.
- Adjacent first-party surfaces excluded from ownership: tests as authority by themselves, documentation-only claims without runtime reachability, external model/MCP decision making, and any manually authored downstream skill or `AGENTS.md` content not produced through MinAgent's own `/init` path.
- First-party operating / deployment modes considered: interactive MinAgent session; built-in workspace tools; terminal modes `auto`/`ask`/`off`; optional local skills and MCP tools; automatic/manual compaction; `/init` project adaptation; `/new`; standard workspace refresh before model requests.
- Recursion level: one MinAgent coding session is the assessed organization. The model actor and its tool loop form the operational S1. External MCP servers and shell processes are tools/dependencies, not automatically separate S1 units at this recursion.
- Reviewed revision: `02880e3c981ba57cd95d2266d6c0ea07b1abe44c`.
- Observation date: 2026-10-02.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

`src/minagent.mjs` owns one iterative assistant/tool loop. Before each model turn it refreshes workspace context and compacts history if necessary, then invokes the configured model with tool schemas. Tool calls are parsed and executed through first-party file/terminal/skill/MCP dispatch; results are appended as tool messages and returned to the same model on the next round. A response can continue for up to 32 tool rounds, while deterministic limits, workspace checks and optional approvals constrain execution without selecting the substantive coding action.

The strongest higher-function path is the documented `/init` command. `src/init-project.mjs` selects bounded project evidence from the workspace. `initializeProject` in `src/minagent.mjs` asks the model to create or update root `AGENTS.md` from the inventory and selected project files, specifically capturing project architecture, important directories, confirmed commands, code conventions and relevant checks. MinAgent writes the model-produced file and immediately refreshes workspace context. `src/workspace.mjs` reloads root `AGENTS.md` before each subsequent model request, so the model-authored project adaptation becomes durable present operating guidance rather than a transient answer or conversation-memory update.

Other plausible higher-function surfaces remain support rather than separate VSM closures. Context compaction summarizes earlier conversation to maintain the same operating session; skills and MCP expose externally supplied tools/instructions; workspace write verification confirms requested bytes after a file operation; terminal `ask` and MCP approvals leave particular tool authority with the user. There is no first-party population of operational S1 units, no whole-current control function above them, no materially independent complementary operational audit path, and no runtime identity/ultimate-policy authority loop.

Primary evidence:

- [`README.md`](https://github.com/Nichonauta/MinAgent/blob/02880e3c981ba57cd95d2266d6c0ea07b1abe44c/README.md)
- [`src/minagent.mjs`](https://github.com/Nichonauta/MinAgent/blob/02880e3c981ba57cd95d2266d6c0ea07b1abe44c/src/minagent.mjs)
- [`src/init-project.mjs`](https://github.com/Nichonauta/MinAgent/blob/02880e3c981ba57cd95d2266d6c0ea07b1abe44c/src/init-project.mjs)
- [`src/workspace.mjs`](https://github.com/Nichonauta/MinAgent/blob/02880e3c981ba57cd95d2266d6c0ea07b1abe44c/src/workspace.mjs)

## Operational model

A user submits a coding request. The model receives current system/workspace guidance and chooses tool calls or a final answer. MinAgent executes permitted tools, records their actual results and returns those results to the same model so later decisions can adapt to repository/process evidence. Separately, when the documented `/init` mode is invoked, MinAgent samples durable project evidence and delegates the content decision for a future-facing project guidance artifact to the model; the resulting `AGENTS.md` is persisted and then loaded into later operational turns.

## S1 — Operations

- State: A
- Function: transform a coding request into repository/process work or a task answer through model-selected actions with returned environment feedback.
- Disturbance / variety regulated: repository/file state, implementation alternatives, tool and process results, endpoint uncertainty, context pressure, workspace guidance and user corrections.
- Decisive decision or feedback right: choose the next substantive coding/tool action and revise subsequent choices from returned environment evidence.
- Decision owner: the configured model actor inside the first-party MinAgent conversation loop.
- Supporting / enforcement mechanisms: tool dispatcher, workspace confinement and write verification, terminal/MCP approval gates, context compaction, token/tool-round limits, skills/MCP adapters and streaming client.
- Closure path: user objective/current context → model chooses tool call or answer → first-party MinAgent executes the permitted action → actual result is appended as a tool message → the same model receives that result and chooses another action or final response.
- Boundary reachability: the documented `minagent`/`node src/minagent.mjs` entrypoint directly instantiates this shipped loop; built-in file tools and optional terminal/skills/MCP tools are presented through that same standard runtime.
- Why this is / is not agent-owned: if the model actor is removed while tool schemas, workspace protections, limits and approvals remain, the runtime can enforce preselected constraints but does not choose task-specific coding actions. The substantive operational discretion therefore belongs to the model actor.
- Evidence: [`README.md`](https://github.com/Nichonauta/MinAgent/blob/02880e3c981ba57cd95d2266d6c0ea07b1abe44c/README.md); [`src/minagent.mjs`](https://github.com/Nichonauta/MinAgent/blob/02880e3c981ba57cd95d2266d6c0ea07b1abe44c/src/minagent.mjs); [`src/workspace.mjs`](https://github.com/Nichonauta/MinAgent/blob/02880e3c981ba57cd95d2266d6c0ea07b1abe44c/src/workspace.mjs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: model inference occurs through an external compatible endpoint, but first-party MinAgent closes its decisions through the workspace/tool feedback loop.

## S2 — Coordination

- State: —
- Function: no material inter-S1 disturbance-attenuation function is supplied at the assessed recursion.
- Disturbance / variety regulated: no interaction-generated conflict or oscillation among multiple operational S1 units is established because the standard MinAgent composition exposes one primary operational agent loop.
- Distinct S1 units: not established. Built-in tools, shell commands, MCP servers and skills are capabilities/dependencies used by the one operating agent rather than first-party autonomous operational units with their own durable local outcome/autonomy at this recursion.
- Inter-S1 disturbance: not established.
- Attenuating coordination relation: not established.
- Feedback into subsequent S1 behaviour: tool results feed the same S1's next decision, not a coordination outcome among distinct S1s.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: it is not; the inspected paths are tool invocation, request sequencing and context transport inside one operational loop.
- Decisive decision or feedback right: not established for S2.
- Decision owner: not established.
- Supporting / enforcement mechanisms: sequential tool-round loop, tool-call count limits, MCP/skill dispatch and process/file execution.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: the model owns one S1's next action, but there is no separate coordination function over multiple S1s to own.
- Evidence: [`README.md`](https://github.com/Nichonauta/MinAgent/blob/02880e3c981ba57cd95d2266d6c0ea07b1abe44c/README.md); [`src/minagent.mjs`](https://github.com/Nichonauta/MinAgent/blob/02880e3c981ba57cd95d2266d6c0ea07b1abe44c/src/minagent.mjs).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: downstream users can connect external multi-agent MCP systems, but adjacent external compositions do not create first-party S2 for MinAgent itself.

### Absence scope

- Surfaces inspected: main model/tool loop, built-in workspace tools, terminal execution, MCP tool exposure, local skills, process cleanup, tool-round/tool-call caps and conversation state.
- Plausible first-party paths checked: MCP servers as separate S1 units, shell processes as S1s, multiple requested tool calls as parallel operations, skills as operational agents and request sequencing as coordination.
- Why no material first-party path remains: every inspected path is a capability or transport used by one primary operational model loop. No first-party standard mode establishes multiple S1 units plus a specific interaction disturbance, attenuation relation and feedback to subsequent S1 behaviour.

## S3 — Inside-and-now control

- State: —
- Function: no separate whole-system current-control function is established above the single operating MinAgent S1.
- Disturbance / variety regulated: context pressure, tool limits, terminal permissions and workspace boundaries are regulated locally, but there is no population-level current resource/commitment control on behalf of a larger operational whole.
- Decisive decision or feedback right: not established for S3.
- Decision owner: not established.
- Supporting / enforcement mechanisms: token/context budgets, automatic compaction, tool-round limits, terminal/MCP approval, process cleanup and workspace safety checks.
- Closure path: not applicable for the negative finding.
- Whole-system current view: MinAgent can estimate its own context, refresh its own workspace snapshot and track its own conversation/tool state; this is the current state of one S1 task, not a whole-system view over several autonomous operational commitments.
- Current-control decision scope: deterministic limits and user approvals constrain one session. No separate actor allocates resources, priorities, commitments or interventions across autonomous S1 units.
- Why this is / is not agent-owned: the model regulates its coding actions as S1, while deterministic runtime mechanisms regulate service/context bounds. Neither establishes a distinct S3 function at the chosen recursion.
- Evidence: [`README.md`](https://github.com/Nichonauta/MinAgent/blob/02880e3c981ba57cd95d2266d6c0ea07b1abe44c/README.md); [`src/minagent.mjs`](https://github.com/Nichonauta/MinAgent/blob/02880e3c981ba57cd95d2266d6c0ea07b1abe44c/src/minagent.mjs).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: current-state visibility is real but remains local operational state rather than metasystemic whole-current control.

### Absence scope

- Surfaces inspected: `/context`, automatic/manual compaction, request/tool-round limits, workspace refresh, process cleanup, terminal/MCP approvals and configuration.
- Plausible first-party paths checked: context accounting as whole-system view, compaction as S3 intervention, tool limits as resource control, approval gates as current-control authority and process cleanup as S3 supervision.
- Why no material first-party path remains: these mechanisms preserve or constrain one operating session. No first-party path observes a whole of distinct operational units and closes a substantive resource/commitment/priority decision back into their current operation.

## S3* — Complementary audit

- State: —
- Function: no material complementary operational-audit loop with sufficiently independent access and returned corrective control is established.
- Disturbance / variety regulated: workspace operations use strong inline validation, but the standard runtime does not supply a separate complementary observer that can challenge ordinary S1 claims through materially different access.
- Decisive decision or feedback right: not established for S3*.
- Decision owner: not established.
- Supporting / enforcement mechanisms: atomic workspace operations, post-write reread/byte comparison, path identity checks, ordinary tool results and tests outside the assessed runtime.
- Closure path: not applicable; inline execution validation returns the result of the same operation, not an independent audit finding into organizational control.
- Claim being audited: no distinct operational claim is assigned to a complementary auditor.
- Ordinary reporting path: built-in tool execution returns actual file/process results as tool messages to the operating model.
- Complementary access path: not established. Post-write verification rereads the just-written target as part of the same first-party tool operation; it does not constitute alternative, sporadic or organizationally independent access beyond the normal production path.
- Independence boundary: none qualifying in the standard distribution. External MCP services or developer tests are adjacent unless specifically composed into the runtime and do not establish first-party audit ownership here.
- Who acts on findings: ordinary tool errors/results return to the operating model as S1 feedback; there is no distinct S3* finding/return path.
- Why this is / is not agent-owned: the model can react to tool failures, while deterministic file validation supports safe execution. No separate agent owns a complementary audit judgment.
- Evidence: [`README.md`](https://github.com/Nichonauta/MinAgent/blob/02880e3c981ba57cd95d2266d6c0ea07b1abe44c/README.md); [`src/workspace.mjs`](https://github.com/Nichonauta/MinAgent/blob/02880e3c981ba57cd95d2266d6c0ea07b1abe44c/src/workspace.mjs); [`src/minagent.mjs`](https://github.com/Nichonauta/MinAgent/blob/02880e3c981ba57cd95d2266d6c0ea07b1abe44c/src/minagent.mjs).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: strong verification is credited as operational safety evidence, not promoted to S3* without complementary independence.

### Absence scope

- Surfaces inspected: file read/write integrity checks, post-write verification, tool error feedback, tests, context reporting, MCP boundary and terminal approval.
- Plausible first-party paths checked: write verification as audit, path checks as independent inspection, external MCP as reviewer, tests as runtime audit and user approval as S3*.
- Why no material first-party path remains: the strongest checks are inline with the ordinary tool path and test whether that same operation succeeded. They do not add a materially independent route to operational reality plus a distinct audit judgment and corrective return closure.

## S4 — Outside-and-then adaptation

- State: A
- Function: model the current project/workspace environment and turn those distinctions into durable project-specific guidance that changes later MinAgent operation.
- Disturbance / variety regulated: variation in repository architecture, important directories, build/test commands, conventions, checks and stale or missing project guidance that would otherwise force later coding turns to rediscover project-specific operating knowledge.
- Decisive decision or feedback right: decide what project distinctions matter and what durable architecture/command/convention/check guidance should be written into the root `AGENTS.md` for subsequent operation.
- Decision owner: the configured model actor invoked by MinAgent's first-party `/init` path.
- Supporting / enforcement mechanisms: deterministic project-file candidate scoring/selection, workspace inventory, bounded file excerpts, secret redaction, atomic workspace write, workspace refresh and automatic `AGENTS.md` reload before model requests.
- Closure path: `/init` invocation → first-party inventory and selected project evidence → model develops project-specific future operating guidance → MinAgent writes/updates root `AGENTS.md` → workspace refresh reloads that guidance → subsequent S1 model requests include it in the system prompt and can operate differently under the returned adaptation.
- Boundary reachability: `/init [focus]` is a documented built-in command in the standard interactive runtime; its implementation calls `collectProjectEssentials`, invokes the configured model, writes `AGENTS.md`, and refreshes the same first-party workspace context used by later requests.
- External distinction: repository/workspace evidence outside the harness itself, including project architecture, important files, commands, conventions and checks selected from the current project.
- Future / prospective distinction: the generated guidance explicitly captures project knowledge intended to shape later coding work rather than merely answer the current request; stale existing guidance is to be corrected for subsequent use.
- Adaptation option generated: the model selects and synthesizes the complete project-specific `AGENTS.md` content from the observed evidence, including which architecture facts, commands, conventions and checks should become durable guidance.
- Path back into current capability / S3: MinAgent persists the selected adaptation as root `AGENTS.md`; `refreshWorkspaceSnapshot` loads it, and workspace inventory reloads `AGENTS.md` before every later model request into the system prompt.
- Why this is / is not agent-owned: the user triggers `/init` and may optionally supply focus, but deterministic selection/writing machinery does not determine the substantive project guidance. If the model actor is removed, the runtime still has an inventory and writer but no autonomous decision over what durable adaptation to synthesize from project evidence. The decisive adaptation judgment is therefore model-owned.
- Evidence: [`README.md`](https://github.com/Nichonauta/MinAgent/blob/02880e3c981ba57cd95d2266d6c0ea07b1abe44c/README.md); [`src/minagent.mjs`](https://github.com/Nichonauta/MinAgent/blob/02880e3c981ba57cd95d2266d6c0ea07b1abe44c/src/minagent.mjs); [`src/init-project.mjs`](https://github.com/Nichonauta/MinAgent/blob/02880e3c981ba57cd95d2266d6c0ea07b1abe44c/src/init-project.mjs); [`src/workspace.mjs`](https://github.com/Nichonauta/MinAgent/blob/02880e3c981ba57cd95d2266d6c0ea07b1abe44c/src/workspace.mjs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: `/init` is user-invoked rather than continuously scheduled, but invocation is not the decisive adaptation judgment. No distinct parent-governed S4 mode is claimed merely because a human can invoke or manually edit project guidance.

## S5 — Identity / ultimate policy

- State: —
- Function: no material runtime identity/ultimate-policy authority loop is established.
- Disturbance / variety regulated: system prompts, `AGENTS.md`, tool/workspace boundaries, terminal mode and MCP approval constrain operation, but the strongest policy premises are externally configured or belong to ordinary task/tool governance rather than runtime identity-level adjudication.
- Decisive decision or feedback right: not established for S5.
- Decision owner: user/operator and static first-party configuration for the strongest candidate policy constraints; the model owns S1 task decisions and S4 project-guidance synthesis, not ultimate organizational identity/policy.
- Supporting / enforcement mechanisms: base system prompt, `AGENTS.md`, workspace boundary, `TERMINAL_MODE`, MCP approval, configuration validation, tool-call/round limits and skills/MCP enablement flags.
- Closure path: not applicable for the negative finding; constraints are loaded/enforced or per-call approval is requested, but no identity/ultimate-policy issue is adjudicated by a legitimate runtime ultimate authority and returned as a revised governing premise.
- Identity / ultimate-policy issue: no first-party standard path frames a genuine MinAgent identity or ultimate-policy dispute for runtime resolution. `/init` adapts project-operating guidance and therefore maps to S4, not S5.
- Ultimate authority: user/operator and shipped/configured constraints for tool permissions and runtime setup; no autonomous ultimate-policy actor is established.
- Return-to-operation path: configured modes and approvals immediately affect ordinary tool execution, and generated `AGENTS.md` affects later work, but these paths do not carry an identity/ultimate-policy decision. The latter is already credited to project adaptation under S4.
- Why this is / is not agent-owned: the model cannot autonomously redefine the runtime's ultimate workspace/approval/configuration premises through a first-party identity-governance loop. Removing the human/config sources leaves enforcement machinery but not an S5 decision process.
- Evidence: [`README.md`](https://github.com/Nichonauta/MinAgent/blob/02880e3c981ba57cd95d2266d6c0ea07b1abe44c/README.md); [`src/minagent.mjs`](https://github.com/Nichonauta/MinAgent/blob/02880e3c981ba57cd95d2266d6c0ea07b1abe44c/src/minagent.mjs); [`src/config.mjs`](https://github.com/Nichonauta/MinAgent/blob/02880e3c981ba57cd95d2266d6c0ea07b1abe44c/src/config.mjs); [`src/workspace.mjs`](https://github.com/Nichonauta/MinAgent/blob/02880e3c981ba57cd95d2266d6c0ea07b1abe44c/src/workspace.mjs).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: durable project guidance is not treated as identity merely because it is loaded into the system prompt; its documented purpose is project-specific future operating knowledge.

### Absence scope

- Surfaces inspected: base system prompt, `AGENTS.md` load/write path, `/init`, configuration/environment settings, workspace confinement, terminal modes, MCP approval, skills/MCP enablement and tool/round limits.
- Plausible first-party paths checked: generated `AGENTS.md` as S5 policy, system prompt as identity, workspace boundary as constitution, terminal/MCP approval as ultimate authority and configuration flags as policy selection.
- Why no material first-party path remains: these surfaces either implement the S4 project-adaptation path, enforce fixed constraints, or delegate ordinary tool/config decisions to the operator. No first-party loop presents a genuine identity/ultimate-policy matter to an ultimate authority and returns that decision as the governing premise of later operation.

## Summary

- Vector: **A · — · — · — · A · —**.
- MinAgent closes an autonomous coding-operation loop (S1=A) and, unusually for a small single-agent harness, also exposes an autonomous project-adaptation loop through `/init` (S4=A): project evidence is modeled into persistent `AGENTS.md` guidance that is reloaded into subsequent operation. No qualifying S2, S3, S3* or S5 closure is established at the reviewed boundary.
