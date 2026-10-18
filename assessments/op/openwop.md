---
harness_id: openwop
project_name: OpenWOP
repository: https://github.com/openwop/openwop
review_ref: 26e6deb5a3554c77f90ba338a8eb2f5244e136ce
reviewed_at: 2026-10-15
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-15
status: excluded-no-agentic-vsm
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# OpenWOP

## Review boundary

- System in focus: the public `openwop/openwop` repository **at exactly** `26e6deb5a3554c77f90ba338a8eb2f5244e136ce`, treated as its supported protocol-contract and conformance product, not as an unbounded umbrella of other `openwop/*` repositories.
- Purpose and identity: publish a versioned OpenWOP workflow/interoperability protocol, schemas, security invariants, RFCs, and a black-box suite for verifying independently implemented host engines.
- Relevant environment: conformance-suite users, implementers, deployed third-party or sibling-repository OpenWOP hosts, protocol clients, test fixtures, and CI/release systems.
- Standard-distribution boundary: root `package.json` (`private: true`, `openwop-spec-corpus`), the published `@openwop/openwop-conformance` CLI and `@openwop/spec-artifacts`; no packaged first-party OpenWOP **execution host** or model/tool agent loop in this repository.
- Credited operating / distribution surfaces: the conformance CLI invoking tests of a **supplied external base URL**; schema/API protocol artifacts; shipped conformance validators and their direct HTTP client; specification generation/validation commands. These are a deterministic standards-testing and publication product, not an autonomous AI harness.
- Adjacent first-party surfaces excluded from ownership: `conformance/src/scenarios/` and fixtures as benchmarks/tests; `conformance/src/lib/scratch-host.ts` as expressly nonexecuting test double; `.claude/` development workflows, CI and publisher scripts, RFCs/roadmap/governance; operational reference hosts, SDKs, registry and CLI in **separate** `openwop/openwop-examples`, `openwop/openwop-sdks`, `openwop/openwop-registry` and `openwop/openwop-cli` repositories.
- First-party operating / deployment modes considered: published spec-artifacts package; conformance CLI in offline mode; black-box `--base-url` testing of a separately operated host; self-test scratch server as a negative boundary check. Described workflow/agent host modes are **not shipped from this review repository**.
- Recursion level: one standards/conformance publishing product at the frozen repository boundary, not a shared operational organization comprising sibling implementations.
- Reviewed revision: `26e6deb5a3554c77f90ba338a8eb2f5244e136ce` (frozen `main` pin from Index candidate #470; no repin to newer code).
- Observation date: 2026-10-15.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The root package identifies a **private spec corpus**; the two published packages distribute a machine-readable contract and a black-box conformance CLI. The CLI explicitly requires a separately deployed server (`--base-url`) for live scenarios or runs a host-free subset (`--offline`). Its `driver.ts` sends HTTP requests to the supplied host; `agentLoop.ts`, `agentRuntime.ts` and `liveRuntime.ts` **query that host's capabilities and invoke its sample seams**. They are not a local agent interpreter, workflow scheduler or model/tool action selector. Some host seams may legitimately soft-skip when unsupported. The local `ScratchHost` describes itself as a test double that **executes nothing**.

The upstream README explicitly locates all v1 and v2 reference hosts and runnable workflow samples in the **separate** `openwop/openwop-examples` repository; even the ten-minute tutorial requires a second clone. The specification defines highly capable host behaviours, but its normative statements are implementation requirements on other systems rather than executable first-party closure by this repository.

Primary pinned sources: [README.md](https://github.com/openwop/openwop/blob/26e6deb5a3554c77f90ba338a8eb2f5244e136ce/README.md), [QUICKSTART-10MIN.md](https://github.com/openwop/openwop/blob/26e6deb5a3554c77f90ba338a8eb2f5244e136ce/QUICKSTART-10MIN.md), [root package.json](https://github.com/openwop/openwop/blob/26e6deb5a3554c77f90ba338a8eb2f5244e136ce/package.json), [conformance/package.json](https://github.com/openwop/openwop/blob/26e6deb5a3554c77f90ba338a8eb2f5244e136ce/conformance/package.json), [spec-artifacts/package.json](https://github.com/openwop/openwop/blob/26e6deb5a3554c77f90ba338a8eb2f5244e136ce/spec-artifacts/package.json), [conformance CLI](https://github.com/openwop/openwop/blob/26e6deb5a3554c77f90ba338a8eb2f5244e136ce/conformance/src/cli.ts), [HTTP conformance driver](https://github.com/openwop/openwop/blob/26e6deb5a3554c77f90ba338a8eb2f5244e136ce/conformance/src/lib/driver.ts), [agent-loop scenario helper](https://github.com/openwop/openwop/blob/26e6deb5a3554c77f90ba338a8eb2f5244e136ce/conformance/src/lib/agentLoop.ts), [agent-runtime scenario helper](https://github.com/openwop/openwop/blob/26e6deb5a3554c77f90ba338a8eb2f5244e136ce/conformance/src/lib/agentRuntime.ts), [live-agent scenario helper](https://github.com/openwop/openwop/blob/26e6deb5a3554c77f90ba338a8eb2f5244e136ce/conformance/src/lib/liveRuntime.ts), [scratch test host](https://github.com/openwop/openwop/blob/26e6deb5a3554c77f90ba338a8eb2f5244e136ce/conformance/src/lib/scratch-host.ts).

## Operational model

The first-party conformance tool accepts a target host and advertised capability set, makes API calls, checks protocol invariants and reports test/certification outcomes. The host decides workflow admission/execution, agent dispatch, interruption, and subsequent operational consequences. The protocol authors define expected behaviours, and fixture test scripts simulate or assert them, but this corpus does not itself ship the operational agentic system described by the standard.

**Counterfactual owner test:** remove `openwop-examples` and any supplied external host while retaining every file and published package in `openwop/openwop`. The corpus can still publish schemas, run offline assertions and report missing host connectivity, but cannot autonomously interpret and execute an open-ended agent task through a first-party model/tool/observation loop. The crucial S1 owner is external to the reviewed product.

## S1 — Operations

- State: —
- Function: protocol-conformance test execution is first-party, but no first-party autonomous agentic workflow operation is shipped at the declared boundary.
- Disturbance / variety regulated: conformance test input and response variation; actual workflow tasks, agent actions, interrupts and state transitions belong to a separate host.
- Decisive decision or feedback right: interpret a user's operational goal, select model/tool/agent actions, integrate observations and choose the next task transition.
- Decision owner: independently implemented OpenWOP hosts and their configured agents, not this conformance/spec corpus.
- Supporting / enforcement mechanisms: JSON Schemas, OpenAPI/AsyncAPI, requirement registries, conformance test driver, CLI and static fixtures.
- Closure path: test scenario → HTTP driver → external host execution → host response → first-party test assertion. There is no returned first-party agent-controlled operational action loop.
- Why this is / is not agent-owned: the `agent*` scenario helper names refer to **remote API probes**, not bundled runtime agent decision rights.
- Evidence: [root package.json](https://github.com/openwop/openwop/blob/26e6deb5a3554c77f90ba338a8eb2f5244e136ce/package.json); [conformance/package.json](https://github.com/openwop/openwop/blob/26e6deb5a3554c77f90ba338a8eb2f5244e136ce/conformance/package.json); [conformance CLI](https://github.com/openwop/openwop/blob/26e6deb5a3554c77f90ba338a8eb2f5244e136ce/conformance/src/cli.ts); [HTTP conformance driver](https://github.com/openwop/openwop/blob/26e6deb5a3554c77f90ba338a8eb2f5244e136ce/conformance/src/lib/driver.ts); [agent-loop scenario helper](https://github.com/openwop/openwop/blob/26e6deb5a3554c77f90ba338a8eb2f5244e136ce/conformance/src/lib/agentLoop.ts); [README.md](https://github.com/openwop/openwop/blob/26e6deb5a3554c77f90ba338a8eb2f5244e136ce/README.md).
- Basis: explicit distribution boundary + source-verified counterfactual.
- Confidence: high.
- Caveats: a different assessment of `openwop/openwop-examples` could have a positive S1; that evidence cannot be transferred to this pinned repository.

### Absence scope

- Surfaces inspected: root and package manifests, shipped CLI, conformance HTTP driver, agent-loop/runtime scenario helpers, self-test scratch host, README/quickstart and published API/spec contract.
- Plausible first-party paths checked: protocol-required run lifecycle; conformance CLI; `agentLoop` and `agentRuntime` helpers; `liveRuntime` helper; self-test `ScratchHost`; published spec-artifacts and distribution script.
- Why no material first-party path remains: the only executable local server is a **nonexecuting test double**; other runtime/agent routes call externally deployed hosts. The repository ships specifications and test machinery, not an owned agentic S1.

## S2 — Coordination

- State: —
- Function: no first-party organization of distinct operating S1 units with disturbance attenuation and returned coordination is shipped.
- Disturbance / variety regulated: normative workflow/worker/dispatch interactions and conformance fan-out are described or tested; actual inter-S1 conflicts occur inside external hosts.
- Decisive decision or feedback right: choose a response to specific interference among distinct active S1 units.
- Decision owner: any implementing external host or user-specified workflow policy.
- Supporting / enforcement mechanisms: workflow/dispatch schemas, scenario fixtures, test parallelism settings.
- Closure path: requirements/test assertions can mark host behaviour conformant; they do not feed a first-party adaptive coordination decision into local S1 operations.
- Why this is / is not agent-owned: topological descriptions and test scenario scheduling are not operational S2 closure by the assessed standard corpus.
- Evidence: [README.md](https://github.com/openwop/openwop/blob/26e6deb5a3554c77f90ba338a8eb2f5244e136ce/README.md); [conformance/package.json](https://github.com/openwop/openwop/blob/26e6deb5a3554c77f90ba338a8eb2f5244e136ce/conformance/package.json); [HTTP conformance driver](https://github.com/openwop/openwop/blob/26e6deb5a3554c77f90ba338a8eb2f5244e136ce/conformance/src/lib/driver.ts); [protocol RFC corpus](https://github.com/openwop/openwop/blob/26e6deb5a3554c77f90ba338a8eb2f5244e136ce/RFCS/0006-orchestrator.md).
- Basis: explicit + structural bounded absence.
- Confidence: high.
- Caveats: an actual separate host may supply S2, but its concrete interference/feedback evidence is outside this assessed standard distribution.

### Absence scope

- Surfaces inspected: normative workflow and multi-agent declarations, conformance dispatch scenarios, CLI run targets and scenario helper driver.
- Plausible first-party paths checked: parallel suite workers, synthetic dispatch fixtures, remote agent/worker dispatch API.
- Why no material first-party path remains: no local operational S1 population exists for an inter-S1 attenuation response; the conformance runner checks external implementations.

## S3 — Inside-and-now control

- State: —
- Function: no first-party whole-current workflow organization with shared operational commitment control.
- Disturbance / variety regulated: host-level resources, run statuses, backpressure, cancellation and prioritization are requirements/probes, not operations regulated here.
- Decisive decision or feedback right: allocate or constrain **current host operations** based on whole-system current visibility.
- Decision owner: implementing hosts/operators outside this repository.
- Supporting / enforcement mechanisms: host API contracts, status schemas, host capability advertisements, conformance certification results.
- Closure path: suite observes and judges API results; there is no first-party current-control decision returned to an operating host under this corpus's authority.
- Why this is / is not agent-owned: conformance checking does not confer runtime control authority over the host's current commitments.
- Evidence: [README.md](https://github.com/openwop/openwop/blob/26e6deb5a3554c77f90ba338a8eb2f5244e136ce/README.md); [conformance CLI](https://github.com/openwop/openwop/blob/26e6deb5a3554c77f90ba338a8eb2f5244e136ce/conformance/src/cli.ts); [HTTP conformance driver](https://github.com/openwop/openwop/blob/26e6deb5a3554c77f90ba338a8eb2f5244e136ce/conformance/src/lib/driver.ts); [OpenAPI contract](https://github.com/openwop/openwop/blob/26e6deb5a3554c77f90ba338a8eb2f5244e136ce/api/openapi.yaml).
- Basis: explicit + structural bounded absence.
- Confidence: high.
- Caveats: the protocol's current-control vocabulary must not be credited as local S3.

### Absence scope

- Surfaces inspected: published host operations contract, CLI and driver, example-host location, execution model helper paths.
- Plausible first-party paths checked: run cancel/status protocol routes, host-side management requirements, suite-wide scheduler and verification result.
- Why no material first-party path remains: requests/test results can inspect external current work, but the reviewed standard product does not own a current-operation control path into its own S1s.

## S3* — Complementary audit

- State: —
- Function: conformance verification does **not** form complementary independent corrective audit of this product's own operations.
- Disturbance / variety regulated: specification compliance and protocol validity across independently supplied hosts.
- Decisive decision or feedback right: independently inspect organizational operation from a distinct evidence path, form an audit judgment and return corrective regulation into the assessed organization's S1/S3.
- Decision owner: a conformance test/criteria publisher or an external host maintainer reviewing results; no closed first-party complementary operational authority established.
- Supporting / enforcement mechanisms: scenario assertions, static verification, certification output, run-result witnesses and scratch-test doubles.
- Closure path: externally operated host → black-box conformance result → human/external maintainer; no returned first-party governance correction to the corpus's own operational S1.
- Why this is / is not agent-owned: independent black-box tests **of other hosts** are not necessarily S3* of the assessed system-in-focus, and the automated checks do not own an organizational corrective-return decision.
- Evidence: [conformance CLI](https://github.com/openwop/openwop/blob/26e6deb5a3554c77f90ba338a8eb2f5244e136ce/conformance/src/cli.ts); [HTTP conformance driver](https://github.com/openwop/openwop/blob/26e6deb5a3554c77f90ba338a8eb2f5244e136ce/conformance/src/lib/driver.ts); [scratch test host](https://github.com/openwop/openwop/blob/26e6deb5a3554c77f90ba338a8eb2f5244e136ce/conformance/src/lib/scratch-host.ts); [conformance/package.json](https://github.com/openwop/openwop/blob/26e6deb5a3554c77f90ba338a8eb2f5244e136ce/conformance/package.json).
- Basis: explicit + structural bounded absence.
- Confidence: high.
- Caveats: do not equate independent testing, certification and audit-event naming with Profile S3* ownership.

### Absence scope

- Surfaces inspected: conformance runner, certification/fixture test surfaces, self-test scratch host, protocol invariants and publications.
- Plausible first-party paths checked: test result reporting as complementary audit, cross-host conformance probes, certification bundle generation.
- Why no material first-party path remains: no owned operational S1/S3 exists here for findings to correct through an independent organizational loop; results are exported to external implementers.

## S4 — Outside-and-then intelligence

- State: —
- Function: protocol roadmap and feature/release evolution do not supply an operational agent-owned future capability adaptation loop in the packaged assessed system.
- Disturbance / variety regulated: future protocol requirements, ecosystem interoperability changes and RFC proposal decisions.
- Decisive decision or feedback right: select a prospective adaptation based on outside observations and return it into current deployed operating capability.
- Decision owner: human specification maintainers/contributors, not a first-party agentic runtime.
- Supporting / enforcement mechanisms: RFC process, roadmap, API/schema releases, CI and manual governance.
- Closure path: maintainer decision → updated specification/releases → external implementer adoption; no first-party agent-controlled prospective adaptation into a local operational S1.
- Why this is / is not agent-owned: a sophisticated RFC ecosystem and persistent specifications are not autonomous organizational adaptation.
- Evidence: [README.md](https://github.com/openwop/openwop/blob/26e6deb5a3554c77f90ba338a8eb2f5244e136ce/README.md); [root package.json](https://github.com/openwop/openwop/blob/26e6deb5a3554c77f90ba338a8eb2f5244e136ce/package.json); [spec-artifacts/package.json](https://github.com/openwop/openwop/blob/26e6deb5a3554c77f90ba338a8eb2f5244e136ce/spec-artifacts/package.json); [protocol RFC corpus](https://github.com/openwop/openwop/blob/26e6deb5a3554c77f90ba338a8eb2f5244e136ce/RFCS/0006-orchestrator.md).
- Basis: explicit + structural bounded absence.
- Confidence: high.
- Caveats: externally developed new host implementations are separate systems and cannot donate S4 closure.

### Absence scope

- Surfaces inspected: RFC corpus, root build/release scripts, published packages, documentation and host-location map.
- Plausible first-party paths checked: evolving protocols, version negotiation, runtime feature advertisement, contributor/CI release automation.
- Why no material first-party path remains: changes are chosen by maintainers and implemented in separate hosts, not by an autonomous first-party S4 controller with return to current operations.

## S5 — Policy and identity

- State: —
- Function: protocol-level identity, authentication and governance rules do not establish first-party autonomous or closed parent-governed **operational** ultimate-policy ownership.
- Disturbance / variety regulated: protocol compatibility, auth rules, security and permission invariants for external hosts.
- Decisive decision or feedback right: resolve an organization's identity or ultimate-policy tension and return that decision to ongoing first-party operations.
- Decision owner: protocol human stewards for specification governance, and separately the deployed host's own operators for runtime identity/policy.
- Supporting / enforcement mechanisms: security invariants, normative authorization schemas, project governance docs and conformance checks.
- Closure path: standards body/stewardship → normative requirements → external host implementation; no bundled first-party organizational S5 return into agentic S1 operation.
- Why this is / is not agent-owned: static rules and stewardship are not a first-party agentic S5; human authorship of a standard is not enough for `P` without a closed parent-governed operating mode.
- Evidence: [README.md](https://github.com/openwop/openwop/blob/26e6deb5a3554c77f90ba338a8eb2f5244e136ce/README.md); [spec-artifacts/package.json](https://github.com/openwop/openwop/blob/26e6deb5a3554c77f90ba338a8eb2f5244e136ce/spec-artifacts/package.json); [conformance CLI](https://github.com/openwop/openwop/blob/26e6deb5a3554c77f90ba338a8eb2f5244e136ce/conformance/src/cli.ts); [OpenAPI contract](https://github.com/openwop/openwop/blob/26e6deb5a3554c77f90ba338a8eb2f5244e136ce/api/openapi.yaml).
- Basis: explicit + structural bounded absence.
- Confidence: high.
- Caveats: no S5 parent mode is borrowed from maintainers merely because policy decisions exist in source governance.

### Absence scope

- Surfaces inspected: security/protocol declaration, governance/RFC process, test assertions, CLI and external-host references.
- Plausible first-party paths checked: host auth/identity requirements, role restrictions, configuration policy, standard maintainers' release decisions.
- Why no material first-party path remains: static normative definitions and external runtime operators do not close an identity/ultimate-policy decision-return loop for a packaged first-party agentic organization.

## Recursion

At the specified system boundary the corpus is a standards publishing/conformance product. Protocol descriptions of nested workflows, orchestrators and workers are statements about possible **other** organizations; they are not first-party recursion observed in this product.

## Variety and escalation

The corpus regulates standardization variety using schemas, specifications, compatibility rules, test assertions and certification reports; implementers respond to test failures and decide their own operational remedies. First-party contributor/release decisions regulate changes to the **standard**, outside the agentic harness's operational-function publication scope.

## Evidence gaps

- None material to the **no packaged runtime** finding at the pinned repository boundary: the upstream explicitly locates executable reference hosts in another repository, and the shipped CLI/test helpers demonstrably call remote host seams.
- This does **not** assess any frozen revision of `openwop/openwop-examples`, whether its host does or does not independently exhibit S1–S5. A later **separate** intake would require its own identity, exact source ref and boundary.
- Source-level inspection and distribution-package declarations were used; no host execution or external provider was run, because they are outside the assessed boundary.

## Assessment summary

**Proposed terminal disposition: `excluded-no-agentic-vsm`.** At the frozen `openwop/openwop` revision, the first-party published product is a protocol/specification corpus plus a black-box conformance tester. Runnable agent/workflow hosts are stored in sibling repositories, not packaged as this product. Under Profile 0.2.4 / Methodology 0.3.7 the repository does not itself ship an agentic S1, so the Index exclusion boundary applies. This does not judge the quality, usability or ecosystem impact of the OpenWOP protocol.

**Proposed vector:** `— · — · — · — · — · —`.
