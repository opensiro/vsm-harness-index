---
harness_id: codely-agent-harness
project_name: Codely Agent Harness
repository: https://github.com/CodelyTV/agent-harness
review_ref: 57090a7301d15722b8885570e239bdd3e719a835
reviewed_at: 2026-10-26
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

# Codely Agent Harness

## Review boundary

- System in focus: The installable Codely skills, conventions, tool hooks, output styles, LSP plugin descriptor and symlink scripts at the pinned repository revision—not the agent hosts in which they are installed.
- Purpose and identity: Distribute reusable coding instructions, planning/review conventions and command safeguards across external coding agents.
- Relevant environment: Operators selecting skills, project source trees, differing host-specific skill locations, unsafe shell command patterns and external Claude Code, Codex, Cursor, Copilot, OpenCode and Junie processes.
- Standard-distribution boundary: The checked-in `.agents/skills/` Markdown command packs, `.claude-plugin/` marketplace descriptors, `.claude/`, `.cursor/`, `.github/` and `.opencode/` integration hooks, `Makefile` and `scripts/generate-*-symlinks.sh`. `npx skills` or a Claude plugin manager installs the material; a separate agent application subsequently interprets the instructions.
- Credited operating / distribution surfaces: [Installation and skills](https://github.com/CodelyTV/agent-harness/blob/57090a7301d15722b8885570e239bdd3e719a835/README.md), [plugin marketplace](https://github.com/CodelyTV/agent-harness/blob/57090a7301d15722b8885570e239bdd3e719a835/.claude-plugin/marketplace.json), [Makefile](https://github.com/CodelyTV/agent-harness/blob/57090a7301d15722b8885570e239bdd3e719a835/Makefile), [Cursor hook](https://github.com/CodelyTV/agent-harness/blob/57090a7301d15722b8885570e239bdd3e719a835/.cursor/hooks/block-export.sh), [OpenCode hook](https://github.com/CodelyTV/agent-harness/blob/57090a7301d15722b8885570e239bdd3e719a835/.opencode/plugins/block-export.ts).
- Adjacent first-party surfaces excluded from ownership: The repository's command authoring and team conventions, agent-role instructions in its skills, host-driven implementation/review steps, third-party editor/model/tool runtimes, documentation examples and contributor maintenance. These may configure or guide an agent but are not a Codely-owned agent loop.
- First-party operating / deployment modes considered: Skills installed into an external coding agent by `npx skills`; Claude Code marketplace plugin installation; symlinked skills/rules for other coding hosts; host-invoked pre-tool hooks; optional external language-server process.
- Recursion level: Codely's distributed configuration/instruction package as a first-party product, not the external agent-enabled project/team receiving the package.
- Reviewed revision: `CodelyTV/agent-harness@57090a7301d15722b8885570e239bdd3e719a835`.
- Observation date: 2026-10-26; pinned static primary-source inspection only.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

This repository packages declarative skills and integration files rather than an independent inference/runtime process. The documented quickstart tells the operator to install selected skills into *chosen coding agents* and later invoke them **inside that agent**. The plugin marketplace lists skills, a simplified-English output style and a `tsc --lsp` integration, none of which launches or governs a first-party model→tool→observation→decision loop. The `Makefile` exposes symlink-generation shell scripts for host-specific directories. [Quickstart and integration table](https://github.com/CodelyTV/agent-harness/blob/57090a7301d15722b8885570e239bdd3e719a835/README.md), [marketplace](https://github.com/CodelyTV/agent-harness/blob/57090a7301d15722b8885570e239bdd3e719a835/.claude-plugin/marketplace.json), [Makefile](https://github.com/CodelyTV/agent-harness/blob/57090a7301d15722b8885570e239bdd3e719a835/Makefile).

Instructions such as `codely-plan-phase-implement` define a human-approved sequence and tell the **host agent** to implement one phase and pause for user review; they do not include a Codely service scheduling or executing that agent. The planning skills describe suggested subagents, but delegation is executed by the host's available tools and model, not by a shipped Codely orchestration runtime. [Implementation skill](https://github.com/CodelyTV/agent-harness/blob/57090a7301d15722b8885570e239bdd3e719a835/.agents/skills/codely-plan-phase-implement/SKILL.md), [subagent planning instructions](https://github.com/CodelyTV/agent-harness/blob/57090a7301d15722b8885570e239bdd3e719a835/.agents/skills/codely-plan-create-subagents/SKILL.md).

The executable hooks are narrow deterministic interceptors. For example, the Cursor `block-export.sh` parses host-delivered JSON and exits with code 2 on matching shell commands; the OpenCode plugin throws on a matching `bash` invocation. The hooks do not select task outcomes, learn from result quality, or own host agent planning. [Cursor hook](https://github.com/CodelyTV/agent-harness/blob/57090a7301d15722b8885570e239bdd3e719a835/.cursor/hooks/block-export.sh), [OpenCode plugin](https://github.com/CodelyTV/agent-harness/blob/57090a7301d15722b8885570e239bdd3e719a835/.opencode/plugins/block-export.ts).

## Operational model

First-party outcomes are installed files, standardized instructions, symlinks and deterministic command rejection. These are useful *supports* for autonomous coding agents, but the operational agent that interprets a skill, chooses an implementation, reads tool results and carries work to completion belongs to the external host. The package ships no independently invoked model session, agent worker, model adapter, task queue or first-party feedback loop; the README explicitly routes actual commands through selected external agents. Therefore the Index first-party autonomous-agent S1 inclusion condition is not established. The proposed terminal disposition is **`excluded-no-agentic-vsm`**, subject to review/admission, not a claim that the package is useless or that an installed host cannot be viable.

## S1 — Operations

- State: —
- Function: Autonomous operational units would interpret goals and environmental feedback to produce coding/documentation outcomes.
- Disturbance / variety regulated: Project-specific implementation needs, code feedback, tests, documentation conventions and tool outcomes.
- Decisive decision or feedback right: The selected external coding agent chooses tools, edits, revisions and completion; Codely skills supply prompts and commands.
- Decision owner: External model/agent host and its operator, not an independently running Codely agent.
- Supporting / enforcement mechanisms: Skills Markdown, host hooks, marketplace descriptors, rules and symlinks.
- Closure path: User installs package → external agent reads guidance → host agent acts; no Codely-owned outcome-feedback decision loop closes inside the reviewed first-party boundary.
- Boundary reachability: Not applicable: external host actor is deliberately excluded from first-party ownership.
- Why this is / is not agent-owned: A skill that tells another agent how to plan or implement is not itself the first-party autonomous operator; removing the external agent leaves inert instructions and deterministic hooks.
- Evidence: [installation flow](https://github.com/CodelyTV/agent-harness/blob/57090a7301d15722b8885570e239bdd3e719a835/README.md), [phase implementation instruction](https://github.com/CodelyTV/agent-harness/blob/57090a7301d15722b8885570e239bdd3e719a835/.agents/skills/codely-plan-phase-implement/SKILL.md).
- Basis: Structural.
- Confidence: High for the inspected distribution.
- Caveats: An assembled product *including* a separately supplied host could have S1, but is not this repository-relative system-in-focus.

### Absence scope

- Surfaces inspected: Entire tracked non-Git file inventory, README install/usage modes, skills, marketplace definitions, host hook code, Makefile and symlink scripts.
- Plausible first-party paths checked: Agent execution through plugin descriptor, RPI subagent skills, model invocation in hooks, phase implementation commands and symlink-generated host paths.
- Why no material first-party path remains: Each path either delivers static instructions/configuration, invokes a deterministic local tool or delegates intelligence to a third-party host; none ships a Codely-owned autonomous operating unit.

## S2 — Coordination

- State: —
- Function: Would attenuate specific inter-S1 conflicts among Codely-operated autonomous units.
- Disturbance / variety regulated: Hypothetical overlapping code edits, resource contention and inconsistent subagent outputs.
- Decisive decision or feedback right: The external agent/user decides how task phases and subagents are coordinated; Codely Markdown describes a proposed procedure only.
- Decision owner: External host/operator.
- Supporting / enforcement mechanisms: Plan-phase checklist conventions and suggested host subagent exploration.
- Closure path: No Codely-operated S1 pair exists for a first-party conflict regulation loop.
- Boundary reachability: Not applicable; host-managed subagents are outside this package boundary.
- Why this is / is not agent-owned: Suggesting concurrent exploration or serial phases neither supplies distinct first-party S1 units nor closes a specific conflict/oscillation response between them.
- Evidence: [subagent planning instructions](https://github.com/CodelyTV/agent-harness/blob/57090a7301d15722b8885570e239bdd3e719a835/.agents/skills/codely-plan-create-subagents/SKILL.md), [phase instruction](https://github.com/CodelyTV/agent-harness/blob/57090a7301d15722b8885570e239bdd3e719a835/.agents/skills/codely-plan-phase-implement/SKILL.md).
- Basis: Structural negative.
- Confidence: High.
- Caveats: An external agent may implement collision control while following these guidelines.

### Absence scope

- Surfaces inspected: Subagent planning skill, phase implementation skills, host integration/marketplace manifests and command hooks.
- Plausible first-party paths checked: Shared work reservations, collision detection, inter-worker priority arbitration, phase handoff and feedback to an internal agent fleet.
- Why no material first-party path remains: The repository has no first-party live S1 fleet, and its sequencing/delegation text does not evidence a function-specific inter-S1 attenuation loop.

## S3 — Inside-and-now control

- State: —
- Function: Would regulate current commitments and resources across the entire first-party operating organization.
- Disturbance / variety regulated: Tool safety, phase scope, implementation review and current work progress.
- Decisive decision or feedback right: A user chooses the plan and approves the next phase; external host owns work execution; hooks enforce preset command filters.
- Decision owner: External user/host for choices, deterministic script for fixed command rejection; no first-party whole-system S3 owner.
- Supporting / enforcement mechanisms: `STOP`/approval instructions, checklist fields, simple `export` command guard, editor-specific tool hooks.
- Closure path: Host tool invocation → scripted allow/reject and operator review; no whole-current first-party S1 regulation/commitment decision and return loop.
- Boundary reachability: Not applicable for positive S3.
- Why this is / is not agent-owned: A guardrail or phase approval is not whole-system resource/accountability regulation, and the scripts do not decide policy or priorities.
- Evidence: [phase implementation](https://github.com/CodelyTV/agent-harness/blob/57090a7301d15722b8885570e239bdd3e719a835/.agents/skills/codely-plan-phase-implement/SKILL.md), [OpenCode guard](https://github.com/CodelyTV/agent-harness/blob/57090a7301d15722b8885570e239bdd3e719a835/.opencode/plugins/block-export.ts).
- Basis: Structural negative.
- Confidence: High.
- Caveats: Human supervision in a host project is at another recursion and does not automatically establish S3=P here.

### Absence scope

- Surfaces inspected: Phase review/approval instructions, security hooks, marketplace components and package scripts.
- Plausible first-party paths checked: Whole-current task ledger, shared resource control, intervention on ongoing first-party agents and parent-governed current-control return.
- Why no material first-party path remains: Only preset rule enforcement and externally performed task-review steps are shipped; no whole-current S1 organization or S3 decision owner exists.

## S3* — Complementary audit

- State: —
- Function: Would independently inspect operational reality and challenge ordinary first-party agent claims.
- Disturbance / variety regulated: Implementation mistakes, unwanted shell commands and possible incorrect coding-agent results.
- Decisive decision or feedback right: A host/user can review the code; the hook merely matches a command string.
- Decision owner: External human/host; no first-party complementary auditor.
- Supporting / enforcement mechanisms: Command block matcher, proposed review checklists and testing guidance.
- Closure path: Host/reader may inspect or block actions; no independent first-party audit finding is returned into Codely-owned operational control.
- Boundary reachability: Not applicable for positive audit.
- Why this is / is not agent-owned: A fixed pre-tool pattern check and instructions to review changes do not access actual outcomes through an independent audit path.
- Evidence: [Cursor hook](https://github.com/CodelyTV/agent-harness/blob/57090a7301d15722b8885570e239bdd3e719a835/.cursor/hooks/block-export.sh), [phase review guidance](https://github.com/CodelyTV/agent-harness/blob/57090a7301d15722b8885570e239bdd3e719a835/.agents/skills/codely-plan-phase-implement/SKILL.md).
- Basis: Structural negative.
- Confidence: High.
- Caveats: External CI or a reviewer may perform real audits at a different system boundary.

### Absence scope

- Surfaces inspected: Host pre-tool hooks, documentation/implementation skills and published plugin descriptors.
- Plausible first-party paths checked: Raw task artifact audit, independent evaluator, reviewer with complementary evidence and finding-to-control return.
- Why no material first-party path remains: Hook checks only proposed command text; review is user/host instruction, not first-party independent evidence adjudication.

## S4 — Outside-and-then intelligence

- State: —
- Function: Would identify external/future changes and return concrete adaptation options to first-party capability.
- Disturbance / variety regulated: Changing coding conventions, model/provider tools, feature needs and defects.
- Decisive decision or feedback right: A person or external coding agent elects to update docs/skills; no first-party ongoing prospective intelligence owner.
- Decision owner: External host/operator and project maintainers.
- Supporting / enforcement mechanisms: `codely-doc-create` prompts that convert conversational corrections into documents and OpenSpec creation guidance.
- Closure path: Operator/host invokes a doc skill → host generates text; no Codely runtime senses external futures, evaluates options and feeds an adaptation decision into its current operations.
- Boundary reachability: Not applicable for positive S4.
- Why this is / is not agent-owned: Reformatting past feedback into conventions can be useful knowledge retention, but a one-shot host-run instruction is not an external-and-prospective adaptation loop with Codely-owned closure.
- Evidence: [doc generation skill](https://github.com/CodelyTV/agent-harness/blob/57090a7301d15722b8885570e239bdd3e719a835/.agents/skills/codely-doc-create/SKILL.md), [OpenSpec skill](https://github.com/CodelyTV/agent-harness/blob/57090a7301d15722b8885570e239bdd3e719a835/.agents/skills/codely-openspec-spec-create-from-code/SKILL.md).
- Basis: Structural negative.
- Confidence: High.
- Caveats: An external host may voluntarily use the new docs to change later behavior; that is not a credited Codely-owned S4 path.

### Absence scope

- Surfaces inspected: Skill documentation and implementation scripts, README and marketplace.
- Plausible first-party paths checked: Runtime learning/replanning, external change sensing, future options/evaluation, parent-promoted skill updates and return to present capability.
- Why no material first-party path remains: Instructions expose no first-party standing agent evaluating prospective external changes or reliably closing adaptation into an owned runtime.

## S5 — Policy and identity

- State: —
- Function: Would adjudicate identity/ultimate-policy tensions and return legitimate governing decisions to the first-party operation.
- Disturbance / variety regulated: Security convention (`export` block), code style and practice preferences.
- Decisive decision or feedback right: Maintainers author guidance; operators choose installation and host policies. No runtime first-party identity controversy/escalation process is wired.
- Decision owner: Outside maintainers/operator, not a first-party governing decision owner at the package runtime boundary.
- Supporting / enforcement mechanisms: README product purpose, `AGENTS.md` conventions, host hook configuration and plugin descriptors.
- Closure path: A maintainer changes static package content in a future release or a user installs preferences; no first-party identity question → legitimate parent ruling → operating return loop at the assessed recursion.
- Boundary reachability: Not applicable for positive S5.
- Why this is / is not agent-owned: A security rule or opinionated style guide is a constraint, not demonstrated identity/ultimate-policy adjudication; one-shot user approvals are task level.
- Evidence: [README purpose](https://github.com/CodelyTV/agent-harness/blob/57090a7301d15722b8885570e239bdd3e719a835/README.md), [Claude pre-tool matcher](https://github.com/CodelyTV/agent-harness/blob/57090a7301d15722b8885570e239bdd3e719a835/.claude/settings.json), [phase human gate](https://github.com/CodelyTV/agent-harness/blob/57090a7301d15722b8885570e239bdd3e719a835/.agents/skills/codely-plan-phase-implement/SKILL.md).
- Basis: Structural negative.
- Confidence: High.
- Caveats: OSS maintainers can exercise legitimate governance over *development* of the package, a separate system-in-focus not borrowed here.

### Absence scope

- Surfaces inspected: Product identity and quickstart, repository rules, approval instructions, published policies and hooks.
- Plausible first-party paths checked: Runtime policy dispute, identity-level escalation to parent, legitimate ruling and returned modification of later first-party operation.
- Why no material first-party path remains: Static conventions and host task approvals are present, but no identity/ultimate-policy decision loop is shipped in the Codely package's operating boundary.

## Recursion

The installed host agent may itself be a viable operating system with a human parent and subsidiary workers. Those are not first-party viable subunits of this configuration package. Skill nesting, phases and symlinks are organizational aids, not proof of independent viable recursion.

## Variety and escalation

Install-time format differences are attenuated by package conventions and symlink tools; shell command variety is reduced by preset string matching. These deterministic measures support external agent use but do not enact the six first-party VSM functions. Task review/approval prompts leave decisions with the host/user, and no first-party algedonic channel or S3/S4/S5 escalation response was evidenced.

## Evidence gaps

No live host/model behavior or end-user private deployments were tested. Such integrations might assemble a larger viable system, but they cannot be attributed to the pinned first-party package without redefining the system boundary. The reviewed file inventory and supported entry points are sufficient for the stated bounded no-agentic-S1 conclusion.
