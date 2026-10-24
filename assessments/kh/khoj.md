---
harness_id: khoj
project_name: Khoj
repository: https://github.com/khoj-ai/khoj
review_ref: ae229ca894c0b80ad84664afcfdde523b5e87057
reviewed_at: 2026-09-15
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
last_checked_ref: ae229ca894c0b80ad84664afcfdde523b5e87057
last_checked_at: 2026-09-17
assessment_changed_at: 2026-09-15
last_reassessment_round: R2
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Khoj

## Review boundary
Khoj at the pinned revision as one configured personal agent using conversation history, private knowledge, internet information and user-enabled capabilities. Hosting, retrieval services and channel adapters are supporting infrastructure.

## Repository architecture
Conversation/provider modules build one personal-agent interaction loop. The personality prompt explicitly frames Khoj or a custom `{name}` as a personal agent, supplies past conversation and user documents as context, and exposes retrieval/media/data capabilities. Custom identity instructions are injected from builder/user-provided `{bio}`.

## Primary evidence
- `src/khoj/processor/conversation/prompts.py`: default and custom personal-agent system prompts, conversation/document context, internet/image/data capabilities and externally supplied custom `bio` instructions.
- `src/khoj/processor/conversation/`: provider-specific implementations plus shared prompt/utils infrastructure support the same conversation-agent boundary.
- Repository source search at the pinned boundary did not establish a first-party multi-S1 coordination, independent verifier/auditor, whole-system regulator or policy-closure subsystem.

## Operational model
The configured personal agent is one S1. Retrieval, internet access, conversation memory and content-generation capabilities increase that operation's variety; they are not separate viable operations by themselves.

## S1 — Operations
`A`: the personal agent selects and combines available knowledge/retrieval/capabilities to produce user-facing outcomes. Confidence: high.

## S2 — Coordination
`—`: no material first-party mutual-adjustment path among autonomous operational agents is supplied at this boundary. Confidence: high.

## S3 — Inside-and-now control
`—`: runtime/admin infrastructure does not provide an autonomous whole-system regulator with authority over multiple S1 commitments/resources. Confidence: high.

## S3* — Complementary audit
`—`: no sufficiently independent first-party verifier/audit actor with complementary access and corrective feedback was found. Confidence: high.

## S4 — Outside-and-then intelligence
`—`: web retrieval, current-date/location context and scheduled/research-style operation expose environmental information to S1, but no distinct future-oriented intelligence function generates adaptation options and couples them into S3. Confidence: high.

## S5 — Policy and identity
`—`: the agent's name/persona/instructions are supplied by static prompt/configuration (`bio`) rather than agent-owned ultimate identity/policy authority. Confidence: high.

## Recursion, variety, escalation
Knowledge and retrieval attenuate a large information environment into task context. Multiple configured personal agents are not assumed recursively viable without their own metasystem closure.