"""Minimal BibTeX entry parser."""
from __future__ import annotations

import re
from typing import Dict


def parse_entry(raw: str) -> Dict[str, str]:
    pattern = r'(\w+)\s*=\s*["{]([^"}]+)'
    return dict(re.findall(pattern, raw))
