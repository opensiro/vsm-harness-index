---
harness_id: bridle
project_name: Bridle
repository: https://github.com/neiii/bridle
review_ref: b46d66828b7c5fdb45698283baecbd7d6dcc13d3
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

# Bridle

## Review boundary

- System in focus: The standalone open-source Bridle CLI/TUI and its two supporting Rust libraries for locating existing coding-harness configurations and discovering downloadable skills, agent descriptions, commands and MCP component manifests.
- Purpose and identity: Give an operator a unified way to see and switch saved settings for Claude Code, OpenCode, Goose, Amp, Copilot CLI and Crush, and install/configure reusable components for these **external** agent tools.
- Relevant environment: Differing target harness configuration paths and file formats, stale or missing installed tools, malformed downloaded package metadata, duplicate/overwritten installed files and user-requested changes between profiles.
- Standard-distribution boundary: `bridle` Rust binary (`clap`/terminal UI), `harness-locate` path/schema/validation library and `skills-locate` GitHub archive parser/discovery library. A configured external Claude/OpenCode/Goose agent and its model/tool loop are adjacent dependencies, not part of Bridle's own operating autonomy.
- Credited operating / distribution surfaces: [CLI and supported operations](https://github.com/neiii/bridle/blob/b46d66828b7c5fdb45698283baecbd7d6dcc13d3/README.md), [top-level command dispatch](https://github.com/neiii/bridle/blob/b46d66828b7c5fdb45698283baecbd7d6dcc13d3/crates/bridle/src/main.rs), [profile persistence/switch](https://github.com/neiii/bridle/blob/b46d66828b7c5fdb45698283baecbd7d6dcc13d3/crates/bridle/src/config/manager/lifecycle.rs), [interactive component installation](https://github.com/neiii/bridle/blob/b46d66828b7c5fdb45698283baecbd7d6dcc13d3/crates/bridle/src/cli/install.rs), [GitHub plugin discovery](https://github.com/neiii/bridle/blob/b46d66828b7c5fdb45698283baecbd7d6dcc13d3/crates/skills-locate/src/discovery.rs).
- Adjacent first-party surfaces excluded from ownership: CLI development CI, Rust integration fixtures, upstream maintainer decision making, external coding-agent processes and the agent role prompts/assets that Bridle merely downloads, parses, validates, installs or copies.
- First-party operating / deployment modes: Local operator-launched TUI, command-line status/config/profile CRUD/switch/diff, interactive GitHub component selection and installation, uninstall, library APIs for harness path discovery and agent frontmatter validation. No integrated LLM provider dispatch, independent model-agent execution or outcome-feedback loop is shipped.
- Recursion level: Bridle's own installation/configuration management activity, not the separate organization of one or several external AI coding assistants subsequently using Bridle-installed components.
- Reviewed revision: `neiii/bridle@b46d66828b7c5fdb45698283baecbd7d6dcc13d3`.
- Observation date: 2026-10-26; frozen source inspection, no live external model/provider execution.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

The `main.rs` entrypoint is a synchronous CLI dispatcher. It routes `status`, `init`, `profile`, `config`, `install`, and `uninstall` into dedicated Rust functions, or opens a TUI. The profile manager copies, backs up, edits and switches each installed coding harness's configuration files. `harness-locate` detects installed harnesses and validates which paths, skills, agent frontmatter and MCP schemas they support. `skills-locate` downloads GitHub archives, reads plugin manifests and extracts package descriptors; Bridle then presents a human component/target selection and writes the translated static artifacts. [CLI dispatcher](https://github.com/neiii/bridle/blob/b46d66828b7c5fdb45698283baecbd7d6dcc13d3/crates/bridle/src/main.rs), [profile lifecycle](https://github.com/neiii/bridle/blob/b46d66828b7c5fdb45698283baecbd7d6dcc13d3/crates/bridle/src/config/manager/lifecycle.rs), [component parser](https://github.com/neiii/bridle/blob/b46d66828b7c5fdb45698283baecbd7d6dcc13d3/crates/skills-locate/src/discovery.rs), [installer](https://github.com/neiii/bridle/blob/b46d66828b7c5fdb45698283baecbd7d6dcc13d3/crates/bridle/src/install/installer.rs).

The sources call installed Claude/OpenCode/etc. **harnesses** and install files named **agents**, but those nouns refer to target applications and their static agent-descriptor files, not Bridle-hosted cognitive workers. Agent validation parses YAML frontmatter (`tools`, `color`, `mode`) and reports schema compatibility. The Bridle installation workflow requires a real interactive terminal and calls an operator selection function; it does not prompt a model to decide which components meet the user's task goal. External users may subsequently execute an AI coding agent configured by Bridle; that agent owns its task reasoning/actions outside the reviewed repository. [README workflow](https://github.com/neiii/bridle/blob/b46d66828b7c5fdb45698283baecbd7d6dcc13d3/README.md#package-manager-for-your-harness), [agent descriptor parser](https://github.com/neiii/bridle/blob/b46d66828b7c5fdb45698283baecbd7d6dcc13d3/crates/skills-locate/src/component/agent.rs), [interactive install entry](https://github.com/neiii/bridle/blob/b46d66828b7c5fdb45698283baecbd7d6dcc13d3/crates/bridle/src/cli/install.rs).

## Operational model

The human operator selects a profile or plugin source and targets; Bridle applies path mappings, validation, copying and installation as deterministic file operations. Repository discovery reads archives/structured metadata rather than autonomously pursuing a free-form engineering objective; the target coding assistants, if later invoked, independently decide their own prompts, tool uses and code edits. Removing the external agents still leaves a functional Bridle configuration utility, but no autonomous task execution remains. Therefore this is a completed source-backed `excluded-no-agentic-vsm` candidate: the presence of *configuration for agents* cannot be borrowed as first-party S1 autonomy.

## S1 — Operations

- State: —
- Function: No first-party autonomous model-backed operational unit performs a user goal and self-directs meaningful tool/response decisions inside Bridle.
- Disturbance / variety regulated: External coding agents may absorb software-task uncertainty, while Bridle itself handles configuration file formats, profile paths and installation compatibility with programmed transformations.
- Decisive decision or feedback right: Operator chooses which target harness, profile and components; code maps, checks and writes files using pre-authored logic. The target coding agent later owns any model reasoning/feedback loop.
- Decision owner: Human command/TUI operator and fixed Rust code for installation; separately installed coding harness owns its own S1 work.
- Supporting / enforcement mechanisms: Command parser, path detection, GitHub source/archive scanning, agent descriptor validation, targeted manifest translation and filesystem profile manager.
- Closure path: Human chooses package/profile → Bridle parses/validates selected files and writes target configuration → reports installed components/status. No first-party model chooses a task action based on the resulting environment and iterates to solve it.
- Boundary reachability: All published commands and parser/install source paths were reviewed at frozen source; they operate independently of configured model providers and do not invoke a first-party agent loop.
- Why this is / is not agent-owned: Agent-descriptor *files* and target harness instances are objects of configuration, not agent-operated work units within Bridle. The Rust utility itself has no autonomous model/task-feedback decision owner.
- Evidence: [explicit config-manager purpose](https://github.com/neiii/bridle/blob/b46d66828b7c5fdb45698283baecbd7d6dcc13d3/README.md), [entire top-level dispatcher](https://github.com/neiii/bridle/blob/b46d66828b7c5fdb45698283baecbd7d6dcc13d3/crates/bridle/src/main.rs), [interactive selection](https://github.com/neiii/bridle/blob/b46d66828b7c5fdb45698283baecbd7d6dcc13d3/crates/bridle/src/cli/install.rs), [agent descriptor parser](https://github.com/neiii/bridle/blob/b46d66828b7c5fdb45698283baecbd7d6dcc13d3/crates/skills-locate/src/component/agent.rs).
- Basis: Explicit product contract plus negative full CLI/runtime boundary inspection.
- Confidence: High.
- Caveats: This is an inclusion-boundary judgment, not a criticism of Bridle's utility or security. Installed external harnesses can have genuine S1=A under separate repository-relative assessment.

### Absence scope

- Surfaces inspected: Bridle entrypoint and subcommands, TUI, profile lifecycle, harness locator and detection, plugin archive discovery, frontmatter parser, install/uninstall and Rust dependency manifests.
- Plausible first-party paths checked: Agent descriptor files, CLI subprocess use, GitHub component installation, MCP configuration import, cross-harness profile switching, any model completion/provider inference or agent tool loop.
- Why no material first-party path remains: Subprocesses open editors/diffs or inspect installed tools; plugin discovery/installation manipulate passive metadata. No first-party iterative model/tool-operational loop exists in the standard Bridle program.

## S2 — Coordination

- State: —
- Function: Would regulate an observed conflict or oscillation between distinct first-party operational agent units and return a coordinated adjustment to them.
- Disturbance / variety regulated: Conflicting profile settings or incompatible agent-descriptor formats are potential configuration errors, not competing Bridle-operated autonomous S1 commitments.
- Decisive decision or feedback right: Human selects a profile/target; compatibility validators reject invalid configuration and installer flags overwrite conditions.
- Decision owner: Operator and deterministic validators; no inter-agent coordinator is present.
- Supporting / enforcement mechanisms: Harness capability matrices, install target filters, component validation and manifest-file overwrite policy.
- Closure path: Profile/package selection → file validation and writing → external agent config changes; no inter-S1 collision verdict returning altered behaviour to distinct Bridle-owned S1s.
- Boundary reachability: All relevant mechanisms are shipped, but none is connected to a first-party inter-S1 task loop.
- Why this is / is not agent-owned: Compatibility between static configurations is not a conflict between operational S1 units, and path conversion does not negotiate among agent workers.
- Evidence: [compatibility checks](https://github.com/neiii/bridle/blob/b46d66828b7c5fdb45698283baecbd7d6dcc13d3/crates/bridle/src/cli/install.rs), [agent schema rules](https://github.com/neiii/bridle/blob/b46d66828b7c5fdb45698283baecbd7d6dcc13d3/crates/harness-locate/src/validation.rs).
- Basis: No S1-owned coordination boundary; no concrete mutual interference/return cycle.
- Confidence: High.
- Caveats: Sharing a utility among many independently executing external coding agents does not transfer their S2 into Bridle.

### Absence scope

- Surfaces inspected: Target selection, profile switching, installer overwrite protection, agent compatibility validation, harness discovery and configuration status.
- Plausible first-party paths checked: Cross-agent simultaneous file access, competing model work, conflict-specific arbitration and returned changed agent commitments.
- Why no material first-party path remains: The inspected code transforms settings on operator command and lacks first-party S1 workers for such conflict to be regulated.

## S3 — Inside-and-now control

- State: —
- Function: Would own a whole-current view and discretionary intervention over Bridle's own autonomous operational units.
- Disturbance / variety regulated: Installed harness availability, active profile changes, MCP and skill compatibility; no ongoing Bridle-owned tasks are jointly managed.
- Decisive decision or feedback right: Operator picks profile switching and component installation; status merely reports config files.
- Decision owner: Operator for configuration decisions, not a Bridle-owned metasystem over S1 execution.
- Supporting / enforcement mechanisms: TUI profile cards, `status`, `profile diff`, config read/write and update/backup.
- Closure path: Human sees configuration → chooses profile → Bridle updates files. This closes configuration administration, not S3 intervention in ongoing first-party operational work.
- Boundary reachability: Available commands are in the standard binary, but no whole-current S1 activity/control loop exists behind them.
- Why this is / is not agent-owned: A dashboard of *installed* agents and profile settings is not an autonomous S3 over live agent commitments, even if it influences external harness starts.
- Evidence: [status/profile command contract](https://github.com/neiii/bridle/blob/b46d66828b7c5fdb45698283baecbd7d6dcc13d3/README.md#commands), [profile switch filesystem operations](https://github.com/neiii/bridle/blob/b46d66828b7c5fdb45698283baecbd7d6dcc13d3/crates/bridle/src/config/manager/lifecycle.rs).
- Basis: First-party operation limited to configuration control of external systems.
- Confidence: High.
- Caveats: Parent human ownership of app preferences is not a substantive S3=P current-control mode over a Bridle-owned viable organization.

### Absence scope

- Surfaces inspected: TUI/dashboard, profile manager, CLI status and diff, installed-harness detection, saved active-profile configuration.
- Plausible first-party paths checked: Whole-live-agent monitoring, budget/priority arbitration, current task reallocations, feedback-based intervention and changed operating commitments.
- Why no material first-party path remains: Status is about files and selected configs, and switch writes target config without controlling an internally operated multi-S1 enterprise.

## S3* — Complementary audit

- State: —
- Function: Would independently inspect real operating outputs/claims and feed an audit judgment back into control.
- Disturbance / variety regulated: Bad agent descriptor frontmatter, schema mismatch, failed component download or incorrect installed configuration.
- Decisive decision or feedback right: Deterministic validators parse metadata and return errors; no independent model/raw task-output audit makes a discretionary correction decision.
- Decision owner: Validation rules programmed by maintainers; operator handles failures.
- Supporting / enforcement mechanisms: Rust validators, manifest records, installation report and CLI diff/status display.
- Closure path: Installer validates descriptor/config → produces error or records completed file write → operator may change selection; no independent audit of external coding agent claims or task artifacts occurs.
- Boundary reachability: Validation/report paths are shipped, but are routine configuration checking, not a complementary operational evidence channel.
- Why this is / is not agent-owned: Parsing agent YAML, CLI diff and testing installation mechanics do not produce an independent S3* audit of autonomous operations.
- Evidence: [Rust validation](https://github.com/neiii/bridle/blob/b46d66828b7c5fdb45698283baecbd7d6dcc13d3/crates/harness-locate/src/validation.rs), [installation reports](https://github.com/neiii/bridle/blob/b46d66828b7c5fdb45698283baecbd7d6dcc13d3/crates/bridle/src/install/installer.rs).
- Basis: Bounded negative; ordinary config validation cannot be promoted to independent complementary audit.
- Confidence: High.
- Caveats: External coding agents may run their own review/tests; they are not first-party Bridle inspection.

### Absence scope

- Surfaces inspected: Agent descriptor parser, schema validation, install report, manifest, profile diff and Rust test inventory.
- Plausible first-party paths checked: Independent verification of actual model task outputs, runtime trace/raw artifact replay, separate auditor with feedback into an S3 decision.
- Why no material first-party path remains: All checks concern config/package correctness rather than separately observed autonomous work and closed corrective control.

## S4 — Outside-and-then intelligence

- State: —
- Function: Would monitor prospective changes in external harness ecosystems, compare strategic options and return capability upgrades to current Bridle operation.
- Disturbance / variety regulated: Changing config schemas, upstream GitHub repositories and AI-agent feature support, but these are encountered only as present selection/install requests.
- Decisive decision or feedback right: User chooses remote source/package and targets; code scans known schemas and copies compatible assets.
- Decision owner: Human operator and hard-coded compatibility capability definitions, not a proactive external/future intelligence agent.
- Supporting / enforcement mechanisms: Downloaded archives, GitHub ref resolution, harness detection maps, static capability tables and installer.
- Closure path: User names source → utility discovers files → user installs translated components. No future scanning/adaptation option is generated and committed through an S3 capability decision.
- Boundary reachability: GitHub download/scan is live but demand-driven and deterministic.
- Why this is / is not agent-owned: Contact with outside repositories is not future strategy or independent capability scouting.
- Evidence: [GitHub discovery](https://github.com/neiii/bridle/blob/b46d66828b7c5fdb45698283baecbd7d6dcc13d3/crates/skills-locate/src/discovery.rs), [supported targets](https://github.com/neiii/bridle/blob/b46d66828b7c5fdb45698283baecbd7d6dcc13d3/README.md#supported-harnesses).
- Basis: Bounded negative for externally prospective strategic adaptation.
- Confidence: High.
- Caveats: User may manually upgrade Bridle or choose novel skills; this is not first-party model-owned S4.

### Absence scope

- Surfaces inspected: GitHub plugin discovery, repository fetch, harness capability listing, config-manager switch, CLI operations.
- Plausible first-party paths checked: Standing trend watcher, model evaluation of upcoming harness API changes, candidate adaptation options and feedback into revised Bridle capabilities.
- Why no material first-party path remains: Every shown remote path is an operator-requested parse/install of current artifacts.

## S5 — Policy and identity

- State: —
- Function: Would adjudicate a legitimacy dispute over Bridle's ultimate identity/policy and return binding governance to its operation.
- Disturbance / variety regulated: Competing ultimate purposes of the utility, rather than ordinary preferences about editor, default harness or active profile.
- Decisive decision or feedback right: Operator writes config preferences; maintainers publish static product purpose and compatibility behavior.
- Decision owner: Outside maintainer/operator, not a first-party runtime constitutional authority.
- Supporting / enforcement mechanisms: README-defined product identity, config TOML preferences, CLI set/get and static validation rules.
- Closure path: Operator changes preferred target/editor/profile and the command later uses it; no authority dispute → identity ruling → binding revised organization policy loop.
- Boundary reachability: Preferences are live, but no live whole-organization identity governance mechanism is exposed.
- Why this is / is not agent-owned: A configured default harness or a project's README is not S5 policy adjudication.
- Evidence: [purpose and core concepts](https://github.com/neiii/bridle/blob/b46d66828b7c5fdb45698283baecbd7d6dcc13d3/README.md#core-concepts), [CLI config setters](https://github.com/neiii/bridle/blob/b46d66828b7c5fdb45698283baecbd7d6dcc13d3/crates/bridle/src/cli/config_cmd.rs).
- Basis: Bounded negative for operationally closed legitimate identity governance.
- Confidence: High.
- Caveats: Public OSS maintainer decisions exist at another organizational recursion and cannot be borrowed by the installed CLI.

### Absence scope

- Surfaces inspected: Documented project purpose, supported-target list, operator config, profile selection and no model runtime.
- Plausible first-party paths checked: Constitutional identity dispute, parent ruling, S3–S4 balance choice and governing return to later operation.
- Why no material first-party path remains: Code supports preference editing but not ultimate-purpose judgment.

## Distributed OSS parent arrangement

Bridle's maintainer(s), contributors, license and release/distribution workflows belong to the upstream development organization. They do not govern one installed copy's first-party autonomous operational units, which are not established.

## Self-hosted and non-human modes

Bridle can run locally and without any configured LLM service, since its own role is to modify agent *configuration* rather than run the agent. CLI invocations can be scripted, but deterministically copying or validating profile files does not become autonomous S1 merely because a separate agent or shell orchestrates the executable.

## Recursion

At the Bridle boundary are CLI configuration commands, profile managers and descriptor/installation parsers. External configured Claude Code/OpenCode/Goose/Copilot/Amp/Crush tools are separate systems; assessments of their S1–S5 cannot be inherited. Bridle is adjacent infrastructure, not an internal recursion with an evidenced agentic loop.

## Variety and escalation

The Rust tool absorbs format/path compatibility variety by fixed mapping and errors. A malformed descriptor is flagged to the operator; config/profile activation copies files. The operator and eventual external agent must handle uncertain task outcomes. The absence of a native operational model feedback cycle closes the exclusion decision without guessing what a downstream coding agent might do.

## Evidence gaps

- The assessment is a frozen source and documented command-boundary analysis. No remote GitHub install, external coding agent, LLM provider or actual target system was run.
- The local assessment environment has no `cargo` binary or prebuilt dependency target; upstream Rust tests were not run here. Index validation and released Methodology contract, not live agent-quality testing, gate publication.
- The conclusion concerns **Bridle's own** operational ownership; it makes no negative assertion about the capabilities of separately installed coding assistants or their agent descriptors.
