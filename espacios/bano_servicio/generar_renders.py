#!/usr/bin/env python3
"""Genera renders de espacio y de cada mueble — Baño de Servicio."""
from __future__ import annotations
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from _comun.catalogo import ids_muebles, mueble
from _comun.render_espacio import generar_axonometria, generar_plano
from _comun.render_mueble import generar_lamina


def main() -> None:
    print(generar_plano("bano_servicio"))
    print(generar_axonometria("bano_servicio"))
    base = Path(__file__).resolve().parent
    for mid in ids_muebles("bano_servicio"):
        dest = generar_lamina(mueble("bano_servicio", mid), base)
        print(dest)


if __name__ == "__main__":
    main()
