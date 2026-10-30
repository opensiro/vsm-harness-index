---
harness_id: agent-harness-csharp
project_name: Agent Harness CSharp
repository: https://github.com/jackhuclan/harness_demo
review_ref: a56e1f8230ed8415d079306602962bb90a79fa03
reviewed_at: 2026-10-29
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

# Agent Harness CSharp

## Review boundary

- System in focus: the shipped C# Agent Harness API and its model/tool session loop, not a semiconductor factory or the repository's contributor organization.
- Purpose and identity: answer user requests by selecting registered tools and returning results through a layered ASP.NET application.
- Relevant environment: API users, an operator-selected OpenAI-compatible model endpoint, local session state and registered demonstration tools.
- Standard-distribution boundary: checked-in Host, AgentCore, Model, Session, Execution, Skills, State and Security projects; configured real-model mode and default rule-based offline mode.
- Credited operating / distribution surfaces: Host DI and /chat entry points, OpenAiLlmClient, Agent.RunAsync/StreamRunAsync and ToolExecutor.
- Adjacent first-party surfaces excluded from ownership: Next.js presentation client, PRD/implementation plans, unit tests, CI and AGENTS contributor instructions; no adjacent actor is borrowed as a deployed regulator.
- First-party operating / deployment modes considered: USE_REAL_LLM=true activates the shipped model client without custom agent composition; false uses a rule-based mock and does not itself demonstrate AI decision ownership.
- Recursion level: one API/session harness. AgentRegistry role names and domain tools do not establish recursive organizations.
- Reviewed revision: `a56e1f8230ed8415d079306602962bb90a79fa03`.
- Observation date: 2026-10-29.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[src/HarnessDemo.Host/Program.cs](https://github.com/jackhuclan/harness_demo/blob/a56e1f8230ed8415d079306602962bb90a79fa03/src/HarnessDemo.Host/Program.cs) assembles in-memory stores, the single Agent controller, a tool registry, request security and API endpoints. [src/HarnessDemo.AgentCore/Agent.cs](https://github.com/jackhuclan/harness_demo/blob/a56e1f8230ed8415d079306602962bb90a79fa03/src/HarnessDemo.AgentCore/Agent.cs) repeatedly builds recent context, asks ILlmClient for a tool or final answer, executes the selected tool and returns its result to the next decision, bounded by six hops. [src/HarnessDemo.Model/OpenAiLlmClient.cs](https://github.com/jackhuclan/harness_demo/blob/a56e1f8230ed8415d079306602962bb90a79fa03/src/HarnessDemo.Model/OpenAiLlmClient.cs) implements real function-calling inference; rule-based mode is an offline substitute. [src/HarnessDemo.AgentCore/ContextManager.cs](https://github.com/jackhuclan/harness_demo/blob/a56e1f8230ed8415d079306602962bb90a79fa03/src/HarnessDemo.AgentCore/ContextManager.cs) retains ten recent messages under a fixed system prompt. Session history and last-answer memory persist only in process. The router logs a route while SessionManager invokes the same Agent.

The OVL extension adds named role definitions, packaged SKILL.md files and semiconductor analysis tools. Many apparent repair, learning and future-maintenance operations are returned demonstration strings: [src/HarnessDemo.Skills/OvlRemainingTools.cs](https://github.com/jackhuclan/harness_demo/blob/a56e1f8230ed8415d079306602962bb90a79fa03/src/HarnessDemo.Skills/OvlRemainingTools.cs) stores custom rules in a static list without wiring them into later decisions; disposition confirmation returns fixed success text. [src/HarnessDemo.Skills/OvlP1Tools.cs](https://github.com/jackhuclan/harness_demo/blob/a56e1f8230ed8415d079306602962bb90a79fa03/src/HarnessDemo.Skills/OvlP1Tools.cs) returns recommendation/compensation/experience text rather than an implemented factory or harness adaptation circuit. These are operational payloads, not metasystem ownership. User-facing confirmations and a fixed keyword gate are not identity governance.

## Operational model

One configured model-backed session is an S1 work unit: it chooses tools and revises its response from tool results. Runtime code owns dispatch, truncation, retries, timeout and hop enforcement. Developers choose tools/prompts and operators choose model configuration. The included AI mode is first-party and reachable; the default mock mode does not receive autonomous credit on its own.

## S1 — Operations

- State: A
- Function: turn user requests into model-selected tool interactions and answers.
- Disturbance / variety regulated: different requests, required tools, failed execution and returned tool observations.
- Decisive decision or feedback right: choose the next tool/arguments or final response after seeing prior results.
- Decision owner: configured model-backed agent in real-model mode.
- Supporting / enforcement mechanisms: DI, HTTP transport, recent-message context, registered tool execution, fixed retries/timeouts and hop cap.
- Closure path: model decision → ToolExecutor → Tool message appended to session → next model decision → answer saved and returned.
- Boundary reachability: documented USE_REAL_LLM=true selects the supplied OpenAiLlmClient in Host; /chat invokes the same first-party Agent loop with no new cognitive implementation.
- Why this is / is not agent-owned: removing model selection leaves only dispatch and fixed constraints, not materially the same task-specific decisions. Mock mode is explicitly excluded from this ownership claim.
- Evidence: [src/HarnessDemo.AgentCore/Agent.cs](https://github.com/jackhuclan/harness_demo/blob/a56e1f8230ed8415d079306602962bb90a79fa03/src/HarnessDemo.AgentCore/Agent.cs); [src/HarnessDemo.Model/OpenAiLlmClient.cs](https://github.com/jackhuclan/harness_demo/blob/a56e1f8230ed8415d079306602962bb90a79fa03/src/HarnessDemo.Model/OpenAiLlmClient.cs); [src/HarnessDemo.Host/Program.cs](https://github.com/jackhuclan/harness_demo/blob/a56e1f8230ed8415d079306602962bb90a79fa03/src/HarnessDemo.Host/Program.cs); [README.md](https://github.com/jackhuclan/harness_demo/blob/a56e1f8230ed8415d079306602962bb90a79fa03/README.md).
- Basis: structural
- Confidence: high for source wiring, not provider compatibility or operational quality.
- Caveats: no live inference tested; generic empty tool schemas and synthetic historical tool-call IDs may limit real endpoint compatibility.

## S2 — Coordination

- State: —
- Function: Inter-unit interference regulation; not established at this boundary.
- Disturbance / variety regulated: AgentRegistry and Router provide role/intent labels, but SessionManager calls the same agent; sequential tool chains do not create distinct mutually interfering autonomous work cells.
- Decisive decision or feedback right: no qualifying function-specific right/return path established.
- Decision owner: no credited owner; developers/operators retain configuration decisions.
- Supporting / enforcement mechanisms: reviewed runtime, state, prompt and domain-tool mechanisms remain operational support.
- Closure path: no qualifying metasystem closure.
- Why this is / is not agent-owned: AgentRegistry and Router provide role/intent labels, but SessionManager calls the same agent; sequential tool chains do not create distinct mutually interfering autonomous work cells.
- Evidence: [src/HarnessDemo.Session/SessionManager.cs](https://github.com/jackhuclan/harness_demo/blob/a56e1f8230ed8415d079306602962bb90a79fa03/src/HarnessDemo.Session/SessionManager.cs); [src/HarnessDemo.Host/Program.cs](https://github.com/jackhuclan/harness_demo/blob/a56e1f8230ed8415d079306602962bb90a79fa03/src/HarnessDemo.Host/Program.cs); [README.md](https://github.com/jackhuclan/harness_demo/blob/a56e1f8230ed8415d079306602962bb90a79fa03/README.md).
- Basis: structural
- Confidence: high within the bounded shipped distribution.
- Caveats: extensions and a real industrial deployment could change the boundary; they are not supplied evidence here.

### Absence scope

- Surfaces inspected: Host wiring/endpoints, Agent/ContextManager, model/role/skill registry, SessionManager/Router, ToolExecutor, state stores, Security, OVL P0/P1/remaining tools, README, PRD/implementation plan and tests/CI roles.
- Plausible first-party paths checked: role selection, concurrent sessions and MultiSkillChainTool sequencing.
- Why no material first-party path remains: No supplied inter-S1 disturbance-specific adjustment and feedback relation is wired; multi-agent extension in README requires new implementation.

## S3 — Inside-and-now control

- State: —
- Function: Whole-harness current resource and commitment regulation; not established at this boundary.
- Disturbance / variety regulated: The controller's six-hop cap, five-second tool timeout and retry are developer-selected enforcement. No whole-current view informs a discretionary allocation/intervention owner.
- Decisive decision or feedback right: no qualifying function-specific right/return path established.
- Decision owner: no credited owner; developers/operators retain configuration decisions.
- Supporting / enforcement mechanisms: reviewed runtime, state, prompt and domain-tool mechanisms remain operational support.
- Closure path: no qualifying metasystem closure.
- Why this is / is not agent-owned: The controller's six-hop cap, five-second tool timeout and retry are developer-selected enforcement. No whole-current view informs a discretionary allocation/intervention owner.
- Evidence: [src/HarnessDemo.Execution/ToolExecutor.cs](https://github.com/jackhuclan/harness_demo/blob/a56e1f8230ed8415d079306602962bb90a79fa03/src/HarnessDemo.Execution/ToolExecutor.cs); [src/HarnessDemo.Host/Program.cs](https://github.com/jackhuclan/harness_demo/blob/a56e1f8230ed8415d079306602962bb90a79fa03/src/HarnessDemo.Host/Program.cs); [README.md](https://github.com/jackhuclan/harness_demo/blob/a56e1f8230ed8415d079306602962bb90a79fa03/README.md).
- Basis: structural
- Confidence: high within the bounded shipped distribution.
- Caveats: extensions and a real industrial deployment could change the boundary; they are not supplied evidence here.

### Absence scope

- Surfaces inspected: Host wiring/endpoints, Agent/ContextManager, model/role/skill registry, SessionManager/Router, ToolExecutor, state stores, Security, OVL P0/P1/remaining tools, README, PRD/implementation plan and tests/CI roles.
- Plausible first-party paths checked: controller limits, session listing, task store, operator configuration and domain budget decomposition.
- Why no material first-party path remains: The API exposes observations and fixed local limits but no first-party whole-system current-control decision/return loop; OVL budget data is task-domain analysis, not allocation of harness resources.

## S3* — Complementary audit

- State: —
- Function: Independent complementary challenge of operational claims; not established at this boundary.
- Disturbance / variety regulated: SensitiveWordAuditor is an input blacklist, not complementary access to the truth of the agent's work. Unit tests and fixed OVL reports do not instantiate a separate deployed audit actor.
- Decisive decision or feedback right: no qualifying function-specific right/return path established.
- Decision owner: no credited owner; developers/operators retain configuration decisions.
- Supporting / enforcement mechanisms: reviewed runtime, state, prompt and domain-tool mechanisms remain operational support.
- Closure path: no qualifying metasystem closure.
- Why this is / is not agent-owned: SensitiveWordAuditor is an input blacklist, not complementary access to the truth of the agent's work. Unit tests and fixed OVL reports do not instantiate a separate deployed audit actor.
- Evidence: [src/HarnessDemo.Security/SensitiveWordAuditor.cs](https://github.com/jackhuclan/harness_demo/blob/a56e1f8230ed8415d079306602962bb90a79fa03/src/HarnessDemo.Security/SensitiveWordAuditor.cs); [src/HarnessDemo.Host/Program.cs](https://github.com/jackhuclan/harness_demo/blob/a56e1f8230ed8415d079306602962bb90a79fa03/src/HarnessDemo.Host/Program.cs); [README.md](https://github.com/jackhuclan/harness_demo/blob/a56e1f8230ed8415d079306602962bb90a79fa03/README.md).
- Basis: structural
- Confidence: high within the bounded shipped distribution.
- Caveats: extensions and a real industrial deployment could change the boundary; they are not supplied evidence here.

### Absence scope

- Surfaces inspected: Host wiring/endpoints, Agent/ContextManager, model/role/skill registry, SessionManager/Router, ToolExecutor, state stores, Security, OVL P0/P1/remaining tools, README, PRD/implementation plan and tests/CI roles.
- Plausible first-party paths checked: input auditor, session logs, OVL diagnostics, domain tests and CI.
- Why no material first-party path remains: All reviewed checks are entry validation, routine tool results or development checks; no sufficiently independent audit judgment with corrective return is supplied.

## S4 — Outside-and-then intelligence

- State: —
- Function: External/prospective adaptation of harness capability; not established at this boundary.
- Disturbance / variety regulated: Domain health forecasts and recipe recommendations are returned tool content; ExperienceLearnTool returns fixed acknowledgement and CustomSkillLearnTool's list is not consulted by later operations.
- Decisive decision or feedback right: no qualifying function-specific right/return path established.
- Decision owner: no credited owner; developers/operators retain configuration decisions.
- Supporting / enforcement mechanisms: reviewed runtime, state, prompt and domain-tool mechanisms remain operational support.
- Closure path: no qualifying metasystem closure.
- Why this is / is not agent-owned: Domain health forecasts and recipe recommendations are returned tool content; ExperienceLearnTool returns fixed acknowledgement and CustomSkillLearnTool's list is not consulted by later operations.
- Evidence: [src/HarnessDemo.Skills/OvlRemainingTools.cs](https://github.com/jackhuclan/harness_demo/blob/a56e1f8230ed8415d079306602962bb90a79fa03/src/HarnessDemo.Skills/OvlRemainingTools.cs); [src/HarnessDemo.Host/Program.cs](https://github.com/jackhuclan/harness_demo/blob/a56e1f8230ed8415d079306602962bb90a79fa03/src/HarnessDemo.Host/Program.cs); [README.md](https://github.com/jackhuclan/harness_demo/blob/a56e1f8230ed8415d079306602962bb90a79fa03/README.md).
- Basis: structural
- Confidence: high within the bounded shipped distribution.
- Caveats: extensions and a real industrial deployment could change the boundary; they are not supplied evidence here.

### Absence scope

- Surfaces inspected: Host wiring/endpoints, Agent/ContextManager, model/role/skill registry, SessionManager/Router, ToolExecutor, state stores, Security, OVL P0/P1/remaining tools, README, PRD/implementation plan and tests/CI roles.
- Plausible first-party paths checked: hardware-health forecasts, recipe optimization, experience learning, custom-skill list, memory store and PRD roadmap.
- Why no material first-party path remains: No shipped path transforms an external/prospective model into a selected change of current harness capability. Domain advice and unwired learning claims do not close adaptation.

## S5 — Policy and identity

- State: —
- Function: Runtime identity or ultimate-policy closure; not established at this boundary.
- Disturbance / variety regulated: ContextManager supplies a fixed system prompt, the auditor enforces keywords and confirmation strings concern ordinary task actions. None routes an identity issue to legitimate authority and returns an authoritative policy decision.
- Decisive decision or feedback right: no qualifying function-specific right/return path established.
- Decision owner: no credited owner; developers/operators retain configuration decisions.
- Supporting / enforcement mechanisms: reviewed runtime, state, prompt and domain-tool mechanisms remain operational support.
- Closure path: no qualifying metasystem closure.
- Why this is / is not agent-owned: ContextManager supplies a fixed system prompt, the auditor enforces keywords and confirmation strings concern ordinary task actions. None routes an identity issue to legitimate authority and returns an authoritative policy decision.
- Evidence: [src/HarnessDemo.AgentCore/ContextManager.cs](https://github.com/jackhuclan/harness_demo/blob/a56e1f8230ed8415d079306602962bb90a79fa03/src/HarnessDemo.AgentCore/ContextManager.cs); [src/HarnessDemo.Host/Program.cs](https://github.com/jackhuclan/harness_demo/blob/a56e1f8230ed8415d079306602962bb90a79fa03/src/HarnessDemo.Host/Program.cs); [README.md](https://github.com/jackhuclan/harness_demo/blob/a56e1f8230ed8415d079306602962bb90a79fa03/README.md).
- Basis: structural
- Confidence: high within the bounded shipped distribution.
- Caveats: extensions and a real industrial deployment could change the boundary; they are not supplied evidence here.

### Absence scope

- Surfaces inspected: Host wiring/endpoints, Agent/ContextManager, model/role/skill registry, SessionManager/Router, ToolExecutor, state stores, Security, OVL P0/P1/remaining tools, README, PRD/implementation plan and tests/CI roles.
- Plausible first-party paths checked: prompt, keyword gate, role definitions, confirmation tools, operator .env and contributor governance.
- Why no material first-party path remains: The supported API modes contain configurable constraints but no function-specific identity/ultimate-policy issue-decision-return circuit, autonomous or parent-governed.

## Distributed OSS parent arrangement

The MIT-licensed public repository includes contributor instructions and CI. These govern repository development; they do not wire a project-wide parent regulator into the assessed API. No organization-level parent state is inferred.

## Self-hosted and non-human modes

The Host supports real-model and offline mock selection through environment settings. Configuration, request blocking and ordinary confirmations do not establish a parent S3/S4/S5 loop. No separately deployed non-human metasystem is supplied.

## Recursion

Named OVL roles and tools do not establish recursive viability; SessionManager uses one Agent controller and the domain tools are not autonomous viable suborganizations.

## Variety and escalation

Recent-context truncation, retries, hop limits and model failure text attenuate local execution variety. REQUIRES_CONFIRM strings expose ordinary task intervention prompts; they do not prove enforced confirmation or an exceptional channel with metasystem closure.

## Evidence gaps

Static source assessment only. The .NET SDK is unavailable in the execution environment, so native build/xUnit tests were not run; no live model/provider call was made. Real function-calling compatibility and effective domain effects are unverified, and no factory-control, clinical, safety or product-quality claim is made. Shipped source paths are sufficient for bounded negative findings; future extensibility is not an unresolved shipped metasystem.
