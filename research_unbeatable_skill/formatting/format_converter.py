"""Simple extension-level format planner."""
from __future__ import annotations


def conversion_plan(src: str, dst: str) -> str:
    return f"Convert {src} -> {dst}: normalize references, validate headings, and re-check figure captions."
