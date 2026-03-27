"""Heuristic source quality scoring."""
from __future__ import annotations
from dataclasses import dataclass


@dataclass
class SourceMeta:
    venue: str
    year: int
    citations: int
    has_code: bool


def score_source(src: SourceMeta) -> int:
    score = 0
    if src.venue.lower() in {"ieee", "acm", "springer", "neurips", "icml", "cvpr"}:
        score += 2
    if src.year >= 2020:
        score += 1
    if src.citations >= 20:
        score += 1
    if src.has_code:
        score += 1
    return score
