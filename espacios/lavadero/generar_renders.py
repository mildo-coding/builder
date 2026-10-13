#!/usr/bin/env python3
"""Genera vistas, axonométrica y fichas de muebles — Lavadero."""
from __future__ import annotations
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from _comun.catalogo import ids_muebles, mueble
from _comun.render_espacio import generar_axonometria, generar_vistas
from _comun.render_mueble import generar_lamina


def main() -> None:
    for dest in generar_vistas("lavadero"):
        print(dest)
    print(generar_axonometria("lavadero"))
    base = Path(__file__).resolve().parent
    for mid in ids_muebles("lavadero"):
        print(generar_lamina(mueble("lavadero", mid), base))


if __name__ == "__main__":
    main()
