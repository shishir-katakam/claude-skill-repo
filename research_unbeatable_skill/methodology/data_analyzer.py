"""Basic experiment summary stats."""
from __future__ import annotations
from statistics import mean
from typing import Iterable


def summarize(values: Iterable[float]) -> dict:
    vals = list(values)
    if not vals:
        return {"count": 0, "mean": None, "min": None, "max": None}
    return {"count": len(vals), "mean": mean(vals), "min": min(vals), "max": max(vals)}
