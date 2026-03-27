"""Structural validator for research claims."""
from __future__ import annotations


def is_testable_claim(text: str) -> bool:
    tokens = text.lower()
    signals = ["improves", "reduces", "increases", "outperforms", "by", "%"]
    return any(s in tokens for s in signals) and len(text.split()) >= 8
