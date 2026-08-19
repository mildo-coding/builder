#!/usr/bin/env python3
"""Genera planta + renders + fichas de muebles de Comedor Diario."""
from __future__ import annotations
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> None:
    runpy.run_path(str(HERE / "generar_renders.py"), run_name="__main__")


if __name__ == "__main__":
    main()
