#!/usr/bin/env python3
"""Fail-closed structural validator for the frozen MegaAgent S fixture packet."""

from pathlib import Path

HERE = Path(__file__).resolve().parent
PACKET = (HERE / "PACKET.md").read_text(encoding="utf-8")
TEMPLATE = (HERE / "REVIEW-TEMPLATE.md").read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


for text in (PACKET, TEMPLATE):
    require(
        "947b42e77551ed1a86456f8a812c72a96a36506a" in text,
        "pinned experimental Skills revision drift",
    )
    require(
        "c2e45ad99d8166db82b8f8516d2bcd722ad8540a" in text,
        "pinned MegaAgent target revision drift",
    )

require(
    "0404f35c88b52443cd0d61e3ab1eb48919ff5b1c" in PACKET,
    "pinned Index baseline drift",
)

for row in ("S1   A", "S2   A", "S3   A", "S3*  A", "S4   —", "S5   —"):
    require(row in PACKET, f"frozen canonical baseline lost: {row}")

for function in ("S1 screening", "S2 screening", "S3 screening", "S3* screening"):
    require(function in PACKET, f"missing eligible per-function screen: {function}")

require(
    "S4 | `—` | ineligible" in PACKET and "S5 | `—` | ineligible" in PACKET,
    "S4/S5 prerequisite exclusions lost",
)

for edge in (
    "material in-domain variety exceeds the current organization",
    "MegaAgent recognizes organizational insufficiency",
    "MegaAgent defines a new bounded operational purpose/domain",
    "MegaAgent creates or reorganizes a lower operational unit",
    "the lower unit gains enough local coordination, current control",
    "bounded autonomy is granted and parent/child authority is integrated",
    "the new recursion demonstrably absorbs variety the prior organization could not",
):
    require(edge in PACKET, f"strong-recursive edge lost: {edge}")

for shortcut in (
    "`add_agent` exists",
    "hierarchy depth increases",
    "a generated prompt calls an agent a manager/CEO/specialist",
    "the parent delegates a difficult subtask",
    "more parallel capacity improves completion",
):
    require(shortcut in PACKET, f"recursive shortcut rejection lost: {shortcut}")

for boundary in (
    "no judgment",
    "does not:\n\n- assert that MegaAgent supports experimental `S`",
    "Review 2 must not see Review 1 reasoning/finding",
    "Neither review should be published",
):
    require(boundary in PACKET, f"independence/judgment boundary lost: {boundary}")

require(
    "candidate-witness | no-candidate-witness | insufficient-evidence" in TEMPLATE,
    "review template lost the three-way per-function screening",
)
require(
    "1. current organization lacks requisite variety:" in TEMPLATE
    and "7. the new recursion absorbs variety the prior organization could not:" in TEMPLATE,
    "review template lost the seven-edge strong-recursive test",
)
require(
    "Do not read another reviewer's reasoning or finding" in TEMPLATE,
    "review independence warning lost",
)

print("MegaAgent frozen S fixture packet validation passed")
