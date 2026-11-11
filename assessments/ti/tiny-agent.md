---
harness_id: tiny-agent
project_name: tiny-agent
repository: https://github.com/HowProgrammingWorks/Agent
review_ref: d4822a9de234ff5dd7a2c7e40f1e2333b10c7827
reviewed_at: 2026-11-11
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# tiny-agent

## Review boundary

- System in focus: the shipped Node.js interactive coding harness, its first-party model/tool loop and workspace tooling, operating on a user-selected local project.
- Purpose and identity: respond to coding requests through a model deciding which local file, command and inspection actions to perform.
- Relevant environment: user requirements, project files and git state, program errors, tool permissions, model availability and external web resources.
- Standard-distribution boundary: `npm start` / `start.js`, `ide/ide.js`, `agent/agent.js`, tool registry and the packaged tools; a configured OpenAI-compatible LLM endpoint provides cognition.
- Credited operating / distribution surfaces: interactive IDE that invokes `runAgent`, first-party tool-call execution and response loop, workspace path containment and configured approval path.
- Adjacent first-party surfaces excluded from ownership: developer ESLint/Prettier and package check scripts, README illustrations, repository maintainers and model-provider service control.
- First-party operating / deployment modes considered: interactive local terminal in a git/non-git directory, configured model/fallback list, user approval versus in-repository auto-approval for eligible tools.
- Recursion level: a single coding-agent work unit performing one user's current task; IDE is its interface, not a higher-level multi-agent organization.
- Reviewed revision: `d4822a9de234ff5dd7a2c7e40f1e2333b10c7827`.
- Observation date: 2026-11-11.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

