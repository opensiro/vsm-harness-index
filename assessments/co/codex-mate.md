---
harness_id: codex-mate
project_name: Codex Mate
repository: https://github.com/SakuraByteCore/codexmate
review_ref: 2374786924999d1c0d9f823971b4d88606d2142c
reviewed_at: 2026-10-31
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

# Codex Mate

## Review boundary

- System in focus: Codex Mate's published Node CLI/Web/MCP local configuration, session and workflow-control product.
- Purpose and identity: manage heterogeneous local coding agents, provider configurations, prompts, session history and declared workflow steps.
- Relevant environment: operator-owned local configuration/session files, model endpoints and separately installed Codex/Claude/OpenCode/Pi and other CLIs.
- Standard-distribution boundary: package.json published cli.js, cli/, lib/, plugins/, skills/ and web-ui surfaces at the exact pinned revision.
- Credited operating / distribution surfaces: configuration/provider bridges, session utilities, workflow engine and supported command/MCP entry points are inspected; no autonomous ownership is credited.
- Adjacent first-party surfaces excluded from ownership: repository CI/release/CodeRabbit workflows, test fixtures and documentation-site build. External CLI internals and user-created workflows/prompts/third-party skills cannot donate ownership.
- First-party operating / deployment modes considered: local Web/CLI, MCP stdio, built-in and custom workflows, direct agent proxy commands, provider bridges and packaged context-recovery skill.
- Recursion level: one Codex Mate installation; external coding-agent organizations are distinct dependencies.
- Reviewed revision: `SakuraByteCore/codexmate@2374786924999d1c0d9f823971b4d88606d2142c`; immutable intake #2446 / serial controller #2447; historical #201 pin preserved.
- Observation date: 2026-10-31.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[README.md](https://github.com/SakuraByteCore/codexmate/blob/2374786924999d1c0d9f823971b4d88606d2142c/README.md); [package.json](https://github.com/SakuraByteCore/codexmate/blob/2374786924999d1c0d9f823971b4d88606d2142c/package.json); [site/guide/limits.md](https://github.com/SakuraByteCore/codexmate/blob/2374786924999d1c0d9f823971b4d88606d2142c/site/guide/limits.md) explicitly describe a local bridge/configuration/session layer over original tools. The package declares external agent installation, rather than bundling an autonomous coding runtime. [cli.js](https://github.com/SakuraByteCore/codexmate/blob/2374786924999d1c0d9f823971b4d88606d2142c/cli.js) implements provider/session controls, native-CLI spawning (runProxyCommand), built-in/custom workflow registration and record persistence. [lib/workflow-engine.js](https://github.com/SakuraByteCore/codexmate/blob/2374786924999d1c0d9f823971b4d88606d2142c/lib/workflow-engine.js) iterates declared steps, resolves templates, evaluates fixed conditions, invokes supplied handlers and honors allowWrite/dryRun; it does not select tool actions through an owned model feedback loop. [lib/mcp-stdio.js](https://github.com/SakuraByteCore/codexmate/blob/2374786924999d1c0d9f823971b4d88606d2142c/lib/mcp-stdio.js) exposes callable tools/resources/prompts to another host.

[cli/openai-bridge.js](https://github.com/SakuraByteCore/codexmate/blob/2374786924999d1c0d9f823971b4d88606d2142c/cli/openai-bridge.js); [cli/claude-proxy.js](https://github.com/SakuraByteCore/codexmate/blob/2374786924999d1c0d9f823971b4d88606d2142c/cli/claude-proxy.js); [cli/local-bridge.js](https://github.com/SakuraByteCore/codexmate/blob/2374786924999d1c0d9f823971b4d88606d2142c/cli/local-bridge.js) transform/proxy inference protocol; forwarding model requests is not owning the caller's operational discretion. The included [skills/context-recovery/SKILL.md](https://github.com/SakuraByteCore/codexmate/blob/2374786924999d1c0d9f823971b4d88606d2142c/skills/context-recovery/SKILL.md) guides an external agent's historical session search/handoff and live-verification discipline, not a Codex Mate-owned continuing coding organization. Prompt plugins supply text presets. Native workflow-engine fixtures test deterministic condition/write behavior. LICENSE/package declare Apache-2.0.

## Operational model

Recommended canonical disposition: **excluded-no-agentic-vsm** at this published control-product boundary. Substantive local control and provider/session/workflow support is established, but no first-party autonomous operational decision/action loop closes the general autonomous-harness inclusion requirement. External agents may perform excellent autonomous work through the bridge; their operational/metasystem rights are not reassigned to this product. The bundled context-recovery instructions and user-authored extensibility were specifically checked before exclusion.

## S1 — Operations

- State: —
- Function: No qualifying first-party autonomous operational work loop.
- Disturbance / variety regulated: Provider/configuration/task/session variety.
- Decisive decision or feedback right: A first-party agent choosing operational actions with returned evidence.
- Decision owner: User, predefined workflow definitions and external CLI agents.
- Supporting / enforcement mechanisms: Proxy spawning, HTTP normalization, native configuration files and deterministic workflow handlers.
- Closure path: Declared steps execute and are logged; proxy command passes input/output to the external CLI. No owned model→tool→feedback decision loop is supplied.
- Why this is / is not agent-owned: Removing the external autonomous caller leaves configuration/session tools and a deterministic step interpreter. The context-recovery skill is a bounded external-host helper, not an installed owned work/recovery organization.
- Evidence: [cli.js](https://github.com/SakuraByteCore/codexmate/blob/2374786924999d1c0d9f823971b4d88606d2142c/cli.js); [lib/workflow-engine.js](https://github.com/SakuraByteCore/codexmate/blob/2374786924999d1c0d9f823971b4d88606d2142c/lib/workflow-engine.js); [package.json](https://github.com/SakuraByteCore/codexmate/blob/2374786924999d1c0d9f823971b4d88606d2142c/package.json); [skills/context-recovery/SKILL.md](https://github.com/SakuraByteCore/codexmate/blob/2374786924999d1c0d9f823971b4d88606d2142c/skills/context-recovery/SKILL.md)
- Basis: structural
- Confidence: high
- Caveats: Source-based boundary judgment; no live model or production effectiveness claim.

### Absence scope

- Surfaces inspected: CLI proxy launch, workflow engine, published package, context skill and README supported modes.
- Plausible first-party paths checked: Native model-protocol bridges, workflow tool callbacks and included agent-readable skill.
- Why no material first-party path remains: The bridges transport another system’s requests, workflow semantics are predeclared, and the skill is session evidence retrieval for that other host; sufficient first-party autonomous operations are not established.

## S2 — Coordination

- State: —
- Function: No first-party S2-specific inter-S1 regulation established.
- Disturbance / variety regulated: Potential contention between independently running external agents.
- Decisive decision or feedback right: Choose/return an interference-specific coordination response.
- Decision owner: Operator or external caller; no first-party agent coordination owner.
- Supporting / enforcement mechanisms: Workflow sequencing/conditions, session metadata and config separation.
- Closure path: Steps consume earlier outputs, but no identified inter-S1 oscillation/conflict plus reciprocal adjustment is implemented.
- Why this is / is not agent-owned: Multi-agent support and dependency ordering alone do not establish S2 or its constructor state.
- Evidence: [lib/workflow-engine.js](https://github.com/SakuraByteCore/codexmate/blob/2374786924999d1c0d9f823971b4d88606d2142c/lib/workflow-engine.js); [cli.js](https://github.com/SakuraByteCore/codexmate/blob/2374786924999d1c0d9f823971b4d88606d2142c/cli.js); [site/guide/tasks.md](https://github.com/SakuraByteCore/codexmate/blob/2374786924999d1c0d9f823971b4d88606d2142c/site/guide/tasks.md)
- Basis: structural
- Confidence: high
- Caveats: Source-based boundary judgment; no live model or production effectiveness claim.

### Absence scope

- Surfaces inspected: Workflow definitions/engine, task documentation, agent proxy and configuration/session paths.
- Plausible first-party paths checked: Dependency/condition sequencing, per-agent config isolation and unified session browsing.
- Why no material first-party path remains: These organize calls/state without a first-party relation regulating a concrete interaction disturbance among autonomous S1 units.

## S3 — Inside-and-now control

- State: —
- Function: No first-party whole-agent-organization current-control loop established.
- Disturbance / variety regulated: Shared commitments/resources across agent work, beyond provider configuration.
- Decisive decision or feedback right: Whole-system discretionary commitment/resource regulation and returned decision.
- Decision owner: Users choose configs and invoke commands; native agents retain work decisions.
- Supporting / enforcement mechanisms: Provider selection, health cleanup, logs and allowWrite/dryRun flags.
- Closure path: Configuration changes affect subsequent provider calls; that is technical management, not evidenced organizational S3.
- Why this is / is not agent-owned: A broad dashboard and write permission do not themselves establish S3; ordinary human config edits do not warrant P.
- Evidence: [cli.js](https://github.com/SakuraByteCore/codexmate/blob/2374786924999d1c0d9f823971b4d88606d2142c/cli.js); [cli/config-health.js](https://github.com/SakuraByteCore/codexmate/blob/2374786924999d1c0d9f823971b4d88606d2142c/cli/config-health.js); [lib/workflow-engine.js](https://github.com/SakuraByteCore/codexmate/blob/2374786924999d1c0d9f823971b4d88606d2142c/lib/workflow-engine.js)
- Basis: structural
- Confidence: high
- Caveats: Source-based boundary judgment; no live model or production effectiveness claim.

### Absence scope

- Surfaces inspected: CLI/Web workflow/config health, record store and supported operator modes.
- Plausible first-party paths checked: Provider switching/cleanup, workflow controls and native-CLI launch.
- Why no material first-party path remains: No function-specific whole-current commitments view with an owned regulating decision/return is supplied at the autonomous-organization boundary.

## S3* — Complementary audit

- State: —
- Function: No deployed complementary operational-audit organization.
- Disturbance / variety regulated: Potential discrepancy between reported agent work and reality.
- Decisive decision or feedback right: Independent audit judgment returning into accountable control.
- Decision owner: No first-party runtime auditor identified.
- Supporting / enforcement mechanisms: Logs, workflow validation, session inspection and config health probes.
- Closure path: Structural workflow validation and exported sessions inform users; no distinct evidence challenge/corrective operational return is installed.
- Why this is / is not agent-owned: CodeRabbit/CI review belongs to repository development; it cannot be borrowed by the distributed product.
- Evidence: [lib/workflow-engine.js](https://github.com/SakuraByteCore/codexmate/blob/2374786924999d1c0d9f823971b4d88606d2142c/lib/workflow-engine.js); [cli/config-health.js](https://github.com/SakuraByteCore/codexmate/blob/2374786924999d1c0d9f823971b4d88606d2142c/cli/config-health.js); [lib/cli-sessions.js](https://github.com/SakuraByteCore/codexmate/blob/2374786924999d1c0d9f823971b4d88606d2142c/lib/cli-sessions.js); [tests/unit/coderabbit-workflows.test.mjs](https://github.com/SakuraByteCore/codexmate/blob/2374786924999d1c0d9f823971b4d88606d2142c/tests/unit/coderabbit-workflows.test.mjs)
- Basis: structural
- Confidence: high
- Caveats: Source-based boundary judgment; no live model or production effectiveness claim.

### Absence scope

- Surfaces inspected: Runtime workflow/config/session paths and development-review boundary.
- Plausible first-party paths checked: Health probes, workflow schema validation, session recovery and repository review integrations.
- Why no material first-party path remains: Routine diagnostics/history retrieval are not a separate authorized complementary audit loop over the product’s agent operations.

## S4 — Outside-and-then intelligence

- State: —
- Function: No first-party externally prospective organizational adaptation loop.
- Disturbance / variety regulated: Future model/tool/environment changes.
- Decisive decision or feedback right: Generate/admit adaptation options and return them into present capability.
- Decision owner: User chooses models, imports skills and updates software.
- Supporting / enforcement mechanisms: Provider model lists, skill marketplace, prompt/history stores and update CLI.
- Closure path: Selection/import/update persist requested choices, without a first-party environmental-option/adoption judgment.
- Why this is / is not agent-owned: Persistence, model discovery, archived-session recovery and software updates alone do not close S4 or a parent adaptation mode.
- Evidence: [cli/update.js](https://github.com/SakuraByteCore/codexmate/blob/2374786924999d1c0d9f823971b4d88606d2142c/cli/update.js); [cli/skills.js](https://github.com/SakuraByteCore/codexmate/blob/2374786924999d1c0d9f823971b4d88606d2142c/cli/skills.js); [lib/cli-models-utils.js](https://github.com/SakuraByteCore/codexmate/blob/2374786924999d1c0d9f823971b4d88606d2142c/lib/cli-models-utils.js); [skills/context-recovery/SKILL.md](https://github.com/SakuraByteCore/codexmate/blob/2374786924999d1c0d9f823971b4d88606d2142c/skills/context-recovery/SKILL.md)
- Basis: structural
- Confidence: high
- Caveats: Source-based boundary judgment; no live model or production effectiveness claim.

### Absence scope

- Surfaces inspected: Update/model/skills/session-context surfaces and documented workflow modes.
- Plausible first-party paths checked: New model discovery, prompt presets, skill imports, context handoff and package update.
- Why no material first-party path remains: These are operator-selected configuration or historical retrieval, not prospective options with a function-specific capability-adaptation return.

## S5 — Policy and identity

- State: —
- Function: No runtime identity/ultimate-policy decision and return path.
- Disturbance / variety regulated: Ultimate policy/identity tension rather than ordinary tool permissions.
- Decisive decision or feedback right: Reach legitimate ultimate authority and return an identity-level decision.
- Decision owner: Human edits prompt/configuration; no identity-level governance loop established.
- Supporting / enforcement mechanisms: AGENTS/CLAUDE editor, prompt presets, write flags and local key ownership.
- Closure path: Prompt/config changes return to native agents, but no ultimate-policy matter/adjudication relationship is supplied.
- Why this is / is not agent-owned: Rule acknowledgment and editable policy text do not establish legitimate S5 closure.
- Evidence: [cli/agents-files.js](https://github.com/SakuraByteCore/codexmate/blob/2374786924999d1c0d9f823971b4d88606d2142c/cli/agents-files.js); [cli/system-prompt-files.js](https://github.com/SakuraByteCore/codexmate/blob/2374786924999d1c0d9f823971b4d88606d2142c/cli/system-prompt-files.js); [plugins/prompt-templates/rule-ack/index.mjs](https://github.com/SakuraByteCore/codexmate/blob/2374786924999d1c0d9f823971b4d88606d2142c/plugins/prompt-templates/rule-ack/index.mjs); [site/guide/limits.md](https://github.com/SakuraByteCore/codexmate/blob/2374786924999d1c0d9f823971b4d88606d2142c/site/guide/limits.md)
- Basis: structural
- Confidence: high
- Caveats: Source-based boundary judgment; no live model or production effectiveness claim.

### Absence scope

- Surfaces inspected: Prompt/system-file editing, plugin rule presets, workflow permissions and local-user boundary.
- Plausible first-party paths checked: Rule acknowledgment, agent prompt editing and allowWrite authorization.
- Why no material first-party path remains: All are text/configuration or ordinary execution permission; no specific identity-level dispute/decision/return mode is supplied.

## Distributed OSS parent arrangement

Local operators own their configuration; repository maintainers and unrelated contributor-agent sessions are not automatically a runtime S3/S4/S5 parent organization.

## Self-hosted and non-human modes

Local self-hosting, native-agent proxy and MCP modes were examined. An MCP host or installed coding CLI is external; the external host can use the tools without donating its internal autonomy.

## Recursion

Multiple agent configurations/sessions and workflow step nesting do not establish recursive viable systems.

## Variety and escalation

The product attenuates configuration/protocol/session variety and reports deterministic failures. These are real mechanisms, with no inference of additional VSM rights from status names.

## Evidence gaps

No live provider, UI deployment, external coding execution or full upstream suite claimed. Five existing native workflow-engine tests passed in their minimal original test harness. Exclusion is source/purpose-relative, not a claim that custom workflows or external agents can never form an autonomous organization.
