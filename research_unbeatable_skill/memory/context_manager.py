"""Persistent context manager for long-running research projects."""
from __future__ import annotations
import json
from pathlib import Path
from typing import Any, Dict


def load_state(path: str) -> Dict[str, Any]:
    p = Path(path)
    if not p.exists():
        return {}
    return json.loads(p.read_text(encoding="utf-8"))


def save_state(path: str, state: Dict[str, Any]) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(state, indent=2), encoding="utf-8")


def update_state(path: str, **updates: Any) -> Dict[str, Any]:
    state = load_state(path)
    state.update(updates)
    save_state(path, state)
    return state
