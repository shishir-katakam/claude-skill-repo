"""Query planner for academic search tasks."""
from __future__ import annotations
from typing import List


def build_queries(topic: str, year_from: int = 2020) -> List[str]:
    base = topic.strip()
    return [
        f'"{base}" survey {year_from}..2026',
        f'"{base}" benchmark dataset',
        f'"{base}" reproducibility',
        f'"{base}" ablation study',
    ]
