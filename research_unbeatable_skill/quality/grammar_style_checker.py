"""Tiny style checks for draft text."""
from __future__ import annotations

import re
from typing import List


def detect_issues(text: str) -> List[str]:
    issues = []
    if re.search(r"\bvery\b", text.lower()):
        issues.append("Avoid weak intensifier 'very'.")
    if "!" in text:
        issues.append("Avoid exclamation marks in academic writing.")
    if len(text.split()) > 350 and "\n\n" not in text:
        issues.append("Split long block into paragraphs.")
    return issues
