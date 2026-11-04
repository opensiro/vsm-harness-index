---
harness_id: must-company-ax-booster-open-agent-harness
project_name: Open Agent Harness
repository: https://github.com/MUST-Company-AX-Booster/Open-Agent-Harness
review_ref: 2b17fda4b5f0fe55dd577913aad8bd5febd4ba92
reviewed_at: 2026-11-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: P
---

# Open Agent Harness

## Review boundary

- System in focus: One deployed Open Agent Harness project-team assistant assembled from this repository's Docker Compose, configuration and first-party plugins/skills plus its **pinned** Hermes Agent submodule. The task boundary is the local team's Slack assistant and its bounded research subagents, not every feature or organization of upstream Hermes Agent independently.
- Purpose and identity: Answer project-team questions using cited Slack/Telegram histories and optional Jira, GitHub and Notion; distinguish proposals from decisions, make owner-confirmed Jira writes and preserve team context.
- Relevant environment: Slack conversations, Telegram groups, Jira tickets, GitHub/Notion documents, PostgreSQL team history, nightly summaries, external LLM provider, allowed users, owner approval and integration failures.
- Standard-distribution boundary: `docker-compose.yml` mounts the project-specific `SOUL.md`, Hermes config, team-history skill and plugins into the Hermes gateway built from gitlink `hermes-agent@f97608f178d1ffeca59860195ab7da295f7c8e5f`. Collector and connectors provide data/tools but are not independent model actors.
- Credited operating / distribution surfaces: [Compose runtime and pinned submodule](https://github.com/MUST-Company-AX-Booster/Open-Agent-Harness/blob/2b17fda4b5f0fe55dd577913aad8bd5febd4ba92/docker-compose.yml), [agent configuration](https://github.com/MUST-Company-AX-Booster/Open-Agent-Harness/blob/2b17fda4b5f0fe55dd577913aad8bd5febd4ba92/hermes/config.yaml), [project SOUL charter](https://github.com/MUST-Company-AX-Booster/Open-Agent-Harness/blob/2b17fda4b5f0fe55dd577913aad8bd5febd4ba92/hermes/SOUL.md), [setup skill](https://github.com/MUST-Company-AX-Booster/Open-Agent-Harness/blob/2b17fda4b5f0fe55dd577913aad8bd5febd4ba92/skills/open-agent-setup/SKILL.md), [team-history skill](https://github.com/MUST-Company-AX-Booster/Open-Agent-Harness/blob/2b17fda4b5f0fe55dd577913aad8bd5febd4ba92/hermes/skills/team-history/SKILL.md), [Jev message router](https://github.com/MUST-Company-AX-Booster/Open-Agent-Harness/blob/2b17fda4b5f0fe55dd577913aad8bd5febd4ba92/hermes/plugins/oa_router/__init__.py), [pinned Hermes identity loader](https://github.com/NousResearch/hermes-agent/blob/f97608f178d1ffeca59860195ab7da295f7c8e5f/agent/prompt_builder.py).
- Adjacent first-party surfaces excluded from ownership: Mascot role names (branding only), screenshots/docs/site, project contributor governance, integration tests/evaluations, setup-agent work before deployment, optional Jev external inference as a distinct organizational owner, and upstream Hermes capabilities disabled by this project config.
- First-party operating / deployment modes considered: Self-hosted Slack gateway with configured model, teamdb and Slack collector; optionally Telegram/Jira/GitHub/Notion; default model and optional configured Jev multi-step routing; up to three short Hermes research subagents; nightly Cron summaries; owner-edited project SOUL and approval-gated Jira writes.
- Recursion level: One project-team assistant instance and its occasional subordinate research cells. Neither six decorative animal personas nor each database connector represents a separate S1 operation unit.
- Reviewed revision: `2b17fda4b5f0fe55dd577913aad8bd5febd4ba92`; Hermes gitlink `f97608f178d1ffeca59860195ab7da295f7c8e5f` inspected at the pinned submodule revision.
- Observation date: 2026-11-04.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Docker Compose builds Hermes Agent from a pinned git submodule and mounts project-specific instructions and plugins. A collector ingests Slack/Telegram history into PostgreSQL/PGroonga; a team database connector supplies read-only history and narrowly permitted summary writes; Jira MCP exposes selected read/create/update/comment APIs; GitHub is configured read-only. The configured Hermes model owns tool selection, response synthesis and, for model-selected multi-step requests, Todo/subagent delegation. The Jev router optionally selects a model/effort and injects a multi-step research guide, but without a fully configured routing ladder it remains off; this model-picker is not the assistant's S3 decision maker. A nightly Cron model summarizes yesterday's team messages for later retrieval, with data stores enforcing access. The human configures `SOUL.md` and integration boundaries, which are loaded as authoritative project identity each turn. [README](https://github.com/MUST-Company-AX-Booster/Open-Agent-Harness/blob/2b17fda4b5f0fe55dd577913aad8bd5febd4ba92/README.md), [Compose](https://github.com/MUST-Company-AX-Booster/Open-Agent-Harness/blob/2b17fda4b5f0fe55dd577913aad8bd5febd4ba92/docker-compose.yml), [config](https://github.com/MUST-Company-AX-Booster/Open-Agent-Harness/blob/2b17fda4b5f0fe55dd577913aad8bd5febd4ba92/hermes/config.yaml).

## Operational model

An authorized Slack user asks about team work; Hermes model selects team-history, Jira and other permitted tools, searches time-bounded evidence, evaluates what was decided, reports source-linked findings and may ask for confirmation before changing Jira. For complex research, an optional configured router prompts Todo planning and several concurrent subordinate research agents; their results return in one call and the Hermes parent chooses how to synthesize them. Overnight, a Cron mode writes domain summaries, which later questions may read. The human installation owner defines project scope and team identity in SOUL and integration configuration. Hard SQL write restrictions, allowed Slack users and provider routing are external/deterministic enforcement, not independent VSM decision actors.

## S1 — Operations

- State: A
- Function: Answer team/project queries, interpret evidence and optionally draft/execute authorized Jira changes through a model/tool feedback loop.
- Disturbance / variety regulated: Ambiguous messages, changing project facts, incomplete histories, source inconsistencies, connector responses and failed searches.
- Decisive decision or feedback right: Choose relevant sources and search queries, reconcile newer versus older facts, decide whether the requested response or a next lookup is needed.
- Decision owner: Model-bearing Hermes Agent session, using first-party team-history skill and linked tool responses.
- Supporting / enforcement mechanisms: Pinned Hermes tool loop, teamdb/Jira connectors, collector, project instructions, permission and write gates.
- Closure path: User question → Hermes model selects a source/tool → reads raw history and task evidence → revises query/reasoning → returns cited answer or asks permission for an action.
- Boundary reachability: Compose actually starts `hermes gateway run` with configured model and mounts `SOUL.md` plus team-history skill; pinned Hermes is a checked-in gitlink built by the standard distribution, not a hypothetical provider API.
- Why this is / is not agent-owned: The agent selects which evidence matters and the response/action; a database, polling loop and optional model selector cannot make those semantic choices.
- Evidence: [Compose](https://github.com/MUST-Company-AX-Booster/Open-Agent-Harness/blob/2b17fda4b5f0fe55dd577913aad8bd5febd4ba92/docker-compose.yml), [team-history decisions/tool search](https://github.com/MUST-Company-AX-Booster/Open-Agent-Harness/blob/2b17fda4b5f0fe55dd577913aad8bd5febd4ba92/hermes/skills/team-history/SKILL.md), [pinned Hermes agent entry](https://github.com/NousResearch/hermes-agent/blob/f97608f178d1ffeca59860195ab7da295f7c8e5f/run_agent.py).
- Basis: explicit + structural.
- Confidence: high for the standard model/tool composition; no external Slack/API-key live replay was run.
- Caveats: A collector or teamdb server alone cannot own the task operation. S1 depends on a user-configured model provider and source access.

## S2 — Coordination

- State: —
- Function: No separately owned regulation of mutual interference among multiple independent operational cells is established in the shipped Open Agent deployment.
- Disturbance / variety regulated: Potential competing subagent actions and shared sources are limited by tool scopes, provider caps and simple request order rather than an active peer-correction loop.
- Decisive decision or feedback right: Detect conflicting commitments of separately acting units and feed a corrective coordination choice to them; not established.
- Decision owner: Hermes parent may launch independent research children, but they return results directly without a shipped inter-child conflict adjudication relation; fixed tool/session caps are deterministic.
- Supporting / enforcement mechanisms: `delegation.max_concurrent_children`, subagent iteration caps, platform toolsets, read-only shared history and allowed SQL writes.
- Closure path: Child results return to the lead and are synthesized as a single answer (S3); no separate inter-child collision detection → coordination decision → revised commitments is traced.
- Why this is / is not agent-owned: The lead receiving parallel facts is not evidence that agents regulate interference among their work, and six mascot roles are expressly decorative.
- Evidence: [README mascot and architecture boundary](https://github.com/MUST-Company-AX-Booster/Open-Agent-Harness/blob/2b17fda4b5f0fe55dd577913aad8bd5febd4ba92/README.md), [delegation caps/toolsets](https://github.com/MUST-Company-AX-Booster/Open-Agent-Harness/blob/2b17fda4b5f0fe55dd577913aad8bd5febd4ba92/hermes/config.yaml), [router's bounded research parallelism](https://github.com/MUST-Company-AX-Booster/Open-Agent-Harness/blob/2b17fda4b5f0fe55dd577913aad8bd5febd4ba92/hermes/plugins/oa_router/__init__.py).
- Basis: structural + explicit.
- Confidence: medium-high for the configured Open Agent distribution.
- Caveats: Upstream Hermes may support additional collaboration modes, but they are not credited unless installed and reachable in this project's actual distribution.

### Absence scope

- Surfaces inspected: Hermes platform/delegation config, router's complex-task plan and subagent rules, collector, teamdb, mascot documentation and Cron summary path.
- Plausible first-party paths checked: Six named role mascots as peer agents; delegated research children as coordinated cells; allowed toolset and max-subagent limits as resource control; project history as a shared work ledger.
- Why no material first-party path remains: Mascots are branding; dispatched children are independent bounded research tasks with parent collection and no dedicated conflict/oscillation correction; limits and shared search are supporting enforcement/transport, not an agent-owned S2 loop.

## S3 — Inside-and-now control

- State: A
- Whole-system current view: For one complex user request, the lead Hermes model sees the full requested outcome, permitted sources, Todo plan, available helper results and current clarification/Jira approval status.
- Current-control decision scope: Split multi-source research into independent agent tasks, prioritize searches, choose whether further evidence is needed, and integrate subordinate findings into one owner-facing project answer.
- Function: Organize current cross-source and delegated research commitments for a whole bounded user task.
- Disturbance / variety regulated: Multiple overlapping sources, limited child budget, insufficient evidence, conflicting status claims and slow tool results.
- Decisive decision or feedback right: Choose 3–6 Todo steps, which independent research tasks merit parallel delegation, wait for helper returns, and change next evidence requests or answer based on combined findings.
- Decision owner: Lead Hermes model (not Jev classifier); user retains permission to approve externally visible Jira mutations.
- Supporting / enforcement mechanisms: `oa_router` complex-task guidance, pinned Hermes Todo/delegation tools, read-only search, child caps, Jira write approval and project charter.
- Closure path: Whole question and available sources → model chooses subtask/resource allocation → parallel agents and tools return evidence → lead decides what still needs verification and whether to deliver, update plan or request consent.
- Boundary reachability: `delegation` is explicitly in the Slack platform toolset, and the model-facing complex-task PLAN is supplied in the documented configured Jev mode; ordinary Hermes delegation remains available independently of that optional selector.
- Why this is / is not agent-owned: The model chooses work partition and integration; the router merely classifies message complexity/model tier, and the three-child cap only limits concurrency.
- Evidence: [model-facing PLAN and routing hook](https://github.com/MUST-Company-AX-Booster/Open-Agent-Harness/blob/2b17fda4b5f0fe55dd577913aad8bd5febd4ba92/hermes/plugins/oa_router/__init__.py), [enabled delegation and limits](https://github.com/MUST-Company-AX-Booster/Open-Agent-Harness/blob/2b17fda4b5f0fe55dd577913aad8bd5febd4ba92/hermes/config.yaml), [pinned Hermes delegation lifecycle](https://github.com/NousResearch/hermes-agent/blob/f97608f178d1ffeca59860195ab7da295f7c8e5f/agent/subagent_lifecycle.py).
- Basis: explicit + structural.
- Confidence: medium; functionality is source-visible, but a full multi-agent Slack session was not replayed.
- Caveats: A single trivial lookup has no active S3 team-control demand. An unconfigured Jev ladder does not supply a model-routing decision, but does not remove Hermes's normal agent/delegation path.

## S3* — Complementary audit

- State: —
- Function: No shipped independently owned complementary audit of the lead/worker's task claims with distinct evidence and corrective return is demonstrated.
- Disturbance / variety regulated: False project status answers and unreliable AI summaries; accuracy guidance requests multiple sources but does not create a separate audit organization.
- Decisive decision or feedback right: Independently challenge a producer's claims using raw primary evidence and return corrective findings to the controller; no distinct role or governed path installed.
- Decision owner: The same Hermes assistant gathers, cross-checks and answers facts; user confirmations and SQL constraints do not decide an independent audit verdict.
- Supporting / enforcement mechanisms: Source citations, team-history chronological checks, Jira status lookups and nightly summaries.
- Closure path: Same agent re-searches evidence before replying; no audit actor independent of producer or guaranteed corrective channel from a separate verifier.
- Why this is / is not agent-owned: Reading multiple sources is normal S1 answer verification, and delegated research facts are not automatically an independently audited production claim.
- Evidence: [SOUL accuracy rules](https://github.com/MUST-Company-AX-Booster/Open-Agent-Harness/blob/2b17fda4b5f0fe55dd577913aad8bd5febd4ba92/hermes/SOUL.md), [history search procedure](https://github.com/MUST-Company-AX-Booster/Open-Agent-Harness/blob/2b17fda4b5f0fe55dd577913aad8bd5febd4ba92/hermes/skills/team-history/SKILL.md), [config toolsets](https://github.com/MUST-Company-AX-Booster/Open-Agent-Harness/blob/2b17fda4b5f0fe55dd577913aad8bd5febd4ba92/hermes/config.yaml).
- Basis: structural + explicit.
- Confidence: medium-high for the shipped deployment.
- Caveats: An independently configured reviewer could be added to Hermes outside this deployment; that is not established by default.

### Absence scope

- Surfaces inspected: Agent instructions, team-history evidence rules, Cron summarization, Jev routing/skills, delegated-child conditions and test/evaluation docs.
- Plausible first-party paths checked: Cross-checking Jira/chat as independent audit; reporter/citation rules; multi-source research delegates; nighttime summary as verification; human approved ticket write.
- Why no material first-party path remains: These mechanisms either verify the same producer's answer, produce ordinary domain data or require a human external review; no separately governed independent raw-evidence audit verdict and controller return is shipped.

## S4 — Outside-and-then intelligence

- State: —
- Function: No first-party prospective environmental scanning that autonomously changes the assistant's future operating repertoire is demonstrated in the actual configured modes.
- Disturbance / variety regulated: New team discussions and changing project facts are retained as summaries but not converted into future capability/strategy updates.
- Decisive decision or feedback right: Choose a revised future operational strategy or skill configuration from external change and return it into future task control; not established.
- Decision owner: Nightly Hermes model creates a retrospective channel summary, while a human configures integrations and project identity; neither is shown deciding and applying future operating adaptation in this distribution.
- Supporting / enforcement mechanisms: `summaries` table, team-history search, Cron trigger and model-selected tools for current queries.
- Closure path: Yesterday's messages → model summary → next query may retrieve facts; no generated adaptation option changes the future monitoring or agent capability policy.
- Why this is / is not agent-owned: Storage/search that improves future factual recall is not itself an S4 outside-and-then adaptation decision. Optional Jev per-message model routing optimizes current question processing, not strategic capability learning.
- Evidence: [nightly summaries prompt](https://github.com/MUST-Company-AX-Booster/Open-Agent-Harness/blob/2b17fda4b5f0fe55dd577913aad8bd5febd4ba92/hermes/cron/nightly-summaries.md), [team-history retrieval](https://github.com/MUST-Company-AX-Booster/Open-Agent-Harness/blob/2b17fda4b5f0fe55dd577913aad8bd5febd4ba92/hermes/skills/team-history/SKILL.md), [router runtime](https://github.com/MUST-Company-AX-Booster/Open-Agent-Harness/blob/2b17fda4b5f0fe55dd577913aad8bd5febd4ba92/hermes/plugins/oa_router/__init__.py).
- Basis: structural + explicit.
- Confidence: medium-high within pinned deployed modes.
- Caveats: Teams may manually edit future tasks after reading summaries; that would require separately established adaptation ownership/return to change this state.

### Absence scope

- Surfaces inspected: Cron summary prompt, team-history skill, Jev routing, project identity file, optional model selector and user instructions.
- Plausible first-party paths checked: Nightly retrospective intelligence, persisted summary retrieval, per-message model tier change, owner project edits and setup skill configuration.
- Why no material first-party path remains: Nightly summary retains prior facts; per-message routing chooses current model resources; project edits are operator setup/identity. No shipped external-future sensing → model option/adaptation decision → changed future capability path is closed.

## S5 — Policy and identity

- State: P
- Identity / ultimate-policy issue: What the self-hosted Open Agent is for, whose project it serves, which product/team terms it adopts and which standing source/action policies bind its replies.
- Ultimate authority in each claimed mode: Legitimate installation/project owner edits the mounted project `SOUL.md` and chooses integration/authorization configuration during setup; the model cannot authoritatively rewrite that read-only-mounted identity file through its disabled file/terminal tools.
- Return-to-operation path: Owner changes project charter in `hermes/SOUL.md` → Compose mounts it into Hermes's home as read-only → pinned Hermes `load_soul_md` inserts its content into subsequent system context → future agent replies and source choices observe the owner's identity/policy.
- Function: Maintain the assistant's local project-team purpose and binding editorial/source boundaries.
- Disturbance / variety regulated: Changes to team identity, authoritative project sources and enduring desired response/governance rules across tasks.
- Decisive decision or feedback right: Define/replace the durable team-agent purpose and source policy, independent of one current lookup.
- Decision owner: Installation owner / authorized project maintainer, not agent subtask router or external model provider.
- Supporting / enforcement mechanisms: Setup skill, editable `SOUL.md`, read-only volume mount, Hermes first-party identity loader, platform toolsets.
- Closure path: Parent decides a policy/identity change → edits persistent charter and restarts/reloads as needed → Hermes assembles revised model prompt → subsequent operational decisions follow it.
- Boundary reachability: The standard Compose mounts this exact SOUL file read-only and the pinned source at gitlink `f97608f` loads it as primary identity; no optional outside reviewer or local test-only code is required.
- Why this is / is not agent-owned: The human changes binding project identity; the model uses it but cannot give itself that ultimate authority through ordinary Slack tool calls.
- Evidence: [project SOUL and About-project block](https://github.com/MUST-Company-AX-Booster/Open-Agent-Harness/blob/2b17fda4b5f0fe55dd577913aad8bd5febd4ba92/hermes/SOUL.md), [setup instructions](https://github.com/MUST-Company-AX-Booster/Open-Agent-Harness/blob/2b17fda4b5f0fe55dd577913aad8bd5febd4ba92/skills/open-agent-setup/SKILL.md), [read-only mount and tool denial](https://github.com/MUST-Company-AX-Booster/Open-Agent-Harness/blob/2b17fda4b5f0fe55dd577913aad8bd5febd4ba92/docker-compose.yml), [pinned Hermes SOUL loader](https://github.com/NousResearch/hermes-agent/blob/f97608f178d1ffeca59860195ab7da295f7c8e5f/agent/prompt_builder.py).
- Basis: explicit + structural.
- Confidence: high for local parent-authorized charter return, with no provider-backed behavioral measurement.
- Caveats: S5 parent mode is the durable project identity, not generic API-key setup, ticket approval or maintainer GitHub governance. Installing a third-party skill cannot authorize contrary identity changes.

## Distributed OSS parent arrangement

Different users deploy separate Open Agent instances with their own `SOUL.md`. Contributors to this GitHub repo and independent Hermes maintainers are not a shared agent parent at the assessed recursion. The positive parent S5 is restricted to each installation's owner-to-runtime charter loop.

## Self-hosted and non-human modes

The deployed bot is local/self-hosted and uses a configured model API; selected Jira/Notion/GitHub tools are bounded by owner consent and environment. A human parent establishes identity in `SOUL.md`; assistant turns can operate without ongoing human guidance, but Jira writes require approval and high-risk tools are removed. Optional Jev routing needs explicit rungs and a configured API key; it is not automatically available just because files are present.

## Recursion

For a complex turn the lead Hermes model can spawn bounded research children, but they receive restricted tools and return evidence to the parent's one answer. The source does not show each child maintaining an independent S1–S5 organization. External Telegram/Slack teams are the environment, not automatically part of the assistant's recursion.

## Variety and escalation

Named source integration/SQL read boundaries attenuate misinformation and data risk. The configured model and helpers select searches and stage commitments; for Jira mutations, approval returns to the human. Nightly summaries condense repeated messages but do not rewrite operating purpose. Missing source access, stale Slack ingestion and conflicting evidence trigger further search or user clarification rather than fabricated policy decisions.

## Evidence gaps

- No live Slack/Telegram/Jira tokens, paid model provider or end-to-end Compose deployment was used; the mapping rests on pinned source, config and installed Hermes gitlink.
- The optional TypeSafe Jev ladder is not filled out in committed config, so S3 relies on standard Hermes model-owned delegation and the documented configured optional mode rather than claiming Jev is active by default.
- No shipped separate complementary S3* auditor, prospective S4 capability update, or inter-subagent interference correction was found in this configured product mode. Generic extensibility and upstream Hermes features outside its installed toolsets were not donated.
