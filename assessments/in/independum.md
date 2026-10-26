---
harness_id: independum
project_name: Independum
repository: https://github.com/radenadam/independum
review_ref: e556a8d48900609d1203d9374375ea6503177d9f
reviewed_at: 2026-10-26
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: excluded-no-agentic-vsm
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Independum

## Review boundary

- System in focus: the currently wired first-party Independum local web/chat application at the frozen revision; not a future full coding-agent product or the independent Pi SDK project.
- Purpose and identity: expose a user-visible, persistent local AI chat interface, including model/provider login, model/thinking selection and inspection of exact request/prompt surfaces; the stated eventual vision is a user-editable agent harness.
- Relevant environment: local browser, project folders and stored chats, user-chosen provider logins, model responses, and developer-installed dependencies.
- Standard-distribution boundary: `pnpm dev` runs the first-party Node/Hono/Vite server and browser UI. `@earendil-works/pi-coding-agent` supplies the underlying session/model transport, but the *actual* Independum chat disables built-in tools and provides no replacement tools.
- Credited operating / distribution surfaces: `packages/independum/src/{cli,create-chat,chat-routes,create-server,create-model-runtime,create-saved-chats}.ts`, browser chat and agent-view components, `docs/decisions/0002-*.md` and `00013` first-chat decision, README and current roadmap.
- Adjacent first-party surfaces excluded from ownership: hypothetical future tool/built-in and plugin code, design decisions describing Pi extension capabilities rather than shipped wiring, contributor `AGENTS.md`/`CLAUDE.md`, CI/build/tests and maintainer roadmap authority. Pi's own independent coding-agent deployments with tools enabled are not this assessed system.
- First-party operating / deployment modes considered: browser chat, session persistence/project navigation, provider/model and thinking-level selection, agent prompt/request inspector and operator stop; no separate shipped headless autonomous tool-task runner found.
- Recursion level: one local Independum instance and its user chat sessions; not the product-development organization.
- Reviewed revision: `e556a8d48900609d1203d9374375ea6503177d9f`.
- Observation date: 2026-10-26.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The [README](https://github.com/radenadam/independum/blob/e556a8d48900609d1203d9374375ea6503177d9f/README.md) explicitly calls Independum early development and not yet usable. Its [roadmap](https://github.com/radenadam/independum/blob/e556a8d48900609d1203d9374375ea6503177d9f/docs/roadmap.md) lists reading/editing files and running commands as work *now*, not as completed. The live [`createChat`](https://github.com/radenadam/independum/blob/e556a8d48900609d1203d9374375ea6503177d9f/packages/independum/src/create-chat.ts) creates Pi `AgentSession`s, persists and reopens chats, streams answers and lets the user choose a model. Crucially it explicitly sets `noTools: "builtin"`, supplies no `customTools`, sets `noExtensions`, `noContextFiles`, `noSkills`, `noPromptTemplates`, and writes a system prompt that the assistant cannot read files or run commands. Its hidden request-capture extension only records the last provider payload for display.

[`chat-routes`](https://github.com/radenadam/independum/blob/e556a8d48900609d1203d9374375ea6503177d9f/packages/independum/src/chat-routes.ts) exposes user-driven chat messages, model/thinking settings, chat navigation, stop and state/stream endpoints. [`cli`](https://github.com/radenadam/independum/blob/e556a8d48900609d1203d9374375ea6503177d9f/packages/independum/src/cli.ts) starts loopback HTTP plus Vite, not an independent autonomous work scheduler. The [first-chat decision](https://github.com/radenadam/independum/blob/e556a8d48900609d1203d9374375ea6503177d9f/docs/decisions/0013-first-chat.md) intentionally chooses a no-tools chat. Tests using fake Pi providers confirm `getAgent().tools` is empty; they establish the implemented boundary, not model quality.

## Operational model and admission decision

Human selects provider/model and sends a chat message → Pi session asks the model and streams/persists the text → browser displays it; human must send another message for the next task. No currently wired autonomous model/tool/observation/action loop over a task environment is exposed by Independum. The Pi SDK can support such a loop *in other compositions*, but the shipped Independum composition expressly disables its tools. Ordinary conversational response choice is not credited as a first-party autonomous S1 task/action unit in the Index's agentic-harness admission scope.

**Proposed canonical disposition: `excluded-no-agentic-vsm`.** The all-`—` vector records this bounded first-party assessment, not a finding that Pi or future Independum versions cannot implement a viable agent harness.

## S1 — Operations

- State: —
- Function: no first-party autonomous environment-task operating unit with a closed observation-to-next-action loop is supplied at this revision.
- Disturbance / variety regulated: provider choice, session continuity and conversational input are handled, but no file, command or tool-action variety is admitted to the model.
- Decisive decision or feedback right: selecting subsequent substantive environment actions from prior tool results is not available; the human determines when another chat request is made.
- Decision owner: the external Pi SDK handles single user-triggered model turns, while Independum configures their UI/session transport; no shipped tool-task agent owner is established.
- Supporting / enforcement mechanisms: model runtime, `AgentSession`, saved chat store, event stream, login and selection routes.
- Closure path: user text → Pi model response → persisted/streamed text; no agent-selected environment action and return of its observation into another autonomous step.
- Why this is / is not agent-owned: there is a model response, but the shipped harness intentionally has zero tools and no independent operational action-selection recurrence.
- Evidence: [create-chat](https://github.com/radenadam/independum/blob/e556a8d48900609d1203d9374375ea6503177d9f/packages/independum/src/create-chat.ts), [chat routes](https://github.com/radenadam/independum/blob/e556a8d48900609d1203d9374375ea6503177d9f/packages/independum/src/chat-routes.ts), [fake-provider assertion](https://github.com/radenadam/independum/blob/e556a8d48900609d1203d9374375ea6503177d9f/packages/independum/src/chat-routes.test.ts).
- Basis: explicit and structural bounded negative.
- Confidence: high.
- Caveats: a future source revision can add real tools; this frozen assessment does not follow the roadmap forward.

### Absence scope

- Surfaces inspected: runtime session constructor, system prompt, chat API/routes, CLI server, browser request UI, project roadmap and Pi design decisions.
- Plausible first-party paths checked: Pi's default coding tools, custom tools, extension hooks, a hidden background task runner, multi-turn chat continuation and future file/command built-ins.
- Why no material first-party path remains: `noTools: "builtin"` and no custom tool registration disable the candidate operational path; request inspection merely observes transport, and the documented file/command capabilities are unfinished.

## S2 — Coordination

- State: —
- Function: no first-party coordination of two operating S1 units exists.
- Disturbance / variety regulated: chat sessions are separate stored conversations, not simultaneously acting work cells with a demonstrated interference mode.
- Decisive decision or feedback right: no inter-S1 conflict-attenuation decision is wired.
- Decision owner: none established at this boundary.
- Supporting / enforcement mechanisms: chat session listing, project grouping, one reply at a time and current-request refusal while busy.
- Closure path: a per-chat busy refusal does not feed a coordination decision among distinct autonomous S1 units.
- Why this is / is not agent-owned: message serialization and session management are not an S2-specific disturbance/closure witness.
- Evidence: [create-chat](https://github.com/radenadam/independum/blob/e556a8d48900609d1203d9374375ea6503177d9f/packages/independum/src/create-chat.ts), [chat routes](https://github.com/radenadam/independum/blob/e556a8d48900609d1203d9374375ea6503177d9f/packages/independum/src/chat-routes.ts).
- Basis: structural bounded negative.
- Confidence: high.
- Caveats: no inference about possible externally built multi-agent compositions.

### Absence scope

- Surfaces inspected: chat sessions, project list, active-reply guard, server routes and UI navigation.
- Plausible first-party paths checked: simultaneous sessions, message routing, workspace grouping and busy guard as potential coordination.
- Why no material first-party path remains: none establishes two agentic operational units, a concrete inter-S1 disturbance, and a regulating feedback path.

## S3 — Inside-and-now control

- State: —
- Function: no whole-current control of an agentic S1 operation portfolio is established.
- Disturbance / variety regulated: current reply status and model/session settings are per-chat controls.
- Decisive decision or feedback right: whole-system resource/commitment priority or corrective intervention remains outside the app's autonomous workflow.
- Decision owner: the operator chooses chat/model and stops replies; deterministic API enforces status.
- Supporting / enforcement mechanisms: `isReplying`, model/thinking routes, chat stop, saved-session metadata.
- Closure path: a human stops/changes one session; no whole-current S1 feedback-to-revised-commitment loop.
- Why this is / is not agent-owned: a chat UI status board is not itself an S3 regulator.
- Evidence: [create-chat](https://github.com/radenadam/independum/blob/e556a8d48900609d1203d9374375ea6503177d9f/packages/independum/src/create-chat.ts), [chat routes](https://github.com/radenadam/independum/blob/e556a8d48900609d1203d9374375ea6503177d9f/packages/independum/src/chat-routes.ts).
- Basis: structural bounded negative.
- Confidence: high.
- Caveats: parent S3 is not implied by generic human model selection.

### Absence scope

- Surfaces inspected: server/route current-state API, session lists, model choices and user stop controls.
- Plausible first-party paths checked: model selection as resource allocation, chat cancellation as intervention, cross-project chat view as whole-current reporting.
- Why no material first-party path remains: these are isolated user choices and transport/status guards rather than current regulation of multiple operational commitments.

## S3* — Complementary audit

- State: —
- Function: no complementary independent operational audit with returned control is supplied.
- Disturbance / variety regulated: a displayed model answer might be wrong, but no independent checking operation is wired.
- Decisive decision or feedback right: independent judgment of direct work evidence and returned correction is absent.
- Decision owner: none established.
- Supporting / enforcement mechanisms: request inspector, saved replies, test fakes and CI.
- Closure path: raw request is shown to the user, not judged by a separately independent auditor and returned into an agentic production decision.
- Why this is / is not agent-owned: transparency of request payload and unit tests for the application are not a complementary S3* path over S1 claims.
- Evidence: [agent inspector](https://github.com/radenadam/independum/blob/e556a8d48900609d1203d9374375ea6503177d9f/packages/independum/src/create-chat.ts), [chat route tests](https://github.com/radenadam/independum/blob/e556a8d48900609d1203d9374375ea6503177d9f/packages/independum/src/chat-routes.test.ts).
- Basis: structural bounded negative.
- Confidence: high.
- Caveats: a human may read and critique an answer outside the first-party audit loop.

### Absence scope

- Surfaces inspected: request capture, UI agent place, route tests, response streaming and saved chats.
- Plausible first-party paths checked: request inspection as audit, fake-provider unit checks and operator review of answers.
- Why no material first-party path remains: they lack a separate operational-reality access path, independent audit judgment and integrated corrective return.

## S4 — Outside-and-then intelligence

- State: —
- Function: no external/prospective capability adaptation of the installed chat system is established.
- Disturbance / variety regulated: future providers, tools and product capabilities are developer roadmap matters.
- Decisive decision or feedback right: developing and selecting future adaptation options from environmental evidence is not supplied by a runtime loop.
- Decision owner: project maintainer owns roadmap; local human chooses a current provider/model.
- Supporting / enforcement mechanisms: provider model lists, login, thinking level and public roadmap.
- Closure path: chosen model changes a present chat setting, not an external research-to-future-capability adoption cycle.
- Why this is / is not agent-owned: provider selection and feature planning alone are not S4.
- Evidence: [roadmap](https://github.com/radenadam/independum/blob/e556a8d48900609d1203d9374375ea6503177d9f/docs/roadmap.md), [create-model-runtime](https://github.com/radenadam/independum/blob/e556a8d48900609d1203d9374375ea6503177d9f/packages/independum/src/create-model-runtime.ts).
- Basis: structural bounded negative.
- Confidence: high.
- Caveats: the development organization may itself learn and adapt; it is outside the selected runtime boundary.

### Absence scope

- Surfaces inspected: model catalog/login, model/thinking choice, roadmap and server bootstrap.
- Plausible first-party paths checked: swapping current models, external provider catalogue, planned file tools and contributor decisions.
- Why no material first-party path remains: no packaged externally prospective sensing/options/adoption loop changes operational capability.

## S5 — Policy and identity

- State: —
- Function: no installed-harness ultimate identity/constitutional policy decision-and-return path is supplied.
- Disturbance / variety regulated: visibility/control of prompt, tool settings and future access boundaries is a product goal rather than current identity-level governance.
- Decisive decision or feedback right: no legitimate identity-policy issue is routed to authority and returned to constrain future operation.
- Decision owner: maintainer sets code/product direction, operator chooses per-chat settings; neither is an evidenced shipped S5 parent mode.
- Supporting / enforcement mechanisms: fixed system prompt, localhost token, login credentials, model choice and read-only agent inspector.
- Closure path: local configuration or access enforcement does not carry an ultimate-policy adjudication into subsequent system operation.
- Why this is / is not agent-owned: the stated editable-agent vision is not live S5 authority; static prompt/access control is not an identity decision.
- Evidence: [README](https://github.com/radenadam/independum/blob/e556a8d48900609d1203d9374375ea6503177d9f/README.md), [create-server](https://github.com/radenadam/independum/blob/e556a8d48900609d1203d9374375ea6503177d9f/packages/independum/src/create-server.ts), [first-chat decision](https://github.com/radenadam/independum/blob/e556a8d48900609d1203d9374375ea6503177d9f/docs/decisions/0013-first-chat.md).
- Basis: structural bounded negative.
- Confidence: high.
- Caveats: no inference about private owner decisions or future governance.

### Absence scope

- Surfaces inspected: fixed prompt, agent inspector, access token, login/model settings, README and design decisions.
- Plausible first-party paths checked: user control over prompt/tools, token/access controls and maintainer roadmap choices.
- Why no material first-party path remains: shipped prompt/tools are read-only/disabled, ordinary authentication is enforcement, and no runtime ultimate-policy issue/authority/return path exists.

## Distributed OSS parent arrangement

Contributor decisions belong to the Independum development project, not a shared control system for independent active agent operating cells. No organization-level parent mode is inferred.

## Self-hosted and non-human modes

Local hosting and a browser UI do not by themselves provide agentic S1 autonomy or an eligible S3/S4/S5 parent-governed path.

## Recursion

Multiple stored chats and projects are separate histories, not evidence of viable recursive S1 units.

## Variety and escalation

The user selects provider/model/effort, chat, project and stop action. Server guards attenuate concurrent replies and token exposure. The model produces text, but no admitted environment-tool feedback is acted on autonomously; session events and provider errors are user-facing status, not evidence of additional VSM metasystem closure.

## Evidence gaps

The repo's early-development disclaimer and no-tools implementation are explicit at the frozen source. Tests use fake providers; no live model, Browser, coding-agent quality or tool-execution experiments were run. A future release with real registered tools would be a new-ref reassessment, not a reason to credit this revision. Existing Pi SDK capabilities were inspected only as a dependency boundary, not a hidden first-party Independum operating mode.
