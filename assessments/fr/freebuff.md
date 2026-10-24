---
harness_id: freebuff
project_name: Freebuff
repository: https://github.com/CodebuffAI/freebuff
review_ref: 8ed5d3e5e58b6a7ea1351efcbaa967b2dc015073
reviewed_at: 2026-10-22
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Freebuff

## Review boundary

- System in focus: the first-party Freebuff **terminal coding-agent distribution** at `CodebuffAI/freebuff@8ed5d3e5`, including the CLI's selected root agent, bundled SDK/runtime and first-party terminal/file tools. This is not a general assessment of the separately hosted Freebuff company or the broader Codebuff OSS framework as another system.
- Purpose and identity: receive a coding request, inspect and change a working project, execute tools/tests, and return the result to the user.
- Relevant environment: the user's repository and terminal, file/system/tool outcomes, model-provider responses, project instructions, local sessions, and user input/interruptions.
- Standard-distribution boundary: the source-built Freebuff CLI entry (`freebuff/cli` using `cli/`) and its bundled `base3-free-*` model-specific roots, `sdk/`, and `packages/agent-runtime/`. The selected Freebuff CLI mode is LITE and the compiled CLI harness constant is `base3`; unsupported custom agent extensions are not credited as default behavior.
- Credited operating / distribution surfaces: `freebuff/cli/build.ts`, `cli/src/utils/freebuff-agent-selection.ts`, `cli/src/utils/constants.ts`, `agents/base3.ts`, the `agents/base3-free-*` definitions, `sdk/src/run.ts`, `sdk/src/client.ts`, `packages/agent-runtime/src/run-agent-step.ts`, and first-party tool handlers under `packages/agent-runtime/src/tools/`.
- Adjacent first-party surfaces excluded from ownership: repository development CI, tests/evals, public agent-definition examples and legacy/rollback `base2` reviewer/parallel-subagent patterns not selected by the distributed Freebuff CLI; separately advertised Desktop/Web/Cloud/Chat product deployment and provider-side orchestration without sufficient inspected source at this frozen commit; external Claude Code/Codex connections, external models/MCP servers, user-installed agents, skills and configured project hooks.
- First-party operating / deployment modes considered: interactive Freebuff terminal, model-picker-specific `base3-free-*` roots, SDK-backed local tool execution, session continuation, and the documented headless/print SDK capability. A source rebuild that changes `CLI_HARNESS` to `base2` is not the observed default distribution; uninspected hosted modes are not used to infer this CLI's autonomy.
- Recursion level: one user-task coding-agent operating unit inside the terminal product; the human supplies purpose and requests, while the model chooses task-local actions.
- Reviewed revision: [`8ed5d3e5e58b6a7ea1351efcbaa967b2dc015073`](https://github.com/CodebuffAI/freebuff/tree/8ed5d3e5e58b6a7ea1351efcbaa967b2dc015073) (original immutable #200 intake).
- Observation date: 2026-10-22 (source inspection at pinned revision; no provider-backed live run).
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

Freebuff is a Bun/TypeScript monorepo. The published terminal interface selects a model-specific bundled root and calls the SDK/runtime. In the selected `base3` mode, the root has project file reads/edits, shell, search, glob, directory listing and to-do tools; CLI-specific web, URL, human-interaction and skill tools extend that set. The reusable runtime streams model-generated calls, dispatches tools, writes tool observations into the message history, repeats model steps until a completion condition, and keeps resumable session state. Providers supply inference, while the repository owns tool execution and the iteration/termination mechanism.

The same repository also contains `base2` multi-agent strategic orchestration, a programmatic `spawn_agents` tool, code reviewers and other specialized agent definitions. Their presence is real but does not make them selected Freebuff CLI ownership: the current `CLI_HARNESS` constant is `base3`, the Freebuff model-selection function selects `base3-free-*`, and that root has no `spawn_agents` or reviewer agent. Conversely, the separate product README advertises Desktop parallel worktrees and hosted products, but this source inspection cannot establish the decisive organization of those different distributions.

User approval/trust policy gates repository-supplied executable agent templates and MCP configuration; local session snapshots, queue controls, budget/step limits and history compaction support task operation. These mechanisms are not by themselves whole-system VSM regulation, future capability adaptation or identity-level policy decisions.

Primary source anchors: [repository map](https://github.com/CodebuffAI/freebuff/blob/8ed5d3e5e58b6a7ea1351efcbaa967b2dc015073/AGENTS.md), [Freebuff root selection](https://github.com/CodebuffAI/freebuff/blob/8ed5d3e5e58b6a7ea1351efcbaa967b2dc015073/cli/src/utils/freebuff-agent-selection.ts#L1-L29), [compiled harness setting](https://github.com/CodebuffAI/freebuff/blob/8ed5d3e5e58b6a7ea1351efcbaa967b2dc015073/cli/src/utils/constants.ts#L130-L168), [root tool definition](https://github.com/CodebuffAI/freebuff/blob/8ed5d3e5e58b6a7ea1351efcbaa967b2dc015073/agents/base3.ts#L14-L128), [runtime loop](https://github.com/CodebuffAI/freebuff/blob/8ed5d3e5e58b6a7ea1351efcbaa967b2dc015073/packages/agent-runtime/src/run-agent-step.ts#L1074-L1320), [agents/tool security documentation](https://github.com/CodebuffAI/freebuff/blob/8ed5d3e5e58b6a7ea1351efcbaa967b2dc015073/docs/agents-and-tools.md).

## Operational model

The credited S1 unit is a model-backed root coding session. It consumes the user's task and project context, chooses file/terminal/search tool calls, receives execution results, and continues or finishes. Its discretion is bounded by fixed tool definitions, user/host permissions, cost/step rules and the chosen provider, none of which supplies the task-level model decision itself. More than one model option is a selectable implementation of the same task unit, not evidence of multiple simultaneously interacting S1 cells at this recursion.

The `base2` code shows a distinct possible orchestration topology, but the frozen default Freebuff CLI selects `base3`; no S2–S5 claim below borrows dormant `base2`, product marketing, repository maintenance or third-party providers.

## S1 — Operations

- State: A
- Function: autonomous coding task execution within one user repository/session.
- Disturbance / variety regulated: uncertain codebase layout, requested change requirements, file/tool errors and tests that inform the next implementation action.
- Decisive decision or feedback right: the root LLM decides what file/search/terminal actions to perform and when to continue or end the current task turn; observed tool results affect the subsequent model step.
- Decision owner: selected `base3-free-*` root model, with runtime execution of its decisions.
- Supporting / enforcement mechanisms: SDK model routing, tools, stream parser, terminal broker, step limit, user consent/trust checks, session serialization and deterministic termination checks.
- Closure path: user prompt/project context → model tool call → tool handler executes → result enters message history → next model iteration or final response; the subsequent user turn can continue stored state.
- Boundary reachability: the compiled Freebuff CLI selects bundled `base3-free-*` roots, whose tool names are installed into the local SDK runtime; the loop and tool dispatch are first-party and active in that mode.
- Why this is / is not agent-owned: the model has task-local discretion over its tool sequence and content. A developer fixes the menu and runtime constraints, but without the model the same task-dependent decisions do not occur. This is an S1 decision, not autonomous organization-level S3/S5.
- Evidence: [Freebuff selection](https://github.com/CodebuffAI/freebuff/blob/8ed5d3e5e58b6a7ea1351efcbaa967b2dc015073/cli/src/utils/freebuff-agent-selection.ts#L9-L29), [base3 root and tools](https://github.com/CodebuffAI/freebuff/blob/8ed5d3e5e58b6a7ea1351efcbaa967b2dc015073/agents/base3.ts#L14-L127), [model stream / tool results](https://github.com/CodebuffAI/freebuff/blob/8ed5d3e5e58b6a7ea1351efcbaa967b2dc015073/packages/agent-runtime/src/run-agent-step.ts#L518-L699), [repeated steps and steering return](https://github.com/CodebuffAI/freebuff/blob/8ed5d3e5e58b6a7ea1351efcbaa967b2dc015073/packages/agent-runtime/src/run-agent-step.ts#L1075-L1320).
- Basis: structural (first-party wired model/tool execution source) plus explicit root instructions.
- Confidence: high for the documented/shipped CLI code path; no live provider trace is claimed.
- Caveats: model service availability and correctness are not attested. Source evidence establishes an executable autonomous task loop, not empirical completion quality.

## S2 — Coordination

- State: —
- Function: no distinct supported coordination function among multiple operational S1 units established for the selected Freebuff `base3` CLI session.
- Disturbance / variety regulated: a potential concurrent agent file/workspace collision or dependence would require separate S1 units and a first-party damping/feedback relation; these are not in the selected root's toolset.
- Decisive decision or feedback right: not established at the selected recursion.
- Decision owner: none established for S2; the single root's tool scheduling is S1 task sequencing.
- Supporting / enforcement mechanisms: sequential model steps, `write_todos`, local run/session state and per-tool broker limits; legacy `base2` has a separate `spawn_agents` implementation but is not the current CLI root.
- Closure path: no qualifying inter-S1 disturbance → attenuation → subsequent S1 feedback path in the selected default distribution.
- Why this is / is not agent-owned: there is a task-owning agent, but no evidence that it owns coordination of distinct operating cells experiencing a specific interference. Multiple provider choices or inactive agent definitions are not such units.
- Evidence: [root is single-loop and omits spawn](https://github.com/CodebuffAI/freebuff/blob/8ed5d3e5e58b6a7ea1351efcbaa967b2dc015073/agents/base3.ts#L14-L55), [current Freebuff harness selection](https://github.com/CodebuffAI/freebuff/blob/8ed5d3e5e58b6a7ea1351efcbaa967b2dc015073/cli/src/utils/freebuff-agent-selection.ts#L9-L29), [base2's separate parallel spawning instructions](https://github.com/CodebuffAI/freebuff/blob/8ed5d3e5e58b6a7ea1351efcbaa967b2dc015073/agents/base2/base2.ts#L189-L252), [separate spawn implementation](https://github.com/CodebuffAI/freebuff/blob/8ed5d3e5e58b6a7ea1351efcbaa967b2dc015073/packages/agent-runtime/src/tools/handlers/tool/spawn-agents.ts#L82-L182).
- Basis: structural.
- Confidence: medium-high within the declared CLI distribution.
- Caveats: Desktop worktree/parallel-agent behavior and alternate base2 builds would require a separately supported, source-inspected system boundary before an S2 claim.

### Absence scope

- Surfaces inspected: Freebuff CLI model/root selection and constants, `base3` model-specific bundled roots, `base2` alternatives, runtime multi-agent handler and its documented deployment boundary.
- Plausible first-party paths checked: default root subagent tool exposure; dependency scheduling/parallel child results in `base2`; advertised Desktop parallel workspaces; generic task/session queues.
- Why no material first-party path remains: the shipped selected CLI root is explicitly single-loop and lacks child spawning; alternative multi-agent templates and separate Desktop operations are not wired into that declared standard mode. Generic sequential task tools cannot attenuate an identified inter-S1 disturbance here.

## S3 — Inside-and-now control

- State: —
- Function: no separate whole-current operating-control function is established at this one-session CLI boundary.
- Disturbance / variety regulated: root turn length, tool outcomes, terminal process lifetime and token/context budgets are local S1 execution constraints, not a portfolio of operational units with shared commitments.
- Decisive decision or feedback right: no first-party whole-system resource/priority/commitment adjustment owner evidenced.
- Decision owner: developer-provided deterministic limits and user task controls support S1; no distinct S3 decision owner.
- Supporting / enforcement mechanisms: run loop step limits, cost accounting, session continuation, history compaction, abort/steer paths, local UI message queue and terminal process broker.
- Closure path: local process/tool/result handling returns to S1, without a separate whole-current intervention into multiple operational commitments.
- Why this is / is not agent-owned: model continuation choices are task-level operations. There is no separate S3 current-control discretion merely because a runtime records and enforces the loop budget.
- Evidence: [runtime steps/compaction/abort](https://github.com/CodebuffAI/freebuff/blob/8ed5d3e5e58b6a7ea1351efcbaa967b2dc015073/packages/agent-runtime/src/run-agent-step.ts#L1050-L1365), [SDK session and step options](https://github.com/CodebuffAI/freebuff/blob/8ed5d3e5e58b6a7ea1351efcbaa967b2dc015073/sdk/src/client.ts#L43-L75), [CLI broker boundary](https://github.com/CodebuffAI/freebuff/blob/8ed5d3e5e58b6a7ea1351efcbaa967b2dc015073/docs/agents-and-tools.md).
- Basis: structural.
- Confidence: medium-high for the CLI operating mode.
- Caveats: hosted Cloud/parallel Desktop fleet controls are beyond this source-supported operating boundary; no inference is made about those separate distributions.

### Absence scope

- Surfaces inspected: CLI root/harness mode, runtime loop/accounting, SDK run/session lifecycle, terminal execution documentation, and multi-agent templates not selected in this distribution.
- Plausible first-party paths checked: user-steering, session queues, step/cost constraints, background subprocess handling, parallel agent manager in another mode, advertised hosted capacity.
- Why no material first-party path remains: these reachable CLI mechanisms execute or bound one S1 task, while the alternative/hosted functions are not evidenced as a current whole-system controller wired to the selected CLI recursion.

## S3* — Complementary audit

- State: —
- Function: no sufficiently independent, operationally returned complementary audit of the selected CLI's S1 claims is established.
- Disturbance / variety regulated: coding mistakes might be caught by tests or reviewers, but a named check is not automatically an independent organization-level challenge path.
- Decisive decision or feedback right: not established for an independent auditor at this boundary.
- Decision owner: task root may run verification tools; the optional `base2` reviewer is a model prompted from parent transcript rather than a default independent raw-evidence assessor.
- Supporting / enforcement mechanisms: typecheck/test commands; standalone optional code-reviewer and evaluation files elsewhere in the monorepo.
- Closure path: normal model→terminal output→model correction is S1 verification. No separately evidenced complementary raw-access/audit-judgment/corrective-return loop in the selected CLI root.
- Why this is / is not agent-owned: `base3` has no reviewer spawn; an optional `base2` review prompt with no tools is not evidence of a materially independent channel in this declared distribution.
- Evidence: [base3 tool list](https://github.com/CodebuffAI/freebuff/blob/8ed5d3e5e58b6a7ea1351efcbaa967b2dc015073/agents/base3.ts#L41-L55), [reviewer lacks tools and inherits parent history](https://github.com/CodebuffAI/freebuff/blob/8ed5d3e5e58b6a7ea1351efcbaa967b2dc015073/agents/reviewer/code-reviewer.ts#L10-L65), [base2 optional review instruction](https://github.com/CodebuffAI/freebuff/blob/8ed5d3e5e58b6a7ea1351efcbaa967b2dc015073/agents/base2/base2.ts#L140-L166).
- Basis: structural.
- Confidence: medium-high for the selected CLI.
- Caveats: a separately operated evaluator or reviewer in another mode could warrant new source-specific study rather than borrowing its label.

### Absence scope

- Surfaces inspected: default root tool exposure, `base2` reviewer prompts, reviewer tool access and inheritance, runtime tool/result loop, repository evaluation/testing adjacency.
- Plausible first-party paths checked: test feedback, alternate code-reviewer, eval files, model self-check and post-edit validation.
- Why no material first-party path remains: the default root has ordinary S1 verification tools only; optional reviewer is not selected and has no independent direct evidence access in its authored definition; repository eval and CI are adjacent development rather than a wired S3* return path.

## S4 — Outside-and-then intelligence

- State: —
- Function: no separate environment-sensing, future-option selection, capability-changing and return-to-current-operation loop is established for the selected CLI root.
- Disturbance / variety regulated: task-local project information, history length and transient model/tool errors, not future viability options at the product recursion.
- Decisive decision or feedback right: no supported agent or parent S4 adaptation choice identified.
- Decision owner: developer/user supplies models, installed skills and updates; model can adapt task tactics inside S1, but not the durable current capability organization on outside-and-then evidence.
- Supporting / enforcement mechanisms: session persistence, history compaction, model picker, skill loader, user project instructions and repository development processes.
- Closure path: current-run context changes may improve later task steps, but no evidenced external-prospective adaptation decision is returned into the ongoing organization's capability setup.
- Why this is / is not agent-owned: a task agent choosing another search or editing a file on request is not a separately established S4 function. Static selected model/skills and CI releases are not in-boundary agent-owned adaptation.
- Evidence: [base3 tools/intent](https://github.com/CodebuffAI/freebuff/blob/8ed5d3e5e58b6a7ea1351efcbaa967b2dc015073/agents/base3.ts#L14-L127), [mechanical compaction](https://github.com/CodebuffAI/freebuff/blob/8ed5d3e5e58b6a7ea1351efcbaa967b2dc015073/packages/agent-runtime/src/run-agent-step.ts#L1090-L1173), [CLI model choice](https://github.com/CodebuffAI/freebuff/blob/8ed5d3e5e58b6a7ea1351efcbaa967b2dc015073/cli/src/utils/freebuff-agent-selection.ts#L1-L29), [agent/skill trust and loading](https://github.com/CodebuffAI/freebuff/blob/8ed5d3e5e58b6a7ea1351efcbaa967b2dc015073/docs/agents-and-tools.md).
- Basis: structural.
- Confidence: medium for the declared CLI; no claims about proprietary hosted learning systems.
- Caveats: the repository advertises research and multiple products, but no credible outside-and-then decision closure in the selected CLI was identified.

### Absence scope

- Surfaces inspected: selected root, model-selection code, SDK/runtime compaction, tools/skills documentation, alternative bundled agents, advertised hosted product boundaries.
- Plausible first-party paths checked: tool-driven research, persistent sessions, skill loading/extension, model changes, automatic compaction and project development/evals.
- Why no material first-party path remains: these are either task-local S1/context operations, operator-selected setup or adjacent development; the selected runtime does not ship an evidenced separate option→selection→capability-return adaptation path.

## S5 — Policy and identity

- State: —
- Function: no first-party identity/ultimate-policy issue, legitimate deciding authority and returned new identity/policy closure is established at the selected coding-session recursion.
- Disturbance / variety regulated: project tool permissions and trust of executable local/registry agents concern action admission, not ultimate purpose/identity determination.
- Decisive decision or feedback right: no qualifying S5 issue-decision-return path; user prompts, model/tool configuration and developer-authored system prompts set preconditions.
- Decision owner: the human/user or developer controls initial purpose, model and tool restrictions, but ordinary approval/configuration does not establish an operationally closed S5 parent mode.
- Supporting / enforcement mechanisms: `AGENTS.md` trust prompt, registry publisher allowlist, executable-agent policy, tool approval, abort and deterministic provider/request restrictions.
- Closure path: grant/deny or configured policy affects whether a task tool runs, but no evidenced identity/ultimate-policy decision is brought to legitimate authority and returned to govern ongoing product identity.
- Why this is / is not agent-owned: an LLM can execute coding tasks but does not own ultimate purpose or adopt/revise governing identity; mechanical trust enforcement is a separate right.
- Evidence: [repository-controlled root instructions](https://github.com/CodebuffAI/freebuff/blob/8ed5d3e5e58b6a7ea1351efcbaa967b2dc015073/agents/base3.ts#L45-L65), [documented trust policy](https://github.com/CodebuffAI/freebuff/blob/8ed5d3e5e58b6a7ea1351efcbaa967b2dc015073/docs/agents-and-tools.md), [agent publisher trust](https://github.com/CodebuffAI/freebuff/blob/8ed5d3e5e58b6a7ea1351efcbaa967b2dc015073/sdk/src/agent-publisher-trust.ts), [SDK options](https://github.com/CodebuffAI/freebuff/blob/8ed5d3e5e58b6a7ea1351efcbaa967b2dc015073/sdk/src/client.ts#L20-L75).
- Basis: structural.
- Confidence: medium-high for CLI.
- Caveats: vendor/business policy and hosted product account governance are external to the documented source-supported coding session.

### Absence scope

- Surfaces inspected: root identity/system instructions, CLI user/agent selection, SDK trust/permission hooks, tool restrictions, public product/repository documentation.
- Plausible first-party paths checked: user prompts and approval, agent publisher trust decisions, project `AGENTS.md`, provider model selection, contributor/release governance.
- Why no material first-party path remains: these set or enforce task inputs, tool admission and product development outside the selected runtime; none shows a legitimate in-boundary identity/ultimate-policy matter being decided and returned to govern the ongoing organization.

## Distributed OSS parent arrangement

The public repo has contributors and release/development processes, but no shared operating parent S5 identity/governance or S3/S4 closed right is claimed from those adjacent activities. User authority over one CLI task is not automatically a project-level parent VSM function.

## Self-hosted and non-human modes

The inspectable terminal distribution may use BYOK and local execution, but changing provider/credentials, approving shell actions or loading skills does not by itself close S3/S4/S5. Additional Desktop, Cloud, Web and alternate source-built root modes should be separately pinned and assessed if their first-party operation and control return become reconstructable. No inference about non-human S5 is made from the coding LLM.

## Recursion

The system is assessed at the single Freebuff terminal coding-task organization: one model-backed S1 operating unit within a larger human/user and vendor environment. Child/agent templates present elsewhere in the repository are not counted as nested VSM recursions in the selected standard root.

## Variety and escalation

The model absorbs local coding variety with project read/edit/shell/test tools; deterministic step/time/permission constraints bound action risk. Tool errors, aborted steps and user steering return to the root/session. Escalation to user approval is a task-level action authorization mechanism, not automatically the algedonic channel or legitimate ultimate S5 closure.

## Evidence gaps

- This is pinned static source review, not a live inference/terminal-e2e trace. Runtime wiring is visible but performance, particular model behavior and successful source-pinned execution were not measured.
- The source tree and README describe a wider multi-product Freebuff ecosystem. Desktop's worktree-based parallel agents and Web/Cloud hosted orchestration are not fully reconstructable from the inspected public CLI implementation and are excluded from this bounded result; the vector must not be generalized to those deployments.
- `base2` multi-agent/reviewer code is present as an alternate/rollback template, but the frozen Freebuff CLI explicitly selects `base3`. A separate source-supported standard mode could warrant a distinct boundary analysis; it is not silently counted here.
