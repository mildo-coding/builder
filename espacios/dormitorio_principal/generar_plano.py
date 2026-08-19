#!/usr/bin/env python3
"""Genera la planta del espacio Dormitorio Principal."""
from __future__ import annotations
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from _comun.render_espacio import generar_plano


def main() -> None:
    dest = generar_plano("dormitorio_principal")
    print(f"OK planta: {dest}")


if __name__ == "__main__":
    main()
