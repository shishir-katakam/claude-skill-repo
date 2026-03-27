"""Reference line formatter."""
from __future__ import annotations


def format_ieee(author: str, title: str, venue: str, year: int) -> str:
    return f'{author}, "{title}," {venue}, {year}.'
