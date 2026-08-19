#!/usr/bin/env python3
"""Genera renders de espacio y de cada mueble — Lavadero."""
from __future__ import annotations
import runpy
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from _comun.catalogo import ids_muebles, mueble
from _comun.render_espacio import generar_axonometria
from _comun.render_mueble import generar_lamina


def main() -> None:
    root = Path(__file__).resolve().parents[2]
    runpy.run_path(str(root / "planos" / "generar_planta_lavadero.py"), run_name="__main__")
    print(generar_axonometria("lavadero"))
    base = Path(__file__).resolve().parent
    for mid in ids_muebles("lavadero"):
        dest = generar_lamina(mueble("lavadero", mid), base)
        print(dest)


if __name__ == "__main__":
    main()
