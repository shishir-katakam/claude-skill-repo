"""Simple citation formatter."""
from __future__ import annotations


def ieee(index: int) -> str:
    return f"[{index}]"


def apa(author: str, year: int) -> str:
    return f"({author}, {year})"
