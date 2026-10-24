---
harness_id: openbots
project_name: OpenBots
repository: https://github.com/abcampbel/open-bots
review_ref: 030b9e58b9df6d8b72588312a702b39ccce78723
reviewed_at: 2026-10-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# OpenBots

## Review boundary

- System in focus: The exact public OpenBots self-hosted Node/Express + Vite/React distribution frozen at `030b9e58b9df6d8b72588312a702b39ccce78723`, including shipped backend entry point, frontend agent personas, chat client, package/build manifest and tests.
- Purpose and identity: Present four domain-persona assistants intended to search, analyze, code, transact and delegate from a browser or self-hosted service. These are *stated product purposes*, not evidence of a working agent loop at this revision.
- Relevant environment: End-user requests, model endpoint configuration, webpages, third-party APIs, code execution, payments, sign-ups and Docker deployment as described in the README.
- Standard-distribution boundary: Git tree at the frozen SHA plus documented `npm run dev` / `npm run build && npm start` / Docker build paths. A separately hosted runtime at `openbots.tech`, a deleted or uncommitted `api/chat.ts`, unrelated project/fork history, server-side proprietary Agnes implementation, external model providers and README-implied services are not first-party shipped code at this ref.
- Credited operating / distribution surfaces: [Express entry](https://github.com/abcampbel/open-bots/blob/030b9e58b9df6d8b72588312a702b39ccce78723/server.ts#L1-L66), [browser chat request](https://github.com/abcampbel/open-bots/blob/030b9e58b9df6d8b72588312a702b39ccce78723/src/App.tsx#L108-L150), [agent personas](https://github.com/abcampbel/open-bots/blob/030b9e58b9df6d8b72588312a702b39ccce78723/src/lib/agents.ts), [package scripts](https://github.com/abcampbel/open-bots/blob/030b9e58b9df6d8b72588312a702b39ccce78723/package.json#L20-L46), [Docker build](https://github.com/abcampbel/open-bots/blob/030b9e58b9df6d8b72588312a702b39ccce78723/Dockerfile#L1-L18). The upstream `api/` directory is **absent from this Git tree**.
- Adjacent first-party surfaces excluded from ownership: README's claims about Agnes 2.5 Pro, benchmarks, 8-step agent loop, delegation, tools and payment mechanisms; tests importing an absent implementation; UI animations, canned persona prompts, Git history before the frozen deletion and any hosted deployment not reproduced by the frozen source.
- First-party operating / deployment modes considered: Documented Node development server, production bundle/start, Docker image and locally configured model endpoint. All converge on the missing backend module before they can start a source-proven agent. The marketing claim of provider fallback does not establish a reachable distribution mode.
- Recursion level: The self-hosted OpenBots service and its four proposed agent roles. Persona cards are not independently viable operational S1 units without their task loop and tool backend.
- Reviewed revision: `030b9e58b9df6d8b72588312a702b39ccce78723` from frozen discovery [#2000](https://github.com/opensiro/vsm-harness-index/issues/2000) and serial batch [#2001](https://github.com/opensiro/vsm-harness-index/issues/2001).
- Observation date: 2026-10-24.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

OpenBots publishes a Vite/React frontend with four predefined agent personas, a TypeScript Express entry and tests of a supposed backend agent loop. In the checked-in `server.ts`, both the health endpoint and `/api/chat` handler require `getApiKeys` or `processChat` imported from `./api/chat`. The local `src/lib/chatEngine.ts` likewise re-exports `../../api/chat`. The test suite's provider, SSRF, x402 and agent-loop tests import functions such as `runClaudeAgent`, `callLocalModel` and `parseX402` from `../api/chat`. **No `api/` path exists in the complete tracked tree at the frozen SHA**. [Server import](https://github.com/abcampbel/open-bots/blob/030b9e58b9df6d8b72588312a702b39ccce78723/server.ts#L1-L38), [frontend re-export](https://github.com/abcampbel/open-bots/blob/030b9e58b9df6d8b72588312a702b39ccce78723/src/lib/chatEngine.ts#L1-L2), [agent-loop test import](https://github.com/abcampbel/open-bots/blob/030b9e58b9df6d8b72588312a702b39ccce78723/tests/agent-loop.test.ts#L1-L8), [tool tests](https://github.com/abcampbel/open-bots/blob/030b9e58b9df6d8b72588312a702b39ccce78723/tests/ssrf.test.ts#L1-L10).

The README and CONTRIBUTING still explicitly identify `api/chat.ts` as the home of provider routing, agent loop, tools, delegation and safety; those descriptions are stale relative to the frozen code. The normal `npm run dev` executes `tsx server.ts`, and production builds bundle the same unresolved import via esbuild. The Dockerfile first runs that build from the public source; it does not download or provide a missing backend module. Thus the compiled server and advertised agent/tool modes cannot be attributed as reachable first-party paths in this distribution. [README claimed location](https://github.com/abcampbel/open-bots/blob/030b9e58b9df6d8b72588312a702b39ccce78723/README.md#L72-L112), [contributor architecture](https://github.com/abcampbel/open-bots/blob/030b9e58b9df6d8b72588312a702b39ccce78723/CONTRIBUTING.md#L24-L44), [scripts](https://github.com/abcampbel/open-bots/blob/030b9e58b9df6d8b72588312a702b39ccce78723/package.json#L20-L46), [Docker](https://github.com/abcampbel/open-bots/blob/030b9e58b9df6d8b72588312a702b39ccce78723/Dockerfile#L1-L18).

The tracked personas provide a name, system prompt, example requests and UI/animation state. They do not alone implement a decision/action/observation cycle; a prompt saying an agent has live market tools is not an installed live market tool. The counterfactual is concrete: with exactly these tracked files, the first-party server's central backend import has no target. The advertised model selection, tool execution, repeated loop and delegation are not observable or buildable from the supplied revision.

## Operational model

A user can select a persona in React, and the client is written to POST a request to `/api/chat`. The Express server is written to call a nonexistent imported `processChat` implementation. No first-party task worker can be constructed on the documented Node or Docker route without adding source files outside the frozen boundary. This is stronger than simply not finding agent-related documentation: an explicit, indispensable import and its tests point to a missing tracked module. The website, screenshots and marketing may correspond to a different distribution, but that cannot silently replace the pinned artifact.

## S1 — Operations

- State: —
- Function: No reachable autonomous first-party operational loop is established in this frozen standard distribution.
- Disturbance / variety regulated: User research, coding, web/API and transactional variety are described, but the module intended to handle those tasks is absent; UI persona selection cannot regulate that variety independently.
- Decisive decision or feedback right: The claimed model-driven tool choice, repeated observation and completion decision would reside in `api/chat.ts` / `processChat` or the alleged hosted Agnes service, neither of which is shipped at the reviewed ref.
- Decision owner: Not established in the frozen distribution. Persona system prompts are configuration text, and a hosted external agent (if it exists) is outside the reviewed source boundary.
- Supporting / enforcement mechanisms: React chat UI, four persona definitions, Express endpoint scaffolding, package scripts and documentation; none substitutes for the missing provider/tool loop.
- Closure path: UI submits task → Express requires `./api/chat` → missing import stops module resolution/build; no first-party model → tool execution → observed result → next-action feedback cycle is reachable from the shipped sources.
- Why this is / is not agent-owned: No executing agent actor or cognitive decision path remains when unshipped/externally claimed code is excluded. Static prompts do not confer task autonomy.
- Evidence: [server import and endpoint](https://github.com/abcampbel/open-bots/blob/030b9e58b9df6d8b72588312a702b39ccce78723/server.ts#L1-L48); [frontend backend re-export](https://github.com/abcampbel/open-bots/blob/030b9e58b9df6d8b72588312a702b39ccce78723/src/lib/chatEngine.ts); [README reference to absent implementation](https://github.com/abcampbel/open-bots/blob/030b9e58b9df6d8b72588312a702b39ccce78723/README.md#L72-L112); [personas](https://github.com/abcampbel/open-bots/blob/030b9e58b9df6d8b72588312a702b39ccce78723/src/lib/agents.ts).
- Basis: Exact frozen Git tree inventory and first-party entry-point import graph; no live model execution.
- Confidence: High for bounded unavailability of the documented standard source distribution, not a verdict about a separately hosted private backend.
- Caveats: A repaired future revision or unpublished module might operate differently, but neither may be imported into this immutable review ref. A new-ref reassessment can evaluate a restored first-party agent loop.

### Absence scope

- Surfaces inspected: Complete frozen `git ls-tree -r HEAD` inventory; server entry; browser client/re-export; agent definitions; provider/loop/SSRf/payment test imports; package scripts; Dockerfile; README and contributor instructions.
- Plausible first-party paths checked: Express `/api/chat` as local S1; `src/lib/chatEngine` as browser S1; four role/persona modules as independent agents; mocked tests as proof of shipped tool loop; hosted runtime or local model configuration as alternate S1.
- Why no material first-party path remains: Every plausible agent execution path requires the absent `api/chat` implementation or an unprovided separate service; the files present contain UI/configuration and references, but no executable first-party model/tool feedback owner.

## S2 — Coordination

- State: —
- Function: No bounded inter-S1 disturbance attenuation among first-party autonomous operational units is established.
- Disturbance / variety regulated: Claimed cross-agent delegation and overlapping code/research responsibilities are not accompanied by reachable first-party agent units or coordination code at the frozen revision.
- Decisive decision or feedback right: A PLUTUS → HEPHAESTUS delegation/merge is advertised but its supposed `delegate` handler belongs to the absent backend.
- Decision owner: Not established; persona switching and UI presentation are client display decisions.
- Supporting / enforcement mechanisms: Four static roles, frontend messages, documented delegate tool and tests importing absent code.
- Closure path: No first-party S1 plurality → observed interference → stabilizing decision → changed sibling S1 action path can execute.
- Why this is / is not agent-owned: Multiple agent *names* and a proposed delegation tool do not demonstrate actual coordinated agents, let alone autonomy-owned S2 regulation.
- Evidence: [README delegation claims](https://github.com/abcampbel/open-bots/blob/030b9e58b9df6d8b72588312a702b39ccce78723/README.md#L27-L58); [agent roles](https://github.com/abcampbel/open-bots/blob/030b9e58b9df6d8b72588312a702b39ccce78723/src/lib/agents.ts); [missing backend dependency](https://github.com/abcampbel/open-bots/blob/030b9e58b9df6d8b72588312a702b39ccce78723/server.ts#L1-L35).
- Basis: Bounded structural absence in the shipping source.
- Confidence: High for this ref.
- Caveats: Does not assert that a different private/hosted implementation cannot coordinate agents.

### Absence scope

- Surfaces inspected: Persona definitions, browser chat, server routes, declared delegate feature, bundled source tree and tests.
- Plausible first-party paths checked: Delegation tool, multi-persona UI, external hosted agent handoffs, concurrent server requests.
- Why no material first-party path remains: No executable first-party S1 instances or source-backed delegate/anti-interference closure are supplied, and concurrent HTTP requests alone are not S2.

## S3 — Inside-and-now control

- State: —
- Function: No whole-current management of the proposed four agents' work priorities, commitments and resource conflicts is established.
- Disturbance / variety regulated: Multi-agent task conflicts and stalled work could require S3, but the frozen code does not supply a current-portfolio manager.
- Decisive decision or feedback right: No shipped owner selects how the four agents' ongoing tasks are reassigned or prioritized from a whole-system current view.
- Decision owner: None established; users select a visible persona and an absent backend would have to execute any agent requests.
- Supporting / enforcement mechanisms: UI chat state, persona labels and advertised time/step limits, the latter without implementation source.
- Closure path: No whole-agent view → S3 decision → revised commitments returned to active first-party S1s is reachable.
- Why this is / is not agent-owned: The existence of four named roles and a claimed team workflow does not instantiate a metasystem manager.
- Evidence: [persona table](https://github.com/abcampbel/open-bots/blob/030b9e58b9df6d8b72588312a702b39ccce78723/README.md#L36-L59); [UI agent definitions](https://github.com/abcampbel/open-bots/blob/030b9e58b9df6d8b72588312a702b39ccce78723/src/lib/agents.ts); [server boundary](https://github.com/abcampbel/open-bots/blob/030b9e58b9df6d8b72588312a702b39ccce78723/server.ts).
- Basis: Structural absence at exact source boundary.
- Confidence: High.
- Caveats: An external/hypothetical supervisor has not been assessed or credited.

### Absence scope

- Surfaces inspected: Four frontend roles, client UI, server endpoint, README architecture, npm scripts and declared tool/delegation surfaces.
- Plausible first-party paths checked: Delegating agent as team manager, PLUTUS/HEPHAESTUS pairing, provider router and server as an implicit supervisor.
- Why no material first-party path remains: The claimed agent/delegation logic is in missing backend source; the remaining frontend/server scaffold has no whole-current regulatory judgment or return into running S1s.

## S3* — Complementary audit

- State: —
- Function: No independent complementary observation that challenges live S1/S3 claims and feeds corrective findings into current management is established.
- Disturbance / variety regulated: Incorrect web claims, code/tool results and payment receipts might require audit, but no first-party audit function is reachable.
- Decisive decision or feedback right: The README advertises citations, safety checks and benchmarks, while actual independent audit verdicts or rework instructions are not implemented in the shipped tree.
- Decision owner: Not established.
- Supporting / enforcement mechanisms: Tool-trail UI and source tests; tests import absent `api/chat` and cannot attest execution at this frozen code boundary.
- Closure path: No live reported S1 outcome → independent audit observation → corrective S3 decision can be followed in source.
- Why this is / is not agent-owned: Displayed traces and unit-test names are not an independent audit-to-control function, especially when the operational entry dependency is absent.
- Evidence: [tool-trail description](https://github.com/abcampbel/open-bots/blob/030b9e58b9df6d8b72588312a702b39ccce78723/README.md#L20-L44); [test dependency](https://github.com/abcampbel/open-bots/blob/030b9e58b9df6d8b72588312a702b39ccce78723/tests/agent-loop.test.ts#L1-L9); [backend import](https://github.com/abcampbel/open-bots/blob/030b9e58b9df6d8b72588312a702b39ccce78723/server.ts#L1-L5).
- Basis: Negative source-path check.
- Confidence: High at the reviewed revision.
- Caveats: Marketing screenshots cannot substitute for source-proven independent inspection and return.

### Absence scope

- Surfaces inspected: Screenshot/tool-trail UI, README benchmark/safety claims, test sources and backend imports.
- Plausible first-party paths checked: Trace UI as audit, web fact checking, independent code tests, payment confirmation, external model reviewing itself.
- Why no material first-party path remains: No independent audit actor, complementary evidence path or findings-to-control feedback is shipped, and the putative operational backend is absent.

## S4 — Outside-and-then intelligence

- State: —
- Function: No prospective outside-environment intelligence and adopted capability adaptation loop is established.
- Disturbance / variety regulated: Changing APIs, market conditions, tool prices and model capabilities are advertised as task inputs, not evidenced drivers of a first-party future organizational adaptation process.
- Decisive decision or feedback right: No shipped actor compares future-relevant alternatives and adopts an upgrade to the harness's ongoing capability.
- Decision owner: Not established; the documented provider fallback is not implemented at the frozen ref, and ordinary configuration would in any event not establish S4 by itself.
- Supporting / enforcement mechanisms: Advertised market snapshot, provider routing and local model configuration fields in documentation and static UI.
- Closure path: No source-backed external sensing → alternative capability design → adopted option → changed future operations path exists.
- Why this is / is not agent-owned: Agent research of current events, if it were implemented, would still be operational task work unless it prospectively changed the system's own capabilities.
- Evidence: [provider/fallback claims](https://github.com/abcampbel/open-bots/blob/030b9e58b9df6d8b72588312a702b39ccce78723/README.md#L144-L204); [missing backend import](https://github.com/abcampbel/open-bots/blob/030b9e58b9df6d8b72588312a702b39ccce78723/server.ts#L1-L5).
- Basis: Bounded absence, stronger than merely missing adaptation documentation.
- Confidence: High.
- Caveats: External maintainers may evolve the product in future commits; repository maintenance is not the assessed runtime S4.

### Absence scope

- Surfaces inspected: Claimed model router, tools/provider config, README roadmap, persona data, build routes and frozen Git inventory.
- Plausible first-party paths checked: Provider selection, live market research, changing API/tool availability, model substitution, self-improvement implied by “Agnes” claims.
- Why no material first-party path remains: The implementation module for routing/tools is absent and no remaining shipped component forms a prospective adaptation and adoption loop into operating capability.

## S5 — Identity and ultimate policy

- State: —
- Function: No legitimate first-party ultimate identity/policy settlement is established for an operating OpenBots organization.
- Disturbance / variety regulated: Brand/persona consistency, payment risk and safe tool access are described, but these are static instructions or proposed tool constraints, not organizational identity conflict closure.
- Decisive decision or feedback right: Persona system prompts set declared identities and README promises transaction confirmation; neither supplies an identity-level policy proposal, legitimate adjudicator and return to whole-system regulation.
- Decision owner: Repository authors/users can write prompts and configure service settings; no operating first-party S5 authority path is shipped.
- Supporting / enforcement mechanisms: Persona systemPrompt constants, advertised payment limits, static flags and UI action affordances.
- Closure path: No identity/ultimate-policy issue → policy authority → binding decision → revised organizational operation loop is present.
- Why this is / is not agent-owned: A mandatory persona claim such as “I run on Agnes” is text, not S5; safety/payment approval, even if restored, is operational permission rather than ultimate identity governance.
- Evidence: [persona policy text](https://github.com/abcampbel/open-bots/blob/030b9e58b9df6d8b72588312a702b39ccce78723/src/lib/agents.ts#L1-L110); [claimed payment configuration](https://github.com/abcampbel/open-bots/blob/030b9e58b9df6d8b72588312a702b39ccce78723/README.md#L160-L205).
- Basis: Negative source-first judgment at standard distribution boundary.
- Confidence: High.
- Caveats: Project author authority outside the shipped runtime is not assessed as S5.

### Absence scope

- Surfaces inspected: Persona prompts, server scaffold, package and deployment configuration, README safety/payment claims, source tests.
- Plausible first-party paths checked: Persona/systemPrompt identity, payment human confirmation, deployment operator configuration, authored policy files or rules.
- Why no material first-party path remains: There is no operational identity issue channel, ultimate authority settlement or accepted-policy return; source has only static constraints, claims and a missing backend dependency.

## Summary and evidence gaps

| Function | S1 | S2 | S3 | S3* | S4 | S5 |
| --- | --- | --- | --- | --- | --- | --- |
| State | — | — | — | — | — | — |

**Proposed disposition: `excluded-no-agentic-vsm`**, not because the product *claims too little*, but because the exact standard Git distribution does not include its indispensable `api/chat` implementation. The shell/Node syntax-independent checks `git ls-tree -r --name-only HEAD` and filesystem existence tests confirm this concrete import gap. A developer can repair it and seek a later new-ref assessment; this frozen review cannot silently use earlier code, an unrelated clone or the hosted website.

No real LLM, provider, Browser, code-execution agent or task-completion run was performed. The source import-resolution conclusion is bounded to the pinned Git tree; no claim is made about private hosted service availability, benchmark validity or model output quality.
