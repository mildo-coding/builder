#!/usr/bin/env python3
"""Render del mueble Mesada de planchado — Lavadero."""
from __future__ import annotations
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from _comun.catalogo import mueble
from _comun.render_mueble import generar_lamina


def main() -> None:
    spec = mueble("lavadero", "MESADA_PLANCHAR")
    dest = generar_lamina(spec, Path(__file__).resolve().parent)
    print(f"OK {dest}")


if __name__ == "__main__":
    main()
