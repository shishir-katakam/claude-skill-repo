"""DOCX conversion command helper."""
from __future__ import annotations


def pandoc_command(input_file: str, output_file: str) -> str:
    return f"pandoc {input_file} -o {output_file}"
