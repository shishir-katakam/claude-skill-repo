"""Export orchestrator placeholder."""
from __future__ import annotations


def build_pdf_command(tex_file: str) -> str:
    return f"pdflatex {tex_file} && bibtex {tex_file.rsplit('.', 1)[0]} && pdflatex {tex_file}"
