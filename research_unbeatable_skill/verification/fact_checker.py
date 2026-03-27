"""Claim verification helper."""
from __future__ import annotations
from typing import Iterable


def verify_claim(claim: str, evidence_items: Iterable[str]) -> bool:
    clean = [e.strip() for e in evidence_items if e and e.strip()]
    if len(clean) < 2:
        return False
    claim_terms = {w.lower() for w in claim.split() if len(w) > 3}
    overlap = any(any(t in e.lower() for t in claim_terms) for e in clean)
    return overlap