`start.js` prepares local configuration and requires an interactive TTY/API key. The terminal `Ide` initializes a provider, a permission callback, workspace file tree and ongoing chat context. `runAgent` performs a bounded model → tool calls → tool result → model cycle, with each model response selecting any loaded `read`, `edit`, `write`, `patch`, `bash`, `check`, `fetch`, `todo` and other tools. The registry loads definitions and executable first-party modules from `tools/`. `workspace` bounds file paths including symlinks; `permissions` asks an operator for selected external-to-git-root actions and permits ordinary in-project actions by the configured default. `llm.js` implements retry/model fallback on transport errors, which is support machinery, not strategic decision ownership. The IDE retains local conversation while running; no durable multi-agent or organization-level control plane appears in the supported distribution. [entrypoint](https://github.com/HowProgrammingWorks/Agent/blob/d4822a9de234ff5dd7a2c7e40f1e2333b10c7827/start.js), [IDE](https://github.com/HowProgrammingWorks/Agent/blob/d4822a9de234ff5dd7a2c7e40f1e2333b10c7827/ide/ide.js), [agent loop](https://github.com/HowProgrammingWorks/Agent/blob/d4822a9de234ff5dd7a2c7e40f1e2333b10c7827/agent/agent.js).

## Operational model

The configured provider generates a model response including tool calls; the first-party runner asks the local permission service, executes the selected tool, injects observed results into the conversation, and lets the model choose subsequent actions. The user owns initial task, credentials and exceptional approvals, but the model owns ordinary task-level decisions. There is one S1 unit: no second autonomous operational cell, whole-system resource/commitment supervisor, independent complementary audit or future-oriented adaptation authority is installed by the described runtime.

## S1 — Operations

- State: A
- Function: perform requested coding and inspection work by repeatedly deciding local actions and revising them against observed tool feedback.
- Disturbance / variety regulated: varied source trees, coding objectives, command/file failures, outputs, and changing project context.
- Decisive decision or feedback right: model selects tool name/arguments, whether to call another tool, and when to conclude; returned observations inform later choices within a 30-step default bound.
- Decision owner: the configured autonomous model, executed through the first-party `runAgent` loop; the human specifies the goal but does not choose each ordinary in-repository step.
- Supporting / enforcement mechanisms: dynamically loaded first-party tool registry, workspace containment, approvals, result truncation, maximum steps, retry/provider fallback and IDE chat display.
- Closure path: user task → provider model choice → first-party permission/tool execution → observed tool result appended to model messages → next autonomous step or final answer.
- Boundary reachability: `start.js` calls the packaged IDE, whose `Ide` composes the provider/permissions and invokes shipped `runAgent` on the user prompt; no separate development-only agent is required.
- Why this is / is not agent-owned: model-generated choices materially change subsequent project operations; deterministic permission checks, tool dispatch and step limits enforce boundaries rather than choose the coding actions.
- Evidence: [bounded model/tool feedback loop](https://github.com/HowProgrammingWorks/Agent/blob/d4822a9de234ff5dd7a2c7e40f1e2333b10c7827/agent/agent.js), [tool definitions and execution](https://github.com/HowProgrammingWorks/Agent/blob/d4822a9de234ff5dd7a2c7e40f1e2333b10c7827/agent/tools.js), [supported run instructions](https://github.com/HowProgrammingWorks/Agent/blob/d4822a9de234ff5dd7a2c7e40f1e2333b10c7827/README.md).
- Basis: explicit model/tool call loop and structural source.
- Confidence: high.
- Caveats: no live paid-model execution was performed; static code establishes available control paths, not model performance or safety.

## S2 — Coordination

- State: —
- Function: no supplied cross-operational-unit conflict damping function at this single-agent recursion.
- Disturbance / variety regulated: file changes or concurrent human actions could collide with the agent's work, but no two distinct first-party S1 units are coordinated.
- Decisive decision or feedback right: none over inter-S1 interference; tool calls are serialized inside one model loop.
- Decision owner: not established for S2; single model controls ordinary tool sequence.
- Supporting / enforcement mechanisms: sequential tool-call runner, workspace root and file editing operations.
- Closure path: tools return to one model; no inter-S1 collision decision is fed to distinct operational units.
- Why this is / is not agent-owned: routing tools or sequencing the same agent's calls is not an S2 witness without distinct S1 units and a specific interference/attenuation relation.
- Evidence: [single `runAgent` iteration and sequential calls](https://github.com/HowProgrammingWorks/Agent/blob/d4822a9de234ff5dd7a2c7e40f1e2333b10c7827/agent/agent.js), [single-session IDE construction](https://github.com/HowProgrammingWorks/Agent/blob/d4822a9de234ff5dd7a2c7e40f1e2333b10c7827/ide/ide.js).
- Basis: bounded negative after S1-unit and coordination search.
- Confidence: high.
- Caveats: users can run independent processes, but the shipped harness does not coordinate them as one first-party organization.

### Absence scope

- Surfaces inspected: agent runner, IDE session/dispatch, bundled tools and README architecture.
- Plausible first-party paths checked: simultaneous model tool calls, terminal pane, workspace file state, chat and task `todo` tool.
- Why no material first-party path remains: these attach to one agent and do not supply distinct S1 work cells or a specific mechanism that attenuates their interference with returned coordination feedback.

## S3 — Inside-and-now control

- State: —
- Function: no whole-system supervisory current-control judgment over multiple operational commitments or shared resources established beyond one bounded task.
- Disturbance / variety regulated: token/provider failures and potentially risky commands are managed with fixed execution limits, retries and approvals, not whole-system S3 choices.
- Decisive decision or feedback right: human selects task and occasional tool approval; configured step limit and retry statuses enforce preset rules, not shared current-operation priorities.
- Decision owner: current task model for S1, operator for isolated permission choices; no S3 owner evidenced.
- Supporting / enforcement mechanisms: `maxSteps`, provider fallback, trust-root permission checks, task `todo` list and IDE status.
- Closure path: permission results or retries return to the same task loop; no separate whole-system S3 resource/commitment decision closes across S1 units.
- Why this is / is not agent-owned: the IDE knows current task messages but has no first-party whole-system current view or discretionary supervisory rights; implementation of fixed constraints is not autonomous S3.
- Evidence: [step bounds and result feedback](https://github.com/HowProgrammingWorks/Agent/blob/d4822a9de234ff5dd7a2c7e40f1e2333b10c7827/agent/agent.js), [approval policy](https://github.com/HowProgrammingWorks/Agent/blob/d4822a9de234ff5dd7a2c7e40f1e2333b10c7827/agent/permissions.js), [provider retry/fallback](https://github.com/HowProgrammingWorks/Agent/blob/d4822a9de234ff5dd7a2c7e40f1e2333b10c7827/agent/llm.js).
- Basis: bounded negative from first-party control paths.
- Confidence: high.
- Caveats: a real operator may supervise multiple unrelated runs outside the packaged single-agent organization.

### Absence scope

- Surfaces inspected: `agent/agent.js`, `agent/llm.js`, `agent/permissions.js`, `ide/ide.js`, README and task/tool definitions.
- Plausible first-party paths checked: fixed step budget, model fallback, operator approval, task list, chat state and terminal status.
- Why no material first-party path remains: no whole-system current view or owner choosing/revising cross-operational resource allocation/commitments with returned operational consequences; local tool gates alone are insufficient.

## S3* — Complementary audit

- State: —
- Function: no sufficiently independent complementary audit of normal agent outcome claims is supplied.
- Disturbance / variety regulated: agent code edits may be incorrect, but checking is a tool in the ordinary agent operation path.
- Decisive decision or feedback right: the same agent may elect to run `check` and read its output; no separate audit actor independently selects contradictory evidence and closes correction.
- Decision owner: model controls normal `check` invocation, deterministic Node/npm scripts report syntax checks; no separate auditor.
- Supporting / enforcement mechanisms: `tools/check`, shell, tool-result logging and IDE displays.
- Closure path: check output feeds directly to the same model if requested; no distinct S3* evidence channel with independent judgment/feedback to a supervisory owner.
- Why this is / is not agent-owned: routine tests and tool observations within the S1 task cannot be relabeled as complementary independent audit.
- Evidence: [ordinary check tool](https://github.com/HowProgrammingWorks/Agent/blob/d4822a9de234ff5dd7a2c7e40f1e2333b10c7827/tools/check/check.js), [tool feedback embedded in same agent's context](https://github.com/HowProgrammingWorks/Agent/blob/d4822a9de234ff5dd7a2c7e40f1e2333b10c7827/agent/agent.js), [IDE result display](https://github.com/HowProgrammingWorks/Agent/blob/d4822a9de234ff5dd7a2c7e40f1e2333b10c7827/ide/chat.js).
- Basis: bounded negative after alternative audit-path inspection.
- Confidence: high.
- Caveats: external human review or CI could audit the work, but neither is wired here as first-party complementary audit closure.

### Absence scope

- Surfaces inspected: checked tool and its invocation, IDE event/results, agent runner, provider, bundled scripts and README.
- Plausible first-party paths checked: `check`/`bash`, command error feedback, chat trace, interactive approval and developer lint/check scripts.
- Why no material first-party path remains: all in-boundary checks operate as routine agent tools or presentation; independent evidence access plus distinct corrective decision path is not supplied in the supported mode.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party prospective external-environment intelligence/adaptation loop with capability change is evidenced.
- Disturbance / variety regulated: external documentation, changing websites and provider availability affect current tasks, but only immediate task response and transport fallback are shipped.
- Decisive decision or feedback right: model chooses current-task `fetch` calls; deterministic provider retry/fallback switches configured endpoints; neither decides a future adaptation program for the harness.
- Decision owner: current coding agent and preconfigured runtime rules; no separate S4 adaptation owner.
- Supporting / enforcement mechanisms: web fetch tool, model fallbacks, system instructions and local file edits.
- Closure path: fetched data informs the present coding turn; retries restore current model requests, without generating external/prospective options and returning them as durable changed current capability/S3.
- Why this is / is not agent-owned: model research or model fallback is not by itself external-and-future organizational adaptation with S3 feedback.
- Evidence: [provider request/fallback logic](https://github.com/HowProgrammingWorks/Agent/blob/d4822a9de234ff5dd7a2c7e40f1e2333b10c7827/agent/llm.js), [fetch tool](https://github.com/HowProgrammingWorks/Agent/blob/d4822a9de234ff5dd7a2c7e40f1e2333b10c7827/tools/fetch/fetch.js), [current-task instructions](https://github.com/HowProgrammingWorks/Agent/blob/d4822a9de234ff5dd7a2c7e40f1e2333b10c7827/agent/instructions.md).
- Basis: bounded negative.
- Confidence: medium-high.
- Caveats: an agent could be prompted to research strategic alternatives as an ordinary user task; no durable first-party organizational future-capability loop is wired by default.

### Absence scope

- Surfaces inspected: fetched-resource tool, provider fallbacks, instructions, IDE and model-to-tool cycle.
- Plausible first-party paths checked: document/web reading, file changes during current task, fallback model list, `todo` planning and local script checks.
- Why no material first-party path remains: neither external/environmental forecasting nor adaptation-option judgment and return into ongoing system capability or S3 is established as a separate organizational closure.

## S5 — Policy and identity

- State: —
- Function: no first-party identity/ultimate-policy deliberation and authoritative return path is established for the runtime organization.
- Disturbance / variety regulated: dangerous shell operations, workspace escape and API credentials are tool safety and deployment boundaries, not an ultimate purpose disagreement.
- Decisive decision or feedback right: operator configures credentials/models and approves selected tool actions; rules are enforced at tool boundary rather than adjudicating organizational identity.
- Decision owner: human for individual permission decisions, developer for static system instructions; no first-party S5 decision authority/path.
- Supporting / enforcement mechanisms: `agent/instructions.md`, permissions/trust root, workspace path checks and provider configuration.
- Closure path: permission allow/deny returns to one tool call, and fixed prompts constrain current action; there is no identity-level dispute → legitimate ultimate authority → changed governing policy returned to later operation.
- Why this is / is not agent-owned: user control and static policy text do not constitute a model-owned or parent-governed identity-policy decision loop.
- Evidence: [operator permission boundary](https://github.com/HowProgrammingWorks/Agent/blob/d4822a9de234ff5dd7a2c7e40f1e2333b10c7827/agent/permissions.js), [static instructions](https://github.com/HowProgrammingWorks/Agent/blob/d4822a9de234ff5dd7a2c7e40f1e2333b10c7827/agent/instructions.md), [configuration](https://github.com/HowProgrammingWorks/Agent/blob/d4822a9de234ff5dd7a2c7e40f1e2333b10c7827/agent/config.template.js).
- Basis: bounded negative.
- Confidence: high.
- Caveats: maintainer decisions and a user's broader organization can set ultimate purpose externally; they are not packaged as the runtime's function-specific S5 return loop.

### Absence scope

- Surfaces inspected: system instructions, IDE approval flow, config/model setup, workspace boundary, agent runner and README.
- Plausible first-party paths checked: prompt constraints, approval/deny, tool trust policy, operator model choice and git-root protection.
- Why no material first-party path remains: these grant permissions or specify standing limits on ordinary operations, without an evidenced identity/ultimate-policy issue, legitimate decision authority and returned policy update at the assessed recursion.

## Distributed OSS parent arrangement

The repository is an open-source teaching implementation with ordinary maintainers, but the running local harness is one user-controlled task cell. Contributor PR decisions and separate operator deployments are not a shared in-runtime supervisory or ultimate-policy authority at this recursion.

## Self-hosted and non-human modes

The local human approves selected tool actions and may configure automatic approval. Removing the human only leaves fixed permission decisions and the autonomous single-task loop; no additional first-party S3/S4/S5 parent configuration with complete function-specific return is demonstrated.

## Recursion

One model-controlled task loop can itself be viewed as a work unit inside a user's larger project, but this distribution does not instantiate multiple independently governed S1 cells or a recursive metasystem. Tool calls are actions, not separate viable subunits.

## Variety and escalation

Unknown tools, malformed tool arguments and permission refusals become ordinary tool-result feedback; model API failures retry/fallback under configured rules. The model loop stops at its step bound or returns a final message. This describes operational error handling, not an independently evidenced algedonic metasystem channel.

## Evidence gaps

Static pinned source inspection establishes the code path, not the outcomes of an actual configured provider run, safety properties of arbitrary shell commands, or behavior under unspecified third-party extensions. No broader S-function credit is taken from those unobserved possibilities.
