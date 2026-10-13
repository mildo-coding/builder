#!/usr/bin/env python3
"""Genera plantas, axonométricas y fichas de muebles.

Uso (solo a pedido del usuario):

    python3 espacios/generar_todo.py
    python3 espacios/generar_todo.py lavadero
"""

from __future__ import annotations

import runpy
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _comun.catalogo import ORDEN_ESPACIOS  # noqa: E402


def _slugs(argv: list[str]) -> list[str]:
    if not argv:
        return list(ORDEN_ESPACIOS)
    conocidos = set(ORDEN_ESPACIOS)
    pedidos: list[str] = []
    for raw in argv:
        slug = raw.strip().lower()
        if slug not in conocidos:
            disponibles = ", ".join(ORDEN_ESPACIOS)
            raise SystemExit(f"Espacio desconocido: {raw}\nDisponibles: {disponibles}")
        if slug not in pedidos:
            pedidos.append(slug)
    return pedidos


def main(argv: list[str]) -> None:
    for slug in _slugs(argv):
        script = HERE / slug / "generar_renders.py"
        if not script.exists():
            raise SystemExit(f"No existe {script}")
        print(f"\n=== {slug} ===")
        runpy.run_path(str(script), run_name="__main__")


if __name__ == "__main__":
    main(sys.argv[1:])
