#!/usr/bin/env python3
"""Planta (vista superior) y alzados (vista de frente) del lavadero.

Geometría: N 2.08 / S 2.65 × L 2.80 m. Escalón este en y = 0.52.
"""
from __future__ import annotations
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from _comun.render_espacio import generar_vistas


def main() -> None:
    for dest in generar_vistas("lavadero"):
        print(f"OK {dest}")


if __name__ == "__main__":
    main()
