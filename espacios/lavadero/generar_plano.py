#!/usr/bin/env python3
"""Planta detallada del lavadero (cota de placard 1.50 × 0.625)."""
from __future__ import annotations

import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main() -> None:
    runpy.run_path(str(ROOT / "planos" / "generar_planta_lavadero.py"), run_name="__main__")


if __name__ == "__main__":
    main()
