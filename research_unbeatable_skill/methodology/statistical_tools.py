"""Utility confidence interval approximation."""
from __future__ import annotations
import math
from typing import Iterable, Tuple


def mean_ci95(samples: Iterable[float]) -> Tuple[float, float, float]:
    data = list(samples)
    n = len(data)
    if n == 0:
        return (float("nan"), float("nan"), float("nan"))
    mu = sum(data) / n
    var = sum((x - mu) ** 2 for x in data) / max(1, n - 1)
    se = math.sqrt(var / n)
    margin = 1.96 * se
    return (mu, mu - margin, mu + margin)
