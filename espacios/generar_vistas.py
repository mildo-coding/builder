#!/usr/bin/env python3
"""Planta (vista superior) y alzados (vista de frente).

Uso (solo a pedido del usuario):

    python3 espacios/generar_vistas.py lavadero
    python3 espacios/generar_vistas.py lavadero N
    python3 espacios/generar_vistas.py
"""

from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _comun.catalogo import ORDEN_ESPACIOS  # noqa: E402
from _comun.render_espacio import generar_alzado, generar_vistas  # noqa: E402


def main(argv: list[str]) -> None:
    args = [a for a in argv if a]
    if not args:
        slugs = list(ORDEN_ESPACIOS)
        muro = None
    else:
        slugs = [args[0]]
        muro = args[1].upper() if len(args) > 1 else None
        if muro and muro not in "NSEO":
            raise SystemExit("El muro debe ser N, S, E u O.")

    for slug in slugs:
        print(f"=== {slug} ===")
        if muro:
            dest = generar_alzado(slug, muro)
            print(dest)
        else:
            for dest in generar_vistas(slug):
                print(dest)


if __name__ == "__main__":
    main(sys.argv[1:])
