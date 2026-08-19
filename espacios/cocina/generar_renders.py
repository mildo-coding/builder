#!/usr/bin/env python3
"""Genera renders de espacio y de cada mueble — Cocina Principal."""
from __future__ import annotations
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from _comun.catalogo import ids_muebles, mueble
from _comun.render_espacio import generar_axonometria, generar_plano
from _comun.render_mueble import generar_lamina


def main() -> None:
    print(generar_plano("cocina"))
    print(generar_axonometria("cocina"))
    base = Path(__file__).resolve().parent
    for mid in ids_muebles("cocina"):
        dest = generar_lamina(mueble("cocina", mid), base)
        print(dest)


if __name__ == "__main__":
    main()
