"""Project-specific context module."""

from __future__ import annotations

PROJECT_CONTEXT = {
  "project_name": "ReceiptsMesh Reputation Market",
  "track": "Agents With Receipts",
  "pitch": "A receipts-native identity and reputation rail for swarms that hire each other, settle work, and publish onchain usage evidence.",
  "overlap_targets": [
    "Olas",
    "PayWithLocus",
    "ENS",
    "Bond.credit",
    "OpenServ",
    "Bankr Gateway"
  ],
  "goals": [
    "discover a bounded opportunity",
    "plan a dry-run-first action",
    "verify receipts and proofs"
  ]
}


def seed_targets() -> list[str]:
    """Return the first batch of overlap targets for planning."""
    return list(PROJECT_CONTEXT['overlap_targets'])
