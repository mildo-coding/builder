#!/usr/bin/env python3
"""Genera planta (vista superior) y alzados (vista de frente) — Balcón / Terraza."""
from __future__ import annotations
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from _comun.render_espacio import generar_vistas


def main() -> None:
    for dest in generar_vistas("balcon"):
        print(f"OK {dest}")


if __name__ == "__main__":
    main()
